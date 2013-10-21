{   # Plates - Downloads approach plates from the FAA website
    # Copyright (C) <2013>  <David O'Connor>

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
    }   

#to-do:
#add more cats?
#printing
# Add code to automatically guess the rest of the plate the person'ns entering based on what's available?
# ^ Perhaps have it autofill even without an error.

import sys
import os
from os.path import exists, join as ospj
import datetime
import tempfile

import yaml
from PyQt5 import QtCore, QtWidgets #QtPrintSupport
import PyPDF2
from requests import get
from requests.exceptions import ConnectionError


from plates_gui import Ui_Main
from about_gui import Ui_About
import module_locator

DIR = module_locator.path()


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_add.clicked.connect(add)
        self.ui.btn_delete.clicked.connect(self.delete)
        #self.ui.btn_print.clicked.connect(self._print)
        self.ui.actionAbout.triggered.connect(self.about)
        
        self.ui.tree_display.setColumnWidth(0, 75) #These would ideally be done in Designer, but it's not supported
        self.ui.tree_display.setColumnWidth(1, 150) #last column's width is automatic
    
    statusSignal = QtCore.pyqtSignal(str)
    progressSignal = QtCore.pyqtSignal(int)      
        
    def delete(self):
        # Removes the selected tree entry from the _plates list, refreshes the tree
        for item in self.ui.tree_display.selectedItems():
            del _plates[self.ui.tree_display.indexOfTopLevelItem(item)]
        refresh_display(_plates)
    
    def about(self):
        # Displays the About window
        self.w = About()
        self.w.show()
 
    def save(self):
        save(_plates, ospj(DIR, 'save.yaml'))
        combined = True if self.ui.actionCombine.isChecked() else False
        save(combined, ospj(DIR, 'combined.yaml'))
 
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Delete:
            self.delete()  
        if e.key() == QtCore.Qt.Key_Return:
            add()
        if e.key() == QtCore.Qt.Key_S and e.modifiers() == QtCore.Qt.ControlModifier:
            self.save()
   
    def download(self):
        default_path = ospj(QtCore.QDir.homePath(),'Downloads','Plates')
        if self.ui.actionCombine.isChecked():
            save_path = QtWidgets.QFileDialog.getSaveFileName(self, "Save plates", default_path, '.pdf') 
            save_path = ''.join(save_path) # f_qt is initially a 2-part tuple of the path, then the filter extension.
        else:
            #If a filename is entered, causes a "path does not exist" GUI error. Fix this when able.
            save_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Save plates (separate files)", default_path)
            #save_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Save plates (separate files)", default_path).setFileMode(QtWidgets.QFileDialog.Directory)
        self.ui.statusbar.showMessage("Download plates...")
        self.ui.progressBar.show() #make signals for these lines too?
        self.ui.progressBar.setMaximum(len(_plates))
        self.ui.progressBar.setFormat('%v / ' + str(len(_plates)))
        self.download_thread = DownloadThread(save_path)
        self.statusSignal.connect(lambda message: self.ui.statusbar.showMessage(message))
        self.progressSignal.connect(lambda progress: self.ui.progressBar.setValue(progress))
        if save_path: # Prevents download if cancel or X is clicked
            self.download_thread.start()


class About(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)


class DownloadThread(QtCore.QThread):
    def __init__(self, save_path):
        QtCore.QThread.__init__(self)
        self.save_path = save_path

    def __del__(self):
        self.wait()
        
    def run(self):
        download(self.save_path)

       
class Plate():
    def __init__(self, ident, high, procedure, suffix, rwy, lr, cat):
        self.ident = ident
        self.high = high
        self.procedure = procedure
        self.suffix = suffix
        self.rwy = rwy
        self.lr = lr
        self.cat = cat
        
    def validate_ident(self):
        # Checks for valid ICAO identifier and runway number. 
        # Returns ident in 3-letter format. (converts 'kgsb' to 'GSB')
        self.ident = self.ident.upper()
        if not self.ident.isalpha() and not self.ident.isdigit():
            return False
        if len(self.ident) < 3:
            return False
        elif len(self.ident) == 4:
            # Removes valid preceding K from self.ident.  
            # Ps are included as both 3 and 4-letter (P-included) codes in self.idents.json.
            if self.ident.startswith('K'):
                self.ident = self.ident[1:]
            else: 
                if not self.ident.startswith('P'):
                    return False
        
        return True
        
    def validate_rwy(self):
        # Checks for valid ICAO identifier and runway number. 
        # Returns rwy number 2-digit format. (converts '8' to '08')
        # Airport diagrams don't have a runway; skips validation.  Empty runway field is OK in some cases.
        if self.procedure == "Airport diagram" or self.rwy == '': 
            self.rwy = ''
        else:
            try:
                int(self.rwy)
            except ValueError as e:
                return False
            else:
                if not 1 <= int(self.rwy) <= 36:
                    return False
        # Checks for valid '0X' format, removes leading 0.
        if self.rwy.startswith('0'):
            self.rwy = self.rwy[1:]
        return True

    def check_url(self):
        # Determines if the input information will return a valid file on the FAA website
        main.ui.statusbar.showMessage("Checking for plate on FAA website...")
        url = self.faa_url()
        try:
            status = get(url, timeout=15).status_code
        except ConnectionError as e:
            main.ui.statusbar.showMessage("Internet connection error")
            return False
        if status == 200:
            return True
        else: 
            main.ui.statusbar.showMessage("Can't find requested plate")
            return False
    
    def faa_url(self):
        high = {
            '': '',
            'High': 'H',
        }
        types = {
            'Airport diagram': 'AD',
            'ILS': 'I',
            'ILS or LOC':  'IL',
            'ILS or LOC-DME': 'ILD',
            'Light visual': 'LIGHT_VIS',
            'Localizer': 'L',
            'NDB': 'N',
            'RNAV (GPS)':  'R',
            'RNAV (RNP)': 'RR',
            'Tacan': 'T',
            'VOR': 'V',
            'VOR-DME': 'VD',
        }
        suffixes = {
            '': '',
            'A': 'A',
            'Y': 'Y',
            'Z': 'Z',
        }
        lr = {
            '': '',
            'L': 'L',
            'C': 'C',
            'R': 'R',
            'LR': 'LR',
        }
        cats = {
            '': '',
            'CAT I': 'C1',
            'CAT II': 'C2',
            'CAT I & II': 'C1_2',
            'CAT II & III': 'C2_3',
            'SA CAT I': 'SAC1',
            'SA CAT I & II': 'SAC1_2',
        }
        try:   
            ident = idents[self.ident]
        except KeyError as e:
            # Returns a deliberately invalid URL to cause check_url to return False without exceptions
            return 'http://aeronav.faa.gov/d-pp/keyerror.PDF'
        _high = high[self.high]
        procedure = types[self.procedure]
        suffix = suffixes[self.suffix]
        rwy = self.rwy
        _lr = lr[self.lr]
        cat = cats[self.cat]
        return 'http://aeronav.faa.gov/d-tpp/{0}/{1}{2}{3}{4}{5}{6}{7}.PDF'.format\
            (VERSION, ident, _high, procedure, suffix, rwy, _lr, cat)
 

def add():
    ident = main.ui.le_ident.text()
    high = main.ui.cb_high.currentText()
    procedure = main.ui.cb_type.currentText()
    suffix = main.ui.cb_suffix.currentText()
    rwy = main.ui.le_rwy.text()
    lr = main.ui.cb_lr.currentText()
    cat = main.ui.cb_cat.currentText()
    plate = Plate(ident, high, procedure, suffix, rwy, lr, cat)
    ident_valid = plate.validate_ident()
    rwy_valid = plate.validate_rwy()
    if not ident_valid and not rwy_valid:
        main.ui.statusbar.showMessage("Invalid airport identifier and runway number")
    elif not ident_valid:
        main.ui.statusbar.showMessage("Invalid airport identifier")
    elif not rwy_valid:
        main.ui.statusbar.showMessage("Invalid runway number")
    else:
        if plate.faa_url() == 'http://aeronav.faa.gov/d-pp/keyerror.PDF':
            main.ui.statusbar.showMessage("Can't find selected airport")
    if ident_valid and rwy_valid and plate.check_url():
        _plates.append(plate)
        main.ui.statusbar.showMessage(' '.join(
        [plate.ident, high, procedure, suffix, plate.rwy, lr, cat, "added"]))
        refresh_display(_plates)
 
def find_version():
    # Determines latest FAA procedure version by checking downloaded file size for descending dates.
    # Checks for valid FAA urls on versions starting January of the next year, in one-month intervals.
    vers = ((datetime.date.today().year + 1) % 100) * 100 + 12 - 11
        # Ceiling checks if the date's before Jan of current year for error code.
    while vers > (datetime.date.today().year % 100) * 100:
        url = ('http://aeronav.faa.gov/d-tpp/{0}/00002AD.PDF'.format(vers)) #Plate used is arbitrary.
        try:
            status = get(url, timeout = 15).status_code
        except ConnectionError as e:
            main.ui.statusbar.showMessage("Internet connection error")
            return 9901
        else:
            if status != 404:
                return vers
            vers -= 1
            if vers % 100 == 0:
                vers -= 88
    main.ui.statusbar.showMessage("Error: Could not find valid plate version.\
                                   Try exiting and relaunching the program.")

def download(save_path):
    progress = 0
    if main.ui.actionCombine.isChecked():
        temp = tempfile.TemporaryDirectory()
        path = temp.name
    else:
        path = save_path
    for plate in _plates:
        filename = ' '.join([plate.ident, plate.high, plate.procedure,
                             plate.suffix, str(plate.rwy + plate.lr + plate.cat + '.pdf')])
        url = plate.faa_url()
        try:
            web_file = get(url, timeout=15).content
        except ConnectionError:
            main.statusSignal.emit("Internet connection error")
        else:
            with open(ospj(path, filename), 'wb')  as f:
                f.write(web_file)
            progress += 1
            main.progressSignal.emit(progress)
    if main.ui.actionCombine.isChecked():
        combine(path, save_path)
        temp.cleanup() # Explicitly cleans up the temp directory.  May not be required.
    main.statusSignal.emit("Download complete")
     
def combine(temp_path, save_path):
# Merges PDFs in the temp directory into Plates.pdf, also in the temp directory.
    filenames = [f for f in os.listdir(temp_path) if f.endswith('.pdf')]     
    if filenames:
        merger = PyPDF2.PdfFileMerger()
        for f in filenames:
            merger.append(fileobj=ospj(temp_path, f))
        with open(save_path, 'wb') as f: 
            merger.write(f)
        merger.close()    

def save(dataset, filename):
# Saves the plates list or combined option to a YAML file
    try:
        with open(filename, 'w') as f:
            f.write(yaml.dump(dataset))
            main.ui.statusbar.showMessage("Selections saved")
    except PermissionError as e:
        main.ui.statusbar.showMessage("Error saving:", filename, "is open. Close and try again.")
        
def load_list(filename):
# Returns the data from a yaml file 
    if exists(filename):
        with open(filename, 'r') as f:
            return yaml.load(f)
    else:
        return []
            
def load_idents(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                x = yaml.load(line)
    except FileNotFoundError as e:
        main.ui.statusbar.showMessage("Error: Cannot find idents.json")
        return {}
    else:
        return x 
    
def refresh_display(plates):
    # Re-populates the display tree based on current plates list.
    main.ui.tree_display.clear()
    for plate in plates:
        if plate.high == 'High':
            procedure_txt = ' '.join([plate.high, plate.procedure, plate.suffix])
        else:
            procedure_txt = ' '.join ([plate.procedure, plate.suffix])
        rwy_txt = ''.join([plate.rwy, plate.lr, ' ', plate.cat])
        item_0 = QtWidgets.QTreeWidgetItem(main.ui.tree_display)
        main.ui.tree_display.topLevelItem(plates.index(plate)).setText(0, plate.ident)
        main.ui.tree_display.topLevelItem(plates.index(plate)).setText(1, procedure_txt)
        main.ui.tree_display.topLevelItem(plates.index(plate)).setText(2, rwy_txt)
    main.ui.progressBar.hide()


    
#def print2(filename):
 #   file = PdfFileReader(open(filename, 'rb'))
  #  doc = QtGui.QTextDocument(file)
   # printer = QtGui.QPrinter()
    #dialog = QtGui.QPrintDialog(printer)
    #if dialog.exec_():
     #   doc.print_(printer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    
    #possibly reorganize or place some/all of these extra lines elsewhere.
    _plates = load_list(ospj(DIR, 'save.yaml'))
    combined = load_list(ospj(DIR, 'combined.yaml'))
    idents = load_idents(ospj(DIR, 'idents.json'))
    # Sets the combined menu option based on loading combined.YAML
    if combined:
        main.ui.actionCombine.setChecked(True)
    else:
        main.ui.actionCombine.setChecked(False)
    refresh_display(_plates)
    VERSION = find_version()
    month = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December'][VERSION % 10]
    main.ui.lbl_version.setText("Plate version: " + month + " 20" + str(int(VERSION / 100)))

    sys.exit(app.exec_())
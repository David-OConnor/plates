{   #Approach Plate Downloader - Downloads approach plates for common SJAFB F-15E destinations
    #Copyright (C) <2013>  <David O'Connor>

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.
    }   


{   #To do:

    #-Allow selection of save directory
    #-Cleanup checkbox code / possibly eliminate checked global
    #-Make universal??
    }

import sys
from os import makedirs, remove, getcwd
from os.path import exists, abspath, dirname
from shutil import rmtree
from urllib.request import urlopen
from urllib.error import HTTPError
from datetime import date
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

from PyQt4 import QtCore, QtGui
from seymour_plates_gui import Ui_Main
from about_gui import Ui_About


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
        global plates
        plates = plates()
        
        self.ui.download_btn.clicked.connect(self.download)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.actionAbout.triggered.connect(self.about)

        for plate in range(len(plates)):
            (self.ui.__getattribute__('cb%s' % plate).stateChanged
            .connect(self.__getattribute__('check%s' % plate)))
            
        #for n in range(len(plates)):
         #   (self.ui.__getattribute__('cb%s' % n).stateChanged
          #  .connect(lambda: self.check(n)))

    def about(self):
        self.w = About()
        self.w.show()

    
    def months(self):
        return [
        '', # to offset 0-based counting
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
        ]

    def download(self):
        if self.ui.actionCombine.isChecked() ==  True:
            download(plates, version, True, mywindow)
            combine()
        else:
            download(plates, version, False, mywindow)
    
    def save(self):
        save(mywindow)    
        
    def check(self, x):
        print (x)
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
            print ("sucess yes!")
        else: 
            plates[x].selected = False
            print ("sucess no!")

    
    def check0(self):
        x = 0
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check1(self):
        x = 1
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check2(self):
        x = 2
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check3(self):
        x = 3
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check4(self):
        x = 4
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check5(self):
        x = 5
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check6(self):
        x = 6
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check7(self):
        x = 7
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check8(self):
        x = 8
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check9(self):
        x = 9
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check10(self):
        x = 10
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check11(self):
        x = 11
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check12(self):
        x = 12
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check13(self):
        x = 13
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check14(self):
        x = 14
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

    def check15(self):
        x = 15
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False
            
    def check16(self):
        x = 16
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False
            
    def check17(self):
        x = 17
        if self.ui.__getattribute__('cb%s' % x).checkState() == 2:
            plates[x].selected = True
        else: 
            plates[x].selected = False

 
class About(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)

 
class Plate(object):
    #Class containing approach plate parameters
    def __init__(self, airport_name, ident, procedure, file_name, selected):
        self.airport_name = airport_name
        self.ident = ident
        self.procedure = procedure
        self.file_name = file_name
        self.selected = selected

        
def find_version(window):
    #Determines latest FAA procedure version by checking downloaded file size for descending dates
    print ("Determining latest procedure version...")
    #Checks for valid FAA urls on versions starting January of the next year, in one-month intervals
    vers = ((date.today().year + 1) % 100) * 100 + 12 - 11
    while vers > (date.today().year % 100) * 100: #Ceiling checks if the date's before Jan of current year for error code
        url = ('http://aeronav.faa.gov/d-tpp/%s/%s.PDF' % (vers, plates[0].file_name))
        try:
            urlopen(url, timeout = 15)
            print ("Version: " + "20" + str(int(vers / 100)) + " " + str(vers % 10))
            return vers
        except HTTPError as e:
            vers -= 1
            if vers % 100 == 0:
                vers -= 88
    window.ui.statusbar.showMessage("Error: Could not find valid plate version.\
    Try exiting and relaunching the program.")
  

def download(plates, version, combined, window):
    #Downloads selected plates to \Plates
    #combined causes save to use a temporary folder, preventing combine() from deleting previously-saved plates
    window.ui.statusbar.showMessage("Downloading plates...")
    if not exists(dir + "\\Plates\\"):
        makedirs(dir + "\\Plates\\")
    count = 0 #to determine if 0 plates are selected
    for plate in plates:
        if plate.selected == True:
            count += 1
            url = 'http://aeronav.faa.gov/d-tpp/%s/%s.PDF' % (version, plate.file_name)
            web_file = urlopen(url)
            if combined == True:
                if not exists(dir + "\\temporary\\"):
                    makedirs(dir + "\\temporary\\")
                save_path = dir + "\\temporary\\" + '%s.pdf' % (plate.ident + ' ' + plate.procedure)
            else:
                save_path = dir + "\\Plates\\" + '%s.pdf' % (plate.ident + ' ' + plate.procedure)
            with open(save_path,'wb') as f:
                f.write(web_file.read())
            print (plate.airport_name + ' ' + plate.procedure + " saved")
    if count > 0:
        print ("Download complete")
        window.ui.statusbar.showMessage("Download complete")
    else: 
        print ("No plates selected")
        window.ui.statusbar.showMessage("No plates selected")

        
def combine():
#Merges PDFs in 'temporary' dir as 'Plates (number merged).pdf', deletes originals and 'temporary'
    filenames = []
    for plate in plates:
        if plate.selected == True:
            filenames.append(str(plate.ident + ' ' + plate.procedure))
            merger = PdfFileMerger()
    if len(filenames) > 0:
        for plate in filenames:
            merger.append(fileobj = dir + "\\temporary\\" + '%s.pdf' % (plate))
        #with open(dir + '\\Plates\\Plates (%s).pdf' % (len(filenames)), 'wb') as f2:
        with open(dir + '\\Plates\\Plates (%s).pdf' % (len(filenames)), 'wb') as f2:
            merger.write(f2)
        merger.close()
        rmtree(dir + "\\temporary\\")

    
def save(window):
#Saves current plates and combined selections as selections.txt
    try:
        with open('selections.txt', 'w') as f:
            for plate in plates:
                if plate.selected == True:
                    f.write(plate.file_name + '\n')
            f.write(str(window.ui.actionCombine.isChecked()) + '\n')
    except PermissionError as e:
        print ("Error saving: Please close selections.txt")
        window.ui.statusbar.showMessage("Error saving: Please close selections.txt")
    print("Selections saved")
    window.ui.statusbar.showMessage("Selections saved")

    
def load(window):
#Loads selections from selections.txt into Plates parameters
#Sets Combine menu checkbox according to selections.txt
    list = []
    try:
        with open('selections.txt', 'r') as f:
            for line in f:
                list.append(line.replace('\n',''))
        if "False" in list:
            window.ui.actionCombine.setChecked(False)
        else:
            window.ui.actionCombine.setChecked(True)
        for plate in plates:
            if plate.file_name in list:
                plate.selected = True
            else:
                plate.selected = False
    except FileNotFoundError as e:
        with open('selections.txt', 'w'):
            pass


def set_cbs(window):
#Sets plate selection checkboxes according to their corresponding Plates parameter
#Does not set combined menu option
    i = 0
    #print (window.ui.cb0.checkState())
    for plate in plates:
        if plate.selected == True:
            (window.ui
            .__getattribute__('cb%s' % (i))
            .setCheckState(QtCore.Qt.Checked)
            )
        else:
            (window.ui
            .__getattribute__('cb%s' % (i))
            .setCheckState(QtCore.Qt.Unchecked)
            )
        i += 1  


def plates():
    return [
    Plate("Seymour Johnson AFB", 'GSB', "Seymour One", '00169SEYMOUR', False),
    Plate("Seymour Johnson AFB", 'GSB', "HI-ILS 8", '00169HILD8', False),
    Plate("Seymour Johnson AFB", 'GSB', "HI-ILS 26", '00169HILD26', False),
    Plate("Seymour Johnson AFB", 'GSB', "HI-TAC 8", '00169HT8', False),
    Plate("Seymour Johnson AFB", 'GSB', "HI-TAC 26", '00169HT26', False),
    Plate("Kinston", 'ISO', "ILS 5", '05038I5', False),
    Plate("Cherry Point", 'NKT', "HI-TAC Y 32L", '00471HTY32L', False),
    Plate("Cherry Point", 'NKT', "HI-TAC Z 32L", '00471HTZ32L', False),
    Plate("Shaw AFB", 'SSC', "HI-ILS 4L", '00409HILD4L', False),
    Plate("Shaw AFB", 'SSC', "HI-ILS 22R", '00409HILD22R', False),
    Plate("Shaw AFB", 'SSC', "HI-TAC 4L", '00409HT4L', False),
    Plate("Shaw AFB", 'SSC', "HI-TAC 22R", '00409HT22R', False),
    Plate("Langley AFB", 'LFI', "HI-ILS 8", '00185HILD8', False),
    Plate("Langley AFB", 'LFI', "HI-ILS 26", '00185HILD26', False),
    Plate("Langley AFB", 'LFI', "HI-TAC 8", '00185HT8', False),
    Plate("Langley AFB", 'LFI', "HI-TAC 26", '00185HT26', False),
    Plate("Oceana NAS", 'NTU', "HI-TAC 5R", '00934HT5R', False),
    Plate("Oceana NAS", 'NTU', "HI-TAC 23LR", '00934HT23LR', False),
    ]


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mywindow = StartQT4()
    mywindow.show()
    
    dir = (abspath(getcwd()))
    
    global version
    version = find_version(mywindow)
    month = mywindow.months()[version % 10]
    mywindow.ui.label.setText("Plate version: " + month + " 20" + str(int(version / 100)) )
    mywindow.ui.statusbar.showMessage("Ready")
    load(mywindow) #sets plates.selected based on selections.txt
    set_cbs(mywindow) #synchronizes checkboxes to corresponding plates.selected values
    
    sys.exit(app.exec_())
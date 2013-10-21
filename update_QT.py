import os

import module_locator


DIR = module_locator.path()
os.system(' '.join(['pyuic5', os.path.join(DIR, 'plates.ui'), '>', os.path.join(DIR, 'plates_gui.py')]))
os.system(' '.join(['pyuic5', os.path.join(DIR, 'about.ui'), '>', os.path.join(DIR, 'about_gui.py')]))

os.system(' '.join(['pyrcc5', os.path.join(DIR, 'plates.qrc'), '-o', os.path.join(DIR, 'plates_rc.py')]))

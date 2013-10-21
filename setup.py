import sys
import os

import cx_Freeze

import module_locator

#includes = ['sip']
includes = ['sip']
DIR = module_locator.path()
base = "Win32GUI" if sys.platform == "win32" else None

cx_Freeze.setup(
    name = "Plates",
    version = "0.3",
    description = "Downloads approach plates",
    options = {'build_exe': {'includes': includes}},
    executables = [cx_Freeze.Executable(os.path.join(DIR, 'plates.pyw'),
                   base=base, icon=os.path.join(DIR, 'icon.ico'))]
)

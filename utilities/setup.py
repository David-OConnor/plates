import sys
import os

import cx_Freeze

import module_locator

includes = ['sip']
name = 'plates'
DIR = module_locator.path()
DIR_PY = os.path.abspath(os.path.join(DIR, os.pardir, name))
DIR_RES = os.path.abspath(os.path.join(DIR, os.pardir, 'resources'))
base = "Win32GUI" if sys.platform == "win32" else None

cx_Freeze.setup(
    name = name,
    version = "0.3",
    description = "Downloads approach plates",
    options = {'build_exe': {'includes': includes}},
    executables = [cx_Freeze.Executable(os.path.join(DIR_PY, name+'.pyw'),
                   base=base, icon=os.path.join(DIR_RES, 'icon.ico'))]
)

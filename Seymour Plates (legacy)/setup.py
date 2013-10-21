import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Seymour Plates",
    version = "1.0",
    description = "Downloads approach plates",
    executables = [Executable("C:\\Users\\David\\Desktop\\Programming\\Approach plates\\Seymour Plates.pyw",
    base = base, icon = 'C:\\Users\\David\\Desktop\\Programming\\Approach plates\icon.ico')]
    )
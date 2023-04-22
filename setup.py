import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Doom Python",
        version = "0.1",
        description = "Doom Python",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Doom.py", base=base, icon="Icon.ico")])

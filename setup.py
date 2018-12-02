from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["PyQt5","sys",],  # 1
	excludes = ["tkinter", "sqlite3"])

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = [Executable("IMLCalc.py", base=base)]

# 3
setup(
    name='IML Calculator',
    version = '0.1',
    author = "IML",
    description = "I'M IML!",
    options = dict(build_exe = buildOptions),
    executables = exe
)
import os
import subprocess

PATH = os.path.join("/home/arjan/Downloads/autoVP", "bin")
print(f"Preparing EXE in {PATH}, please wait...")
os.chdir(os.path.join("/home/arjan/Downloads/autoVP", "scripts"))

NAME = "autoVP"
OPTIONS = "--onefile --clean --noconsole"
MAIN_FILE = "..\autoVP\__main__.py"
OUTPUT_DIR = "--distpath ../bin/ --workpath ../bin/build --specpath ../bin/"
# ICON = "-i ICON_DIR"
# EXTRA_DATA = "--collect-data EXTERNAL_PACKAGE"
# SPLASH_SCREEN = "--splash SPLASH_IMG_DIR"

with open('../bin/logfile.txt', 'w+') as logFile:
    results = subprocess.run(f"..\..\0_gui_dev_venv\Scripts\pyinstaller.exe --name \"{NAME}\" {MAIN_FILE} {OPTIONS} {OUTPUT_DIR}", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    logFile.write(results.stdout)
    
print("Done!")
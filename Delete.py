import os
import configparser

import sys

# Get the directory of the current script or executable
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    current_directory = os.path.dirname(sys.executable)
else:
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
config_path = os.path.join(current_directory, 'config.ini')

# Read ini file
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')
repo_path = config.get('Settings', 'repo_path')

repo_path = repo_path.replace("/","\\")

if os.path.exists(repo_path):
    desktop_ini_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.lower() == 'desktop.ini':
                file_path = os.path.join(root, file)
                desktop_ini_files.append(file_path)

    print(f"Path Searched: {repo_path}")
    print(f"Found files Below: {repo_path}")
    for each in desktop_ini_files:
        print(each)

    # Ask user to press any key to proceed
    input("Hit Enter to confirm deletion of dekstop.ini Files above, or close the consol to stop")

    for each in desktop_ini_files:
        os.remove(each)

else:
    print(f"Provided Path wasnt found")
    
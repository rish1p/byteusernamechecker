import requests
import pyfiglet
import sys
import os
import random
from colorama import Fore
from halo import Halo
url = "https://api.byte.co/account/register/precheck"
afile = "available.txt"
cfile = "usernames.txt"

def count():
    namecount = 0
    with open(cfile) as f:
            for namecount, l in enumerate(f):
                pass
            namecount = namecount + 1


    return namecount

def check():
    with open(cfile, "r+") as fp:
        line = fp.readline()
        checked = 0
        f= open(afile,"a+")
        f.write(f"------Session Started-------\n")
        while line:
            name = line.strip()
            data = {"username":name}
            r = requests.post(url, json=data)
            status = r.json()
            if status["success"] == 0:
                print(f"{name}" + Fore.RED + ' Taken')
            if status["success"] == 1:
                print(f"{name}" + Fore.GREEN + ' Available')
                f.write(f"{name}\n")

            line = fp.readline()
            if not line.strip():
                print("")
                print(f"{count()}" + Fore.RED + ' usernames ' + Fore.LIGHTYELLOW_EX + 'checked')
                print("--------------------------------------------------------------")
                f.write("BTC Donations: 1JiFCwiTSf4cXcPVakp2G5hCg3PS392Ltd\n")
                f.write("")
                f.write("DM @r1shi for other payment methods\n")
                result = pyfiglet.figlet_format("RISHI = GOD", font = "slant" )
                print(result + "--------------------------------------------------------------")
                f.close()


def initialize():
   print(Fore.RED + 'BYTE Username Checker' + Fore.GREEN + ' by Rishi' + Fore.RESET + ' THIS IS A FREE PROGRAM.')
   print(Fore.LIGHTYELLOW_EX + 'Follow me' + Fore.LIGHTCYAN_EX + ' on IG' + Fore.RED + ' @r1shi')
   print("")
   print("BTC Donations are welcome!" + Fore.LIGHTYELLOW_EX + ' 1JiFCwiTSf4cXcPVakp2G5hCg3PS392Ltd')
   print(f"{count()} usernames have been detected in usernames.txt")
   print (f"{count()}" + u" تم اكتشاف أسماء المستخدمين في usernames.txt")
   print("Press ENTER to begin checking for available usernames")
   print(u"اضغط ENTER لبدء التحقق من أسماء المستخدمين المتوفرة")
   input("")
   check()


if __name__ == "__main__":
    initialize()
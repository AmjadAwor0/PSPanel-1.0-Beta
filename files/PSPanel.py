#
#   PSPanel by TSH.
#   From PC
#

# COLORS = {\
# "black":"\u001b[30;1m",
# "red": "\u001b[31;1m",
# "green":"\u001b[32m",
# "yellow":"\u001b[33;1m",
# "blue":"\u001b[34;1m",
# "magenta":"\u001b[35m",
# "cyan": "\u001b[36m",
# "white":"\u001b[37m",
# "yellow-background":"\u001b[43m",
# "black-background":"\u001b[40m",
# "cyan-background":"\u001b[46;1m",
# }
import platform
import sys
import requests
import urllib3
# from mysql import connector
import os
import socket
from tabulate import tabulate
import configparser
from pathlib import Path

if float(platform.python_version()[:3]) < 3.6 and float(platform.python_version()[:3]) > 3.11 :
    print(u"\033[1mPython version should be between 3.6 to 3.11")
    sys.exit()

version="1.1 Beta"
print(u"\u001b[34;1mWelcome to PSPanel "+version+u"!\u001b[37;0m")
print(u"\u001b[32mConnecting...\u001b[37;0m")
offline1=False
conoffline=False
name=""
username=""
payload=""
mode=""
owner=""
url = "https://www.facebook.com"
timeout = 15

# def error(Error: str):
#     o3=open("/opt/pspanel/Errors")
#     o3.writelines()

def isConnect():
    try:
        s = socket.create_connection(
              ("www.facebook.com", 80))
        if s is not None:
            s.close
        return False
    except OSError:
        pass
    return True
offline1=isConnect()

def system(command: str):
    os.system(command)

while(offline1==True and conoffline==False):
    if offline1==True:
        print("Continue offline? (Yes/Reconnect)")
        x=input(u"\u001b[36;1m-> \u001b[37;0m")
        if x=="Yes":
            conoffline=True
        else:
            if x=="Reconnect":
                offline1=isConnect()
                if offline1:
                    print("Still offline")
                else:
                    print("Connected!")
            else:
                print("Reply not found")

os.system("clear")

# mydb = connector.connect(
# host="localhost",
# user="root",
# password="",
# database="pspanel"
# ) 

# if mydb.is_connected()==True:
#     print("connected")
#     os.system("clear")
# else:
#     print("Can't connect to PSPanel, Try again later.")
print(u"\u001b[34;1mWelcome to PSPanel "+version+u"!\u001b[37;0m")
print("""
<-(    Get payloads from internet     )->
<-(     Publish your own payloads     )->
<-(  Use payloads and Hack Anything!  )->
<-(     Type dotshow to show help     )->
""")
while(True):
    x=input(u"\u001b[36;1mPS "+u"\u001b[34;1m"+"("+payload+")"+u"\u001b[36;1m"+u"> \u001b[37;0m")
    words=x.split()
    if x!="":
        if words[0]=="set":
            if payload=="":
                print("'set' command is used to edit 'options' file while using a payload\nIf you're using a payload, maybe options file isn't exist!\nTell the owner of the payload if something wrong happened.")
            else:
                try:
                    config = configparser.ConfigParser()
                    config.read("/opt/pspanel/payloads/"+payload+"/options")
                    topsecret = config[words[1]]
                    topsecret[words[2]] = words[3]     # mutates the parser
                    with open("/opt/pspanel/payloads/"+payload+"/options", 'w') as configfile:
                        config.write(configfile)
                    # ini_file = IniOpen("/opt/pspanel/payloads/"+payload+"/options")
                    # print(ini_file.parse) # prints the entire nested dictionary
                    # print(ini_file.read(words[1], words[2]))
                    # ini_file.write(words[1],words[2], words[3])
                    # config = configparser.ConfigParser()
                    # myfile = Path("/opt/pspanel/payload/"+payload+"/options")  #Path of your .ini file
                    # config.read("/opt/pspanel/payload/"+payload+"/options")
                    # config.set(words[1],words[2], words[3])
                    # config.write(myfile.open("w"))
                    # if mode=="python" or mode=="python\n":
                    #     system("python /opt/pspanel/payloads/"+payload+"/start.py")
                    # elif mode=="bash" or mode=="bash\n":
                    #     system("sh /opt/pspanel/payloads/"+payload+"/start.sh")
                    # elif mode=="shpy" or mode=="shpy\n":
                    #     system("python /opt/pspanel/payloads/"+payload+"/start.py")
                    # else:
                    #     print("This version of PSPanel doesn't support the language of this payload!")
                except Exception as err:
                    print(err)
        if words[0]=="use":
            if words[1]=="payload":
                try:
                    o=open("/opt/pspanel/payloads/"+words[2]+"/mode")
                    o2=open("/opt/pspanel/payloads/"+words[2]+"/owner")
                    x2=o2.readlines(0)
                    x1=o.readlines(0)
                    if x1[0]=="python" or x1[0]=="python\n":
                        payload=words[2]
                        mode=x1[0]
                        owner=x2[0]
                        print("Payload changed to "+payload)
                        print("Payload mode: "+mode)
                        print("Payload owner: "+owner)
                    elif x1[0]=="bash" or x1[0]=="bash\n":
                        payload=words[2]
                        mode=x1[0]
                        owner=x2[0]
                        print("Payload changed to "+payload)
                        print("Payload mode: "+mode)
                        print("Payload owner: "+owner)
                    elif x1[0]=="shpy" or x1[0]=="shpy\n":
                        payload=words[2]
                        mode=x1[0]
                        owner=x2[0]
                        print("Payload changed to "+payload)
                        print("Payload mode: "+mode)
                        print("Payload owner: "+owner)
                    else:
                        print("This version of PSPanel doesn't support the language of this payload!")
                except FileNotFoundError:
                    print("You didn't download this payload!\nYou can use: install payload [git/psdata] "+words[2]+"\nIf this payload exist, maybe the the files isn't exist!\nTell the owner of the payload if something wrong happened.")
        elif words[0]=="dotshow":
            system("cat /opt/pspanel/help")
        elif words[0]=="install":
            if words[1]=="payload":
                if words[2]=="git":
                    # os.system("mkdir /opt/pspanel/payloads/"+words[3])
                    os.system("cd /opt/pspanel/payloads/ && git clone https://github.com/"+words[3]+"/"+words[4])
                elif words[2]=="psdata":
                    os.system("echo Can't install")
                else:
                    print("Can't install from "+words[2])
        elif words[0]=="help":
            if payload=="":
                print("'help' command is used to show help files while using a payload\nIf you're using a payload, maybe help file isn't exist!\nTell the owner of the payload if something wrong happened.")
            else:
                try:
                    system("cat /opt/pspanel/payloads/"+payload+"/help")
                except Exception as err:
                    print(err)
                    print("'help' command is used to show help files while using a payload.\nIf you're using a payload, maybe help file isn't exist!\nTell the owner of the payload if something wrong happened.")
        elif words[0]=="start":
            if payload=="":
                print("'start' command is used to excute 'start' file while using a payload\nIf you're using a payload, maybe start file isn't exist!\nTell the owner of the payload if something wrong happened.")
            else:
                try:
                    if mode=="python" or mode=="python\n":
                        system("python /opt/pspanel/payloads/"+payload+"/start.py")
                    elif mode=="bash" or mode=="bash\n":
                        system("sh /opt/pspanel/payloads/"+payload+"/start.sh")
                    elif mode=="shpy" or mode=="shpy\n":
                        system("python /opt/pspanel/payloads/"+payload+"/start.py")
                    else:
                        print("This version of PSPanel doesn't support the language of this payload!")
                except Exception as err:
                    print("'start' command is used to excute 'start' file while using a payload.\nIf you're using a payload, maybe options file isn't exist!\nTell the owner of the payload if something wrong happened.")
        elif words[0]=="options":
            if payload=="":
                print("'options' command is used to edit 'options' file while using a payload\nIf you're using a payload, maybe options file isn't exist!\nTell the owner of the payload if something wrong happened.")
            else:
                try:
                    o=open("/opt/pspanel/payloads/"+payload+"/options")
                    system("cat /opt/pspanel/payloads/"+payload+"/options")
                except Exception as err:
                    print("'options' command is used to edit 'options' file while using a payload\nIf you're using a payload, maybe options file isn't exist!\nTell the owner of the payload if something wrong happened.")
        elif words[0]=="clear":
            os.system("clear")
        # elif words[0]=="setup":
        #     os.system("sudo sh setup.sh")
        #     os.system("exit 1")
        elif words[0]=="exit":
            os.system("exit")
        elif words[0]=="read":
            os.system("cat /opt/pspanel/payloads/"+payload+"/"+words[1])
        elif words[0]=="payloads":
            os.system("ls /opt/pspanel/payloads/")
        #Accounts:
        # elif words[0]=="signin":
        #     username=input("Username: ")
        #     password=input("Password: ")
        #     config = configparser.ConfigParser()
        #     config.read("/opt/pspanel/auto")
        #     topsecret = config["ACCOUNT"]
        #     topsecret["username"] = '"'+username+'"'
        #     topsecret["password"] = '"'+password+'"'
        #     with open("/opt/pspanel/auto", 'w') as configfile:
        #         config.write(configfile)
        #     print("Welcome!")
        # elif words[0]=="newacc":
        #     name=input("Name: ")
        #     username=input("Username: ")
        #     password=input("Password: ")
        #     retype=input("Retype Password: ")
        #     github=input("Github Username: ")
        #     print("Welcome!")
        # elif words[0]=="add":
        #     if words[1]=="payload":
        #         print("Adding payload "+words[2]+" to your account...")
        #         #adding
        #         print("Done!")
        # elif words[0]=="upload":
        #     if words[1]=="payload":
        #         print("Uploading payload "+words[2]+" to your github account...")
        elif words[0]:
            print(u"\u001b[31;1m[!]'"+x+u"' command not found[!]\u001b[37;0m")
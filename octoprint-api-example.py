#!/usr/bin/env python

# super quick example api client for octoprint to micro-phat-led hat
# code needs some serious refactoring

import requests
import time

from microdotphat import write_string, write_char, scroll, clear, show

# api key from octo
headers={'x-api-key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

temp = 0

# should be passed as a parameter
url = "https://octoprint.local/api/printer/tool"


# grab the temp, refact to switch multifunction?
def get_extruder_temp(temp):
    resp = requests.get(url,headers=headers, verify=False)
    data = resp.json()
    #print "Debug - Current Hotend Temp: ", data['tool0']['actual']
    temp = data['tool0']['actual']
    return temp;

# erase the micro-phat
clear()

# check every 5s and display on the micro-phat - needs to be in string format, kerning removes garbling
while True:
    led_temp = get_extruder_temp(temp)
    write_string("T:" + str(led_temp), kerning=False)
    show()
    time.sleep(5)


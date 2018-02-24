import requests
import os
import json
import urllib2, base64
import datetime
import csv
from dateutil import parser
from dateutil import tz

rawDataObj = {}
clientHost = "http://45.79.200.211:8500"

def processRaw(arg):
    print arg.payload
    params = str(arg.payload)
    dataToProc = params.split(",")

    try:
        if dataToProc[0] != '0':

            rawDataObj["deviceId"] = dataToProc[1]
            rawDataObj["humidity"] = dataToProc[2]
            rawDataObj["temperature"] = dataToProc[3]
            rawDataObj["light"] = dataToProc[4]
            rawDataObj["doorCnt"] = dataToProc[7]
            rawDataObj["powerCnt"] = dataToProc[8]
            rawDataObj["battery"] = dataToProc[9]
            rawDataObj["signal"] = dataToProc[11]
            rawDataObj["timestamp"] = str(datetime.datetime.now())

            if dataToProc[5] == '1':
                rawDataObj["doorStatus"] = "closed"

            elif dataToProc[5] == '0':
                rawDataObj["doorStatus"] = "open"

            if dataToProc[6] == '1':
                rawDataObj["powerStatus"] = "on"

            elif dataToProc[6] == '0':
                rawDataObj["powerStatus"] = "off"

            print rawDataObj
            postData(rawDataObj)

    except Exception as e:
        print e

def postData(arg):
    headers = {'content-type' : 'application/json'}

    #Post the requst body
    try:
        resp = requests.post(data = json.dumps(arg), url = clientHost, headers = headers)
        print "Response status code.. " + str(resp.status_code)
    except Exception as e:
        print e

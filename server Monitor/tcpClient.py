import socket
import sys
import json
import urllib2, base64
import datetime
import csv
from dateutil import parser
from dateutil import tz
import time

rawDataObj = {}

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('45.79.200.211', 8500)
print >>sys.stderr, 'connecting to %s port %s' % server_address


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
            rawDataObj["timestamp"] = str(time.time())

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

        sock.connect(server_address)

        sock.sendall(json.dumps(arg))

        # Look for the response
        amount_received = 0
        #amount_expected = len(message)

        # while amount_received > 0:
        #     data = sock.recv(16)
        #     amount_received += len(data)
        #     print >>sys.stderr, 'received "%s"' % data

    except Exception as e:
        print e

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()


# try:
#
#     # Send data
#     message = 'This is the message.  It will be repeated.'
#     print >>sys.stderr, 'sending "%s"' % message
#     sock.sendall(message)
#
#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print >>sys.stderr, 'received "%s"' % data
#
# finally:
#     print >>sys.stderr, 'closing socket'
#     sock.close()

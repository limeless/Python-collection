import xmlrpclib
import json
import time
import base64
import ConfigParser
import sys
import os
from os import path, environ


def getConfigFolder():
    appfolder = "PyBitmessage"
    dataFolder = None
    if "BITMESSAGE_HOME" in environ:
        dataFolder = environ["BITMESSAGE_HOME"]
        if dataFolder[-1] not in [os.path.sep, os.path.altsep]:
            dataFolder += os.path.sep
    elif sys.platform == 'darwin':
        if "HOME" in environ:
            dataFolder = path.join(os.environ["HOME"], "Library/Application Support/", appfolder) + '/'
    elif 'win32' in sys.platform or 'win64' in sys.platform:
        dataFolder = path.join(environ['APPDATA'].decode(sys.getfilesystemencoding(), 'ignore'), appfolder) + path.sep
    else:
        try:
            dataFolder = path.join(environ["XDG_CONFIG_HOME"], appfolder)
        except KeyError:
            dataFolder = path.join(environ["HOME"], ".config", appfolder)
        dataFolder += '/'
    return dataFolder

	
def getBMConfig(setting_key):
    value = None
    try:
        value = cp.get(settings_section, setting_key)
    except Exception as e:
        pass
    return value

	
def getBitmessageEndpoint():
	username = getBMConfig("apiusername")
	password = getBMConfig("apipassword")
	host = getBMConfig("apiinterface")
	port = getBMConfig("apiport")
    return "http://"+username+":"+password+"@"+host+":"+port+"/"


def listAddresses():
	jsonAddresses = json.loads(api.listAddresses())
	list = []
	y = 0
	for x in jsonAddresses['addresses']:
		list.append(jsonAddresses['addresses'][y]['address'].encode('ASCII', 'ignore'))
		y += 1
	return list


def sendMessages(addrs):
	with open('content.txt', 'r+') as f:
		con = f.read().split('\n', 1)
		subject = con[0]
		content = con[1]
	subject = subject.encode('utf-8').strip()
	subjectdata = base64.b64encode(subject)
	msgdata = content.encode('utf-8').strip()
	msg = base64.b64encode(msgdata)
	while True:
		for j in addrs:
			ackData = api.sendMessage(j, j, subjectdata, msg, 2)
			print 'Sending: ', ackData
			time.sleep(2)
		print 'All Chans are sent, sleep 3600 seconds.'
		time.sleep(3600)
	return


if __name__ == "__main__":
	api = xmlrpclib.ServerProxy(getBitmessageEndpoint())
	cp = ConfigParser.SafeConfigParser()
	cp.read(getConfigFolder() + 'keys.dat')
	settings_section = 'bitmessagesettings'
	
	sendMessages(listAddresses())

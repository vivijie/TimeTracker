#!/usr/bin/python
import datetime
import time
import csv
import sqlite3
from AppKit import NSWorkspace

# Initial environment
activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
currentApp = activeAppName	
print "The currentApp is: " + currentApp
appTime = 0
appList = {}
appArray = {}
# Initial appArray
timeStart = datetime.datetime.now()
appArray[timeStart] = currentApp

# record time data
for i in range(10):
	activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
	timeStart1 = datetime.datetime.now()
	if currentApp == activeAppName:
		t = datetime.datetime.now()
		time.sleep(1)
		
		# record log
		appTime += 1 
		print "Log: " + activeAppName + "_" + str(t) + "%d" % appTime


		# record app time to dictionary
		if appList.has_key(currentApp):
			appList[currentApp] = appList[currentApp]+ 1

		else:
			appList[currentApp] = 0
			appList[currentApp] = appList[currentApp]+ 1
	

	else:
		timeStart2 = datetime.datetime.now()
		
		currentApp = activeAppName
		timeStart = datetime.datetime.now()

		appArray[timeStart] = currentApp
		print timeStart
		appTime = 0
		print "Switch to: %s" % currentApp
		continue



print appList
print appArray

# write appArray to csv
with open('timedate.csv', 'wb') as f:
	w = csv.DictWriter(f, appArray.keys())
	w.writeheader()
	w.writerow(appArray)


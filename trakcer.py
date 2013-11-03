#!/usr/bin/python
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
timeStart = int(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
appArray[timeStart] = currentApp

# record time data
for i in range(10):
	activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
	if currentApp == activeAppName:
		t = int(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
		time.sleep(1)
		
		# record log
		appTime += 1 
		print activeAppName + "%d %d" % (t, appTime)


		# record app time to dictionary
		if appList.has_key(currentApp):
			appList[currentApp] = appList[currentApp]+ 1

		else:
			appList[currentApp] = 0
			appList[currentApp] = appList[currentApp]+ 1
	

	else:
		currentApp = activeAppName
		timeStart = int(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

		appArray[timeStart] = currentApp
		print timeStart
		appTime = 0
		print "Switch to: %s" % currentApp
		continue

print appList
print appArray
# # sort the appArray
# appArraySorted = sorted(appArray.iteritems(), key=lambda d:d[0])
# print appArraySorted

# write appArray to csv
with open('timedate.csv', 'wb') as f:
	w = csv.DictWriter(f, appArray.keys())
	w.writeheader()
	w.writerow(appArray)

# # wirte appArray to sqlite
# conn = sqlite3.connect('appList.db')
# c = conn.cursor()
# # c.execute("""CREATE TABLE appList (id integer primary key,name varchar(20) UNIQUE,time integer)""")
# c.execute("UPDATE appList VALUES (?,?)", [dict["name"], dict["time"]])
# conn.commit()
# conn.close()
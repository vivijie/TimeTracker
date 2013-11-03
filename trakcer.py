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


# record time data
for i in range(20):
	activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
	if currentApp == activeAppName:
		t = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
		time.sleep(1)
		
		# record log
		appTime += 1 
		print activeAppName + "_" + t + " %d" % appTime


		# record app time to dictionary
		if appList.has_key(currentApp):
			appList[currentApp] = appList[currentApp]+ 1

		else:
			appList[currentApp] = 0
			appList[currentApp] = appList[currentApp]+ 1
	

	else:
		currentApp = activeAppName
		appTime = 0
		print "Switch to: %s" % currentApp
		continue

print appList
# write appList to csv
with open('timedate.csv', 'wb') as f:
	w = csv.DictWriter(f, appList.keys())
	w.writeheader()
	w.writerow(appList)

# # wirte appList to sqlite
# conn = sqlite3.connect('appList.db')
# c = conn.cursor()
# # c.execute("""CREATE TABLE appList (id integer primary key,name varchar(20) UNIQUE,time integer)""")
# c.execute("UPDATE appList VALUES (?,?)", [dict["name"], dict["time"]])
# conn.commit()
# conn.close()
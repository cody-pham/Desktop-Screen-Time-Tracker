import time
from datetime import date
from win32gui import GetWindowText, GetForegroundWindow
import json
import os

currentApp = GetWindowText(GetForegroundWindow())
start = time.time()
  
filename = './screentime/raw/' + str(date.today()) + '.txt'
with open (filename, 'a', encoding='utf-8') as f:
    while not currentApp.startswith('GENERATEREPORT'):
        if (GetWindowText(GetForegroundWindow()) != currentApp):     
            if(currentApp != "" and currentApp !="Task Switching"):
                f.write(currentApp + ", " + str(int(time.time()- start)) + "\n")

            currentApp = GetWindowText(GetForegroundWindow())
            start = time.time()

f.close()
result = {'Discord': 0, 'VALORANT  ': 0, 'Visual Studio Code': 0, 'Google Chrome': 0, 'Other': 0}
with open(filename) as f:
    Lines = f.readlines()
    
    for line in Lines:
        start = 0
        for x in range(len(line)):
            try:
                if (line[x] == '-'):
                    start = x + 2
                elif (line[x] == ','):
                    end = x
            except:
                pass
        app = line[start:end]  
        tim = int(line[end + 1:])  
        
        if (app not in result):
            app = 'Other'
        result[app] += tim
f.close()
day = str(date.today())
for appname in result:
    with open('./screentime/data/' + appname + '.json', 'r+') as f1:
        line = f1.readline()
        data = json.loads(line)
        if (day in data):
            oldtime = int(data[day])
            data[day] = oldtime + int(result[appname])
        else:
            data[day] = result[appname]
        jsonObject = json.dumps(data)
    with open('./screentime/data/' + appname + '.json', 'w') as f1:
        f1.write(jsonObject)
    f1.close()
os.remove(filename)

    
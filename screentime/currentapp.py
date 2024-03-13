import time
from datetime import date
from win32gui import GetWindowText, GetForegroundWindow

currentApp = GetWindowText(GetForegroundWindow())
start = time.time()
  
filename = './screentime/raw/' + str(date.today()) + '.txt'
with open (filename, 'a', encoding='utf-8') as f:
    while currentApp != "GENERATEREPORT - Programming - Visual Studio Code":
        
        if (GetWindowText(GetForegroundWindow()) != currentApp):     
            if(currentApp != "" and currentApp !="Task Switching"):
                f.write(currentApp + ", " + str(int(time.time()- start)) + "\n")

            currentApp = GetWindowText(GetForegroundWindow())
            start = time.time()

f.close()



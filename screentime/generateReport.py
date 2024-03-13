import json
import os
 
for file in os.listdir('./screentime/raw'):
    f = open('./screentime/raw/' + file, 'r')
    # f1 = open('./screentime/parsed/' + file, 'w')
    Lines = f.readlines()
    result = {}

    for line in Lines:
        start = 0
        for x in range(len(line)):
            if (line[x] == '-'):
                start = x + 2
            elif (line[x] == ','):
                end = x

        app = line[start:end]  
        time = int(line[end + 1:])  
        
        if (app not in result):
            result[app] = time
        else:
            result[app] += time
    
    date = file[:len(file) - 4]
    for appname in result:
        with open('./screentime/csv/' + appname + '.csv', 'a') as f1:
            f1.write(date + ',')
            f1.write(str(result[appname]))
            f1.write('\n')
    
    ######## fix delete of raw files ###############
    f.close()
    os.remove('./screentime/raw/' + file)

    # f1.write(json.dumps(result, indent=2))
    

            
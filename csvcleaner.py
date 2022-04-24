from csv import reader
import pandas as pd
import time

timestart = time.perf_counter() #start timer
timelist = []
openlist = []
highlist = []
lowlist = []
closelist = []
volumelist = []
finaldict = {}

with open('USDJPY_H1.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    rowcount = 0
    for row_reader in csv_reader:
        if(rowcount != 0):
            row = row_reader[0]
            spacecounter = 0
            tabcounter = 0
            charcounter = 0
            for char in row:
                if(char == ' ' or char == '\t'):
                    if(char == ' '):
                        spacecounter = spacecounter + 1
                    elif(char == '\t'):
                        tabcounter = tabcounter + 1
                    if(spacecounter == 1 and tabcounter == 1):
                            timecounter = charcounter
                    if(spacecounter == 1 and tabcounter ==2 ):
                            opencounter = charcounter
                    if(spacecounter ==1 and tabcounter == 3 ):
                            highcounter = charcounter
                    if(spacecounter==1 and tabcounter == 4 ):
                            lowcounter = charcounter 
                    if(spacecounter==1 and tabcounter == 5 ):
                            closecounter = charcounter
                charcounter = charcounter + 1
            timecell = row[:timecounter]
            opencell = row[timecounter+1:opencounter]
            opencell = float(opencell)
            highcell = row[opencounter+1:highcounter]
            highcell = float(highcell)
            lowcell = row[highcounter+1:lowcounter]
            lowcell = float(lowcell)
            closecell = row[lowcounter+1:closecounter]
            closecell = float(closecell)
            volumecell = row[closecounter+1:]
            volumecell = int(volumecell)
            finaldict[timecell] = {'Open':opencell,'High':highcell,'Low':lowcell,'Close':closecell,'Volume':volumecell}
        rowcount = rowcount + 1
    read_obj.close
columns = ('Open','High','Low','Close','Volume')
df = pd.DataFrame(finaldict).T
df.to_csv('USDJPY_H1_final.csv')
print("csv printed.")
timestop = time.perf_counter() #stop timer
timetaken = timestop-timestart
print("Time taken: "+str(timetaken) + "seconds")
#This is a script built to clean up csv files taken from https://forexsb.com/historical-forex-data
#The data from the csv files are all in 1 column, thus this script helps to read the whole csv and separate the data into separate columns

from csv import reader
import pandas as pd
import time

timestart = time.perf_counter() #start timer
#-----------------------initialise lists to add on to the final csv--------------------------------
timelist = []
openlist = []
highlist = []
lowlist = []
closelist = []
volumelist = []
finaldict = {} #use this for the dataframe
#--------------------------------------------------------------------------------------------------
with open('USDJPY_H1.csv','r') as read_obj: #open the csv file
    csv_reader = reader(read_obj) #reads all the lines in the csv, returns as a list of lists
    rowcount = 0 #initialise counter
    for row_reader in csv_reader:
        if(rowcount != 0): #the first row consists of the column names
            row = row_reader[0] #since all the data is in 1 column, use the first element of the row.
            spacecounter = 0
            tabcounter = 0
            charcounter = 0
            for char in row: #go through all the characters in a row
                if(char == ' ' or char == '\t'): #check for a space or a tab, the separating character
                    if(char == ' '):
                        spacecounter = spacecounter + 1
                    elif(char == '\t'):
                        tabcounter = tabcounter + 1
                    if(spacecounter == 1 and tabcounter == 1):
                            timecounter = charcounter #timecounter is a marker to indicate the end of the time column
                    if(spacecounter == 1 and tabcounter ==2 ):
                            opencounter = charcounter
                    if(spacecounter ==1 and tabcounter == 3 ):
                            highcounter = charcounter
                    if(spacecounter==1 and tabcounter == 4 ):
                            lowcounter = charcounter 
                    if(spacecounter==1 and tabcounter == 5 ):
                            closecounter = charcounter
                charcounter = charcounter + 1
            timecell = row[:timecounter] #time value
            opencell = row[timecounter+1:opencounter] #open value
            opencell = float(opencell) #convert from string to float
            highcell = row[opencounter+1:highcounter] #high value
            highcell = float(highcell)
            lowcell = row[highcounter+1:lowcounter] #low value
            lowcell = float(lowcell)
            closecell = row[lowcounter+1:closecounter] #close value
            closecell = float(closecell)
            volumecell = row[closecounter+1:] #volume value
            volumecell = int(volumecell)
            finaldict[timecell] = {'Open':opencell,'High':highcell,'Low':lowcell,'Close':closecell,'Volume':volumecell} #append
        rowcount = rowcount + 1
    read_obj.close
columns = ('Open','High','Low','Close','Volume')
df = pd.DataFrame(finaldict).T #transpose the dataframe for the correct orientation
df.to_csv('USDJPY_H1_final.csv') #write to csv file
print("csv printed.")
timestop = time.perf_counter() #stop timer
timetaken = timestop-timestart
print("Time taken: "+str(timetaken) + "seconds")

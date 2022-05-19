# csvcleaner
A python script used to tidy up the format of a csv when the data is all acquired in 1 column, the script separates all the data into separate columns
The idea came about when I had to analyse data from a CSV file, but all the information was kept in 1 column instead of multiple columns, which made it unusable
The csv file was taken from https://forexsb.com/historical-forex-data

The purpose of this script is to clean up the CSV file into a readable, workable format
First, the code retrieves the libraries needed. The most important one here is pandas.
Next, the dictionary, finaldict, is initialised as a blank dictionary. This will be used for the DataFrame object.
The script then opens up the CSV file in read mode and calls the reader object, which returns a nested list of all the rows within a list
Since all the information was stored in the first column, and since the reader object is a nested list, the script only needs to work with the first element of each row list

In the for loop per row, the script works as such:
1. Read every character.
2. Check if the character is a space or a tab (\t).
3. If the character is a space or tab, check the conditions according to how many tabs and spaces.
4. Assign the character marker to the current character marker according to the condition (date, high, low, etc).
5. Find the different column information by extracting specific parts of the string using the character markers.
6. For column values that are supposed to be numerical values, convert from string to float or int.
7. Append to the finaldict dictionary with the date as the key and the column info as key values.

After the for loop is over, convert the finaldict dictionary to a DataFrame object using pandas.
Save the DataFrame object into a csv format.

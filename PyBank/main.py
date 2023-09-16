#import modules
import os
import csv

#set file path
csvpath = os.path.join("Resources","budget_data.csv")

#print financial analysis and what we will be seraching for
print("Financial Analysis")
print("-----------------------------")

#Predefine variables that will be used.
month = 0
total = 0

#Open CSV with UTF-8 encoding (Following code was provided in class)
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    #loops through each row of the csv file
    for row in csvreader:

        #(PART 1) Get month total
        #counting the rows in the csv files. Each row is a new month
        #we make sure row doesn't add to counter when it's the first row because it doesn't count as a month
        #we make sure there are no repeats by storing the previous row[0] and making sure it doesn't equal current row[0]
        if row[0] != "Date":

            #since each row equals a month, we want to get the total rows to determine the months
            month = month + 1
            current_row = row[0]

        #(PART 2) Get Total Profit
        #don't want to add first row which is a string
        if row[1] != "Profit/Losses":

            #loop through data and add totals at each iteration
            total = total + int(row[1])

    #Print total months
    print("Total Months: " + str(month))
    
    #Print total profits
    print("Total: $" + str(total))

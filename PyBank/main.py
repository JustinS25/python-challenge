#import modules
import os
import csv


#text file path/open (learned from online code)

filepath = os.path.join("Analysis","text.txt")
#will use "filename" to print results to text file in Analysis folder
filename = open(filepath,"w")

#set file path
csvpath = os.path.join("Resources","budget_data.csv")


#print financial analysis to terminal and text file
print("Financial Analysis")
print("Financial Analysis", file = filename)
print("-----------------------------")
print("-----------------------------", file = filename)

#Predefine variables that will be used.
month = 0
total = 0
net_change_list = []
net_change = 0
greatest_inc = 0
greatest_dec = 0
greatest_month_inc = 0
greatest_month_dec = 0
x = 0

#Open CSV with UTF-8 encoding (Following code was provided in class)
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

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
    print("Total Months: " + str(month), file = filename)
    
    #Print total profits
    print("Total: $" + str(total))
    print("Total: $" + str(total), file = filename)


with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    #removes the header
    header = next(csvreader)
    first_row = next(csvreader)
    #first data in profits/losses
    previous_row = int(first_row[1])
    #loops through each row of the csv file
    for row in csvreader:
        
        #(PART 3) Average Change
        #Change = new profit/loss - previous profit/loss
        #create a list to store monthly changes
        #AskBCS was helpful in using lists for storing the net changes

        net_change = int(row[1]) - previous_row

        #make a list of all profits/losses
        net_change_list.append(net_change)
        previous_row = int(row[1])

       #(PART 4) Greatest Increase/Decrease in profits

        greatest_inc = max(net_change_list)
        #want to index which row of list had greatest increase so we can return row[0] of index
        greatest_month_inc = net_change_list.index(greatest_inc)

        greatest_dec = min(net_change_list)
        #want to index which row of list had greatest decrease so we can return row[0] of index
        greatest_month_dec = net_change_list.index(greatest_dec)

#want to get average of net change list
avg_change = sum(net_change_list)/len(net_change_list)
#round average change to 2 decimal places
avg_change = round(avg_change,2)
#print average change
print("Average Change: $" + str(avg_change))
print("Average Change: $" + str(avg_change), file = filename)


with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    #removes the header
    header = next(csvreader)
    first_row = next(csvreader)
    #first data in profits/losses
    previous_row = int(first_row[1])
    #loops through each row of the csv file
    counter_inc = 0

    for row in csvreader:
        if counter_inc == greatest_month_inc:
            print("Greatest Increase in Profits: " + row[0] + " $" + str(greatest_inc))
            print("Greatest Increase in Profits: " + row[0] + " $" + str(greatest_inc), file = filename)
            counter_inc += 1
        else:
            counter_inc += 1

with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    #removes the header
    header = next(csvreader)
    first_row = next(csvreader)
    #first data in profits/losses
    previous_row = int(first_row[1])
    #loops through each row of the csv file
    counter_dec = 0
    for row in csvreader:
        if counter_dec == greatest_month_dec:
            print("Greatest Decrease in Profits: " + row[0] + " $" + str(greatest_dec))
            print("Greatest Decrease in Profits: " + row[0] + " $" + str(greatest_dec), file = filename)
            counter_dec += 1
        else:
            counter_dec += 1


filename.close()
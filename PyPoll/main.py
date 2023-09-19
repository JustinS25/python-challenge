import os
import csv

#text file path/open (learned from online code)

filepath = os.path.join("Analysis","text.txt")
#will use "filename" to print results to text file in Analysis folder
filename = open(filepath,"w")

#set file path
csvpath = os.path.join("Resources","election_data.csv")

#print Election Results to terminal and text file
print("Election Results")
print("Election Results", file = filename)
print("-----------------------------")
print("-----------------------------", file = filename)

#predefine variables that will be used
vote_total = 0
charles_counter = 0
diana_counter = 0
raymon_counter = 0
names = []
#Open CSV with UTF-8 encoding (Following code was provided in class)
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #set first row as header, start at next row for counting
    header = next(csvreader)

    for row in csvreader:

        #(PART 1) print total votes
        #need to create counter to count each iteration of loop
        vote_total += 1

        #(PART 2) print total votes/percentage of each candidate
        #create counter for each candidate that tallys a vote when row[2] = candidate
        if row[2] == "Charles Casper Stockham":
            names.append("Charles Casper Stockham")
        if row[2] == "Diana DeGette":
            names.append("Diana DeGette")
        if row[2] == "Raymon Anthony Doane":
            names.append("Raymon Anthony Doane")

    #for loop to count how many times name appears in "names" list
    for name in names:
        if name == "Charles Casper Stockham":
            charles_counter += 1
        if name == "Diana DeGette":
            diana_counter += 1
        if name == "Raymon Anthony Doane":
            raymon_counter += 1

    #calculate percentage of votes for each candidate rounded to 3 decimal places
    charles_pct = round(charles_counter/vote_total * 100,3)
    diana_pct = round(diana_counter/vote_total * 100,3)
    raymon_pct = round(raymon_counter/vote_total * 100,3)

#print total votes to terminal and text file
print("Total Votes: " + str(vote_total))
print("Total Votes: " + str(vote_total), file = filename)
print("-----------------------------")
print("-----------------------------", file = filename)

#print percentage votes and total votes to terminal and text file
print("Charles Casper Stockham: " + str(charles_pct) + "% (" + str(charles_counter) +")")
print("Charles Casper Stockham: " + str(charles_pct) + "% (" + str(charles_counter) +")", file = filename)
print("Diana DeGette: " + str(diana_pct) + "% (" + str(diana_counter) +")")
print("Diana DeGette: " + str(diana_pct) + "% (" + str(diana_counter) +")", file = filename)
print("Raymon Anthony Doane: " + str(raymon_pct) + "% (" + str(raymon_counter) +")")
print("Raymon Anthony Doane: " + str(raymon_pct) + "% (" + str(raymon_counter) +")", file = filename)

print("-----------------------------")
print("-----------------------------", file = filename)


#want index of name index to print directly from list
charles_index = names.index("Charles Casper Stockham")
diana_index = names.index("Diana DeGette")
raymon_index = names.index("Raymon Anthony Doane")

#print winner using if statement
if charles_counter > diana_counter and charles_counter > raymon_counter:
    print("Winner: " + str(names[charles_index]))
    print("Winner: " + str(names[charles_index]), file = filename)
    print("-----------------------------")
    print("-----------------------------", file = filename)
if diana_counter > charles_counter and diana_counter > raymon_counter:
    print("Winner: " + str(names[diana_index]))
    print("Winner: " + str(names[diana_index]), file = filename)
    print("-----------------------------")
    print("-----------------------------", file = filename)
if raymon_counter > charles_counter and raymon_counter > diana_counter:
    print("Winner: " + str(names[raymon_index]))
    print("Winner: " + str(names[raymon_index]), file = filename)
    print("-----------------------------")
    print("-----------------------------", file = filename)

filename.close()
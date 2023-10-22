# Assignment 3 - Python Challenge- PyPoll Analysis
#You will be given a set of poll data called election_data.csv . The dataset is composed of three columns: "Voter ID",
# "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the
# following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# Import os & Csv Modules
import os
import csv
# Set the Csv File path
csvpath = os.path.join("Resources","election_data.csv")
# Create the variables
totalvotecount = 0
candidatelist =[]
uniquecandidate =[]
individualvotecount =[]
individualvotepercent =[]
# Open the csv file using the file path
with open(csvpath,encoding='UTF-8')as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    # skip the header
    header = next(csvreader)
    #The total number of votes cast
    for row in csvreader:
        totalvotecount = totalvotecount + 1    
        #Set the ccandidate names in candidatelist 
        candidatelist.append(row[2])
    # To find the unique cansidate and append in the uniquecandidate list 
for x in sorted(set(candidatelist)):
    uniquecandidate.append(x)
    # y is the total number of votes per candidate
    y = candidatelist.count(x)
    individualvotecount.append(y)
    # z is the percentage of each candidates votes
    z= round((y/totalvotecount) * 100,2)
    individualvotepercent.append(z)
Winningcount = max(individualvotecount)
winner = uniquecandidate[individualvotecount.index(Winningcount)]
#Print the outputs
print("------------------------------------------------------")
print("            Election Results         ")
print("------------------------------------------------------")
print("Total Vote count is :",str(totalvotecount))
print("------------------------------------------------------") 
for i in range(len(uniquecandidate)):
    print(uniquecandidate[i] + ": " + str(individualvotepercent[i]) +"% (" + str(individualvotecount[i])+ ")") 
        
print("*****************************************************")
print("The winner is: "  + winner)
print("******************************************************")
# Set output Path
outputpath = os.path.join("Analysis","PyPoll_Analysis.txt")
# Export the Election Results in the text file
with open(outputpath,"w") as textfile:
    textfile.write("------------------------------------------------------"'\n')
    textfile.write("            Election Results         "'\n')
    textfile.write("------------------------------------------------------"'\n')
    textfile.write("Total Vote count is :" + str(totalvotecount) + '\n')
    textfile.write("-------------------------------------------------------"'\n')
    for i in range(len(uniquecandidate)):
        textfile.write(uniquecandidate[i] + ": " + str(individualvotepercent[i]) +"% (" + str(individualvotecount[i])+ ")" + '\n')
    textfile.write("*****************************************************"'\n')
    textfile.write("The winner is: "  + winner + '\n')
    textfile.write("******************************************************")
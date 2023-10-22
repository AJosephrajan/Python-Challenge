# Assinment-3 Python Challenge 
# This assignment we have to work on the Budgetdata file using csv reader and writer functions

# Import Modules
import os
import csv
# Set Csv file path
csvpath = os.path.join("C:\Assignment3-Python Challenge\Python-Challenge\PyBank\Resources","Budgetdata.csv")
# Creating a Empty list to hold the data
Budgetdata=[]
increasedate =""
decreasedate =""
# Open the File path
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Looping through the data to store in the dictionary
    header =next(csvreader)
    for row in csvreader:
        Budgetdata.append({"month": row[0],"totalvalue": int(row[1]),"valueChange": 0})

        # Total Number of Months included in the data set, Calculate Total Months
        totalmonths = len(Budgetdata)
   # 1. Calculating the profit/losses changes through loop
   # set the Initial Amount as previous amount
    previousamount = Budgetdata[0]["totalvalue"]

    # 3. The net total amount of "Profit/Losses" over the entire period
    for x in range(1,totalmonths):
        Budgetdata[x]["valueChange"]= Budgetdata[x]["totalvalue"] - previousamount
        # set Previous amount to the current value
        previousamount = Budgetdata[x]["totalvalue"]

    # Calculating Total amount
    totalamount=sum(row['totalvalue'] for row in Budgetdata)  
    # 3.1 Calculating the average of those changes
    totalchange=sum(row['valueChange'] for row in Budgetdata) 
    average =round(totalchange /(totalmonths-1),2) 
    # 4.The greatest increase in profits (date and amount) over the entire period
    greatestincrease = max(row['valueChange'] for row in Budgetdata)
    greatestincrease =0
    for row in Budgetdata:
        if row['valueChange'] > greatestincrease:
            greatestincrease = row['valueChange']
            increasedate =row["month"]
          
    # 5.The greatest deccrease in profits (date and amount) over the entire period
    greatestdecrease= min(row['valueChange'] for row in Budgetdata)
    greatestdecrease= 0
    for row in Budgetdata:
        if row['valueChange'] < greatestdecrease:
            greatestdecrease = row['valueChange']
            decreasedate =row["month"]

    # Print the results
    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: ", totalmonths)
    print("Total Value: " , totalamount)
    print("The Average Change: ",average)
    # print("Greatest Increase in Profits", greatestincrease)
    # print("Greatest Decrease in Profits", greatestdecrease)
    print(f'Greatest Increase in Profits: {increasedate}  (${greatestincrease}))')
    print(f'Greatest decrease in Profits: {decreasedate}  (${greatestdecrease}))')
    # Export the analysis into a text file 
    # Set Path for the putput file
    outputfilepath = os.path.join("C:\Assignment3-Python Challenge\Python-Challenge\PyBank\Analysis", "Pybank_Budget Analysis.txt")
    with open(outputfilepath,"w") as textfile:
        textfile.write("  Financial Analysis \n" )
        textfile.write("-------------------------------\n")
        textfile.write("Total Months: " + str(totalmonths)+'\n')
        textfile.write("Total Value: " + str(totalamount) + '\n')
        textfile.write("The Average Change:" + str(average)+'\n')
        textfile.write(f'Greatest Increase in Profits: {increasedate}  (${greatestincrease})\n')
        textfile.write(f'Greatest decrease in Profits: {decreasedate}  (${greatestdecrease})\n')
        textfile.close()

# import os and csv and ooperator modules
import os
import csv
import operator

# create path for pyBank data in and out -- N.B. CREATE EMPTY budget_data_out.csv file in csvpathout!
csvpath = os.path.join("budget_data.csv")
csvpathout = os.path.join("budget_data_out.csv")

# PASS 1 Open budget_data csv using csvreader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    #Check reader meta and column data
    #print(csvfile)
    #for row in csvreader:
    # print(row)
 
 # skip the header 
    next(csvreader)

# Count total records (months) in file
    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    months = len(list(csvreader))
    print("Total Months: " + str(months))
   
# PASS - 2 Open budget_data csv using csvreader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Skip header
    next(csvreader)

 # Calculate and display sum of profit/loss
    numbers = (int(row[1]) for row in csvreader)
    total = sum(numbers)
    print("Total: $" + str(total))
# Do i really want to cast back to str for total output number?

# PASS 3 -- Open and read input, open output - calculate and output P&L change
with open(csvpathout, 'w', newline = "") as csvfileout,  open(csvpath, newline = "") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ",")
     csvwriter = csv.writer(csvfileout, delimiter = ",")
    # print(csvfile)
    # print(csvfileout)
     next(csvreader)
     csvwriter.writerow(['dte', 'pnl', 'pnlcha'])
     pnl = []
     pnlCha = []
     pnlPrev = 0
     #Loop through, generating values
     for row in csvreader:
         # Grab date
         dte = row[0]
         # Current record PNL
         pnl = int(row[1])
         #Calc pnlCha(nge) with pnl-pnlPrev
         pnlCha = (pnl - pnlPrev)
         #Current pnl becomes pnlPrev for next iter
         pnlPrev = int(row[1])
         #print(dte, pnl, pnlCha)
         # Output for PASS 4 and to read data to complete report
         csvwriter.writerow([dte, pnl, pnlCha])
        
  # PASS 4 -- Open and read output file above as new input
with open(csvpathout, newline = "") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ",")
     # print(csvreader)

     # Calculate and display Avg of profit/loss after rec 2 skip
     next(csvreader)
     next(csvreader)
     numbers = (int(row[2]) for row in csvreader)
     totCha = sum(numbers)
     pnlAvg = float(totCha/85)
    # print(totCha)
     print("Average Change: $" + str("%.2f" % pnlAvg))

 # PASS 5 -- Open and read output file above as new input
with open(csvpathout, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Find and display max month/P&L with desc sort
    sortDown = sorted(csvfile, key=lambda row: row[2], reverse = True)
#    sortDown = sorted(csvfile, key=operator.itemgetter(3), reverse = True)
itDown = iter(sortDown)
next(itDown)
print("Greatest Increase in Profits: " + dte + " ($" + str(pnlCha)+")")

 # PASS 6 -- Open and read output file above as new input
with open(csvpathout, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Find and display min month/P&L with asc sort
    sortUp = sorted(csvfile, key=lambda row: row[2], reverse = False)
    #sortUp = sorted(csvfile, key=operator.itemgetter(3), reverse = False)
itUp = iter(sortUp)
next(itUp)
print("Greatest Decrease in Profits: " + dte + " ($" + str(pnlCha)+")")

RptPathOut = os.path.join("Financial_Analysis.txt")
with open(RptPathOut, 'a') as FinReport:
    FinReport.write("Financial Analysis\n")
    FinReport.write("----------------------------\n")
    FinReport.write("Total Months: " + str(months) + "\n")
    FinReport.write("Total: $" + str(total) + "\n")
    FinReport.write("Average Change: $" + str("%.2f" % pnlAvg) + "\n")
    FinReport.write("Greatest Increase in Profits: " + dte + " ($" + str(pnlCha) + ")\n")
    FinReport.write("Greatest Decrease in Profits: " + dte + " ($" + str(pnlCha) + ")\n")
    FinReport.close()


# Instructions from readme
#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change 
# in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#As an example, your analysis should look similar to the one below:


 # Financial Analysis
 # ----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
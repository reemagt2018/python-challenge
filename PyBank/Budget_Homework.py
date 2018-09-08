import csv
with open(r"C:\Users\reema\Desktop\PythonStuff\Budget_Data.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  DatesConsidered = []
  Profit_Loss = []
  Change_data=[]
  previous_amount=0
  total=0
  #next(reader)
  for row in reader:
      print(row['Date'], row['Profit/Losses'])
      DatesConsidered.append(row['Date'])
      total=total + int(row['Profit/Losses'])
      Profit_Loss.append(row['Profit/Losses'])
      print (Profit_Loss)
for Amount_data in Profit_Loss:
    #print(Profit_Loss[Amount_data])
    Change_data.append(int(Amount_data)- previous_amount)
    previous_amount=int(Amount_data)

# Drop the first record as it doesnt show any change
Change_data.pop(0)
print (Change_data)
max_change=Change_data.index(max(Change_data))
min_change=Change_data.index(min(Change_data))

Date_positive_change=DatesConsidered[max_change + 1]
Date_negative_change=DatesConsidered[min_change + 1]

print (max_change)
print (min_change)
print(Date_positive_change)
print(Date_negative_change)



#     #  print (row['Date'],)
# # Alternative way to open a file
# total = 0
# f = open('Budget_Data.csv')
# next(f)
# csv_f = csv.reader(f)
# DatesConsidered = []
# for row in csv_f:
#   #print (row[0])
#   DatesConsidered.append(row[0])
#   print (int(row[1]))
#
 # total=total+ int(row[1])
  #print (DatesConsidered)
DatesConsidered = set(DatesConsidered)
#print (DatesConsidered)
print (f'No of dates ={len(DatesConsidered)}')
print (f'total = {total}')

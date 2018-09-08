import csv
with open(r"C:\Users\reema\Desktop\PythonStuff\election_data_0907.csv",encoding='utf-8') as csvfile:
  reader = csv.DictReader(csvfile)
  Candidates_considered = []
  Votes = []
  Votes_candidates=[]
  Unique_Candidates=[]
  Percentage_vote=[]

  #next(reader)
  for row in reader:
      #print (row)

      #print(row['\ufeffVoter ID'], row['Candidate'])
      Candidates_considered.append(row['Voter ID'])
      Votes_candidates.append(row['Candidate'])
Total_votes=len(Candidates_considered)

Unique_Candidates=set(Votes_candidates)
mynewlist = list(Unique_Candidates)
# print (Unique_Candidates)
# print (mynewlist)
# print (len(mynewlist))
Votes=  [0] * len(mynewlist)
# print (Votes)

# Loop unique candidates to get the count of votes they recived
for i in range(len(mynewlist)):
    # print (i)
    # print (mynewlist[i])

    count=0
    for candidates in Votes_candidates:
        #print (candidates)
    #    break
    #    print (Votes[i])
        if mynewlist[i]==candidates:
           count=count+1

    # print (count)
    # print (i)
    # print(Votes)

    Votes[i]=Votes[i] + count
print (Votes)
print (mynewlist)
print (Total_votes)
#percent = round(int(row[6]) / int(row[5]))
Percentage_vote = [x / Total_votes * 100 for x in Votes]
Percentage_vote = [round(x) for x in Percentage_vote]
#Percentage_vote = (Votes/Total_votes)
print (Percentage_vote)
winner_index=Votes.index(max(Votes))
winner=mynewlist[winner_index]
print (winner)



#print (f'No of dates ={len(DatesConsidered)}')
#print (f'total = {total}')

studentscores= [[40, 50, 67, 80, 30],
               [30, 56, 48, 12, 45],
               [36, 56, 40, 46, 45],
               [30, 76, 48, 52, 45],
               [90, 86, 78, 32, 45],
               ]

sum =0
x =1
for studentscore in studentscores:
  len_score = len(studentscore)

for score in studentscore:
  sum +=int(score)
  
  avg =sum/len_score
  
  print(f'{x} total score is {sum}\n{x} total course is {len_score}\n Average_score is {avg}\n')  
  x +=1
                

        # average_score = sum/len_score
        # print(f'{student} total score {sum}\n{student} total course is {len_score} \n{student} Average score is {average_score} \n')
        
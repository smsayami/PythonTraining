students_scores = [85,78,92,67,59,74,88]
print("Each student's score and grade:")
for score in students_scores:

    if score>=90 and score<=100:
        print(score,"-","Grade A")
    elif score>=80 and score<=89:
        print(score,"-","Grade B")
    elif score>=70 and score<=79: 
         print(score,"-","Grade C")
    elif score>=60 and score<=69:
        print(score,"-","Grade D")
    else:
        print(score,"-","Grade F")  
                    
   
   


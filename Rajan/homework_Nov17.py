score = int(input("Please type your score\n"))
if score>=60 and score<=100:
    print("you are passed")
elif score>=0 and score<60:
    print("you are failed")
else:
    print("Invalid number, not in range 0-100")        
if score>=90 and score<=100:   
    print("Grade A")
elif score>=80 and score<90:
    print("Grade B")
elif score>=70 and score<80:
    print("Grade C")
elif score>=60 and score<70:
    print("Grade D")   
elif score<60 and score>=0: 
    print("Grade F")
  
        
 
      

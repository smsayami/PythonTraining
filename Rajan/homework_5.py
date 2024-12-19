students =[
 {"name":"Alice","score":85},
 {"name":"Bob","score":78},
 {"name":"Charlie","score":92},
 {"name":"David","score":67},
 {"name":"Eva","score":59},
 {"name":"Frank","score":74},
 {"name":"Grace","score":88}
]
#highest_score=max(student["score"] for student in students)
#print(f"{highest_score}")
#for student in students:
    #print(f"{student["name"]}:{student["score"]}")

total_score=sum(student["score"] for student in students)
average_score=total_score/len(students)
#print(f"{average_score}")
#for student in students:
    #elif score>=80:
        #Grade="B"
    #elif score>=70:
        #Grade="C"
    #elif score>=60:
        #Grade="D"
    #else:
        #Grade="F"    
    #print(f"{student['name']}:{score} Grade:{Grade}")     

average_above= [student for student in students if student["score"]>average_score]
print(f" Number of students scoring above average:{len(average_above)}")













































Student_Score = input("enter student's score : ").split()
for n  in range(0 , len(Student_Score)):
    Student_Score[n] = int(Student_Score[n])

highest_score = Student_Score[0]
for Score in Student_Score:
    if Score > highest_score : 
        highest_score = Score
print(f"the highest score is {highest_score}")
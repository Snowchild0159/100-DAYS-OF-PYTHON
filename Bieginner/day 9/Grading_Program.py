Student_Score = {
    "Snow" : 98,
    "Seefon" : 70,
    "Shs" : 62,
    "Monzer" : 84,
}
Student_Grade = {}
for student in Student_Score : 
    Score = Student_Score[student]
    if Score > 90 :
        Student_Grade[student] = "Outstanding!!!"
    elif Score > 80 :
        Student_Grade [student] = "Exceed Expectation!"
    elif Score > 70 :
        Student_Grade[student] = "acceptable"
    else:
        Student_Grade[student] = "Fail"

print(Student_Grade)
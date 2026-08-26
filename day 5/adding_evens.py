student_score = input("enter student heights : ").split()
for n  in range(0 , len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

total_even_number = 0
for even in student_score : 
    if even % 2 == 0 :
        total_even_number+= even
print(f"the total of even numbers is {total_even_number}")
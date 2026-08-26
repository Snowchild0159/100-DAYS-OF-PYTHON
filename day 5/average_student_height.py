student_height = input("enter student heights : ").split()
for n  in range(0 , len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0 
for height in student_height:
    total_height += height

student_number = 0
for student in student_height: 
    student_number +=1

average_of_student_height = round(total_height / student_number)
print(average_of_student_height)











#another solution :
# summation = 0    
# for n  in range(0 , len(student_height)):
#     student_height[n] = int(student_height[n])

#     summation += student_height[n]
#     student_number = n + 1
# avg = round(summation / student_number)
 
# print(student_height)
# print(avg)
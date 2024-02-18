# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_number = 0
number_of_students = 0 
for i in student_heights:
    number_of_students = number_of_students + 1
    total_number = total_number + i

# print(total_number)
# print(number_of_students)

average = round(total_number / number_of_students)
print(average)

import numpy as np

student_marks = np.array([
    [78, 85, 90],   # Student 1
    [62, 70, 60],   # Student 2
    [92, 88, 95],   # Student 3
    [45, 50, 55],   # Student 4
    [80, 75, 70]    # Student 5
])

subjects = np.array(["Maths" , "English" , "Science"])

#subject wise average 

subjectwise_avg = np.mean(student_marks , axis=0)
i = 0
while i < len(subjects):
    print(f"{subjects[i]}" , ":" , round(subjectwise_avg[i] , 2))
    i += 1

#student wise average 
print("\n")
student_avg = np.mean(student_marks , axis=1)
i = 0
while i <len(student_marks):
    print(f"Student", i+1 , ":" ,  round(student_avg[i] , 2))
    i += 1

print("\nHighest and Lowest marks")
print("Highest marks overall: " , np.max(student_marks))
print("Lowest marks overall: " , np.max(student_marks))

topper_index = np.argmax(student_avg)
print("\nTopper is Student" , topper_index + 1 , "with average: " , round(student_avg[topper_index] , 2))

passed = student_marks >=40
passed_student = np.all(passed , axis=1) 

print("Passed and Failed students status")

i=0
while i < len(passed_student):
    if passed_student[i]:
        print("Student" , i+1 , "PASS")
    else:
        print("Student" , i+1 , "FAIL")
    i += 1

print("Total number of passed students: " , np.sum(passed_student))
print("Total number of failed students: " , len(passed_student) - np.sum(passed_student))

student_average = np.mean(student_marks , axis=0)
plt.figure(figsize=(10,5))
plt.plot(subjects, student_average, marker = 'o')
plt.xlabel("Subjects")
plt.ylabel("Average marks")
plt.title("Students marks analyzer")
plt.show()

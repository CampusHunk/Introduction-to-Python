# **Enrolling**

# Imagine, you are developing a rule in terms of logical and comparison operations to determine whether you should enroll a 
# student in your course or not. The rule itself looks like this:

average_grade = int(input("Enter the average grade:"))
recommended_by_tutor = bool(input("Enter if recommended by tutor:"))
finished_introductory_course = bool(input("Enter if finished introductory course:"))
introductory_course_grade = int(input("Enter introductory course grade:"))

enroll_student = ((average_grade >= 40 and recommended_by_tutor) 
or (finished_introductory_course and introductory_course_grade > 85))
print(enroll_student)

# Parameters meaning:

# average_grade is an integer variable that shows the student's average grade.
# recommended_by_tutor is a bool variable that shows whether the student has a recommendation from the tutor.
# finished_introductory_course is a bool variable that shows whether the student finished the introductory course.
# introductory_course_grade is an integer variable that shows the student's introductory course grade.

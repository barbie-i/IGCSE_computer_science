#a list, with square brackets, that stores boolean values
#a list is a variable
homework_status_of_students = [True, False, True, True, False]
print(homework_status_of_students)
homework_status_of_students.sort()
#built in function, dot operation
print(homework_status_of_students)

#show how many false values are in this data structure
number_of_falses = homework_status_of_students.count(False)
print(number_of_falses)

#show how many true values are in this data structure
number_of_trues = homework_status_of_students.count(True)
print(number_of_trues)

#iterate (traverse the data structure)
for student in homework_status_of_students:
    print(student)

#list: amount of money each student

money_each_student_has_in_their_pocket = [1, 2, 3, 2, 5]
print(money_each_student_has_in_their_pocket)

money_each_student_has_in_their_pocket.sort()
print(money_each_student_has_in_their_pocket)

two_dollars = money_each_student_has_in_their_pocket.count(2)
print(two_dollars)

#add a value, append is a built-in function that adds
money_each_student_has_in_their_pocket.append(6)
print(money_each_student_has_in_their_pocket)

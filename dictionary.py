#key - student name, value is going to be a boolean value, pet/ no pet
has_pets = {"Mars": False, "Henry": False, "Barbie": True,
"Adrian": True, "Angelina": False}
#curly braces are for lists
#data structure operations - add, delete, search, sort

student_has_pet = has_pets.get("Mars")
#dot operator, method is a function that is built in
print("The student has a pet: ", student_has_pet)

#traverse
for student in has_pets:
    print(student, has_pets.get(student))

#remove method - pop()
student_removed = has_pets.pop("Adrian")
print(student_removed)
print(has_pets)

#no longer has Adrian in it

student_scores = {"Adrian": [90, 93, 92], "Charlie": [88, 90, 89]}

#list: square brackets, dictionary: curly braces

student_scores = student_scores.get("Adrian")
for score in student_scores:
    print(score)

#siblings

apple_sibling = {"apple": ["banana", "papaya", "watermelon"]}

get_sibling = apple_sibling.get("apple")
get_sibling.sort()
for sibling in get_sibling:
    print(sibling)

#curly braces are for dictionaries and square brackets are for lists

#dictionary homework 

students_and_the_subjects_they_take = {"Apple": ["Math", "Chemistry"],
"Orange": ["Chinese", "English"]}

get_apple_timetable = students_and_the_subjects_they_take.get("Apple")
get_apple_timetable
for apple_info in get_apple_timetable:
    print(apple_info)














#lists, create a list of integers to represent the daily temperature of 
#temperature in celsius

daily_temperature_list = [35, 37, 36]
print ("the daily temperature list",daily_temperature_list)

daily_temperature_list.sort()
for sorting_list in daily_temperature_list:
    print(sorting_list)

daily_temperature_list.append(31)
print(daily_temperature_list)

daily_temperature_list.sort()
print(daily_temperature_list)

#append is add
#index, the first one is 0
#sort = ()
#dot operation needs parentheses!!! :)
#pop : removes and returns the last value 
#from the List or the given index value.
#don't set variables for dot operations

daily_temperature_list.pop(1)
print(daily_temperature_list)
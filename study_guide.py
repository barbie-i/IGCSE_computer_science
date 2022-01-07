
#1 variables -

    #a) Write a boolean to represent whether or not you will pass the exam

will_pass = True
will_not_pass = False

one_possible_result_of_the_exam = will_pass and will_not_pass
print("one possible result of the exam", one_possible_result_of_the_exam)

another_possible_result_of_the_exam = will_pass or will_not_pass
print("another possible result of the exam", another_possible_result_of_the_exam)

    #b) Write an integer variable to represent your score on the exam

#TEST PREP
will_eat_donut = True
will_not_eat_donut = False

donut_1 = will_eat_donut and will_not_eat_donut
print("An outcome", donut_1)

donut_2 = will_eat_donut or will_not_eat_donut
print("Another outcome", donut_2)

#another one

will_arrive = True
will_not_arrive = False

a_possibility = will_arrive and will_not_arrive
print("One possibility is", a_possibility)

another_possibility = will_arrive or will_not_arrive
print("Another possibilty is", another_possibility)













score = 95
print(score)

    #c) Write a floating point variable to represent the class average

class_average_score = 95.5
print(class_average_score)

    #d) Write a string variable to represent something you'd say to your friend in the morning

what_I_say_to_my_friend_in_the_morning = "Good morning"
print(what_I_say_to_my_friend_in_the_morning)















#2 iterations - for loops -

    #a) Write a for loop that prints "I am a polite and kind person" 10 x

for hopefully_not_a_lie in range (10):
    print("I am a polite and kind person", hopefully_not_a_lie + 1)

#TEST PREP
for definitely_not_a_lie in range (5):
    print("Pigeons love donuts", definitely_not_a_lie + 1)

#another one
for people in range (7):
    print("Here's the truth", people + 1)

#lastly
for pigeons in range (9):
    print("Pigeons are cute", pigeons + 1)
    
















#3 control flow - write a simple if-elif statement to describe this...

    #a) if student has a grade of 90-100, print "you're a rockstar'"
    #b) elif student has a grade of 80-90, print "you are great"
    #c) elif student has a grade of 70-80, print "not bad, keep working"
    #d) else, print "don't lose hope, you can do it"

student_grade = 70

if student_grade > 90 and student_grade <= 100:
    print("you're a rockstar")

# 91 ~ 100

elif student_grade > 80 and student_grade <= 90:
    print("you are great")

#81 ~ 90

elif student_grade > 70 and student_grade <= 80:
    print("not bad, keep working")

# 71 ~ 80

else:
     print("don't lose hope, you can do it")

# 70 and anything below

#4 arithmetic operations - write code to complete the following calculation

1 + 5
99999 - 9494
384384 * 999
24 / 2
90 % 10

#1 + 5
a = 1
b = 5
c = a + b
print(c)

#99999 - 9494
d = 99999
e = 9494
f = d - e
print(f)

#384384 * 999
g = 384384
h = 999
i = g * h
print(i)

#24 / 2
j = 24
k = 2
l = j / k
print(l)

#90 % 10
m = 90
n = 10
o = m % n
print(o)

# There are 21 computer science students, each student has $15.5 dollars
# how much money does the class have in total?

number_of_students = 21
money_of_each_student = 15.5
money_in_total = number_of_students * money_of_each_student
print("the class has",money_in_total,"dollars in total")

#5 string operations

#write a line of code to find the length of this string
#peint the length on the screen

alphabet = "abcdefghijklmnopqrstuvwxyz"
length = len(alphabet)
print(length)

#len tells you the length of a string

#write a code tp find the index (position) of the letter t
#print it


position_of_letter_t = alphabet.index("t")
print(position_of_letter_t + 1)
#index shows you the order of something in a string (dot = built in methods)
# + 1 makes it more accurate

#write code to ask for the user's name
name = input("Enter your name:")

#output the uset input on the screen 
print("Good morning", name)
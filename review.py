
#data types
#1 write a variable that stores a boolean value

from addition import adding_function


is_prepared_for_student = True
pays_attention_in_class = False
sleeps_in_class = False

#2 write a variable that stores an integer

number_of_students = 88

#3 write a variable that stores a floating point number

grades_average = 99.9

#loops
#1 write a for loop that says "happy birthday Barbie + Howard" 14x

for statement in range(14):
    print("happy birthday Barbie + Howard", statement + 1)

#write a while loop to print "good morning" x4

message = 0
while (message < 4):
    print("good morning", message + 1)
    message = message + 1

#functions
#write a function that takes is two argument and returns the sum of them

def add_function(number, another_number):
    return number + another_number

result = adding_function(1, 2)
print(result)

#random number generation
import random

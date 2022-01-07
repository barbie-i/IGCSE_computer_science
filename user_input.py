
#ask user to enter a number (integer)
#save it in a variable called "number"

user_input = input("Enter a number:") #input = function, tells user to enter a number as an input

#defining a new function called "get_square"
#it takes one value and returns value * value (square)

def get_square (placeholder):
    return user_input * user_input

square = get_square(user_input)
print(square)

an_input = input("Enter your name:")

print("good morning", an_input)




























#TEST PREP
wanna_input_something = input("Enter your code number:")

def get_cube(placeholder):
    return wanna_input_something * wanna_input_something * wanna_input_something

cube = get_cube(wanna_input_something)
print(cube)

#another
your_input = input("Enter a number you want times 2:")

def number_times_two(placeholder):
    return your_input * 2

times_2 = number_times_two(your_input)
print(times_2)

#final tests
ones_input = input("Enter a number you want to minus 2:")

def minus_2_function(placeholder):
    return ones_input - 2

minus_2 = minus_2_function(ones_input)
print(minus_2)

#another one ok?
urinput = input("Enter a number that you want to plus 7:")

def plus_7_function(placeholder):
    return urinput + 7

plus_7 = plus_7_function(urinput)
print(plus_7)

#promise it's the last
enter_input = input("Enter a number you want to multiply it by 5:")

def multiply_by_5_function(placeholder):
    return enter_input * 5

multiplies_5 = multiply_by_5_function(enter_input)
print(multiplies_5)
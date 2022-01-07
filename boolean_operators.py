
is_computer_science_student = False
is_chang_jung_student = True

is_enrolled_and = is_computer_science_student and is_chang_jung_student
print('the value of our AND statement', is_enrolled_and) #false

#AND: both values must be true for the expression to be true
#OR: only one true value is needed in order for the OR statement to be true

is_enrolled_or = is_computer_science_student or is_chang_jung_student
print('the value of our OR statement', is_enrolled_or) #true

if(is_chang_jung_student and is_computer_science_student):
    print("You are enrolled in my computer science class") #the IF statement is false = IGNORED
elif(not is_computer_science_student and is_chang_jung_student):
    print("You are not in my computer science class") #This IF statement is true = USES

#IGNORES FALSE STATEMENTS

is_dumb = True
is_not_dumb = False

intelligence = is_dumb and is_not_dumb
print("the value of our and statement is", intelligence)

if(is_dumb and is_not_dumb):
    print("The statement of this is... it won't print this haaha")

elif(is_dumb or is_not_dumb):
    print("The statement of this is true, so it prints it out")
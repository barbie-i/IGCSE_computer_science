
#programs make decisions based on control logic (control flow)

student_grade = 93

if student_grade > 90:
    print("Your grade is an A")

elif student_grade < 90 and student_grade > 80:
    print ("Your grade is a B")

elif student_grade < 80 and student_grade > 70:
    print("Your grade is a C")

else:
     print("Your grade is a D or F")

#if, elif, and else!
#: makes indent in the next line
#() and "" are close together, things before or after it do not need spaces
#... between them

#write a program using if-elif-else that...
#looks at a variable for temperature
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, and it's above 5 C,print it's cold
#else print "bring an umbrella just in case"

temperature = 20

if temperature > 30:
    print("It's hot")

elif temperature > 10 and temperature < 30:
    print("It's warm")

elif temperature < 10 and temperature > 5:
    print("It's cold")

else:
    print("Bring an umbrella just in case")



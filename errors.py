
#user input error - this throws an exception if the input is not an integer

try:
    age = int(input("Enter your age:"))
    calculation = 10/age

#putting the two errors together to avoid repition!
except (ValueError, ZeroDivisionError) as error:
    print("Please enter a valid age")
    print(error)
else:
    print("no exceptions were thrown")

#try-catch block
#the age's value must be an integer value (specifically asked)
#Even if there is an error, THE PROGRAM MUST GO ON.
#blue green is error type

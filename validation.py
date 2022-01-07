
#length check

#data vallidation - admin password

admin_password = input("Enter your new password: ")
admin_password_length = len(admin_password)

if(admin_password_length >= 6 and admin_password_length <= 12):
    print("passowrd is updated")
else:
    print("password must be 6 - 12 characters")

#check if user enters an empty string

name = input("Enter your name: ")

name_length = len(name)

#is this value equal to zero? We're not assigning a variable! So do not use "="
if(name_length == 0):
    print("You cannot enter an empty name")
elif(name_length < 3):
    print("Name must be more than three letters")
elif(name_length > 25):
    print("Name must be less than 25 characters")
else:
    print("Password updated")

#validation task - write code that takes user input and validates its length
#ask the user for a restaurant name
#validate the name is greater than 5 letters and less than 25 letters

pet_name = input("Enter a pet name: ")
pet_name_length = len(pet_name)

if(pet_name_length > 2 and pet_name_length <= 20):
    print("ok")

else:
    print("length must be more than 2 letters and 20 letters at most")

#1 - get name of restaurant
restaurant_name = input("Enter a restaurant name: ")
print(restaurant_name)

#2 - get length
restaurant_name_length = len(restaurant_name)
print(restaurant_name_length)

#3 - validation
if(restaurant_name_length == 0):
    print("You must enter something")
elif(restaurant_name_length < 5):
    print("You must enter a name with more than five letters")
elif(restaurant_name_length > 55):
    print("You must enter a name with less than 55 letters")
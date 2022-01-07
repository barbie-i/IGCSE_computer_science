


#return length of a string -len ()
#introducing "len"
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
#tells you the "amount" of letters that make up the string value
print(alphabet_length)

uppercase_alphabet = alphabet.upper()
print(uppercase_alphabet)

#advanced bonus
#the variable letter is automatically defined in this line
for letter in range(alphabet_length):
    print("this is printed same # times as the length alphabet")

#ASCII
#convert character to its ASCII code - ord()
english_a = "a"
ASCII_a = ord(english_a)
print(ASCII_a)

#the other way around
#convert ASCII back into a_z character - chr()
ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)

#another example
ASII_code_for_a_letter = 255
result = chr(ASII_code_for_a_letter) #convert it to an english character
print(result)

#add two strings together
string_one = "good morning"
string_two = "my neighbor"
combined = string_one + " " + string_two #the one in the middle is an empty space
print(combined)

#return the position of a specific letter

alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_d = alphabet.index("d")
print(position_of_letter_d + 1)
#index shows you the order of something in a string (dot = built in methods)


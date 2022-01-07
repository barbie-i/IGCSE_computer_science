
#Question 1
cows = 5000
chickens = 2000
sheep = 188
total_of_animals = cows + chickens + sheep
print(total_of_animals)

#Question 2
surviving_cows = cows - 230
surviving_sheep = sheep - 78
current_total_of_animals = surviving_cows + chickens + surviving_sheep
print(current_total_of_animals)



#Question 4
for hopefully_not_a_lie in range (10):
    print("I am getting smarter and smarter every day in every way", hopefully_not_a_lie + 1)

#Question 5
message = 0
while (message < 7):
    print("I know what I'm talking about", message + 1)
    message = message + 1


#Question 6
money_in_wallet = 77
if money_in_wallet > 90 and money_in_wallet <= 100:
    print("you can buy a snack that's between 90-100 dollars")
elif money_in_wallet > 80 and money_in_wallet <= 90:
    print("you can by a snack that's between 80-90 dollars")
elif money_in_wallet > 70 and money_in_wallet <= 80:
    print("you can buy a snack that’s between 70-80 dollars")
else:
    print("only buy a snack less than 70 dollars")

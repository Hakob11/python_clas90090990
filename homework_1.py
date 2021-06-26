# print("Welcome to our Food Court")
# dish = int(input(" Choose Kebab [1] or Pizza [2]"))
# addition = int(input("Choose Ketchup [1] or Mayo [2]"))
#
# price_kebab = 1200
# price_pizza = 3000
#
# ketchup_price = 110
# mayo_price = 200



# kilometers = int(input("enter number: "))
# miles = kilometers * 0.62
# print(kilometers, "kilometer is",  miles, "miles")


# height = float(input("enter user' height: " "km"))
# weight = int(input("enter users' weight: " " kg"))
# BMI = float(weight/(height * height))
# print(BMI)


# userNumber = int(input(" Please enter a number from 0 through 6: "))
#
# if userNumber == 0:
#     print( "Monday" )
# elif userNumber == 1:
#     print( "Tuesday")
# elif userNumber == 2:
#     print("Wednesday")
# elif userNumber == 3:
#     print("Thursday")
# elif userNumber == 4:
#     print("Friday")
# elif userNumber == 5:
#     print("Saturday")
# elif userNumber == 6:
#     print("Sunday")
# else:
#     print(userNumber, " is not a number from 0 to 6. Please enter a correct number ")

# text = input("tell me something:\n")
#
# index_of_not = text.find("not")
# index_of_poor = text.find("poor")
#
#
# if index_of_not < index_of_poor and index_of_not >= 0:
#     result = text[:index_of_not] + "is good" + text[index_of_poor + 4:]
# else:
#     result = text
# print(result)

## Homework 16/06/21
#----exercise 1----


# number = int(input(" Enter number: "))
# factorial = 1
# if (number < 0):
#     print("Cannot compute factorial for negative number ")
# elif (number < 2):
#     print("{}! = {}".format(number, factorial))
# else:
#     for result in range(number, 1, -1):
#         factorial = result * factorial
#     print(" Factiorial {}! = {}".format(number, factorial ))



#----exercise 2----


# for i in range(0, 5,):
#     cul = reversed(0, 5)
#     print("*" * i,cul )


#----exercise 3----


# for i in range(1, 51):
#     print(i, end= " ")



# #----exercise 4----

import random

comp_wins = 0
user_wins = 0

def choose_option():
     user_choice = input("Choose Rock, Paper or Scissors: ")
     if user_choice in ["Rock", "rock", "r" , " R"]:
         user_choice = "r"
     elif user_choice in ["Paper", "paper", "p" , "P"]:
         user_choice = "p"
     elif user_choice in ["Scissors", "scissors", "s" , "S"]:
         user_choice = "s"
     else:
         print("I don't understand please try again.")
         choose_option()
     return user_choice

def computer_option():
     comp_choice = random.randint(1, 3)
     if comp_choice == 1:
         comp_choice = "r"
     elif comp_choice == 2:
         comp_choice = "p"
     else:
         comp_choice = "s"
     return comp_choice

while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied. ")
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissor. You win.")
            user_wins += 1



    elif user_choice == "p":
        if comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied. ")
        elif comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissor. You lose.")
            comp_wins += 1


    elif user_choice == "s":
        if comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied. ")
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            user_wins += 1
        elif comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1



print("User wins" + str(user_wins))
print("Computer wins" + str(comp_wins))

player = input("Do you want to play again?:  Yes / No ")
   if user_choice in ["Yes", "yes", "y", "Y"]:
       pass

   elif user_choice in ["no", "No", "n", "N"]:
       break


   else:
       print("Your choice should be yes or not")











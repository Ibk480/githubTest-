#import random
#you can use askpython for resoursce pool
#random_integer = random.randint(1, 10)
#print(random_integer)

#random_float = random.random()
#print(random_float)

#love_score = random.randint(1, 100)
#print(f"Your love score is {love_score}")

#Data structure 
#for example list: fruits = [item1, item2]
#you can store items in a list and retrieve them in the order it was stored 
#for example below
#states_of_america = [0] this will bring the first item on the list 
#states_of_america =[-1] this will bring the last item on the list 
#you can change the stored information in a list 
#for example states_of_america[1] = "the information you wish to change"
#if you want to add to the list you created already....(Use the function append)
#states_of_america.append("Ibkland")
#you can add a whole new list using the extend function
#states_of_america.extend(["Ibkland", "Jack Bauer Land"])

#Auditorium Work
#names = ["angela", "Ben", "Jenny", "Micheal", "Chloe"]
#names = names_string.split(",")
#import random

#num_items = len(names)
#random_choice = random.randint(0, num_items -1)
#print(names[random_choice])


#reminder on Len function 
#Eg print(len(states_of_america))
# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
#     "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
#     "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
#     "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
#     "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
#     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
#     "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# print(len(states_of_america))
# print(states_of_america[49])
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states -1])
# dirty_dozen = ["strawberries", "Spinach", "Kale", "Nectarines", "Apples","Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# Rock paper scissors game
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# else:
#   print(game_images[user_choice])

#   computer_choice = random.randint(0, 2)
#   print("Computer chose:")
#   print(game_images[computer_choice])

#   if user_choice == 0 and computer_choice == 2:
#     print("You win!")
#   elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#   elif computer_choice > user_choice:
#     print("You lose")
#   elif user_choice > computer_choice:
#     print("You win!")
#   elif computer_choice == user_choice:
#     print("It's a draw")

#we want to start over for better understanding and documentation 
# Day 1
print("Hello World! ")
# Texts are known as strings 
# print("Hello World!\nHello World!") this is a manual way of duplication
# concatenation
print("Hello " + "Bukunmi")
# Using the input function. len is a function used to calculate length 
# input("What is your name?")
# print("Hello " + input("what is your name?"))
# Variables
# name = input("What is your name?")
# print(name)
# print(len(input("What is your name?")))
# name = input("What is your name?")
# length = len(name)
# print(length) (\n is used to go to the next page)

# print("Welcome to the band name generator")
# city = input("what's the name of the city you grew up in ?\n")
# pet_name = input("what's your pet's name?\n")
# Band_name = (city + " " +  pet_name)
# print("Your band name could be " + Band_name)



# Day Two (2)
# Data types, Numbers, Operations, Type conversion and F-Strings
# Strings(Texts, created with double quotes. Important to note that any thing even numbers inside the double quotes is treated as strings )
#  Integer(Whole number you can type them without the double quotes. Underscore(_) represents comma),
# Float(Any number with decimal point) 
# Boolean (True or False     begins with a capital letter   with no "" )
# print("Hello"[0]) This is done to print out the letter H. This can be done for the rest of them (This method is called subscripting)
# print(54 + 1)
# num_char = len(input("What is your name?"))
# print("Your name has " +  num_char) The lesson here is that you cannot add a string to an integer 
# print(type(num_char)) This function can be used to check data types 
# Typecasting or type conversion in the example below we converted integer to string
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")
# This is not limited to strings and integers only. Example below 
# a = float(123)
# print(70 + a)
# For exponetial sign (**) for mathematical operations PEMDAS is the order it follows. Multiplication and division are on the same level sort of
# print(2**2)
# print(int(3 * 3 + 3 / 3 - 3))
# print(round(8/3, 2)) #using the round function. using comma helps specify how many numbers you want to round it to 
# using the flow division 
# print(8 // 3)
# using varriables for example the result is divided again. If you ant to carry out another operation, just add = to the back
# result = 4 / 2
# result /=2 this is really handy in manipulating previous values
# print(result)
# F-string  goes in front of the double qoutes "" F string sort of allows you convert between data types..... not exactly but you get the idea 
# num_char = len(input("What is your name?")) take a look at the example below 
# print(f"Your name has   {num_char} ")
# score = 0
# height = 1.8
# iswinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {iswinning}")
# Final project for Day 2
# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill?\n"))
# People = int(input("How many people to split the bill?\n"))
# per_tip = int(input("What percentage tip would you like to give?\n"))
# pert_tip = (per_tip / 100)
# temp_bill = (total_bill * pert_tip)
# total_tip_bill = (temp_bill + total_bill)
# tip_amount = round(total_tip_bill / People)
# print(f"Each person should pay: {tip_amount}")


# Day 3
# Conditional Statements: if/else statement follwed by : find example below.
# Remember that you have to include the = sign if you want to carry along the value for the threshold 
# Nested if / else statement multiple conditional statements.... you can use elif function which means else if
# Logical Operators: comparison operators... <>= >= <=  ==(Equal to) !=(not equal to)
# , Code Blocks and Scope 
# water_level = 90
# if water_level > 80:
#     print("Drain water")
# else:
# #     print("continue")
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
# bill = 0

# if height >= 120: 
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth ticket are $7.")
#     elif age >= 45 or age<= 55:
#         print("Everything is going to be ok. You get to ride for free.")
#     else:
#         bill = 12
#         print("Adult ticket are $12.")
        
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         bill += 3 #you are adding 3 to any of the bill that meets the condition given
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry,you have to grow taller before you can ride.")
    
# Using logical operators 
# They are "and" when you are using this,(A and B) they both have to be true for the entire line of code to be true
# a = 12
# a > 15
# print(a)
#"or": using this operator, only one of the as to be true for the entire line to be true. it is only when both of them are false that the entire thing is false 
# "not" : This is just the opposite 


# Day 3 Project
# Quick tip : lower() is used to convert to lower case no matter how the text is written 
# print("Welcome to Treasure Island. ")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a cross road where do you want to go?. Type "Left" or "Right" ').lower() #Using single quotes at the beginning and end of the entire string allows you to use the double quotes as strings. Also the \ allows you to ignore the single quote infront of (you\re)

# if choice1  == "left":
#     choice2 = input('You came to a lake, There is an island in the middle of the lake. Type "wait" to wait for a boat, Type "swim" to swim across.').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue,\nWhich colour do you choose?").lower()
#         if choice3 == "red":
#             print("You got eaten by a lion. Game Over.")
#         elif choice3 == "yellow":
#             print("You lucky dog. You found the treasure, you win!.")
#         elif choice3 == "blue":
#             print("You suck, you bloody ass loser. You lose!!!")
#         else:
#             print("It's a room full of fire. You lose!!!")

        
#     else:
#         print("You got attacked by a megalodone. Game Over.")
        
    
    
    
# else:
#     print("You fell into a hole. Game Over.")
        
    
        
# Day 4 
# Randomisation and Python Lists
#You can get good resources from askpython.com

# import random
# import my_module


# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)


# random_float = random.random()
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}") #Using f string here allows you to express the integer along side the string
# Lists is a data structure(A way of organizing and storing data in python)
# List = [item1, Item2]
# states_of_America = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    # "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    # "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    # "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    # "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
    # "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
    # "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    # "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    # "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_America[-4]) #This is how you pull items from the list(when you use the negative sign, it starts counting from backwards ) 
# states_of_America[0] = "Bukunmi" #This is how you change items in a list
# states_of_America.append("Bukunmiland") #This is how you add items to the list(This adds single items i think )
# states_of_America.extend(["Bukunmiland", "Gabe'sland", "DunmoyeLand"]) #Remember that you have to put lists in a []
# print(states_of_America)
# print(len(states_of_America)) #counting
# print(states_of_America[49])
# num_of_states = len(states_of_America)
# print(states_of_America[num_of_states - 1]) #Try remember we were trying to solve an error

# fruits = ["Strawberries", "Peaches", "Pears", "Nectarines", "Apples", "Grapes", "Cherries", "Blueberries"]
# vegetables = ["Spinach", "Kale, collard & mustard greens", "Bell & hot peppers", "Green beans"]   
      
# dirty_dozen = [fruits, vegetables]  
# print(dirty_dozen)

# Final Project of the Day
# # Rock paper Scissors
# import random 



# rock = ('''____, O
#    /   /M|
#   /|MMMMMMMM
#   {| | // |}
# -_}| |/ \ |{_apx''')


# paper = (''' _ __   __ _ _ __   ___ _ __ 
# | '_ \ / _` | '_ \ / _ \ '__|
# | |_) | (_| | |_) |  __/ |   
# | .__/ \__,_| .__/ \___|_|   
# | |         | |              
# |_|         |_|''')


# scissors = (''' _       ,/'
#   (_).  ,/'
#    _  ::
#   (_)'  `\.
#            `\.''')




# game_images = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: #This line had to be on top for the other lines to run perfectly 
#     print("You typed an invalid number, you lose")
# else:
#     #This line had to be moved a second to solve for the inavailability of the image to represent the condition 
#     print(game_images[user_choice])
#     computer_choice = random.randint(0,2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win")
#     elif computer_choice == user_choice:
#         print("It's a draw")


# Day 5
# For Loops, Range and Code Blocks
# For Loop it allows you to execute the same line of code multiple times 
# fruits = ["Apple", "Peach", "Pear",]
# for objects in fruits:
#      print(objects)
#      print(objects + " Pie")
#      print(fruits)
# using loop with range function: it won't print the last number(Remember)
# for number in range(1, 20, 5): #the numbers signify start stop and step(this means how many paces you want it to jump)
#     print(number)
# total = 0 #she called this an accumilattor 
# for number in range(1, 101):
#     total += number
# print(total)
#               #Password Generator Project
# import random
# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '()', ')', '*', '+']

# print("Welcome to the pyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy Level 
# # password = ""
# # for char in range(1, nr_letters + 1):
# #     password += random.choice(letter)
    
# # for char in range(1, nr_symbols + 1):
# #     password += random.choice(symbols)
    
# # for char in range(1, nr_numbers + 1):
# #     password += random.choice(numbers)
# # print(password)
      
#     # random_char = random.choice(letter) This explains in details what she did
#     # password += random_char
#     # print(password)
    

# # # for num in range(1, nr_symbols + 1 ):
# #     random_num = random.choice(numbers)
# #     print(random_num)
    
# # Hard Level The reason for the hard level is because it will be easy to hack the password if the hacker knows the exact position of different characters
# password_list = []
# for char in range(1, nr_letters + 1):
#     password_list += random.choice(letter)
    
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
    
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
# print(password_list)
# # You using the shuffle function
# random.shuffle(password_list)
# print(password_list)
# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")


          # Day 6
# Code Blocks Functions
# Functions refer to resources in the chrome's bookmark
print("Hello")
num_char = len("Hello")
print(num_char)

# Defining Functions

def my_function():
    print("Hello")
    print("Bye")
    
my_function()  #Calling the function. (Using the function)

#Indentation four spaces for indentation  
# For the challenge in Reeborg's world
# This while loop was used 
# while not at_goal():       while loop
    # if front_is_clear():
    #     move()
    # else:
    #     jump()
    
# for steps in range(6)
    # jump()

# while something_is_true:
    # Do this 
    # Then do this
    #then do this until it is not longer true 

#   while loop can turn to an infinite loop if the condition never becomes false


        #Day 7

          # Hangman you need to create a flow chart. See your downlaods forrefrence 
import random
# Step one
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)



guess = input("Guess a letter: ").lower()
print(guess)

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
        
    else:
        display += "_"
print(display)     
        
a = "7"
b = "8"
print(a+b)

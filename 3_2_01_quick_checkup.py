# Create a simple Python command line application that does the following:

# Prints "Hello User!"
print('Hello User!')

# Then asks "What is your name?"
name = input('What is your name? ')

# Then responds "Hello <user's name>"
print(f'Hello {name}')

# Then asks: "What is your favorite number? "
number = int(input('What is your favorite number? '))

# Then responds: "Your favorite number is lower than mine.", 
# "Your favorite number is higher than mine.", or "Your favorite number is the same as mine!" depending on your favorite number.
import random

# enables random choice based on set list
# set_list_of_options = [1,2,3,4,5]
#fav_number = random.choice(set_list_of_options)

# random integer between start and end integer
rando_number = random.randint(2,10)
# print(rando_number)

# compares user selected number to computer-generated rando_number to output the appropriate if statement
if number > rando_number:
  print(f'Your favorite number is greater than mine.')
elif number < rando_number:
  print(f'Your favorite number is less than mine.')
else:
  print(f'your favorite number is the same as mine.')



# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
print(computer_choice)
if user_choice == 'r':
  if computer_choice == 'r':
    print('tied')
  elif computer_choice == 'p':
    print('lost')
  else:
    print('won')
elif user_choice == 'p':
  if computer_choice == 'r':
    print('won')
  elif computer_choice == 'p':
    print('tied')
  else:
    print('lost')
else:
  if computer_choice == 'r':
    print('lost')
  elif computer_choice == 'p':
    print('won')
  else:
    print('tied')
## code to run with numbers resetting at 0 each time
# set starting variable values
proceed = 'y'

# set while statement to loop as long as proceed equals 'y'
while proceed == 'y':
  # ask for user input
  total_numbers = int(input('How many numbers do you want to print? '))
  
  # starts number chain over at 0 each time
  i = 0

  # loops through numbers from 0 (starting value of i) to the user-defined number (total_numbers)
  while i <= total_numbers:
    # print all numbers 0 through total_numbers value
    print(i)
    # increment i counter by 1
    i += 1
  
  # asks for user input; if 'y' is entered, while loop starting at line 6 will continue
  proceed = input('Do you want to continue? (y)es, (n)o ')
  
## code to run with continuous chain of numbers
# proceed = 'y'
# i = 0

# while proceed == 'y':
#   total_numbers = int(input('How many numbers do you want to print? '))

## adds the previous value of i to the number that the user input
## to continue the number chain from where it left off
#   total_numbers += i

#   while i <= total_numbers:
#     print(i)
#     i += 1
    
#   proceed = input('Do you want to continue? (y)es, (n)o ')
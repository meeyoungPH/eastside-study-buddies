

# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 2

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
# Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.
for candy in candy_list:
  index = candy_list.index(candy)
  print(f'{index} {candy}')

# For example: "[0] Snickers"
# Create a second loop that runs for a set number of times determined by the variable allowance.
# For example: If allowance is equal to five, the loop should run five times.
# Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.

# set counter for while loop to 0
counter = 0

# loop will run as long as counter is less than the value for allowance
while counter < allowance:  
  
  # solicit a choice of candy from the user and store as in integer so that it can be used as an index number in the following line
  # choice is equal to the index number of the candy in candy_list
  choice = int(input('Choose a number of the candy you want: '))
  
  # adds the name of the candy from the candy_list to the candy_cart list
  candy_cart.append(candy_list[choice])
  
  # print to view the candies present in the candy_cart each iteration of the loop - this is a check for debugging purposes and can be commented out
  print(candy_cart)
  
  # the below statement is shorthand for counter = counter + 1
  counter += 1

# For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.
# Use another loop to print all of the candies selected to the terminal.

# iterate through each candy name in the candy_list
for candy in candy_list:
  # each time a new candy name is being compared, the counter for purchased candies is set to zero. 
  # This will count the number of that type of candy selected by the user.
  purchased = 0
  
  # next, iterate through each candy stored in the candy_cart that was selected by the user
  # compares each option ("candy") in the candy_list to each selection ("item") in the candy_cart
  for item in candy_cart:
    # if the the values for candy and item are equal, increment the purchased counter by 1
    if candy == item:
      purchased += 1
  
  # once the for loop is complete, print the name of the candy and the value of the purchased counter
  print(candy, purchased)

# Bonus
# Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.

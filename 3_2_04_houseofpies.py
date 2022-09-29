# Create an order form that displays a list of pies to the user in the following way:
# Welcome to the House of Pies! Here are our pies:

# ---------------------------------------------------------------------
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak

# store the pie choices in a list
pie_choices = ['(1) Pecan', '(2) Apple Crisp', '(3) Bean', '(4) Banoffee', '(5) Black Bun', '(6) Blueberry', '(7) Buko', '(8) Burek', '(9) Tamale', '(10) Steak']

# print a welcome message
print('Welcome to the House of Pies! Here are our pies:')

# loop through pie_choices to print each pie option in turn
for pie in pie_choices:
  print(pie)

# Then, prompt the user to enter the number for the pie they would like to order.

# set a starting value for the variable used in the while loop
proceed = "Yes"

# create an empty list to store user choices
picked_pies = []

# this while loop will run while proceed equals yes
while proceed == "Yes":
  
  # saves the number of the pie selected as an integer for use in the next line
  # note that the number corresponding to the pie in the printed menu is greater than the index position by 1
  choice = int(input('Which pie would you like? Enter a number. '))
  
  # add the name of the pie from pie_choices to the picked_pies list
  picked_pies.append(pie_choices[choice-1])
  
  # prints the list of user selected pies. Can be commented out, since this was for debugging.
  print(picked_pies)
  
  # Immediately follow up their order with Great! We'll have that <PIE NAME> right out for you, 
  # and then ask if they would like to make another order. If so, repeat the process.
  print(f"Great! We will have that {pie_choices[choice-1]} right out for you.")
  proceed = input('Would you like another pie? Yes or No: ')

# Once the user is done purchasing pies, print the total number of pies ordered.
print(f'{len(picked_pies)} pies ordered' )

# Modify the application so that at the conclusion of the transaction, the user's purchases are listed out, with the total pie count broken by each pie. For example:
# You purchased:
# 0 Pecan
# 0 Apple Crisp
# 0 Bean
# 2 Banoffee
# 0 Black Bun
# 0 Blueberry
# 0 Buko
# 0 Burek
# 0 Tamale
# 1 Steak

# loop through names of pies in pie_choices list
for pie in pie_choices:
  
  # set counter to 0 to start
  purchased_pies = 0
  
  # loop through user choices stored in picked_pies for comparison
  for choice in picked_pies:
    
    # compare user choice to current pie being compared in pie_choices
    if choice == pie:
      
      # if pies match, increment counter by 1
      # syntax below is the same as purchased_pies = purchased_pies + 1
      purchased_pies += 1
      
  # prints list of all available pies along with number of pies purchased of each
  print(pie, purchased_pies)
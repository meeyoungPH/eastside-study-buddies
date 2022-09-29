# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)

# this is the corresponding for statement in the comprehension format that can be written in one line.
result = [x for x in range(10)]
print(result)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)
    
# corresponding comprehension to the above for statement
result = [x for x in range(20, 30)]
print(result)

# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
for word in words:
    print(word)

# corresponding comprehension to the above for statement
# the output happens to look exactly like the words list
pbj = [word for word in words]
print(pbj)

# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")

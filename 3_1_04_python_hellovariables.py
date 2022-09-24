name = 'Bob'
country = 'USA'

age = 65
hourly_wage = 13

satisfied = False

daily_wage = hourly_wage * 8

# when printing using the traditional syntax (with plus signs between strings and variables)
# any non-string must be converted to string, like age in this example

print('Hello my name is ' + name + '. I am from ' + country + ' and I am ' + str(age) + ' years old.')

# f-string statements can print a mixture of variable types
print(f'Hello my name is {name}. I am from {country} and I am {age} years old.')
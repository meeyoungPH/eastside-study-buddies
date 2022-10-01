sample = [23,45,456,2,5,67,2323,56,7,123]

# prints length of list
length_of_list = len(sample)
#print(length_of_list) #10

sum_of_list = sum(sample)
#print(sum_of_list)

sample2 = [['Jun-10',34543],['Jun-11',3],['Jun-12',343],['Jun-13',341],['Jun-14',32],['Jun-15',33],['Jun-16',343]]

length_of_list2 = len(sample2)
print(length_of_list2)

# this will not work
# sum_of_list2 = sum(sample2) 


subtotal = []

# method 1: loop through the rows of data, where 'row' stores the actual values of data
for row in sample2: # row = ['Jun-10',34543'],['Jun-11',3], etc...
  subtotal.append(row[1])

print(subtotal) # [34543, 3, 343, 341, 32, 33, 343]
print(sum(subtotal)) # 35638

subtotal2 = []
# method 2: loop through the row numbers up to the length of the dataset
# use this method so that you can access rows above or below the current row
for rownumber in range(len(sample2)): # rownumber = 0 through 6
  subtotal2.append(sample2[rownumber][1]) 

  current_row_value = sample2[rownumber][1]
  # you can't do this part using method 1
  prior_row_value = sample2[rownumber-1][1]

print(subtotal2) # [34543, 3, 343, 341, 32, 33, 343]
print(sum(subtotal2)) # 35638


sample = [23,45,456,2,5,67,2323,56,7,123]

# prints length of list
length_of_list = len(sample)
#print(length_of_list) #10

sum_of_list = sum(sample)
#print(sum_of_list)

sample2 = [['Jun-10',34543],['Jun-11',3],['Jun-12',343],['Jun-13',341],['Jun-14',32],['Jun-15',33],['Jun-16',343]]

length_of_list2 = len(sample2)
print(length_of_list2)

# sum_of_list2 = sum(sample2)

subtotal = []
for row in sample2:
  subtotal.append(row[1])

print(subtotal)
print(sum(subtotal))

subtotal2 = []

for rownumber in range(len(sample2)): # rownumber = 0 through 6
  subtotal2.append(sample2[rownumber][1]) 

print(subtotal2)
print(sum(subtotal2))
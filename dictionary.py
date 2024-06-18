

# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating an empty dictionary
output = {}

# adding items to the dictionary using a loop
for i in range(len(keys)):
	output.update({keys[i]: values[i]})

# print output
print(output)





# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating an empty dictionary
output = {}

# adding items to the dictionary using a loop
for key, value in zip(keys, values):
	output[key] = value

# print output
print(output)




# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating an empty dictionary
output = {}

# adding items to the dictionary using a loop
for i, key in enumerate(keys):
	output[key] = values[i]

# print output
print(output)

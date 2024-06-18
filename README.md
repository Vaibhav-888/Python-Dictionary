# Python-Dictionary
Loop through the empty dictionary in python.


### Adding Items to a Dictionary in a Loop in Python

#### Introduction
In Python, you can dynamically add items to a dictionary within a loop using the dictionary’s key-value assignment. This article explains how to add items to a dictionary in a loop using Python programming.

#### Example
Input:
```python
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]
```
Output:
```python
{'Name': 'GeeksforGeeks', 'Website': 'https://www.geeksforgeeks.org/', 'Topic': 'Programming', 'Founded': 2009}
```

### Methods to Add Items to a Dictionary in a Loop
There are different methods to add items to a dictionary in a loop in Python. Below, we explain all the possible approaches with practical implementation.

### 1. Using For Loop and update Method
In this approach, we use a loop to iterate over keys and values and update the dictionary using the `update()` method. This method creates the dictionary and stores it in the `output` variable, which we then print.

```python
# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating  an empty dictionary
output = {}

# adding items to the dictionary using a loop
for i in range(len(keys)):
    output.update({keys[i]: values[i]})

# print output
print(output)
```

Output:
```python
{'Name': 'GeeksforGeeks', 'Website': 'https://www.geeksforgeeks.org/', 'Topic': 'Programming', 'Founded': 2009}
```

### 2. Using zip Method
In this approach, we use the `zip()` method in the for loop, which pairs corresponding keys and values to the output dictionary. This method properly creates the dictionary and adds it to the `output` variable.

```python
# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating  an empty dictionary
output = {}

# adding items to the dictionary using a loop
for key, value in zip(keys, values):
    output[key] = value

# print output
print(output)
```

Output:
```python
{'Name': 'GeeksforGeeks', 'Website': 'https://www.geeksforgeeks.org/', 'Topic': 'Programming', 'Founded': 2009}
```

### 3. Using enumerate Method
In this approach, we use the `enumerate()` method in the for loop to iterate over the keys, using the index to access the corresponding values and adding them to the `output` dictionary variable.

```python
# input data for dict
keys = ['Name', 'Website', 'Topic', 'Founded']
values = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]

# creating  an empty dictionary
output = {}

# adding items to the dictionary using a loop
for i, key in enumerate(keys):
    output[key] = values[i]

# print output
print(output)
```

Output:
```python
{'Name': 'GeeksforGeeks', 'Website': 'https://www.geeksforgeeks.org/', 'Topic': 'Programming', 'Founded': 2009}
```

### Conclusion
These methods demonstrate how to add items to a dictionary in a loop in Python. Each method provides a different approach to achieve the same result, and the choice of method depends on the specific requirements of your project.

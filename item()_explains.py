my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items(): # The .items() method is used with dictionaries in Python. 
    # It returns a view object that displays a list of a dictionary’s key-value tuple pairs. 
    # This is useful when you want to iterate over both keys and values in a dictionary.
    print(f"Key: {key}, Value: {value}")

# Output
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3    
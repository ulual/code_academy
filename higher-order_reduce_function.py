from functools import reduce
 
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list)

letters = ['r', 'e', 'd', 'u', 'c', 'e']

"""
Given a list of letters, use the reduce() higher-order function with a lambda function to combine the letters into a single word:
"""
# your code below:
word = reduce( lambda x,y: x + y, letters)
print(word)
# remember to import the reduce function

# store the result of your reduce function in the variable word


# print word


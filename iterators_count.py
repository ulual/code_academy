#Let’s use the count() itertool to manage our pet store!

#Instructions
#Checkpoint 1 Passed
#1.
#We have several 13.5lb bags of dog food to display. Our single shelving #unit however can only hold a maximum of 1,000lbs. Let’s figure out how #many bags of food we can display!

#First, import the itertools module at the top line of the code editor.

#Checkpoint 2 Passed
#2.
#Next, initialize a for loop with a count() iterator that keeps track of #the weight on the shelf.

#Within the for loop body:

#Provide a stop condition using max_capacity to terminate the loop
#Increment num_bags on each iteration.
#Checkpoint 3 Passed
#3.
#Print the num_bags result to see how many bags will fit on the shelving #unit.

# Checkpoint 1
import itertools
max_capacity = 1000
num_bags = 0

# Checkpoint 2
for i in itertools.count(start=13.5, step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1

# Checkpoint 3
print(num_bags)


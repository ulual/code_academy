#1.
#A list student_standings of four student’s class standings is inside the #generator function student_standing_generator().

#Finish the function by adding a for loop that traverses through the #student_standings list and yields 500 for each 'Freshman' value.

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for student in student_standings:
    if student == 'Freshman':
      yield 500
#Outside the function, retrieve the iterator object by calling #student_standing_generator() and set it to a variable called #standing_values.
standing_values = student_standing_generator()
#3.
#Print out the values within the returned standing_values generator using #the Python built-in function next().

#Two values of 500 should be retrieved since our student_standings list #contained two 'Freshman' values.
print(next(standing_values))
print(next(standing_values))
#4.
#Use next() one more time on the generator object. What occurs?
print(next(standing_values))
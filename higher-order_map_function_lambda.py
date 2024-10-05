grade_list = [3.5, 3.7, 2.6, 95, 87]

# Using lambda expression, write a code to convert gpa grade format into a percent grade 
# by creating a variable grades_100scale.
# Then list the results and assign a variable updated_grade_list.
# Your code below:
# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)
print(grades_100scale)
# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)


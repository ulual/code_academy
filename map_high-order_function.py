def add_2(a):
    return a+2
iter_list = [2,3,5]
added_2 = map(add_2, iter_list)
print(added_2)
print(list(added_2))

doubled = map(lambda input: input+2, iter_list)
print(list(doubled))

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:

# assign the result of your map function to the variable grades_100scale

grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 

updated_grade_list = list(grades_100scale)

# print updated_grade_list


print(updated_grade_list)
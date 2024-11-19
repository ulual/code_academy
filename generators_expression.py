def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Checkpoint 1
cs_courses = cs_generator()
for course in cs_courses:
  print(course)

# Checkpoint 2
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))

# Checkpoint 3
for course in cs_generator_exp:
  print(course)


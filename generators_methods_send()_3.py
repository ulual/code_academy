
max_students = 100

def generator():
  count = 0
  while count <= max_students:
    n = yield count
    if n is not None:
      count = n
    count += 1

student_id_generator = generator()
for i in student_id_generator:
  # Write your code below
  if i == 1:
    i = student_id_generator.send(50)
  
  print(i)
  
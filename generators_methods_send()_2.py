MAX_STUDENTS = 100

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    n = yield student_id
    if n is not None:
      student_id = n
      continue
      print(n)    
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
  if i == 1:
    i = student_id_generator.send(90)
  
  print(i)
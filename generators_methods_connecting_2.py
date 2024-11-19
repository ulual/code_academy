def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
# Checkpoint 1
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10,15)
  yield from non_science_students(25,30)
  
# Checkpoint 2
student_generator = combined_students()

for i in student_generator:
  print (i)

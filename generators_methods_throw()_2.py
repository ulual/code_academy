def generator():
  i = 0
  while True:
    yield i
    i += 1

my_generator = generator()
for item in my_generator:
    if item == 3:
        my_generator.throw(ValueError, "Bad value given")

    print(item)
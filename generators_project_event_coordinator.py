guests = {}
# Task #1
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  new_guest = None
  age = 0
  while True:
    if new_guest is None:
      line_data = text_file.readline().strip().split(",")
    if line_data is not None:
      if len(line_data) < 2:
      # If no more lines, close file
        text_file.close()
        break
      guest = line_data[0]
      age = int(line_data[1])
    
    new_guest = yield guest
    if new_guest is not None:
      new_guest_split = new_guest.split(",")
      guest = new_guest_split[0]
      age = int(new_guest_split[1])
    guests[guest] = age

def generator():
  count = 0
  while True:
    n = yield count
    if n is not None:
      count = n
    count += 1

# Task #1
print("======= TASK#1 1ST 10 GUESTS LIST =======")
names = read_guestlist('guest_list.txt')
for i in range(10):
  print(next(names))
print("=========================================\n")

# Task #2
#print(guests)
print("======= TASK#2 ADDING A NEW GUEST =======") 
print("======= Print guests before adding a new guest. =======")
print(guests)
names.send("Jane,35")
print("======= Print guests after adding a new guest. =======")
print(guests)
print("=========================================\n")

# Task #3
print("======= TASK#3 Next name after the 10th GUESTS (Dixie) =======")
#print(next(names))
#print(next(names))
#print(next(names))
#print(next(names))
#print(next(names))
names = read_guestlist('guest_list.txt')
for i in range(-9, 3, 1):
  print(next(names))
print("=========================================\n")

# Task #4
print("====== TASK#4 BARTENDER LIST FOR OVER 21 ======")
bartender_generator = (guest for guest, age in guests.items() if age >= 21)
for guest in bartender_generator:
  print(guest)
print("Guest List below for reference:")
print(guests)
print("=========================================\n")

# Task #5
print("====== TASK#5 Assign meals to each table and the seats at the tables. ======")
def table_one():
  for seat in range(1, 6):
    seat_info = "Seat {}".format(seat)
    yield ("Chicken", "Table 1", seat_info)

def table_two():
  for seat in range(1, 6):
    seat_info = "Seat {}".format(seat)
    yield ("Beef", "Table 2", seat_info)
  
def table_three():
  for seat in range(1, 6):
    seat_info = "Seat {}".format(seat)
    yield ("Fish", "Table 3", seat_info)
print("=========================================\n")
# Task #6
print("====== TASK#6 To assign a table and seat number with meal selection to each guest. ======")
import itertools
tables = itertools.chain(table_one(), table_two(), table_three())
guests_seats = ((guest, next(tables)) for guest in guests.keys())
for seat in guests_seats:
  print(seat)
print("=========================================\n")
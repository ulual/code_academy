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

# Task #1
print("======= GUEST LIST =======")
guest_generator = read_guestlist("guest_list.txt")
guest_counter = 0
for guest in guest_generator:
  if guest_counter < 10:
    print(guest)
    guest_counter += 1
  else:
    break

# Task #2
guest_generator.send("Jane,35")

# Task #3
for guest in guest_generator:
  print(guest)

# Task #4
print()
print("===== BARTENDER LIST =====")
bartender_generator = (guest for guest, age in guests.items() if age >= 21)
for guest in bartender_generator:
  print(guest)

# Task #5
print()
print("=== TABLES SEATS ===")
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
    yield ("Chicken", "Table 3", seat_info)

# Task #6
import itertools
tables = itertools.chain(table_one(), table_two(), table_three())
guests_seats = ((guest, next(tables)) for guest in guests.keys())
for seat in guests_seats:
  print(seat)
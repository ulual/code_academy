def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # Checkpoint 5
    location = 'back'
  return location

# Checkpoint 1
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

# Checkpoint 2 
def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

#Checkpoint 3
def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

# Checkpoint 4
test_row_1()
test_row_20()
test_row_40()

#The code provided is a simple test suite for the function `get_nearest_exit`, which determines the nearest exit location based on a given row number. Here's a breakdown of the key concepts:
#1. **Conditional Statements**: The `get_nearest_exit` function uses `if`, `elif`, and `else` statements to determine the location of the nearest exit based on the `row_number`. If the row number is less than 15, the exit is at the 'front'. If it's less than 30, the exit is in the 'middle'. Otherwise, it's at the 'back'.
#2. **Assertions**: The `assert` statements in the test functions check if the `get_nearest_exit` function returns the expected result. If the condition is false, an error message is displayed.
#3. **Testing Functions**: Each test function (`test_row_1`, `test_row_20`, `test_row_40`) tests a specific case for the `get_nearest_exit` function. They are called at the end to run the tests.
#This code helps ensure that the `get_nearest_exit` function behaves as expected for different row numbers.
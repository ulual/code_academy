# Checkpoint 1
staff = {
  'Austin': {
      'floor managers': 0,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 1,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 0,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Checkpoint 2
  try:
    print_staff_report(location, staff)
  # Checkpoint 3
  except:
    print('Could not print sales report for ' + location)

#The code provided is designed to print a report of staff at different locations. Here's a breakdown of the key concepts:
#1. **Nested Dictionaries**: The `staff` dictionary contains other dictionaries for each location. Each inner dictionary holds the number of 'floor managers' and 'sales associates'.
#2. **Function Definition**: The `print_staff_report` function takes a location and a dictionary of staff numbers. It calculates the ratio of sales associates to floor managers and prints a report.
#3. **Error Handling with `try` and `except`**: The `try` block attempts to call `print_staff_report`. If an error occurs (like division by zero when there are no managers), the `except` block catches it and prints an error message.
#4. **Looping through a Dictionary**: The `for` loop iterates over each location and its corresponding staff dictionary in `staff.items()`.
#In this code, if a location has zero floor managers, a division by zero error will occur, and the `except` block will handle it by printing an error message.
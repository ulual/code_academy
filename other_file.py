# other_file.py
from employee import Employee

def create_employee():
  print("Employee is starting their job...")
  employee1 = Employee()
  employee1.name = "Blake"
  employee1.working(employee1.name)

create_employee();

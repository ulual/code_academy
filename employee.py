# employee.py
class Employee(object):
  name = "Sam"
  company = "ILoveCode Inc."
  age = 30
  is_on_vacation = False

  def working(self, employee_name):
    self.name = employee_name
    print(f"{employee_name} is working")
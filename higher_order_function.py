def total_bill(func, value):
    total = func(value)
    return total

def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total

print(total_bill(add_tax, 100))
print(total_bill(add_tip, 100))

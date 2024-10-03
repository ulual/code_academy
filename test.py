def print_data(positional_arg, **data):
  print(positional_arg)
  for arg in data.values():
    print(arg)

print_data('position 1', a='arg1', b=False, c=99)
#Comments

total = 100
def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return tax
  return new_total

print(add_tax)
print(add_tax(100))


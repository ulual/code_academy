def print_data(positional_arg, **data):
  print(positional_arg)
  for arg in data.values():
    print(arg)

print_data('position 1', a='arg1', b=True, c=100)
#Comments

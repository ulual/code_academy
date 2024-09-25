# name_and_namespace
#Built-In
print(dir(__builtins__))

# Global
print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 
print(globals())
# Write Checkpoint 2 here: 
global_variable = 'global'
# Write Checkpoint 3 here: 
def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'
print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here: 
print(globals())

# Local
global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'   
  print(num1 + num2)
  print(locals())

add(5, 10) 

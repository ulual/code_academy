print(globals())
# globals output
# None}

def simple_math_func():
  x = 10
  y = 2
  mult = x * y
  add = x + y

print(locals())
# locals output
# None, 'simple_math_func': <function simple_math_func at 0x103cc85e0>}
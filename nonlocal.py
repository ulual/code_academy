def enclosing_function():
  var = "value"

  def nested_function():
    nonlocal var
    var = "new_value"

  nested_function()
  print(var)

enclosing_function()

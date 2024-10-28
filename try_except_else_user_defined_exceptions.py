# Checkpoint 1

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

# Checkpoint 2
class InventoryError(Exception):
  pass

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  # Checkpoint 3
  if quantity > supply:
    raise InventoryError
  # Checkpoint 4
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 1 # Change the value to show the exception.
submit_order(instrument, quantity)
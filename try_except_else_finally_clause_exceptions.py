customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
# Write your code below:
finally:
  database.disconnect_from_database()

# Output

#Establishing connection to instrument database server...
#Instrument: Kora
#Family: Strings
#Origin: West Africa
#Kora
#Destroying connection to instrument database server...
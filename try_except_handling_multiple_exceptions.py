# Checkpoint 1
instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo' # Type an instrument that is not listed in the dictionary to show a KeyError.
discount = 20 # Change this digit into a str(string) ex. '20' to show a TypeError.
# To show KeyError or TypeError, change the variable name discount to discount1.

# Checkpoint 2
try:
  display_discounted_price(instrument, discount)
# Checkpoint 3
except KeyError:
  print('An invalid instrument was entered!')
# Checkpoint 4
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')
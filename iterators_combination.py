#Now, let’s try using a combinations itertool within our pet store!

#Instructions
#Checkpoint 1 Passed
#1.
#We have another shelving unit to display by the register that can only hold 3 collars. We have a list of #collars of varying colors and sizes.

#We want to know how many different combinations exist to display a set of 3 collars. Use the combinations() #itertool to do this. Set the returned iterator to a variable named collar_combo_iterator.

#Checkpoint 2 Passed
#2.
#Using a for loop, print each item in collar_combo_iterator to see all the possible collar combinations.

import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Checkpoint 1
collar_combo_iterator = itertools.combinations( collars , 3 )

# Checkpoint 2
for combo in collar_combo_iterator:
  print( combo )
#1. We have separate lists of SKUs for each bag of dog food per brand. Obtain a master list of SKU numbers #for all bags of dog food, regardless of brand.

#Use the chain() itertool set to a variable named all_skus_iterator to combine the SKU lists.

#Checkpoint 2 Passed
#2. Using all_skus_iterator implement a for loop to output each SKU.

import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for skus in all_skus_iterator:
  print(skus)
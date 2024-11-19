dog_foods = {
    "Great Dane Foods": 4,
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8
}

for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags")

dog_food_iterator = iter(dog_foods)
print(dog_food_iterator)

sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
sku_iterator_object_one = sku_list.__iter__()
sku_iterator_object_two = iter(sku_list)
print(dir(sku_list))
print(sku_iterator_object_one)
print(sku_iterator_object_two)

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = sku_iterator.__next__()
print(next_sku)

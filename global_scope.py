#Code Academy code
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}
def print_available(color):
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')
#def print_all_colors_available():
#  for color in paint_gallons_available:
#    print(color)

print_available('blue')
#print_all_colors_available()

#My code
#dictionary of my dogs.
name_of_my_dog = {
  'Kolohe': 3,
  'Emma': 1,
  'Pono': 1
}
#function 1
def print_of_my_dogs_name(dog_name):
  print('My dog age is ' + str(name_of_my_dog[dog_name]) + ' and the name is ' + dog_name + '.')
#function 2
def print_all_dog_name():
  for dog_name in name_of_my_dog:
    print(dog_name)

#function 1
print_of_my_dogs_name('Kolohe')
#function 2
print_all_dog_name()


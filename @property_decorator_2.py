class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


box = Box(45)

box.setWeight(-5) 
print(box.getWeight())

box.setWeight(5)
print(box.getWeight())

box = Box(10)

print(box.weight) #this calls .getWeight()

box.weight = 5 #this called .setWeight()

del box.weight #this calls .delWeight()

box.weight = 15 #box.__weight is unchanged

print(box.weight) #this calls .getWeight()

#Test
#Test_2
#Test_3

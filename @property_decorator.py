class Box:
  def __init__(self, weight):
    self.__weight = weight # "__weight" is a private attribute because is using a "__" dunder notation.

  def getWeight(self): # getter
    return self.__weight
 
  def setWeight(self, weight): # setter
    if weight >= 0:
      self.__weight = weight

box = Box(10)

box.setWeight(-5) 
print(box.getWeight()) # It is not going to print a -5 because it is only going to pass a weight >= to 0.

box.setWeight(10)
print(box.getWeight())
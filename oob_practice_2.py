class Bird:
  # Class attribute
  is_hungry = True

parakeet = Bird()
parrot = Bird()


print("Birds are hungry!")
print("Feeding birds...")

parakeet.is_hungry = True
parrot.is_hungry = True

print("Birds fed!")
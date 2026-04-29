pets = []
removedPets = []

quantityNames = int(input("enter quantity of pet names: "))

for i in range(quantityNames):
    pet_name = input(f"enter pet name {i + 1}: ")
    pets.append(pet_name)

print("\npets:")
for pet in pets:
    print(pet)

while pets:
    pet_removed = pets.pop()
    removedPets.append(pet_removed)

print("\nremoved pets pile:")
print(removedPets)

while removedPets:
    recovered_pet = removedPets.pop()
    pets.append(recovered_pet)

print("\nrestored pets:")
for pet in pets:
    print(pet)
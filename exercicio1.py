quantity = int(input("enter quantity of animals that are entering in: "))

petsPetPallet = []

for i in range(1, quantity):
    animal = input(f"enter animal number #{i + 1}: ")
    petsPetPallet.append(animal)

index = int(input(f"wanna see a specific animal? Enter index (0 to {quantity - 1}): "))

print(petsPetPallet[index])
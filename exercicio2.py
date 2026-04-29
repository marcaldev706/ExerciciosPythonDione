print("enter the following animals names: (Bingo, Sabrino, Kiko, Princesa n' Bobby)")

firstAnimalName = input("first name: ")
secondAnimalName = input("second name: ")
thirdAnimalName = input("third name: ")
forthAnimalName = input("forth name: ")
fifthAnimalName = input("fifth name: ")

petsPetPallet = [
    firstAnimalName,
    secondAnimalName,
    thirdAnimalName,
    forthAnimalName,
    fifthAnimalName
]

request = input("enter a name of an animal, and we will see if it's on the list: ")

for i in range(len(petsPetPallet)):
    if petsPetPallet[i] == request:
        print(f"animal found in index {i}: {petsPetPallet[i]}")
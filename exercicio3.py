dogFood = 'Ração Arcanine para cães adultos'
beans = 'Semente de girassol Viridian'
cook = 'Biscoito Persa'
foodRatata = 'Ração Ratata para Hamster'
fishFood = 'Alimento para peixes magikarp'

productList = [dogFood, beans, cook, foodRatata, fishFood]

while True:
    for i in range(len(productList)):
        print(f"{i}: {productList[i]}")

    try:
        index = int(input("enter a index number: "))

        if 0 <= index < len(productList):
            print("product:", productList[index])
        else:
            print("invalid index")

    except ValueError:
        print("enter a valid index number: ")

    again = input("wanna try again? (y/n): ").lower()

    if again != 'y':
        print("breaking program...")
        break
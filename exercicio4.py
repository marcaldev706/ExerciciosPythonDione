shoppingList = []

shoppingList.append("Ração Arcanine")
shoppingList.append("Biscoito Persa")
shoppingList.append("Semente de girassol")
shoppingList.append("Alimento para peixes Magikarp")

print("Itens at the list so far: ")
print("\nShopping list:")
for i in shoppingList:
    print("Item:", i)

response = input("wanna enter more items? (y/n): ").lower()

while response == 'y':
    item = input("enter item: ")
    shoppingList.append(item)
    response = input("wanna add another item? (y/n): ").lower()

print("\nShopping list:")
for i in shoppingList:
    print("Item:", i)
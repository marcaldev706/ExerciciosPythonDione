itensQuantity = int(input("enter quantity of items that are entering in stock: "))

itemName = []
itemPrice = []
itemQuantity = []

for i in range(itensQuantity):
    name = input("nter item name: ")
    price = float(input("enter item unit price: "))
    quantity = int(input("enter item quantity: "))
    
    itemName.append(name)
    itemPrice.append(price)
    itemQuantity.append(quantity)

print("\nItems registered:")
for i in range(itensQuantity):
    print(f"{i} - {itemName[i]} , price: {itemPrice[i]} , Stock: {itemQuantity[i]}")

cart_total = 0

while True:
    choice = input("\nselect item index and quantity or type 'end': ")
    
    if choice.lower() == "end":
        break

    try:
        index, quantity = map(int, choice.split())

        if index < 0 or index >= itensQuantity:
            print("invalid index!")
            continue

        if quantity > itemQuantity[index]:
            print("there is no stock for that!")
            continue

        itemQuantity[index] -= quantity
        cart_total += itemPrice[index] * quantity

        print(f"Added {quantity}x {itemName[index]} to cart.")

    except:
        print("invalid input")

print(f"\ntotal price: {cart_total}")
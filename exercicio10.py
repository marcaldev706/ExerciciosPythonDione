stock = []

quantityStock = int(input("enter growlith store quantity of items: "))

for i in range(quantityStock):
    item = input(f"enter stock item {i + 1}: ")
    stock.append(item)

print("\growlith stock items:")


response = input("wanna Growlith stock items? (y/n): ")

if response == 'y':
    for item in stock:
        print(item)
        print("thank you")
else:
    print("thank you.") 
    
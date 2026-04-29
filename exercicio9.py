queue = []

quantityOrders = int(input("enter quantity of orders: "))

for i in range(quantityOrders):
    order = input(f"enter order #{i + 1}: ")
    queue.append(order)

print("\norders:")
for order in queue:
    print(order)

print("\r processing orders, wait a bit...")

for i in range(len(queue)):
    currentOrder = queue.pop(0)
    print(f"order processed: {currentOrder}")
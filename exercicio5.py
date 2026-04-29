clientsQueue = []

clientsQuantity = int(input("how many clients are in line? "))

for i in range(clientsQuantity):
    name = input(f"write clients name {i+1}: ")
    clientsQueue.append(name)

print("\nline:")
for cliente in clientsQueue:
    print(cliente)

print("\ninitiating...\n")

for i in range(len(clientsQueue)):
    cliente_atual = clientsQueue[i]
    print(f"client reception: {cliente_atual}")

    print("shopping process...\n")

print("all clients has been attended!")
historyList = []

quantity = int(input("how any pages did you visit? "))

for i in range(quantity):
    page = input(f"enter page {i + 1}: ")
    historyList.append(page)

response = input("wanna visit history? (y/n): ")

if response == 'y':
    print("\nvisit history:")
    
    for visit in historyList:
        print(visit)
else:
    print("thank you, see you next time.")    
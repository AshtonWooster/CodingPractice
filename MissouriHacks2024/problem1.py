items1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 3]
max_items = 5
current_bag = []


def sum(arr):
    total = 0
    for item in arr:
        total = total + item
    
    return total


for item in items1:
    if sum(current_bag) + item > max_items:
        current_bag = [item]
    else:
        current_bag.append(item)
    
print("Bag: \n")

resultant = ""
for item in current_bag:
    resultant = resultant + str(item) + " "

print(resultant)
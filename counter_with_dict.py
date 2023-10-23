items = {}
while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item == "done":
        break
    elif item in items:
        items [item] += 1
    else:
        items [item] = 1

print(items)
            

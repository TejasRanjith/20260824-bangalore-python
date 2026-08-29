bag = ["staff", "potion", "spellbook"]
item = input("Ënter the item to add to the bag: ")
bag.append(item)
print("Portal transition activated!")
print("Elected Oldest item: ",bag.pop(0))
print("Current items in the magic bag: ",bag)

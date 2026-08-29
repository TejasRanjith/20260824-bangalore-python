vip = ['Guido', 'Esha', 'Rajan', 'Kishori']
while True:
    name = input("Enter your name: ")
    if name in vip:
        print(f"{name} moved to the front!")
        index = vip.index(name)
        vip.pop(index)
        vip.insert(0,name)
    else:
        print("Access denied. Not on the VIP list.")
    print("Current VIP queue: ", vip)
        
    if name == "exit":
        break
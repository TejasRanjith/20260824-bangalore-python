train = ["oil", "iron", "gold", "coal", "timber", "coal"]

inspect = input("Enter the resource to inspect: ")
if inspect in train:
    print("Number of coal wagons:", train.count(inspect))
    print("First coal wagon is at index: ", train.index(inspect))
else:
    print("Resource not found on train!")

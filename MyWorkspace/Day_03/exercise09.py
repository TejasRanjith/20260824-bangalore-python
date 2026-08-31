n = int(input("Enter the number of soldiers: "))
k = int(input("Enter the Elimination Interval: "))
remove = k-1
soldiers = [n+1 for n in range(n)]

print("Soldier circle initialized:",soldiers)

for i in range(len(soldiers)-1):
    print("Eliminated soldier:",soldiers.pop(remove),"  Remaining:",soldiers)
    remove+=k-1
    remove = remove % (n-(i+1))

print("The sole survivor is:",soldiers[0])
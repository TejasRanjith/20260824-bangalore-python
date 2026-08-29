n = int(input("Enter the number of soldiers: "))
soldiers = [n+1 for n in range(n)]
k = int(input("Enter the Elimination Interval: "))
i=0
while n > 1 and i < 5:
    print(soldiers.pop(i+k-1))
    print(soldiers)
    n-=1
    i+=1
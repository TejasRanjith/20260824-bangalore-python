numbers = [n+1 for n in range(10)]

print(list(filter(lambda x:x%2,numbers)))
print(list(map(lambda x: x*2,numbers)))
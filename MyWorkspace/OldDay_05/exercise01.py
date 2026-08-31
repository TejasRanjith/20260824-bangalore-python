def factorial(n):
    tot = 1
    for num in range(n,0,-1):
        tot = tot*num
    return tot


def combinations(n,r):
    if n >= r:
        return factorial(n)/(factorial(r) * factorial(n-r))
    else:
        return None

print(combinations(1,0))
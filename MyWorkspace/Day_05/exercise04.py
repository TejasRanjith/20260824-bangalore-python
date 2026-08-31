def power(base,exp):
    if exp > 1:
        return int(base*power(base,exp-1))
    else:
        return base
print(power(2,5))
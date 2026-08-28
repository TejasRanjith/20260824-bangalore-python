def main():
    d,flag=2,True
    n = int(input("Enter a positive number: "))
    if n<0:
        print("Enter a positive number please.")
    elif n == 1:
        print("number 1, is neither prime nor composite.")
    else:
        while d <= n//2:
            if n % d == 0:
                d+=1
                print(f"{n} is not a prime number because it is divisible by {d-1}.")
                flag = False
                break
            d+=1
        if flag:
            print(f"{n} is a prime number.")
            

if __name__ == '__main__':
    main()
    
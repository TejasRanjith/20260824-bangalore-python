def main():
    n = int(input("Enter a natural number to calculate sum upto: "))
    n=n//1
    if n <= 0:
        print("Enter a valid natural number!")
    else:
        sum = (n*(n+1))/2
        print(sum)

if __name__ == '__main__':
    main()
    
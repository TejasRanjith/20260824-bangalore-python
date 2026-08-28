def main():
    n = abs(int(input("Please Provide an Integer: ")))
    if n % 2 == 0:
        print(f"{n} is odd.")
    else:
        print(f"{n} is even.")
        
if __name__ == '__main__':
    main()
    
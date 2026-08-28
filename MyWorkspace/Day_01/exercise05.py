def main():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    operator = input("Enter the operator: ")
    print("Result: ",eval(f"{num1} {operator} {num2}"),sep="")
    
if __name__ == '__main__':
    main()
    
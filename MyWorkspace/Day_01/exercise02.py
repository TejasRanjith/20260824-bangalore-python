def main():
    lim,output = 0,""
    a,b=0,1
    n=int(input("Enter a positive number"))
    if n<0:
        print("please enter a valid number")
    elif n==0:
        print("Empty series.")
    else:
        output+=f"{a},"
        while lim<n-1:
            output+=f"{b},"
            a,b = b,a+b;
            lim+=1
    print(output[:-1])
main()
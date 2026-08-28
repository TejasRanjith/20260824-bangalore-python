def main():
    email = input("Enter the Email: ")
    if "@" in email:
        new = email.split(sep = "@")
        print(new[0])
    else:
        print("Invalid Email!")

if __name__ == '__main__':
    main()
    
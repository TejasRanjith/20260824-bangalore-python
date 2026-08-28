def main():
    full_name = input("Enter your full name: ")
    name = full_name.split()
    output = ""
    for word in name[:-1]:
        output+=f"{word[0]}. "
    output+=name[-1]
    print(output)

main()
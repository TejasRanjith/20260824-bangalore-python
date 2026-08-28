def main():
    sentence = input("Enter your sentence : ")
    output = ""
    new = sentence.split()
    for word in new:
        output+= word[0].upper()
        output+= word[1:].lower()
        output+= " "
    print(output)

if __name__ == '__main__':
    main()
    
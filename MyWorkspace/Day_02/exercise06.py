def main():
    phrase = input("Enter the Phrase : ")
    shift = int(input("Enter the Shift Integer: "))
    output=""
    for letter in phrase:
        if letter.isupper():
            output += chr(ord(letter)+shift).upper()
        elif letter.islower():
            output += chr(ord(letter)+shift).lower()
        else:
            output += letter
    print(output)
main()

def main():
    sentence = input("Enter a sentence to analyze: ")
    char = len(sentence)
    words = len(sentence.split())
    print("Total Characters: ", char)
    print("Total Words: ", words)

if __name__ == '__main__':
    main()
    
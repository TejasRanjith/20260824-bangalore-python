def main():
    phrase = input("Enter the Phrase: ")
    sub = input("Enter the Substring to count: ")
    count,index = 0,phrase.find(sub)
    while index >-1:
        count+=1
        index = phrase.find(sub,index+1)
    print(count)
    
main()
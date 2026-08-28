def main():
    k = 0
    phrase = input("Enter the Phrase: ") + " "
    while k < len(phrase):
        compressed,count = "",1
        for i in range(len(phrase)-1):
            if phrase[i] == phrase[i+1]:
                count+=1
            else:
                compressed+=f"{phrase[i]}{count}"
                count =1
        k+=1
    if len(compressed) > len(phrase):
        print(phrase)
    else:
        print(compressed)
        
main()
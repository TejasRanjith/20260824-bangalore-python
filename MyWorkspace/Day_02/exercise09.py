def palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False

def main():
    text = input("Enter the Text String: ")
    pal,j = [],0
    while j <= len(text):
        for i in range(2,len(text)):
            if palindrome(text[j:i]) and len(text[j:i]) > 1:
                pal.append(text[j:i])
        j+=1

    print(max(pal))
    print(pal)

main()
            
    

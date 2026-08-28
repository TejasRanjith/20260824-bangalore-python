def main():
    k,j=0,0
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = []
    while j < len(words):
        group = [words[j]]
        for i in range(1,len(words)-1):
            if sorted(words[j]) == sorted(words[i]):
                group.append(words[i])
            else:
                print("False")
        j+=1
        result.append(group)
        
    print(result)
        
    
main()
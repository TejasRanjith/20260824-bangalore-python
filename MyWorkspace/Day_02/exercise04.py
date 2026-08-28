def main():
    sentence = input("Enter the Sentence: ")
    count=0
    count_a,count_e,count_i,count_o,count_u = 0,0,0,0,0
    for char in sentence:
        if char == 'a':
            count_a+=1
        elif char == 'e':
            count_e+=1
        elif char == 'i':
            count_i+=1
        elif char == 'o':
            count_o+=1
        elif char == 'u':
            count_u+=1
        elif char.isalpha():
            count+=1
        else:
            pass
    print(f"""
Vowel Frequencies:
a: {count_a}
e: {count_e}
i: {count_i}
o: {count_o}
u: {count_u}
Total Consonants: {count}
          """)
            
            

if __name__ == '__main__':
    main()
    
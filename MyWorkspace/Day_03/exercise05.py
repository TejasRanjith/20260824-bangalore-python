phrase = input("Enter the Secret Message : ")
words = phrase.split()
output = []
for word in words:
    output.append(word[::-1])
print(' '.join(output))

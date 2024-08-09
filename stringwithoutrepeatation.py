def substring(s):
    char_set = set(s)
    return len(char_set),s
   
word = input("Enter a string: ")
result = substring(word)
print("The length of substring:""is", result[0], "and the substring is", result[1])

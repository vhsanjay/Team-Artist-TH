def permute(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for p in permute(remaining):
            permutations.append(char + p)
    return permutations

word = input("Enter a string: ")
result = permute(word)
print("All permutations of the string are:", result)

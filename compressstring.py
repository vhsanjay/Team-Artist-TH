def compress_string(string):
    if not string:
        return string
    compressed = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed += string[i - 1] + str(count)
            count = 1
    compressed += string[-1] + str(count)
    if len(compressed) < len(string):
        result = compressed
    else:
        result = string
    return result

word = input("Enter a string to compress: ")
if word:
    compressed_string = compress_string(word)
    print("Compressed string:", compressed_string)
else:
    print("No input provided.")

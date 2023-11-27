def split_and_join(line):
    words = line.split(" ")
    joined_string = "-".join(words)
    return joined_string
line = "this is a string"
result = split_and_join(line)
print(result)
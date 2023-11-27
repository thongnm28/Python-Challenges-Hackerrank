def swap_case(s):
    swapped_string = ""
    for char in s:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char
    return swapped_string

s = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(s)
print(result)
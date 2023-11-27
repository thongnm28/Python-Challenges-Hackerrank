def validate_string(string):
    results = [
        any(char.isalnum() for char in string),
        any(char.isalpha() for char in string),
        any(char.isdigit() for char in string),
        any(char.islower() for char in string),
        any(char.isupper() for char in string)
    ]
    return results
string = input()
results = validate_string(string)
for result in results:
    print(result)
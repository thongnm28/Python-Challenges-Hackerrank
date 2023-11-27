import string

def print_rangoli(size):
    lst = list(string.ascii_lowercase)
    lst = lst[:size]
    width = 4 * (size - 1) + 1

    for i in range(1, size + 1):
        res = lst[size - i + 1:][::-1] + lst[size - i:]
        line = "-".join(res).center(width, "-")
        print(line)

    for i in range(1, size):
        res.pop(size - i)
        res.pop(size - i - 1)
        line = "-".join(res).center(width, "-")
        print(line)
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
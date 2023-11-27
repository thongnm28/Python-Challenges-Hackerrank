if __name__ == '__main__':
    N = int(input())
    list = []

    for _ in range(N):
        command, *args = input().split()

        if command == 'insert':
            index = int(args[0])
            element = int(args[1])
            list.insert(index, element)
        elif command == 'print':
            print(list)
        elif command == 'remove':
            element = int(args[0])
            list.remove(element)
        elif command == 'append':
            element = int(args[0])
            list.append(element)
        elif command == 'sort':
            list.sort()
        elif command == 'pop':
            list.pop()
        elif command == 'reverse':
            list.reverse()
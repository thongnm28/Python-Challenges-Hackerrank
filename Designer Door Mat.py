def mat(breadth, length):
    a = '-'
    b = '.|.'

    for i in range(1, breadth, 2):
        f = (b * i).center(breadth * 3, a)
        print(f)

    print('WELCOME'.center(3 * breadth, a))

    for i in range(breadth - 2, 0, -2):
        h = (b * i).center(breadth * 3, a)
        print(h)

N, M = map(int, input().split())
mat(N, M)
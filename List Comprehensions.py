if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                coordinates.append([i, j, k])

    filtered_coordinates = []
    for coord in coordinates:
        if sum(coord) != n:
            filtered_coordinates.append(coord)

    print(filtered_coordinates)
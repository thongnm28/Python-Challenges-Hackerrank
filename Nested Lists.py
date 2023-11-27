if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [score for _, score in students]
    second_lowest_score = sorted(set(scores))[1]

    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    second_lowest_students.sort()

    for name in second_lowest_students:
        print(name)
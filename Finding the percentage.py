if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *marks = input().split()
        scores = list(map(float, marks))
        student_marks[name] = scores
    query_name = input()

    query_scores = student_marks[query_name]
    average_score = sum(query_scores) / len(query_scores)

    print("{:.2f}".format(average_score))
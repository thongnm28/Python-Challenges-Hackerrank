if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)
    runner_up_score = max(filter(lambda x: x != max_score, arr))

    print(runner_up_score)
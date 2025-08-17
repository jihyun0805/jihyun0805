import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_max = 0
    for i in range(N):
        for j in range(M):
            flower_sum = matrix[i][j] # 기준점
            distance = matrix[i][j] # 기준점에 있는 숫자 즉, 거리
            for r in range(4):
                for c in range(1, distance+1):
                    nx = i + di[r] * c
                    ny = j + dj[r] * c

                    if 0 <= nx < N and 0 <= ny < M:
                        flower_sum += matrix[nx][ny]
            sum_max = max(flower_sum, sum_max)

    print(f'#{test_case} {sum_max}')
# Считываем три числа: N (ряды), M (колонки) и K (целевое количество кварталов)
N, M = map(int, input().split("x"))
K = int(input())


if (K % N == 0 and K // N < M) or (K % M == 0 and K // M < N):
    print("успешно")
else:
    print("неосуществимо")
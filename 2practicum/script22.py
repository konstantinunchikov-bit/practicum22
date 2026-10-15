
N, K, M = map(int, input().split())

total_rides = 2 * N

runs = (total_rides + K - 1) // K


total_time = runs * M

print(total_time)

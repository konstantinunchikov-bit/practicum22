
start, end = input().split('-')

x1 = ord(start[0]) - ord('a') + 1
x2 = ord(end[0]) - ord('a') + 1

y1 = int(start[1])
y2 = int(end[1])
dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")

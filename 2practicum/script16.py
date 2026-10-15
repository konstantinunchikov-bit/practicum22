a, b = map(int, input().split("x"))
if a <= 13 and b <= 13:
    if a**2 + b**2 <= 169:
        print("да")
    else:
        print("нет")
else:
    print("нет")

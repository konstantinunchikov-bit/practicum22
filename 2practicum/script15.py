a = int(input())
if (a > 999 and a <= 9999):
    b = str(a)
    if b[0] == b[1] or b[0] == b[2] or b[0] == b[3]:
        print("error")
    elif b[1] == b[0] or b[1] == b[2] or b[1] == b[3]:
        print("error")
    elif b[2] == b[0] or b[2] == b[1] or b[2] == b[3]:
        print("error")
    elif b[3] == b[0] or b[3] == b[1] or b[3] == b[2]:
        print("error")
    elif 1900 <= a <= 2050:
        print("error")
    else:
        print("OK")
else:
    print("error")

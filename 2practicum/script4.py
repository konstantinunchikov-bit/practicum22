a, b, c= map(int, input().split())
if a > b and a > c:
    print(a)
elif c > b and c > a:
    print(c)
elif b > a and b > c:
    print(b)


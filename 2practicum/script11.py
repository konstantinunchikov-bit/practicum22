a = int(input())
if a % 10 == 0 or a % 10 > 4:
    print(a, "попугаев")
if a % 10 == 1:
    print(a, "попугай")
if 2 <= a % 10 <= 4:
    print(a, "попугая")

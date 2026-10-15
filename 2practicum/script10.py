xc = int(input("XC"))
yc = int(input("YC"))
r = int(input("radius"))
x = int(input("x"))
y = int(input("y"))
if (xc - r <= x <= xc +r) and (yc - r <= y <= yc +r):
    if ((xc - r == x) or (xc + r == x)) and ((yc -r == y) or (yc +r == y)):
        print("на окружности")
    else:
        print("внутри окружности")
else:
    print("вне окружности")
    
    

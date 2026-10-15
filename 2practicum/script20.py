
cell = input("Введите координату клетки")

col = ord(cell[0]) - ord('a') + 1
row = int(cell[1])

if (col + row) % 2 == 0:
    print("Черная")
else:
    print("Белая")


A, B = map(int, input("Введите размеры отверстия A и B: ").split("x"))
C, D, E = map(int, input("Введите размеры кирпича C, D и E: ").split("x"))


hole = sorted([A, B])

brick = sorted([C, D, E])


if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("да")
else:
    print("нет")

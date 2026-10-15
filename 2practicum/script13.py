a = int(input())
b = int(input())
a1 = 0.453592 * a
b1 = 0.0254 * b
bmi = a1 / b1**2

if bmi < 16:
    print("выраженный дефицит массы тела")
elif bmi < 18.5:
    print("недостаточная масса тела")
elif bmi < 25:
    print("норма")
elif bmi < 30:
    print("избыточная масса тела")
elif bmi < 35:
    print("ожирение первой степени")
elif bmi < 40:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")

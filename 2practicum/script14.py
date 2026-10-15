n = int(input("Введите количество кнатов: "))
galleons = n // 493
remainder = n % 493

sickles = remainder // 29
knuts = remainder % 29

if galleons > 0:
    print(galleons, "галлеонов")
if sickles > 0:
    print(sickles, "сиклей")
if knuts > 0:
    print(knuts, "кнатов")

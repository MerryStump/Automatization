def spisok(list_1, list_2):
    return list(set(list_1) & set(list_2))


def stroka(list_1):
    bukvi = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', ]
    slova = list_1
    vivod = []
    for i in range(0, len(slova)):
        if slova[i][0].lower() in bukvi:
            vivod.append(slova[i])
    return vivod


def fibo(n):
    if n in (1, 2):
        return 1
    return fibo(n - 1) + fibo(n - 2)  # подсмотрел в интрнете, но понял рекурсию

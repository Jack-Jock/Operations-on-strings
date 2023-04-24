def plus():
    s1 = input("Введіть першу строку : ")
    s2 = input("Введіть другу строку : ")
    print("Їх сума : ",s1+s2)

def multi():
    s1 = input("Введіть строку : ")
    factor = int(input("Введіть множник : "))
    answer = s1 * factor
    print("Множена строка : ",answer)

def lenght():
    s1 = input("Введіть строку : ")
    print("Довжина строки : ",len(s1))

def accessindex():
    s1 = input("Введіть строку : ")
    print("Довжина строки : ", len(s1))
    index = int(input("Введіть номер букви : "))
    print("Буква : ",s1[index-1])

def polindrom():
    s1 = input("Введіть строку : ")
    s1 = s1.casefold()

    reversed_s1 = reversed(s1)

    if list(s1) == list(reversed_s1):
        print("Строка є поліндромом")
    else:
        print("Строка не поліндром")

def countsymbol():
    count = 0
    s1 = input("Введіть строку : ")
    symbol = input("Введіть символ кількісь яких потрібно порахувати : ")

    for i in s1:
        if i == symbol:
            count += 1

    print("Кількість символів : ",count)

def deletesymbol():
    s1 = input("Введіть строку : ")
    symbol = input("Введіть символ(символи) які потрібно видалити : ")
    new_s1 = ""

    for char in s1:
        if char not in symbol:
            new_s1 = new_s1 + char

    print("Строка після змін : ",new_s1)

def sortstr():
    s1 = input("Введіть строку : ")
    print("1: Сортування за алфавітом\n2: Зворотне сортування")

    number = int(input("Оберіть дію : "))

    if number == 1:
        new_sort = [i.lower() for i in s1.split()]
        new_sort.sort()

        sort_s1 = ''
        for i in new_sort:
            sort_s1 += str(i)
            sort_s1 += ' '
        print(sort_s1)
    else:
        new_sort = [i.lower() for i in s1.split()]
        new_sort.sort()
        new_sort.reverse()

        sort_s1 = ''
        for i in new_sort:
            sort_s1 += str(i)
            sort_s1 += ' '
        print(sort_s1)

def substr():
    s1 = input("Введіть строку : ")
    sub_str = input("Введіть підстроку для перевірки на належність : ")

    if sub_str in s1:
        print("Підстрока належить строці")
    else:
        print("Підстрока не належить строці")

def slicestr():
    s1 = input("Введіть строку : ")
    print("Довжина строки : ", len(s1))
    print("Оберіть тип зрізу: \n 1: Зріз без початку \n 2: Зріз без кінця \n 3: Стандартний зріз")

    number = int(input("Оберіть дію : "))

    if number == 1:
        indexY = int(input("Введіть порядковий номер кінцевої точки : "))
        print("Зріз без початку : ",s1[:(indexY-1)])
    elif number == 2:
        indexX = int(input("Введіть порядковий номер початкової точки : "))
        print("Зріз без кінця : ", s1[(indexX-1):])
    elif number == 3:
        indexX = int(input("Введіть порядковий номер початкової точки : "))
        indexY = int(input("Введіть порядковий номер кінцевої точки : "))
        print("Стандартний зріз : ", s1[(indexX-1):(indexY-1)])

def compstr():
    s1 = input("Введіть першу строку : ")
    s2 = input("Введіть другу строку : ")

    if s1.lower() == s2.lower():
        print("Строки співпадають")
    else:
        print("Строки не співпадають")
import operations


def main():

    print("Оберіть дію:\n 0: Додавання строк\n 1: Множення строк\n 2: Довжина строки\n 3: Доступ до букви за индексом"
          "\n 4: Перевірка строки на поліндром \n 5: Кількість певних символів\n 6: Видалення певних символів"
          "\n 7: Сортування строки\n 8: Належність підстроки\n 9: Зріз строк\n 10: Порівняння строк")

    number = int(input("Введіть дію: "))

    if number == 0:
        operations.plus()
    elif number == 1:
        operations.multi()
    elif number == 2:
        operations.lenght()
    elif number == 3:
        operations.accessindex()
    elif number == 4:
        operations.polindrom()
    elif number == 5:
        operations.countsymbol()
    elif number == 6:
        operations.deletesymbol()
    elif number == 7:
        operations.sortstr()
    elif number == 8:
        operations.substr()
    elif number == 9:
        operations.slicestr()
    elif number == 10:
        operations.compstr()


if __name__ == "__main__":
    main()


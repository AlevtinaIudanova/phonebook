from logger import input_data, print_data, change_data, delete_data


def interface():
    print('Добрый день! Вы попали на специальный бот справочник от GB! \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменить данные \n 4 - Удалить данные')
    command = int(input('Введите число '))

    while command != 1 and command != 2  and command != 3 and command != 4:
        print('Неправильнный ввод')
        command = int(input('Введите число '))


    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()





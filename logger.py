from data_create import name_data, surname_data, phone_data, address_data
from data_create import new_name_data, new_surname_data, new_phone_data, new_address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате ввести данные\n\n" 
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2  and var != 3 and var != 4:
        print('Неправильнный ввод')
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n\n")
        



def print_data():
    
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
               data_first_list.append(''.join(data_first[j:i+1]))
               j = i

        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def change_data():

    variant = int(input(f"Из какого файла вывести данные\n\n" 
    f"1 Вариант: 1 вариант \n"
    f"2 Вариант: 2 вариант\n"
    f"Выберите вариант: "))
    if variant == 1:
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            new_command = int(input(f'Введите данные, которые хотите изменить: \n 1 - name \n 2 - surname \n 3 - phone \n 4 - adress\n'))
            if new_command == 1:
                new_name_data()
            elif new_command == 2:
                new_surname_data()
            elif new_command == 3:
                new_phone_data()
            elif new_command == 4:
                new_address_data()

        if var == 1:
            with open('data_first_variant.csv', 'w', encoding='utf-8') as f:   
                new_name = new_name_data
                f.write(f"{new_name}:\n\n")
            


                
            

        
            
           









    elif variant == 2:
        print('Вывожу данные из 2 файла: \n')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            print(*data_second)

    while var != 1 and var != 2:  #and var != 3 and var != 4:
        print('Неправильнный ввод')
        var = int(input('Введите число '))
   
 
        

   
        
    
    
        



def delete_data():
    print('Удаление данных: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_delete = f.readlines()
        data_new_list = []
        j = 0
        for i in range(len(data_delete)):
           if data_new[i] == '\n' or i == len(data_new) - 1:
               data_new_list.append(''.join(data_new[j:i+1]))
               j = i 
        print(''.join(data_new_list))

input_data()
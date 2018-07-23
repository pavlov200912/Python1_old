#Lesson 5
import lesson05_easy as easy
import os

# HomeWork
cur_dir = os.getcwd()
while True:
    try:
        i = int(input('1. Перейти в папку' + '\n'
                      '2. Просмотреть содержимое текущей папки' + '\n' +
                      '3. Удалить папку' + '\n' +
                      '4. Создать папку' + '\n'
                      '5. Выйти' + '\n'))
    except:
        print('Input error')
        continue
    if i > 5 or i < 1:
        print('Input error')
        continue
    if i == 1:
        print('В какую папку перейти?')
        count = 0
        list = easy.show_dirs(cur_dir)
        for item in list:
            count += 1
            print(str(count) + ' : ' + item)
        print(str(count + 1) + ': ..')
        try:
            number = int(input('Введите порядковый номер:\n'))
        except:
            print('Input error')
            continue
        if number == count + 1:
            cur_dir, was = os.path.split(cur_dir)
        else:
            cur_dir = os.path.join(cur_dir, list[number - 1])
        print('Текущая директория:' + cur_dir)
    if i == 2:
        easy.show_all(cur_dir)
    if i == 3:
        print('Какую папку удалить?')
        list = easy.show_all(cur_dir)
        try:
            number = int(input('Введите порядковый номер:\n'))
        except:
            print('Input error')
        if number >= len(list) or number < 0:
            print('Input error')
        else:
            easy.delete_dir(list[number - 1])
    if i == 4:
        name = input('Введите имя для новой папки:')
        easy.create_dir(name)
    if i == 5:
        break
    print('_________________________________')
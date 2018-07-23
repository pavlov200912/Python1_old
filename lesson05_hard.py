# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import shutil
import re
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cp <file_name> - создает копию указанного файла")
    print("cp <file_name> - создает копию указанного файла")


def make_dir():
    if not file_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), file_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(file_name))
    except FileExistsError:
        print('директория {} уже существует'.format(file_name))


def copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if file_name not in os.listdir(os.getcwd()):
        print("Указанного файла нет в директории")
        return
    try:
        shutil.copy(os.path.realpath(os.path.join(os.getcwd(),file_name))
                , str('1' + file_name))
    except:
        print('Unknown error')
        return
    print('Файл успешно скопирован')


def remove():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if file_name not in os.listdir(os.getcwd()):
        print("Указанного файла нет в директории")
        return
    if input(f'Удалить файл {file_name}? (y/n)') == 'y':
        try:
            os.remove(os.path.join(os.getcwd(),file_name))
        except:
            print("Removing error")
            return
        print('Файл успешно удален')
        return
    print("Файл не удален")


def curdir():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if re.match('[A-Z]:\*',file_name) is None:
        if file_name not in os.listdir(os.getcwd()):
            print('Указан неверный путь')
            return
        else:
            if file_name == '..':
                os.chdir(os.path.split(os.getcwd())[0])
            else:
                os.chdir(os.path.join(os.getcwd(), file_name))
    elif os.path.exists(file_name):
        os.chdir(file_name)
    print(f'Выполнен переход в {os.getcwd()}')


def ls():
    print(os.getcwd())


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp":copy,
    "rm":remove,
    "cd":curdir,
    "ls":ls
}



try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


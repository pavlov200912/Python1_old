#Lesson 5
import os
import shutil


def create_dir(name):
    try:
        os.mkdir(name)
    except:
        print(f'Eror!Directory already exist!')


def delete_dir(name):
    try:
        os.rmdir(name)
    except:
        print(f'Eror!Directory already deleted or not empty!')


def easy_1():
    while True:
        try:
            ch = int(input('[1] - создать dir_1 - dir2' + '\n'
                           '[2] - удалить ' + '\n'
                           '[3] - break' + '\n'))
        except:
            print('Input Error')
            continue
        if ch == 1:
            print('Creating new dirs...')
            for i in range(1,10):
                item = 'dir_' + str(i)
                dir = os.path.join(os.getcwd(), item)
                create_dir(dir)
            print('Your files now:' + str(os.listdir(os.getcwd())))
        if ch == 2:
            print('Creating new dirs...')
            for i in range(1,10):
                item = 'dir_' + str(i)
                dir = os.path.join(os.getcwd(), item)
                delete_dir()
            print('Your files now:' + str(os.listdir(os.getcwd())))
        if ch == 3:
            break


def show_dirs(name):
    # return [o for o in os.listdir(name) if os.path.isdir(o)]
    l = []
    for file in os.listdir(name):
        if '.' not in file:
            l.append(file)
    return l

def self_copy():
    print('Self-Copying')
    shutil.copy(os.path.realpath(__file__),'copy.py')


if __name__ == '__main__':
    easy_1()
    show_dirs(os.getcwd())     #easy 2
    self_copy()     #easy 3


import local as lc
import os, os.path

path = input(lc.PATH)

def catalog_go(path, level=1):

    a = 'Level=', level, 'Content', os.listdir(path)
    list.append(a)
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            catalog_go(path+'\\'+i, level+1)

def moveUp(path):
    '''На уровень вверх'''
    path = path.split('\\')
    path = path[:len(path)-1]
    path = "\\".join(path)
    os.chdir(path)
    return path


def moveDown(path):
    '''На уровень вниз'''
    while True:
        try:
            path = path + '\\' + input()
            os.chdir(path)
            print(os.getcwd())
            break
        except FileNotFoundError:
            print()
        return path


def countFiles(path, list_of_files):
    '''Количество файлов в каталоге и подкаталогах'''
    for name in os.listdir(path):
        path = os.path.join(path, name)
        if os.path.isfile(path):
            list_of_files.append(path)
        else:
            countFiles(path, list_of_files)
    return len(list_of_files)


def countBytes(path, size):
    '''Размер каталога, включая подкаталоги'''
    for name in os.listdir(path):
        path = os.path.join(path, name)
        if os.path.isfile(path):
            size += os.path.getsize(path)
        else:
            countBytes(path, size)
    return size


def findFiles(name_file, path):
    '''Поиск файла в каталоге и подкаталогах'''
    for name in os.listdir(path):
        path = os.path.join(path, name)
        if os.path.isfile(path) and name == name_file:
            print()
            return path
        else:
            return findFiles(name_file, path)


list = []


menu = int(input(lc.MENU))

catalog_go(path)
lel = 1
list_of_files = []
size = 0
while menu != 7:
    if menu == 1:
        for i in list:
            if int(i[1]) == lel:
                print(i)
        menu = int(input())
    if menu == 2:
        moveUp(path)
        menu = int(input())
    if menu == 3:
        moveDown(path)
        menu = int(input())
    if menu == 4:
        countFiles(path, list_of_files)
        menu = int(input())
    if menu ==5:
        countBytes(path, size)
        menu = int(input())
    if menu ==6: # поиск файла
        name = input()
        findFiles(name_file, path)


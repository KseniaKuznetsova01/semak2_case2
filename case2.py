from typing import List, Any
import glob
import local as lc
import os, os.path
from os.path import isfile, join, exists
import sys


def catalog_go(path, level=1):

    a = 'Level=', level, 'Content', os.listdir(path)
    list.append(a)
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            catalog_go(path+'\\'+i, level+1)


path = input(lc.PATH)

def moveUp():
    '''На уровень вверх'''
    path = os.getcwd()
    path = path.split('\\')
    path = path[:len(path)-1]
    path = "\\".join(path)
    os.chdir(path)
    return path


def moveDown(path):
    '''На уровень вниз'''
    while True:
        try:
            path = path + '\\' + input(local.INP)
            os.chdir(path)
            print(os.getcwd())
            break
        except FileNotFoundError:
            print(local.ERROR2)
        return path


def countFiles(dir, list_of_files):
    '''Количество файлов в каталоге и подкаталогах'''
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            list_of_files.append(path)
        else:
            countFiles(path, list_of_files)
    return len(list_of_files)


def countBytes(dir, size):
    '''Размер каталога, включая подкаталоги'''
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            size += os.path.getsize(path)
        else:
            countBytes(path, size)
    return size


def findFiles(target, dir):
    '''Поиск файла в каталоге и подкаталогах'''
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path) and name == target:
            print(local.FIND)
            return path
        else:
            return findFiles(target, dir)

b = 0
c = 0
list = []

if os.path.isfile(path):
    b += 1
if os.path.isdir(path):
    c += 1
menu = int(input(lc.MENU))

catalog_go(path)
lel = 1

while menu != 7:
    if menu == 1:
        for i in list:
            if int(i[1]) == lel:
                print(i)
        menu = int(input())
    if menu == 2:
        lel -= 1
        for i in list:
            if int(i[1]) == lel:
                print(i)
        menu = int(input())
    if menu == 3:
        moveDown(path)
        menu = int(input())
    if menu == 4:
        countFiles(dir, list_of_files)
        menu = int(input())
    if menu ==5:
        countBytes(dir, size)

        menu = int(input())
    if menu ==6: # поиск файла
        findFiles(target, dir)


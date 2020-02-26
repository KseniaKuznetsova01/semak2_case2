from typing import List, Any
import glob
import local as lc
import os, os.path


def catalog_go(path, level=1):

    a = 'Level=', level, 'Content', os.listdir(path)
    list.append(a)
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            catalog_go(path+'\\'+i, level+1)


path = input(lc.PATH)

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
        lel += 1
        for i in list:
            if int(i[1]) == lel:
                print(i)
        menu = int(input())
    if menu == 4:
        list1 = os.listdir(path)
        number_files = len(list)
        print(number_files)
        menu = int(input())
    if menu == 5:
        os..count.Bytes(path)
        menu = int(input())

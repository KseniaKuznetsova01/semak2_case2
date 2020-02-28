import local as lc
import os, os.path

path = input(lc.PATH)
list = []
level = 1
def catalog_go(path, level):

    a = 'Level=', level, 'Content', os.listdir(path)
    list.append(a)
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            catalog_go(path+'\\'+i, level+1)

menu = int(input(lc.MENU))
lel=1

catalog_go(path, level)

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
        count = 0
        for directory, subdirectory, files in os.walk(path):
            count += 1
        print(count)
        menu = int(input())
    if menu == 5:
        print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)))
        menu = int(input())
    if menu == 6:
        name_file = input()
        for files in os.walk(path):
            for i in files:
                for e in i:
                    a = e.find('.')
                    if a!=-1:
                        name = files[:a-1]
                        print(name)
                        if os.path.isfile(path) and name == name_file:
                            print(path)

else:
    print('ERROR')
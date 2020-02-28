import local as lc
import os, os.path

path = input(lc.PATH)
list = []
level = 1


def catalog_go(path, level):
    list_a = 'Level=', level, 'Content', os.listdir(path)
    list.append(list_a)
    for k in os.listdir(path):
        if os.path.isdir(path + '\\' + k):
            catalog_go(path + '\\' + k, level + 1)


menu = int(input(lc.MENU))

lel = 1

try:

    catalog_go(path, level)

except FileNotFoundError:
    print(lc.NOT)
    print(lc.ERROR3)

try:
    while menu != 7:
        if menu == 1:
            for i in list:
                if int(i[1]) == lel:
                    spis = i[3]
                    print(lc.LIST)
                    for j in spis:
                        print(j)

            menu = int(input(lc.MENU))
        if menu == 2:
            lel -= 1
            for i in list:
                if int(i[1]) == lel:
                    spis = i[3]
                    for j in spis:
                        print(j)
            menu = int(input(lc.MENU))
        if menu == 3:
            lel += 1
            print(lc.LIST_1.format(str(list[1][1])))
            for i in list:
                if int(i[1]) == lel:
                    spis = i[3]
                    for j in spis:
                        print(j)
            menu = int(input(lc.MENU))
        if menu == 4:
            count = 0
            c = 0
            for directory, subdirectory, files in os.walk(path):
                if files:
                    count += 1
                elif subdirectory:
                    c += 1
            print(lc.FILE, count)
            print(lc.DIR, c)
            menu = int(input(lc.MENU))
        if menu == 5:
            print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)), lc.BYT)
            menu = int(input(lc.MENU))
        if menu == 6:  # не работает!
            name_file = input()
            for files in os.walk(path):
                for i in files:
                    for e in i:
                        a = e.find('.')
                        if a != -1:
                            name = files[:a - 1]
                            print(name)
                            if os.path.isfile(path) and name == name_file:
                                print(path)
        if menu == 7:
            print(lc.END)
            break
    else:
        print(lc.ERROR)

except ValueError:
    print(lc.ERROR)
except TypeError:
    print(lc.ERROR)
except FileNotFoundError:
    print(lc.NOT)

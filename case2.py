import local as lc
print(lc.MENU)
Menu = int(input())
while Menu != 7:
    ...
    Menu = int(input(lc.MENU))
def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT
            print('Работа программы завершена.')
            break
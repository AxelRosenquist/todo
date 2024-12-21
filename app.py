import os
import file

def clearTerminal():
    os.system('cls')
    print('Todo list\n')

def mainMenu():
    clearTerminal()
    print('Press what option you wanna do then press enter')
    print('1. List tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Exit the application')


def listTasks():
    clearTerminal()
    tasks = file.getTasks()
    if not tasks:
        print('There are no tasks.')
    else:
        for task in tasks:
            print(task)

def addTask():
    clearTerminal()
    newTask = input('Enter a new task to add to the list:\n\n')
    file.addTask(newTask)
    

def deleteTask():
    clearTerminal()
    file.deleteTask()


def main():
    while True:
        mainMenu()
        option = input("\nSelect option: ")

        match option:
            case '1':
                listTasks()
            case '2':
                addTask()
            case '3':
                deleteTask()
            case '4':
                exit()
            case _:
                os.system('cls')
                input('Entered a faulty value.')
        input('Press enter to return to the main menu')

    

main()
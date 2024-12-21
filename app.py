import os

tasks = ['ML algorithms', 'neural networks', 'LLM']

def mainMenu():
    os.system('cls')
    print('Todo list')
    print('Press what option you wanna do then press enter')
    print('1. List tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Exit the application')


def listTasks():
    os.system('cls')
    for task in tasks:
        print(f'- {task}')

    
def addTask():
    os.system('cls')
    newTask = input('Enter a new task to add to the list:\n\n')
    tasks.append(newTask)
    print(f'\n{newTask} was added to the list')


def deleteTask():
    os.system('cls')
    localTasks = tasks
    taskToDelete = input('Enter a what task to dekete from the list:\n\n')
    if taskToDelete.isdigit():
        deletedTask = localTasks[taskToDelete-1]
        print(f'Deleting task {taskToDelete}. {deletedTask}')
        localTasks.pop(taskToDelete - 1)
        print(f'\nTask was successffully delete')
    else:
        for i in range(len(localTasks)):
            if localTasks[i].lower() == taskToDelete.lower():
                print(f'Deleting task{i}. {taskToDelete}')
                localTasks.pop(i)
                print(f'\nTask was successffully delete')


def main():
    while True:
        mainMenu()
        option = input("\nSelect option: ")

        match option:
            case '1':
                listTasks()
                input('\nPress enter to return to the main menu')
            case '2':
                addTask()
                input('\nPress enter to return to the main menu')
            case '3':
                pass
            case _:
                os.system('cls')
                input('Entered a faulty value, press enter to return to main menu')

main()
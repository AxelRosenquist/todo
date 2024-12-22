import os
import subprocess
import file

def clear_terminal():
    os.system('cls')
    print('Todo list\n')

def main_menu():
    clear_terminal()
    print('Press what option you wanna do then press enter')
    print('1. List tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Sync task changes to GitHub')
    print('5. Exit the application')


def list_tasks():
    clear_terminal()
    tasks = file.get_tasks()
    if not tasks:
        print('There are no tasks.')
    else:
        for task in tasks:
            print(task)

def add_task():
    clear_terminal()
    newTask = input('Enter a new task to add to the list:\n\n')
    file.add_task(newTask)
    

def delete_task():
    clear_terminal()
    file.delete_task()


def sync_tasks():
    clear_terminal()
    answer = input('Are you sure you want to push the changes to the GitHub repo? y/n\n')
    if answer.lower() == 'y':
        subprocess.run(['git','add', 'tasks.json'])
        subprocess.run(['git','commit', '-m', "'Automatic commit, updated tasks.json'"])
        subprocess.run(['git','push'])
    elif answer.lower() == 'n':
        print('Canceled the sync of tasks changes.')


def main():
    while True:
        main_menu()
        option = input("\nSelect option: ")

        match option:
            case '1':
                list_tasks()
            case '2':
                add_task()
            case '3':
                delete_task()
            case '4':
                sync_tasks()
            case '5':
                exit()
            case _:
                os.system('cls')
                input('Entered a faulty value.')
        input('Press enter to return to the main menu')

    

main()
import os
import json

taskfile = 'tasks.json'

def create_file():
    local_taskFile = taskfile
    if not os.path.exists(local_taskFile):
        with open(local_taskFile, 'w') as JSON_tasks:
            JSON_tasks.write('[]')
         

def get_tasks() -> list[str]:
    create_file()
    with open(taskfile, 'r') as JSON_tasks:
        return json.load(JSON_tasks)

def write_changes(tasks : list[str]):
    with open(taskfile, 'w') as JSON_tasks:
            json.dump(tasks, JSON_tasks, indent=2)

def add_task(new_task : str):
    tasks = get_tasks()
    if new_task in tasks:
        print(f'\nThe task {new_task} already exists')
    else: 
        tasks.append(new_task)
        write_changes(tasks)
        print(f'\nAdded {new_task} to the list')


def delete_task():
    tasks = get_tasks()
    if len(tasks) == 0:
        input('\nNo task to delete.')
        return
    task_to_delete = input('Enter a what task to delete from the list:\n\n')
    if task_to_delete.isdigit():
        task_to_delete = int(task_to_delete)
        if len(tasks) < task_to_delete:
            input(f'\nTask number {task_to_delete} does not exist.')
            return
        deleted_task = tasks[task_to_delete-1]
        print(f'Deleting task {task_to_delete}. {deleted_task}')
        tasks.pop(task_to_delete - 1)
        write_changes(tasks)
        input(f'\nTask was successffully deleted.')
    else:
        for i in range(len(tasks)):
            if tasks[i].lower() == task_to_delete.lower():
                print(f'Deleting task {i + 1}. {task_to_delete}')
                tasks.pop(i)
                write_changes(tasks)
                print(f'\nTask was successffully deleted.')
                return
        else:
            print(f'The task {task_to_delete} does not exist.')


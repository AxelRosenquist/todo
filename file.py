import os
import json

taskfile = 'tasks.json'

def createFile():
    localTaskFile = taskfile
    if not os.path.exists(localTaskFile):
        open(localTaskFile, 'x')
         

def getTasks() -> list[str]:
    createFile()
    with open(taskfile, 'r') as JSONTasks:
        return json.load(JSONTasks)

def writeChanges(tasks : list[str]):
    with open(taskfile, 'w') as JSONTasks:
            json.dump(tasks, JSONTasks, indent=2)

def addTask(newTask : str):
    tasks = getTasks()
    if newTask in tasks:
        print(f'\nThe task {newTask} already exists')
    else: 
        tasks.append(newTask)
        writeChanges(tasks)
        print(f'\nAdded {newTask} to the list')


def deleteTask():
    tasks = getTasks()
    if len(tasks) == 0:
        input('\nNo task to delete.')
        return
    taskToDelete = input('Enter a what task to delete from the list:\n\n')
    if taskToDelete.isdigit():
        taskToDelete = int(taskToDelete)
        if len(tasks) < taskToDelete:
            input(f'\nTask number {taskToDelete} does not exist.')
            return
        deletedTask = tasks[taskToDelete-1]
        print(f'Deleting task {taskToDelete}. {deletedTask}')
        tasks.pop(taskToDelete - 1)
        writeChanges(tasks)
        input(f'\nTask was successffully deleted.')
    else:
        for i in range(len(tasks)):
            if tasks[i].lower() == taskToDelete.lower():
                print(f'Deleting task {i}. {taskToDelete}')
                tasks.pop(i)
                writeChanges(tasks)
                input(f'\nTask was successffully deleted.')
getTasks()

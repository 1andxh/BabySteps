import os

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open('task.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def view():
    try:
        print('\nfile location: ')
        print(f'tasks.txt is located at: {os.path.abspath('tasks.txt')}')
        print('\nContents of tasks.txt: ')
        print('-' * 20)
        with open('tasks.txt', 'r') as file:
            contents = file.read()
            if contents:
                print(contents)
            else:
                print("file is empty!")

        print('-' * 20)
    except FileNotFoundError:
        print('file not created yet')


tasks = load_tasks()

while True:
    choice = input('what would you like to do? (\n1.add \n2.show \n3.delete \n4.view \n5.quit\nenter choice: ')

    if choice == 'add':
        task = input('Enter task to add: ')
        tasks.append(task)
        print('task added!')

    elif choice == 'show':
        if len(tasks) == 0:
            print('no tasks yet!')

        else:
            print('\nAvailabe tasks: ')
            for index, task in enumerate(tasks, 1):
                print(f'{index}.{task}')

    elif choice == 'delete':
        if not tasks:
            print('No tasks to delete!')
            continue
        print('\nCurrent tasks: ')
        for index, task in enumerate(task, 1):
            print(f'{index}.{task}')

        try:
            task_num = int(input('which task do you want to delete? (enter number): '))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num -1)
                save_tasks(tasks)
                print(f'Deleted task: {deleted_task}')
        except ValueError:
            print('Invalid task number!')

    elif choice == 'view':
        view()

    elif choice == 'quit':
        break

    else:
        print('Invalid choice! Please type add or show')

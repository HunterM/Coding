import csv

path = "D:/Coding/Coding/Sem151222/"

def update_base():
    with open('LecFile.csv', 'w') as book:
        book.writelines(f'{contact}')
    
def del_base():
     with open('LecFile.csv', 'w') as book:
        book.writelines(f'')
    
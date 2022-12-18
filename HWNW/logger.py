import csv
import model
import view

def addcontact_new(contact):
    try:
        with open('UsersFile.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('UsersFile.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([contact.split(' ||')])
    except FileNotFoundError:
        with open('UsersFile.txt', 'w', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('UsersFile.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])

def get_base():
    with open('UsersFile.txt', 'r', encoding='utf-8') as book:
        return book.read()
    # with open('UsersFile.csv', 'r') as f:
    #     return book.read()
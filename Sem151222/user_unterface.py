
def read_stroka():
    my_lines = []
    with open('Coding\Sem151222\LecFile.csv', 'r') as f:
            for i in f:
                my_lines.append(i.split(';'))
    print(my_lines)
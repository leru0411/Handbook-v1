#хранение данных телефонной книги

def read_file():
    with open('handbook.csv', 'r') as file:
        print(file.read()) 


def add_name(data):
    with open('handbook.csv', 'a') as file:
        file.write('Имя;{}\n'
                    .format(data)) 

def add_number(data):
    with open('handbook.csv', 'a') as file:
        file.write('Номер телефона;{}\n'
                    .format(data)) 


def add_about(data):
    with open('handbook.csv', 'a') as file:
        file.write('Описание;{}\n\n'
                    .format(data)) 


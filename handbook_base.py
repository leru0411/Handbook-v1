#хранение данных телефонной книги

def read_file():
    with open('handbook.csv', 'r') as file:
        return file.read()

def add_name(data):
    with open('handbook.csv', 'a') as file:
        file.write('Name;{};'
                    .format(data)) 

def add_number(data):
    with open('handbook.csv', 'a') as file:
        file.write('Phone_number;{};'
                    .format(data)) 


def add_about(data):
    with open('handbook.csv', 'a') as file:
        file.write('About;{};\n'
                    .format(data)) 


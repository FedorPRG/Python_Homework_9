import json

def read_phonebook(path = 'phonebook.json'):
    with open(path, 'r',encoding='utf-8') as file:
        data = json.load(file)
        file.close()
    return data

dir = read_phonebook()

def directory_add(name,family,number,coment):
    dir[family]=f'{name}, {number}, {coment}'

def search(family):
    stroka=''
    for key, value in dir.items():
        if key==family:
            stroka=str(key)+', '+str(value)
            print(key, value, sep=', ')
            return  stroka 
    else: 
        print(f'Записи с фамилией {family} нет')
        stroka='Записи с фамилией '+family+' нет'
        return stroka

def delete(family):
    for key, value in list(dir.items()):
        if key==family:
            del dir[family]
            print('Фамилия удалена')
            return 'Фамилия удалена'            
    print(f'Записи с фамилией {family} нет')
    return 'Записи с фамилией '+family+' нет'  
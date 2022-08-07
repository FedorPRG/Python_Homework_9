import json

def print_var_1(stroka):
    with open('result_var_1.txt','w',encoding='utf-8') as file:
        file.write(stroka)
def print_var_2(stroka):
    with open('result_var_2.txt','w',encoding='utf-8') as file:
        file.write(stroka)

def write_phonebook(dic,path = 'phonebook.json'):
    with open(path, 'w',encoding='utf-8') as file:
        json.dump(dic, file, indent=2)
        file.close()


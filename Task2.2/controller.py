import data_keeper 
import input_data
import output_data

#def start():
    # i=1
    # while i==1:
    #     print('Вы находитесь в телефонном справочнике.\n\
    # Введите номер команды:\n\
    # 1.Показать весь справочник (запись в файл)\n\
    # 2.Поиск номера телефона по фамилии\n\
    # 3.Добавить контакт\n\
    # 4.Удалить контакт\n\
    # 5.Запись справочника в phonebook.json')
        #com=input_data.get_com()
        #if com==1:
def com_1_viev_print(format):
            stroka=''
            #format=input_data.output_format()
            if format==1:                
                for key, value in data_keeper.dir.items():
                    stroka=stroka+str(key)+', '+str(value)+'\n'
                    print(key, value, sep=', ')
                output_data.print_var_1(stroka)
                return stroka
            else:
                for key, value in data_keeper.dir.items():
                    print(key)
                    stroka=stroka+key+'\n'
                    for i in value:
                        if i==',':
                            print('')
                            stroka=stroka+'\n'
                        elif i==' ':
                            continue
                        else:
                            print(i,end='')
                            stroka=stroka+i
                    print('\n')
                    stroka=stroka+'\n'+'\n'
                output_data.print_var_2(stroka)
                return stroka



def com_2_search(family):
            #family=input_data.for_search()
            return data_keeper.search(family)

def com_3_add(family, name, number, coment):
            #family, name, number, coment = input_data.new_data()
            data_keeper.directory_add(family, name, number, coment)

def com_4_del(family):            
            #family=input_data.for_delete()
            return data_keeper.delete(family)

def com_5_write():            
            output_data.write_phonebook(data_keeper.dir)
        #i=int(input('Желаете продолжить? (1-да, 2-нет)'))

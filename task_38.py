print( "Телефонная книга" '\n') 
 


def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data
    
 
def scan(data):
    for i in  data:
        print(i)
        
def search(data):
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')

def delete(data):
    name = input("Введите имя для удаления: ")
    for i in data:
        if name in data[i]:
            del data[i]

def add(data):
    print("Введите имя контакта: ")
    name = input("> ")
    print("Введите номер телефона контакта: ")
    phone = input("> ")
    new_contact = {'name': name, 'phone': phone}
    data.append(new_contact)
    print('Контакт добавлен')


def main():
    my_choice = -1
    data = readfile('tel.txt') 
    while my_choice != 0:
        print('Выберите одно из действий: \n')

        print('1 - Просмотр всех записей справочника')
        print('2 - Поиск по справочнику')
        print('3 - Добавить контакт')
        print('4 - Удалить контакт')
        print('0 - выход из программы ', '\n')

        my_choice = input("Выберите действие:")
        dict_command = {'1' :  scan, '2' : search, '3' : add, '4' : delete}
        dict_command[my_choice](data)



if __name__ == '__main__':
    main()


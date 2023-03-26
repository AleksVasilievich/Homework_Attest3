from datetime import datetime


#  Элементарные методы
class Function(object):
    def input_notes(self):
        id_int = abs(int(input('Введите натуральное число, новый id ->  ')))
        id_str = str(id_int)
        head_n = input('Введите заголовок ->  ')
        body_n = input('Введите текст заметки ->  ')
        date_n = str(datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))
        notes = (id_str + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
        print(notes)
        return notes

    # Ввод данных
    def save_notes(self, note='00;TEST;test;00.00.00\n'):
        with open('data.csv', 'a', encoding='utf_8') as file:
            file.write(note)

    # Сохранить данных

    def reads_notes(self):
        with open('data.csv', 'r', encoding='utf_8') as file:
            return print(file.read())

    # Чтение из файла

    def deletes(self):
        with open('data.csv', 'w', encoding='utf_8') as file:
            file.write('')

    # Запись в файл пустого списка

    def view_id(self):
        a = ''
        array = list()
        array1 = list()
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array[0]:
                for j in i:
                    if j != ';':
                        a += j
                    elif j == ';':
                        break
                array1.append(a)
                a = ''
            print(array1)
            return array1

    # Вывести всё что находится до ";" в каждой строке
    def error_notes(self):
        print('No Comand !!!')

    # Вывести сообщение об ошибке
    def exit(self):
        print('Goodbye')
# Завершение программы

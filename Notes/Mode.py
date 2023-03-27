from Function import Function


class Mode(object):
    def read_id_notes(self):
        f = Function()
        try:
            arr = f.view_id()
            temp = input(' Введите номер ID ->   ')
            temp_id = arr.index(temp)
            array = list()
            array1 = list()
            with open('data.csv', 'r', encoding='utf_8') as file:
                array.append(file.read().split())
                for i in array[0]:
                    array1.append(i)
            print(*array1[temp_id])
            return [array1, temp_id]
        except Exception:
            f.error_notes()

    # Читаем строку файла по id
    def delete_id_notes(self):
        f = Function()

        try:
            array1 = Mode.read_id_notes(self)[0]
            print('Подтвердите свой выбор !!!')
            temp_array = Mode.read_id_notes(self)[1]
            array = array1[0:temp_array] + array1[(temp_array + 1):]
            with open('data.csv', 'w', encoding='utf_8') as file:
                for i in array:
                    file.writelines('%s\n' % i)
                print('Эти данные удалены !!!')

        except Exception:
            f.error_notes()

    # Удоляем строку файла по id
    def edit(self):
        f = Function()
        print('Удалим редактируемую заметку и напишем новую ')
        Mode.delete_id_notes(self)
        f.input_notes(self)
        return

# Редактируем файл


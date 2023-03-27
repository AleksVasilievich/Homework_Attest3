from Function import Function
from Mode import Mode

class Menu(object):
    def menu(self):
        mo = Mode
        f = Function()
        f.salute()

        comand = input()

        if comand == '1':
            f.input_notes(self)
            self.menu()

        elif comand == '2':
            # f.save_notes(self)
            print()
        elif comand == '3':
            f.reads_notes(), self.menu()
            print()
        elif comand == '4':
            mo.read_id_notes(object)
            print()
        elif comand == '5':
            f.deletes(), f.reads_notes(), self.menu()
            print()
        elif comand == '6':
            mo.delete_id_notes(object)
            print()
        elif comand == '7':
            f.exit()
        else:
            print("Поверьте вводимые данные")
            self.menu()




from Function import Function
from Menu import Menu
from Mode import Mode
class Main(object):
    if __name__ == '__main__':

        f = Function()
        me = Menu()
        mo = Mode()
        me.menu()

        # f.input_notes()
        # f.save_notes()
        f.reads_notes()
        # f.deletes()
        # f.reads_notes()
        f.view_id()



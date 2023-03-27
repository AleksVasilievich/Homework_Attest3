from datetime import datetime


class Notes(object):
    def __init__(self, id_int=abs(int()), head_n='', body_n='',
                 date_n=str(datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))):
        self.id_int = id_int
        self.head_n = head_n
        self.body_n = body_n
        self.date_n = date_n

    def get_id(self):
        return self.id_int

    def get_head(self):
        return self.head_n

    def get_body(self):
        return self.body_n

    def get_data(self):
        return self.date_n

    def set_id(self, id_int):
        self.id_int = id_int

    def set_head(self, head_n):
        self.head_n = head_n

    def set_body(self, body_n):
        self.body_n = body_n

    def set_data(self):
        self.date_n = str(datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))

from datetime import datetime

class Field:
    def __init__(self,value):
        self.__value=None
        self.value=value

    @property
    def get_value(self):
        return self.__value

    @get_value.setter
    def set_value(self,value):
        self.__value=value


class Name(Field):
    def __init__(self,name):
        self.name=name
        super().__init__(name)


    def __str__(self):
        return f'{self.name}'

class Phone(Field):

    def __init__(self, number):
        super().__init__(number)
        self.valid(number)



    def __str__(self):
        return f'{self.value}'


    def valid(self,phone):
        if len(phone) == 10 and phone.isdigit():
            self.value = phone
        else:
            raise ValueError("Invalid phone number format")

class Birthday:
    def __init__(self,year,month,day):
        self.data=self.valid_data_time(year,month,day)

    def valid_data_time(self,year,month,day):
        try:
            result=datetime(year,month,day)
            return result
        except ValueError:
            raise ValueError


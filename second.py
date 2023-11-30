from ferst import *


class Record:

    def __init__(self,name,birthday=None):
        self.name=Name(name)
        self.birthday=birthday
        self.phones=[]


    def add_phone(self,number):
        if number:
            num=Phone(number)
            self.phones.append(num.value)

    def __str__(self):
        return f'{self.name} {self.phones}'

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, phone_old, phone_new):
        for phone_obj in self.phones:
            index=0
            if phone_obj == phone_old:
                self.phones[index]=phone_new
                break
            index+=1

    def find_phone(self, number):
        if number in self.phones:
            return Phone(number)

    def days_to_birthday(self):
        if self.birthday:
            now_data = datetime.now()
            old_data = datetime(year=self.birthday.data.year, month=self.birthday.data.month, day=self.birthday.data.day)
            if now_data.month <= old_data.month:
                days_before_birthday = old_data.replace(year=now_data.year)
                result = days_before_birthday - now_data
            else:
                days_before_birthday = old_data.replace(year=now_data.year + 1)
                result = days_before_birthday - now_data

            return f'{result.days} days before birthday {self.name}'
        return f'birthday is unknown'


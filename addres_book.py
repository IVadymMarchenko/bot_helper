from collections import UserList, UserDict
from second import *
import pickle

class AddressBook(UserDict):

    def add_contacts(self):
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        record = Record(name)
        record.add_phone(phone)
        birthday = input('Enter birthday: ')
        if birthday:
            year, month, day = map(int, birthday.split('-'))
            record.birthday = Birthday(year, month, day)

        self.data[record.name.name]=record
        print('User add')


    def delete(self):
        name=input('Введите имя ').lower().strip()
        if name in self.data.keys():
            del self.data[name]
            print('Контакт удален')
        else:
            return f'Такого контакта нет'


    def display_all_contacts(self):
        for name, phone in self.data.items():
            print(f'{phone}')


    def save_to_file(self):
        file_name=input()
        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)
            print(f'Контакты записаны в файл: {file_name}')

    def read_from_file(self):
        file_name=input('Введите имя файла: ')
        with open(file_name, "rb") as file:
            self.data = pickle.load(file)
        for i in self.data.values():
            print(i)

    def seach_contact(self):
        seach_list=[]
        something=input('Введите имя или телефон ')
        for name,phone in self.data.items():
            if something.strip().lower() in name or something.strip() in phone:
                seach_list.append(f'{phone}\n')
        if seach_list:
            print(''.join(seach_list))
        else:
            print( f'Совпадений нет')

    def days_to_birthday(self):
        name=input('Enter name: ')
        if name in self.data.keys() and self.data[name].birthday:
            record = self.data[name]
            print(f"{record.days_to_birthday()}")
        else:
            print('День рождения не известен')

    def display_part_contacts(self):
        note = int(input('Enter num '))
        if note > len(self.data):
            note = len(self.data)
        index_iteration = 0
        list_data = list(self.data.items())
        while index_iteration < len(list_data):
            contacts = [f'{record}' for name, record in list_data[index_iteration:index_iteration + note]]
            print('\n'.join(contacts))
            index_iteration += note

    def remove_phone(self):
        name=input('enter name: ')
        if name in self.data:
            record=self.data[name]
            old_phone=input('enter old phone: ')
            new_phone=input('enter new phone: ')
            index_phone = record.phones.index(old_phone)
            record.phones[index_phone] = new_phone
            print('ok')
        else:
            print('no')















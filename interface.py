from addres_book import *

class ConsoleInterface:
    def __init__(self, address_book):
        self.address_book = address_book

    def display_menu(self):
        print("1. Add Contact")
        print("2. Seach contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Save to file")
        print("6. read from file")
        print("7. Display part contacts")
        print('8. Days to birthday ')
        print('9: All Commands')
        print('10: remove phone')

    def run_program(self):
        self.display_menu()
        while True:
            command=input('Enter the command: ')
            if command=='1':
                self.address_book.add_contacts()
            elif command=='2':
                self.address_book.seach_contact()
            elif command=='3':
                self.address_book.delete()
            elif command=='4':
                self.address_book.display_all_contacts()
            elif command=='5':
                self.address_book.save_to_file()
            elif command=='6':
                self.address_book.read_from_file()
            elif command=='7':
                self.address_book.display_part_contacts()
            elif command=='8':
                self.address_book.days_to_birthday()
            elif command=='9':
                self.display_menu()
            elif command=='10':
                self.address_book.remove_phone()
            else:
                print('Enter command from 1-8')
if __name__=='__main__':
    book=AddressBook()
    adres_book=ConsoleInterface(book)
    adres_book.run_program()



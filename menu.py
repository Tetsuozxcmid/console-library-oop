from main import *
from models import *



def menu():
    hub = {"1": "Добавить книгу",
    "2": "Вывести книги",
    "3": "Удалить книгу",
    "4": "Изменить статус книги ",
    "5":"Найти книгу",
    "6":"Выход"
    }
    print(hub)
    
    
def main():
    lib = Library()
    while True:
        menu()
        choice = input("Выберите номер действия : ")
        if choice == "1":
            add_new_book(lib)
        elif choice == "2":
            display(lib)
        elif choice == "3":
            delete_book_books(lib)
        elif choice == "4":
            change(lib)
        elif choice == "5":
            find_book(lib)
        elif choice == "6":
            print("Выход из программы... ")
            break

if __name__ == "__main__":
    main()


        

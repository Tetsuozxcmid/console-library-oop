import uuid 
from models import Library, Book
book_status = ("в наличии", "выдана","нет в наличии")


def add_new_book(library: Library):
    
    id = uuid.uuid4()
    name = input("Введите название книги ")
    year = int(input("Введите год издания "))
    author = input("Введите автора книги ")
    print(f"Введите статус книги  {book_status}")
    while True:
        check_status = input("Введите статус: ")
        if check_status in book_status:
            status = check_status
            break
        else:
            print(f"Такого статуса нет. Доступные статусы: {book_status}")

    
    book = Book(str(id), name, year,author,status)
    library.add_book(book)

def display(library: Library):
    library.display_all_books()
    

def delete_book_books(library: Library):
    while True:
        book_id = input("Введите айди книги для удаления  ")
        library.delete_book(book_id=book_id)
        print("Книга удалена ")

def change(library: Library):
    book_id = input("Введите айди книги ")
    while True:
        new_status = input(f"Введите статус ").strip()
        if new_status in book_status:
            break
        else:
            print(f"Статус недоступен, вот список доступных: {book_status}")

    library.change_status(book_id=book_id,new_status=new_status)

def find_book(library: Library):
    search = input("Введите поиск по 1. Название 2. Год  3. Автор ")
    while True:
        if search not in ("1", "2", "3"):  
            print("Неверный тип поиска")
            search = input("Введите поиск по 1. Название 2. Год  3. Автор ") 
            continue  
        else:
            if search == "1":
                keyword = input("Введите название книги ")
            elif search == "2":
                keyword = int(input("Введите год "))
            else:  
                keyword = input("Введите автора книги ")
            library.finder(search=search, keyword=keyword)
            break  



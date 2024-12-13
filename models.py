import json
book_status = ("в наличии", "выдана","нет в наличии")

class Book:
    def __init__(self, id, name, year, author,status):
        self.id = id
        self.name = name
        self.year = year 
        self.author = author
        self.status = status

    def __str__(self):
        return f'{self.id}{self.name}{self.year}{self.author}{self.status}'
    
    def convert(self):
        return{
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "author":self.author,
            "status":self.status
        }
    

class Library:
    def __init__(self):
        self.books = dict()

        try:
            with open("library.json", "r",encoding="utf-8") as file:
                data = json.load(file)
                for i in data:
                    book = Book(i["id"],i["name"],i["year"],i["author"],i["status"])
                    self.books[book.id] = book
        except FileNotFoundError:
            print("Создайте первую позицию ")
        

    def add_book(self,book: Book):
            self.books[book.id] = book
            self.save_file()
            

    def save_file(self):
        with open("library.json","w",encoding="utf-8") as file:
            data = [book.convert() for book in self.books.values()]
            json.dump(data,file,indent=4,ensure_ascii=False)


    def delete_book(self, book_id):
                if book_id in self.books:
                    del self.books[book_id]
                    self.save_file()


    def display_all_books(self):
        if len(self.books) == 0:
                 print("Книг нету, добавьте ее ")
        for  book_id, book in self.books.items():
            print(f' \n Название - {book.name} \n Автор - {book.author} \n Год - {book.year} \n Статус - {book.status} \n id - {book_id}')

    def change_status(self,new_status,book_id):
         for book in self.books.values():
              if book.id == book_id:
                   book.status = new_status
                   self.save_file()

    def finder(self, keyword, search):
        found = False  
        if search.lower() == "2":
            for book_id, book in self.books.items():
                if keyword == book.year:
                    print(f"Год - {book.year} Название - {book.name} Автор - {book.author} id - {book_id}")
                    found = True
        elif search == "1":
            for book_id, book in self.books.items():
                if keyword.lower() in book.name.lower():
                    print(f"Название - {book.name} \n Год - {book.year} \n Автор - {book.author} \n id - {book_id}")
                    found = True
        elif search == "3":
            for book_id, book in self.books.items():
                if keyword.lower() in book.author.lower():
                    print(f"Автор - {book.author} \n Название - {book.name} \n Год - {book.year} \n id - {book_id}")
                    found = True

        if not found:
            print("Такая книга не найдена")
        
             
         
                
           
                            
              
                   
         
                   
                   
         
                   


            


    
                   
                   


    
            


    
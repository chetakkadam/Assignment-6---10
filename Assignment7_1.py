class BookStore:
    NoOfBooks = 0;

    def __init__(self, name, author):
        self.BookName = name;
        self.AuthorName = author;
        BookStore.NoOfBooks += 1;

    def Display(self):
        print("BookName : ", self.BookName, ' by ', self.AuthorName, ' , ','No of Books : ', self.NoOfBooks);
        

def main():
    bookentry1 = BookStore('Linux System Programming', 'Robert Love');
    bookentry1.Display();

    bookentry2 = BookStore('C Programming', 'Dennis Ritchie');
    bookentry2.Display();

if __name__ == "__main__":
    main();

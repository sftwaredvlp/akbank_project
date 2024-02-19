import time


class Library:
    def __init__(self, books_file="books.txt"):
        """
        Set the default books file for the Library object at initialization.
        """
        self.books_file = books_file
        self.books = []

    def load_books(self):
        """
        Open the "books" file and load books.
        """
        try:
            with open(self.books_file, 'r') as file:
                self.books = [line.strip() for line in file]
        except FileNotFoundError:
            print("The books file was not located. Kindly make a fresh one.")

    def list_books(self):
        """
        List of all books in the library.
        """
        print("--- BOOKS ---")
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Books are not available.")

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.books.append(book)
        self.save_books()
        print(f"{book} has been incorporated into the library.")

    def remove_book(self, book):
        """
        Remove a book from the library.
        """
        if book in self.books:
            self.books.remove(book)
            self.save_books()
            print(f"{book} has been expelled from the library.")
        else:
            print(f"{book} is not in the library.")

    def save_books(self):
        """
        Spare the current list of books to the books record.
        """
        with open(self.books_file, 'w') as file:
            for book in self.books:
                file.write(book + '\n')


def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            lib.load_books()
            lib.list_books()
        elif choice == '2':
            book = input("Enter the book's name: ")
            lib.add_book(book)
        elif choice == '3':
            book = input("Enter the name of the book to remove: ")
            lib.remove_book(book)
        elif choice == '4':
            print("See you...!")
            time.sleep(3)
            break
        else:
            print("For choice => Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
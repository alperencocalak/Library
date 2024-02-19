class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            print("*** List of Books ***")
            for book in books:
                book_info = book.strip().split(",")
                print("Book:", book_info[0], "Author:", book_info[1])

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{book_title}' added successfully.")

    def remove_book(self):
        book_title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        removed = False
        for book in books:
            if book_title.lower() not in book.lower():
                new_books.append(book)
            else:
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_books)
            print(f"Book '{book_title}' removed successfully.")
        else:
            print(f"Book '{book_title}' not found.")

# Creating an object named "lib" with Library class
lib = Library()

# Creating a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


#Creating library class and its methods.

class Library: 
    def __init__(self):
        # Using a+ to access the file and if the file doesn't exist the method will
        # create books.txt file.
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        # Listing all books in the books.txt file
        print("\n")
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            for book in books:
                book_info = book.strip().split(", ")
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")
        else:
            print("No books available.")

    def add_book(self):
        # Getting all informations about book. Then checking whether the book already
        # exist in the books.txt file.
        
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        release_date = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title}, {author}, {release_date}, {num_pages}\n"
        

        
        # Check if the book already exists. If the book is already in the file,
        # the code will not be saving the book.
        # This code is not sensitive to extra spaces or case differences in the book name entry.
        self.file.seek(0)
        existing_books = self.file.readlines()
        for book in existing_books:
            if title in book:
                print(f"The book '{title}' already exists.")
                return
        
        self.file.write(book_info)
        print("Book added successfully.")

    # Removing book from file
    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0) #cursor goes to beginning of the file
        new_books = []
        found = False
        for book in books:
            book_info = book.strip().split(", ")
            if book_info[0] == title_to_remove:
                found = True
            else:
                new_books.append(book)
        if found:
            self.file.truncate(0)  # Clear the file contents
            self.file.writelines(new_books)
            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found.")

# Create the Library object
lib = Library()

# Menu to interact with the Library object
while True:
    print("\n*** MENU ***")
    print("1. List Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")
    choice = input("Enter your choice (1-3), to exit press q: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3, or 'q'.")

# Library Book Management System

# Store books as a list of dictionaries
library = []

# Function to display all books in a table
def view_books():
    if not library:
        print("\nNo books in the library.\n")
        return
    print("\n{:<5} {:<30} {:<20} {:<6}".format("No.", "Title", "Author", "Year"))
    print("-" * 65)
    for i, book in enumerate(library, start=1):
        print("{:<5} {:<30} {:<20} {:<6}".format(
            i, book['title'], book['author'], book['year']
        ))
    print()

# Function to add a new book
def add_book():
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    while True:
        year = input("Enter Year Published: ").strip()
        if year.isdigit():
            year = int(year)
            break
        else:
            print("Invalid year. Please enter numbers only.")
    library.append({'title': title, 'author': author, 'year': year})
    print("\n✅ Book added successfully!\n")

# Function to search for books by title or author
def search_book():
    if not library:
        print("\nNo books to search.\n")
        return
    keyword = input("Enter Title or Author to search: ").strip().lower()
    results = [book for book in library if keyword in book['title'].lower() 
                                          or keyword in book['author'].lower()]
    if results:
        print("\nSearch Results:")
        print("{:<5} {:<30} {:<20} {:<6}".format("No.", "Title", "Author", "Year"))
        print("-" * 65)
        for i, book in enumerate(results, start=1):
            print("{:<5} {:<30} {:<20} {:<6}".format(i, book['title'], book['author'], book['year']))
        print()
    else:
        print("\nNo matching books found.\n")

# Function to remove a book
def remove_book():
    if not library:
        print("\nNo books to remove.\n")
        return
    view_books()
    while True:
        try:
            choice = int(input("Enter the book number to remove: "))
            if 1 <= choice <= len(library):
                removed = library.pop(choice - 1)
                print(f"\n✅ '{removed['title']}' removed successfully!\n")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to update a book's details
def update_book():
    if not library:
        print("\nNo books to update.\n")
        return
    view_books()
    while True:
        try:
            choice = int(input("Enter the book number to update: "))
            if 1 <= choice <= len(library):
                book = library[choice - 1]
                print("\nLeave blank to keep the existing value.")
                new_title = input(f"Enter new title ({book['title']}): ").strip()
                new_author = input(f"Enter new author ({book['author']}): ").strip()
                new_year = input(f"Enter new year ({book['year']}): ").strip()

                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_year.isdigit():
                    book['year'] = int(new_year)

                print("\n✅ Book updated successfully!\n")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
def main():
    while True:
        print("=" * 40)
        print("📚 Library Book Management 📚")
        print("=" * 40)
        print("1. Add a New Book")
        print("2. View All Books")
        print("3. Search for a Book")
        print("4. Remove a Book")
        print("5. Update Book Details")
        print("6. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            print("\n📖 Thank you for using the Library Book Management System. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()

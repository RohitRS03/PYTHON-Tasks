class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if not title or not isinstance(title, str):
            print("Invalid book title.")
            return
        if not isinstance(quantity, int) or quantity <= 0:
            print("Invalid quantity. Please enter a positive integer.")
            return

        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"Added {quantity} copies of '{title}' to the collection.")

    def remove_book(self, title, quantity):
        if not title or not isinstance(title, str):
            print("Invalid book title.")
            return
        if not isinstance(quantity, int) or quantity <= 0:
            print("Invalid quantity. Please enter a positive integer.")
            return

        if title in self.books:
            if self.books[title] > quantity:
                self.books[title] -= quantity
                print(f"Removed {quantity} copies of '{title}' from the collection.")
            elif self.books[title] == quantity:
                del self.books[title]
                print(f"Removed all copies of '{title}' from the collection.")
            else:
                print(f"Cannot remove {quantity} copies of '{title}'. Only {self.books[title]} copies available.")
        else:
            print(f"'{title}' is not in the collection.")

    def view_books(self):
        if self.books:
            print("Book Collection:")
            for title, quantity in self.books.items():
                print(f"{title}: {quantity} copies")
        else:
            print("The book collection is empty.")

    def get_total_books(self):
        total_books = sum(self.books.values())
        print(f"Total number of books: {total_books}")


def display_menu():
    print("\nMenu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. View Book Collection")
    print("4. Get Total Books")
    print("5. Exit")


def main():
    book_collection = BookCollection()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            quantity = int(input("Enter quantity to add: "))
            book_collection.add_book(title, quantity)
        elif choice == '2':
            title = input("Enter book title: ")
            quantity = int(input("Enter quantity to remove: "))
            book_collection.remove_book(title, quantity)
        elif choice == '3':
            book_collection.view_books()
        elif choice == '4':
            book_collection.get_total_books()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

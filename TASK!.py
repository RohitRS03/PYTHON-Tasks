#Task 1
class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"Added {quantity} copies of '{title}' to the collection.")

    def remove_book(self, title, quantity):
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

# Example usage
book_collection = BookCollection()
book_collection.add_book("Mahabharat", 7)
book_collection.add_book("Ramayan", 5)
book_collection.view_books()
book_collection.remove_book("Mahabharat", 7)
book_collection.view_books()
book_collection.get_total_books()
book_collection.remove_book("Ramayan", 5)
book_collection.view_books()
book_collection.get_total_books()







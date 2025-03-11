import json
import os

BOOKS_FILE = "books.json"

# Load books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, "r") as file:
                return json.load(file) 
        except json.JSONDecodeError:
            return []  # If file is empty or corrupted, return empty list
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)  

# Initialize book list
books = load_books()

def add_book():
    title = input("Enter book title: ").strip()
    if any(book["title"].lower() == title.lower() for book in books):
        print("⚠️ This book already exists!\n")
        return
    
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read = input("Have you read it? (yes/no): ").strip().lower()
    
    if read not in ["yes", "no"]:
        print("⚠️ Invalid input! Enter 'yes' or 'no'.\n")
        return
    
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
    books.append(book)  
    save_books(books)  
    print(f"✅ '{title}' added successfully!\n")

def remove_book():
    global books  
    
    if not books:
        print("⚠️ No books in the library to remove.\n")
        return
    
    title = input("Enter book title to remove: ").strip()
    new_books = [book for book in books if book["title"].lower() != title.lower()]
    
    if len(new_books) == len(books):
        print(f"⚠️ No book found with title '{title}'.\n")
        return
    
    books = new_books  
    save_books(books)  
    print(f"✅ '{title}' removed successfully!\n")

def list_books():
    if not books:
        print("⚠️ No books found in your library.\n")
        return
    
    print("\n📚 Your Library:")
    for book in books:
        print(f"- {book['title']} by {book['author']} ({book['year']}, {book['genre']}) - Read: {book['read']}")
    print()

def search_book():
    query = input("Enter title or author to search: ").strip().lower()
    results = [book for book in books if query in book["title"].lower() or query in book["author"].lower()]
    
    if results:
        print("\n🔎 Search Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}, {book['genre']}) - Read: {book['read']}")
        print()
    else:
        print("⚠️ No matching books found.\n")

def stats():
    total = len(books)
    read = sum(1 for book in books if book["read"] == "yes")
    unread = total - read
    
    print(f"\n📊 Library Stats: {total} Books | ✅ Read: {read} | 📖 Unread: {unread}\n")

def main():
    while True:
        print("\n📚 Personal Library Manager")
        print("1️⃣ Add a Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ List All Books")
        print("4️⃣ Search for a Book")
        print("5️⃣ Show Library Statistics")
        print("6️⃣ Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            stats()
        elif choice == "6":
            print("👋 Exiting... .Have a great day!")
            break
        else:
            print("⚠️ Invalid choice, please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()

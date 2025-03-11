# Personal Library Manager CLI

## 📖 Overview
The **Personal Library Manager CLI** is a Python-based command-line application that allows users to efficiently manage their personal book collection. It provides an intuitive interface for adding, removing, searching, and displaying books while persisting data in a JSON file to ensure information is retained between sessions.

## 🚀 Features
- **Add a Book**: Store book details including title, author, publication year, genre, and read status.
- **Remove a Book**: Delete a book from your collection using its title.
- **List All Books**: View a neatly formatted list of all stored books.
- **Search for a Book**: Find books based on title or author.
- **Display Library Statistics**: Get insights on the number of books read/unread.
- **Persistent Storage**: Books are stored in `books.json` to maintain data across sessions.

## 🛠️ Installation & Setup
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/shezafatima/Personal-Library-Manager-CLI.git
   cd personal-library-manager-cli
   ```
2. Run the program:
   ```sh
   python library_manager.py
   ```

## 📌 Usage
Once the program is running, users will see a menu with the following options:

```
📚 Personal Library Manager
1️⃣ Add a Book
2️⃣ Remove a Book
3️⃣ List All Books
4️⃣ Search for a Book
5️⃣ Show Library Statistics
6️⃣ Exit
```

### Example Actions
- **Adding a Book:**
  - Select `1`, then enter the book details.
  - Example:
    ```
    Enter book title: Harry Potter
    Enter author: J.K Rowling
    Enter publication year: 1997
    Enter genre: Fiction
    Have you read it? (yes/no): yes
    ```
- **Removing a Book:**
  - Select `2`, then enter the book title to remove.
- **Searching for a Book:**
  - Select `4`, then enter the title or author name.
- **Exiting the Application:**
  - Select `6` to safely exit the program.

## 📂 File Structure
```
📂 personal-library-manager-cli/
│── 📄 library_manager.py    # Main script for managing books
│── 📄 books.json            # Storage file for book data
│── 📄 README.md             # Project documentation
```

---

💡 *Developed by Sheza Fatima with ❤️ for book lovers!* 📚


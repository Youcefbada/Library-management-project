import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyodbc

def book(isbn):
    # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
    access_database_path = 'Database/Database.accdb'
    connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    try:
        # Get book information
        cursor.execute('SELECT ISBN, Book_name, publishername, typedelivre, numberpage, edition, bookyears, disponible, Ncopie FROM book WHERE ISBN = ?', (isbn,))
        book_info = cursor.fetchone()

        if book_info:
            # Get borrower IDs from brrow table
            cursor.execute('SELECT ID FROM brrow WHERE ISBN = ?', (isbn,))
            borrower_ids = cursor.fetchall()

            # Get member names from member table using borrower IDs
            member_names = []
            for borrower_id in borrower_ids:
                cursor.execute('SELECT ID, Name, Second_Name FROM member WHERE ID = ?', (borrower_id[0],))
                member_info = cursor.fetchone()
                if member_info:
                    member_names.append(member_info)

            # Display the information in a tkinter window
            display_info_in_window(book_info, member_names)
        
        else:
            messagebox.showinfo('Book Not Found', f'No book found with ISBN {isbn}')

    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Database error: {e}')

    finally:
        # Close the database connection
        conn.close()

def display_info_in_window(book_info, member_names):
    # Create a tkinter window
    window = tk.Tk()
    window.title('BookWise -Book Information and Borrowers-')
    window.geometry("600x600")

    # Display book information
    tk.Label(window, text='Book Information', font=('bold', 14)).pack()
    for i, label in enumerate(['ISBN', 'Book Name', 'Publisher Name', 'Type of Book', 'Number of Pages', 'Edition', 'Year of Publication', 'Available', 'Number of Copies']):
        tk.Label(window, text=f'{label}: {book_info[i]}').pack()

    # Display borrower information
    tk.Label(window, text='\nBorrowers', font=('bold', 14)).pack()
    for i, member_info in enumerate(member_names, start=1):
        tk.Label(window, text=f'Member {i}: ID: {member_info[0]}, Name: {member_info[1]}, Second Name: {member_info[2]}').pack()

    # Run the tkinter main loop
    window.mainloop()


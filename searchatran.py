import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyodbc
def tans(tran_number):
    # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
    access_database_path = 'Database/Database.accdb'
    connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
    conn = pyodbc.connect(connection_string)    
    cursor = conn.cursor()

    try:
        # Get borrow information
        cursor.execute('SELECT TranNumber, ID, ISBN, startdate, enddate FROM brrow WHERE TranNumber = ?', (tran_number,))
        borrow_info = cursor.fetchone()

        if borrow_info:
            # Get member information
            cursor.execute('SELECT Name, Second_Name FROM member WHERE ID = ?', (borrow_info[1],))
            member_info = cursor.fetchone()

            # Get book name from book table using ISBN
            cursor.execute('SELECT Book_name FROM book WHERE ISBN = ?', (borrow_info[2],))
            book_name = cursor.fetchone()

            # Display the information in a tkinter window
            display_info_in_window(borrow_info, member_info, book_name)
        
        else:
            messagebox.showinfo('Transaction Not Found', f'No transaction found with TranNumber {tran_number}')

    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Database error: {e}')

    finally:
        # Close the database connection
        conn.close()

def display_info_in_window(borrow_info, member_info, book_name):
    # Create a tkinter window
    window = tk.Tk()
    window.title('BookWise -Borrow Information and Related Data-')
    window.geometry("600x600")

    # Display borrow information
    tk.Label(window, text='Borrow Information', font=('bold', 14)).pack()
    labels = ['TranNumber', 'ID', 'ISBN', 'Start Date', 'End Date']
    for i, label in enumerate(labels):
        tk.Label(window, text=f'{label}: {borrow_info[i]}').pack()

    # Display member information if available
    if member_info:
        tk.Label(window, text='\nMember Information', font=('bold', 14)).pack()
        tk.Label(window, text=f'Name: {member_info[0]}, Second Name: {member_info[1]}').pack()
    else:
        tk.Label(window, text='\nMember Information', font=('bold', 14)).pack()
        tk.Label(window, text='Member information not available').pack()

    # Display book information if available
    if book_name:
        tk.Label(window, text='\nBook Information', font=('bold', 14)).pack()
        tk.Label(window, text=f'Book Name: {book_name[0]}').pack()
    else:
        tk.Label(window, text='\nBook Information', font=('bold', 14)).pack()
        tk.Label(window, text='Book information not available').pack()

    # Run the tkinter main loop
    window.mainloop()

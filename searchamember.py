import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyodbc

def member(member_id):
    access_database_path = 'Database/Database.accdb'
    connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
    conn = pyodbc.connect(connection_string)    
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT ID, Name, Second_Name, Speciality, phonenumber, Email, Age, Gender, Address FROM member WHERE ID = ?', (member_id,))
        member_info = cursor.fetchone()
        if member_info:
            cursor.execute('SELECT ISBN FROM brrow WHERE ID = ?', (member_id,))
            isbn_values = cursor.fetchall()
            book_names = []
            for isbn in isbn_values:
                cursor.execute('SELECT Book_name FROM book WHERE ISBN = ?', (isbn[0],))
                book_name = cursor.fetchone()
                if book_name:
                    book_names.append(book_name[0])
            display_info_in_window(member_info, book_names)
        else:
            messagebox.showinfo('Member Not Found', f'No member found with ID {member_id}')

    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Database error: {e}')
    finally:
        conn.close()
def display_info_in_window(member_info, book_names):
    window = tk.Tk()
    window.title('BoookWise -Member Information and Books-')
    window.geometry("600x600")
    tk.Label(window, text='Member Information', font=('bold', 14)).pack()
    for i, label in enumerate(['ID', 'Name', 'Second_Name', 'Speciality', 'Phone Number', 'Email', 'Age', 'Gender', 'Address']):
        tk.Label(window, text=f'{label}: {member_info[i]}').pack()
    tk.Label(window, text='\nBook Names', font=('bold', 14)).pack()
    for i, book_name in enumerate(book_names, start=1):
        tk.Label(window, text=f'Book {i}: {book_name}').pack()
    window.mainloop()

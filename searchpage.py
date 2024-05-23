import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pyodbc
import sqlite3
from tkinter import messagebox
from datetime import datetime, timedelta
def searchpages():
    global root
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    root = tk.Tk()
    root.geometry("1700x900")
    root.resizable(False, False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg='#34495e')
    window_width = 1700
    window_height = 900
    center_window(root, window_width, window_height)
    my_frame1 = ctk.CTkFrame(root, corner_radius=20)
    my_frame1.grid(row=0, column=0, padx=(300, 100), pady=5, sticky="new")
    def addmembers2():
        from addmember import addmembers
        root.after(3,root.destroy)
        addmembers()
    def transactionspage2():
        from transaction import transactionspage
        root.after(3,root.destroy)
        transactionspage()
    def addbooks2():
        from addbook import addbooks
        root.after(3,root.destroy)
        addbooks()
    def calculate_late():
            # Connect to the SQLite database
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)  
            cursor = conn.cursor()

            # Fetch data from the 'brrow' table
            cursor.execute("SELECT ID, ISBN, startdate, enddate FROM brrow")
            borrow_data = cursor.fetchall()

            # Calculate late days and filter the data
            late_data = []
            for row in borrow_data:
                book_id, isbn, start_date_str, end_date_str = row
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
                today_date = datetime.now()
                late_days = (today_date - end_date).days
                if late_days > 0:
                    late_data.append((book_id, isbn, late_days))
            return late_data
    def show_late_list():
        late_data = calculate_late()

        # Clear previous data in the treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the treeview
        for row in late_data:
            tree.insert("", "end", values=row)

    def show_member_and_book_info(event):
        selected_item = tree.selection()
        if selected_item:
            selected_id = tree.item(selected_item)['values'][0]

            # Connect to the SQLite database
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)  
            cursor = conn.cursor()
                # Fetch member information
            cursor.execute("SELECT Name, Second_name, phonenumber FROM member WHERE ID=?", (selected_id,))
            member_info = cursor.fetchone()
                # Check if member_info is None
            if member_info is None:
                messagebox.showerror("Member Information", "No information found for the selected member.")
                return
                # Fetch book information
            cursor.execute("SELECT Book_name FROM book INNER JOIN brrow ON book.ISBN = brrow.ISBN WHERE brrow.ID=?", (selected_id,))
            book_name = cursor.fetchall()
                # Check if book_name is None
            if book_name is None:
                messagebox.showerror("Book Information", "No information found for the selected book.")
                return
                # Display the information in a new window
            info_window = tk.Toplevel(root)
            info_window.title("About")
            info_window.geometry("200x200")
            tk.Label(info_window, text="Name:").pack()
            tk.Label(info_window, text=member_info[0]).pack()
            tk.Label(info_window, text="Second Name:").pack()
            tk.Label(info_window, text=member_info[1]).pack()
            tk.Label(info_window, text="Phone Number:").pack()
            tk.Label(info_window, text=member_info[2]).pack()
            tk.Label(info_window, text="Book Name:").pack()
            tk.Label(info_window, text=book_name[0]).pack()
    from searchabook import book
    from searchamember import member
    from searchatran import tans
    searchbox1 = ctk.CTkEntry(my_frame1, placeholder_text='Search..', width=320, corner_radius=20, border_width=3, border_color='lightgreen')
    searchbox1.grid(row=0, column=0, padx=15, pady=10)
    def searchbook():
        if (searchbox1.get()):
            book(searchbox1.get())
        else : 
            messagebox.showerror("ERROR","please enter the data")
    def searchmember():
        if (searchbox1.get()):
            member(searchbox1.get())
        else :
            messagebox.showerror("ERROR","please enter the data")
    def searchtran():
        if (searchbox1.get()):
            tans(searchbox1.get())
        else : 
            messagebox.showerror("ERROR","please enter the data")
    searchmember = ctk.CTkButton(my_frame1, text='Search Member ', width=64, corner_radius=20, fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', border_width=3, border_color='lightgreen',command=searchmember)
    searchmember.grid(row=0, column=1, padx=0, pady=10)
    searchtranscation = ctk.CTkButton(my_frame1, text='Search Transaction ', width=64, corner_radius=20, fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', border_width=3, border_color='lightgreen',command=searchtran)
    searchtranscation.grid(row=0, column=3, padx=0, pady=10)
    searchBook = ctk.CTkButton(my_frame1, text='Search Book ', width=64, corner_radius=20, fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', border_width=3, border_color='lightgreen',command=searchbook)
    searchBook.grid(row=0, column=5, padx=0, pady=10)
    my_frame2 = ctk.CTkFrame(root, corner_radius=20)
    my_frame2.grid(row=0, column=0, padx=100, pady=70, sticky="nsw")
    MainMenuTitle = ctk.CTkLabel(my_frame2, text='Manage')
    MainMenuTitle.grid(row=0, column=0, padx=(10, 10), pady=7)
    Button1 =  ctk.CTkButton(my_frame2, text='Add Book', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=addbooks2)
    Button1.grid(row=1, column=0, padx=(10, 10), pady=7)
    Button2 = ctk.CTkButton(my_frame2, text='Add Transaction', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=transactionspage2)
    Button2.grid(row=2, column=0, padx=(10, 10), pady=7)
    Button3 = ctk.CTkButton(my_frame2, text='Add Member', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=addmembers2)
    Button3.grid(row=3, column=0, padx=(10, 10), pady=7)
    Button4 = ctk.CTkButton(my_frame2, text='Late', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen')
    Button4.grid(row=4, column=0, padx=(10, 10), pady=7)
    my_frame7 = ctk.CTkFrame(root, corner_radius=20)
    my_frame7.grid(row=0, column=0, padx=(300, 100), pady=70, sticky="nsew")
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 10))
    tree = ttk.Treeview(my_frame7, columns=("ID", "ISBN", "Late Days"))  
    tree.heading("#0", text="Head")
    tree.heading("ID", text="ID")
    tree.heading("ISBN", text="ISBN")
    tree.heading("Late Days", text="Late Days")
    tree.column("#0", stretch=tk.NO, width=0)
    tree.column("ID", anchor=tk.CENTER, width=300)
    tree.column("ISBN", anchor=tk.CENTER, width=300)
    tree.column("Late Days", anchor=tk.CENTER, width=300)
    tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    vsb = ttk.Scrollbar(my_frame7, orient="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, pady=10, sticky="ns")
    tree.configure(yscrollcommand=vsb.set)
    tree.bind("<ButtonRelease-1>", show_member_and_book_info)
    my_frame7.rowconfigure(0, weight=1)
    my_frame7.columnconfigure(0, weight=1)
    tree.grid(sticky="nsew")
    show_late_list()

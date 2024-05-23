import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
from textonimage import brow
import sqlite3
from tkinter import messagebox
from datetime import datetime
import pyodbc

def transactionspage():
    global root
    import pyodbc

    def get_disponible_by_isbn2(isbn, whatwewant):
        # Connect to the Access database
        access_database_path = 'Database/Database.accdb'
        connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
        conn = pyodbc.connect(connection_string)
        
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        try:
            # Execute the query to select the 'disponible' column where ISBN matches
            query = f"SELECT {whatwewant} FROM book WHERE ISBN = ?"
            cursor.execute(query, (isbn,))

            # Fetch the result
            result = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            conn.close()

            # Return the result as a boolean (True if 'Y', False if 'N', None if no match is found)
            return True if result and result[0] == True else (False if result and result[0] == False else None)

        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            # Handle the error as needed, e.g., log it or raise an exception
            return None

    def get_disponible_by_isbn(isbn,whatwewant):
        # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
        access_database_path = 'Database/Database.accdb'
        connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
        conn = pyodbc.connect(connection_string)         # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute the query to select the 'disponible' column where ISBN matches
        query = f"SELECT {whatwewant} FROM book WHERE ISBN = ?"
        cursor.execute(query, (isbn,))
        # Fetch the result
        result = cursor.fetchone()
        # Close the cursor and connection
        cursor.close()
        conn.close()
        # Return the result (or None if no match is found)
        return result[0] if result else None
    def is_valid_date(date_str):
        try:
            # Attempt to parse the date using the specified format
            datetime_object = datetime.strptime(date_str, '%d/%m/%Y')
            # If successful, the date is valid
            return True
        except ValueError:
            # If an exception is raised, the date is not valid
            return False
    
    def is_first_date_greater(date1_str, date2_str):
        # Check if both dates are valid
        if not is_valid_date(date1_str) or not is_valid_date(date2_str):
            return False

        # Parse the date strings into datetime objects
        date1 = datetime.strptime(date1_str, '%d/%m/%Y')
        date2 = datetime.strptime(date2_str, '%d/%m/%Y')

        # Compare the dates
        return date1 > date2
    def close_window():
        new_window.destroy()
    def has_duplicate_isbn_for_id(database_path, borrower_id):
        access_database_path = 'Database/Database.accdb'
        connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
        conn = pyodbc.connect(connection_string)        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the query to count occurrences of each ISBN for the given ID
        query = "SELECT ISBN, COUNT(*) FROM brrow WHERE ID = ? GROUP BY ISBN HAVING COUNT(*) > 1"
        cursor.execute(query, (borrower_id,))

        # Fetch the result
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return True if there are duplicates, False otherwise
        return len(result) > 0
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
    root.title('BookWise - TRANSACTION - ')
    window_width = 1700
    window_height = 900
    center_window(root, window_width, window_height)
    my_frame1 = ctk.CTkFrame(root, corner_radius=20)
    my_frame1.grid(row=0, column=0, padx=(300, 100), pady=5, sticky="new")
    def addmembers2():
        from addmember import addmembers
        root.after(3,root.destroy)
        addmembers()
    def searchpages2():
        from searchpage import searchpages
        root.after(3,root.destroy)
        searchpages()
    def addbooks2():
        from addbook import addbooks
        root.after(3,root.destroy)
        addbooks()
    #_set_appearance_mode('dark')
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
    #1# Main Menu
    my_frame2 = ctk.CTkFrame(root, corner_radius=20)
    my_frame2.grid(row=0, column=0, padx=100, pady=70, sticky="nsw")
    MainMenuTitle = ctk.CTkLabel(my_frame2, text='Manage')
    MainMenuTitle.grid(row=0, column=0, padx=(10, 10), pady=7)
    Button1 =  ctk.CTkButton(my_frame2, text='Add Book', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=addbooks2)
    Button1.grid(row=1, column=0, padx=(10, 10), pady=7)
    Button2 = ctk.CTkButton(my_frame2, text='Add Transaction', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen')
    Button2.grid(row=2, column=0, padx=(10, 10), pady=7)
    Button3 = ctk.CTkButton(my_frame2, text='Add Member', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=addmembers2)
    Button3.grid(row=3, column=0, padx=(10, 10), pady=7)
    Button4 = ctk.CTkButton(my_frame2, text='Late', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=searchpages2)
    Button4.grid(row=4, column=0, padx=(10, 10), pady=7)
    #4# Add Transactions Page
    my_frame5 = ctk.CTkFrame(root, corner_radius=20)
    my_frame5.grid(row=0, column=0, padx=(300, 100), pady=70, sticky="nsew")
    age = ctk.CTkLabel(my_frame5, text='Member ID :')
    age.grid(row=0, column=0, padx=(0, 300), pady=10, sticky="ew")
    ID = ctk.CTkEntry(my_frame5, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    ID.grid(row=1, column=0, padx=200, pady=0)
    DoB = ctk.CTkLabel(my_frame5, text='Book ISBN :')
    DoB.grid(row=2, column=0, padx=(0, 300), pady=10, sticky="ew")
    ISBN = ctk.CTkEntry(my_frame5, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    ISBN.grid(row=3, column=0, padx=200, pady=0)
    DoB = ctk.CTkLabel(my_frame5, text='From Date (DD/MM/YYYY)')
    DoB.grid(row=4, column=0, padx=(0, 300), pady=10, sticky="ew")
    DoB_ = ctk.CTkEntry(my_frame5, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    DoB_.grid(row=5, column=0, padx=200, pady=0)
    Address = ctk.CTkLabel(my_frame5, text='To Date (DD/MM/YYYY)')
    Address.grid(row=6, column=0, padx=(0, 300), pady=10, sticky="ew")
    Address_ = ctk.CTkEntry(my_frame5, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    Address_.grid(row=7, column=0, padx=200, pady=0)
    def savetansaction():
        if is_valid_date(Address_.get()) : 
            if is_valid_date(DoB_.get()) : 
                if is_first_date_greater(Address_.get(),DoB_.get()) :
                    dipon = get_disponible_by_isbn2(str(ISBN.get()),"disponible")
                    print(dipon)
                    nco = get_disponible_by_isbn(str(ISBN.get()),"Ncopie")
                    access_database_path = 'Database/Database.accdb'
                    connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
                    conn = pyodbc.connect(connection_string)  
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM member WHERE ID = ?", (str(ID.get()),))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        cursor.execute("SELECT COUNT(*) FROM book WHERE ISBN = ?", (str(ISBN.get()),))
                        count2 = cursor.fetchone()[0]
                        if count2 > 0:
                            database_path = access_database_path
                            has_duplicate_isbn = has_duplicate_isbn_for_id(database_path,str(ID.get()))
                            if has_duplicate_isbn:
                                messagebox.showerror("ERROR","This member get this book before")
                            else : 
                                if ((dipon == True) & (int(nco)> 0)) :
                                    #try :
                                        query = "SELECT TOP 1 TranNumber FROM brrow ORDER BY ID DESC"
                                        cursor.execute(query)
                                        result = cursor.fetchone()
                                        # Check if there is a result
                                        if result is not None:
                                            number_value = result[0]
                                            number = number_value + 1 
                                            data_to_insert = (number , str(ID.get()) ,str(ISBN.get()) , str(DoB_.get()) , str(Address_.get()))
                                            cursor.execute('INSERT INTO brrow (TranNumber,ID,ISBN,startdate,enddate) VALUES (?,?,?,?,?)', data_to_insert)
                                            brow(str(ID.get()),str(ISBN.get()),str(DoB_.get()),str(Address_.get()),number)
                                            query = "UPDATE book SET Ncopie = ? WHERE ISBN = ?"
                                            nco = int(nco) -1 
                                            cursor.execute(query, (str(nco), str(ISBN.get())))
                                        else:
                                            number = 1
                                            data_to_insert = (number , str(ID.get()) ,str(ISBN.get()) , str(DoB_.get()) , str(Address_.get()))
                                            cursor.execute('INSERT INTO brrow (TranNumber,ID,ISBN,startdate,enddate) VALUES (?,?,?,?,?)', data_to_insert)
                                            query = "UPDATE book SET Ncopie = ? WHERE ISBN = ?"
                                            nco = int(nco) -1 
                                            brow(str(ID.get()),str(ISBN.get()),str(DoB_.get()),str(Address_.get()),number)
                                            cursor.execute(query, (str(nco), str(ISBN.get())))
                                        conn.commit()
                                        conn.close()
                                        message_box = messagebox.showinfo("OK", "OK")
                                    #except : 
                                     #   messagebox.showerror('ERROR','There is a problem in database please check the file')
                                else : 
                                    messagebox.showerror('ERROR',"the book not aviable")
                        else: 
                            messagebox.showerror('ERROR','there is no book with this ISBN ')
                    else :
                        messagebox.showerror('ERROR','there is no member with this ID ')
                else : 
                    messagebox.showerror('ERROR','End date must be big than take date')
            else : 
                messagebox.showerror('ERROR','Data type of date is DD/MM/YYYY')
        else : 
            messagebox.showerror('ERROR','Data type of date is DD/MM/YYYY')
    savebuttonTransactions = ctk.CTkButton(my_frame5, text='Save Transaction', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=savetansaction)
    savebuttonTransactions.grid(row=19, column=0, padx=(250, 0), pady=20, sticky='e')
    tk.Label(my_frame5,text="Back a Boook",font=('Times 20')).place(x=500,y=450)
    DoB = ctk.CTkLabel(my_frame5, text='Tran Num :')
    DoB.place(x=450,y=500)
    numbertoremove = ctk.CTkEntry(my_frame5, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    numbertoremove.place(x=450,y=530)
    def removetran():
        if (numbertoremove.get()) :
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT ISBN FROM brrow WHERE TranNumber = ?', (numbertoremove.get(),))
            isbn_value = cursor.fetchone()
            if isbn_value:
                cursor.execute('DELETE FROM brrow WHERE TranNumber = ?', (numbertoremove.get(),))
                isbn =  isbn_value[0]  
                query = "UPDATE book SET Ncopie = ? WHERE ISBN = ?"
                nco = get_disponible_by_isbn(str(isbn),"Ncopie")
                nco = int(nco) + 1
                cursor.execute(query, (str(nco), str(isbn)))
                conn.commit()
                messagebox.showinfo("ERROR",f"Row with TranNumber {numbertoremove.get()} deleted successfully.")
            else:
                messagebox.showerror("ERROR",f"No row found with TranNumber {numbertoremove.get()}. Nothing deleted.")
        else : 
            messagebox.showerror("ERROR","Enter a Value please")
    def beforeremove():
        new_window = tk.Toplevel(root)
        new_window.title("BookWise -Remove Transaction-")
        new_window.geometry("400x300")
        custom_font = ("Arial", 12)
        label = tk.Label(new_window, text=f"Are you Sure remove Transaction : {numbertoremove.get() }",font=custom_font)
        label.pack()
        label = tk.Label(new_window, text="")
        label.pack()
        label = tk.Label(new_window, text="")
        label.pack()
        def test22():
            removetran()
            close_window()
        yes_button = tk.Button(new_window, text="Yes", bg='green', fg='white', width=10, height=2,font=custom_font,command=test22)
        yes_button.pack()
        label = tk.Label(new_window, text="")
        label.pack()
        no_button = tk.Button(new_window, text="No", bg='red', fg='white', width=10,height=2,font=custom_font,command=close_window)
        no_button.pack()
    remove = ctk.CTkButton(my_frame5, text='Remove', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=beforeremove)
    remove.place(x = 900,y=520)
    root.mainloop()


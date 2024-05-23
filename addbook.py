import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import pyodbc
import sqlite3 
from tkinter import messagebox
def addbooks():
    global root
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    root = tk.Tk()
    root.geometry("1700x900")
    window_width = 1700
    window_height = 900
    root.resizable(False, False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg='#34495e')
    root.title('BookWise - ADD BOOK - ')
    center_window(root, window_width, window_height)
    my_frame1 = ctk.CTkFrame(root, corner_radius=20)
    my_frame1.grid(row=0, column=0, padx=(300, 100), pady=5, sticky="new")
    def close_window():
        new_window.destroy()
    def addmembers2():
        from addmember import addmembers
        root.after(3,root.destroy)
        addmembers()
    def transactionspage2():
        from transaction import transactionspage
        root.after(3,root.destroy)
        transactionspage()
    def searchpages2():
        from searchpage import searchpages
        root.after(3,root.destroy)
        searchpages()
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
    Button1 =  ctk.CTkButton(my_frame2, text='Add Book', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen')
    Button1.grid(row=1, column=0, padx=(10, 10), pady=7)
    Button2 = ctk.CTkButton(my_frame2, text='Add Transaction', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=transactionspage2)
    Button2.grid(row=2, column=0, padx=(10, 10), pady=7)
    Button3 = ctk.CTkButton(my_frame2, text='Add Member', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=addmembers2)
    Button3.grid(row=3, column=0, padx=(10, 10), pady=7)
    Button4 = ctk.CTkButton(my_frame2, text='Late', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=searchpages2)
    Button4.grid(row=4, column=0, padx=(10, 10), pady=7)
    # book 
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    my_frame3 = ctk.CTkFrame(root, corner_radius=20)
    my_frame3.grid(row=0, column=0, padx=(300, 100), pady=70, sticky="nsew")
    a11 = ctk.CTkLabel(my_frame3, text='Name of The Book')
    a11.place(x=40, y=17)
    a1 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a1.place(x=30, y=47)
    a22 = ctk.CTkLabel(my_frame3, text='Number of Page :')
    a22.place(x=510, y=17)
    a2 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a2.place(x=500, y=47)
    a33 = ctk.CTkLabel(my_frame3, text='Author Name')
    a33.place(x=40, y=90)
    a3 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a3.place(x=30, y=120)
    a44 = ctk.CTkLabel(my_frame3, text='Disponible or not (Y/N):')
    a44.place(x=510, y=90)
    a4 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a4.place(x=500, y=120)
    a55 = ctk.CTkLabel(my_frame3, text='edition:')
    a55.place(x=40, y=160)
    a5 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a5.place(x=30, y=190)
    a66 = ctk.CTkLabel(my_frame3, text='Publish Year')
    a66.place(x=510, y=160)
    a6 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a6.place(x=500, y=190)
    a77 = ctk.CTkLabel(my_frame3, text='Copies Available')
    a77.place(x=40, y=230)
    a7 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a7.place(x=30, y=260)
    a88 = ctk.CTkLabel(my_frame3, text='Categories')
    a88.place(x=510, y=230)
    a8 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a8.place(x=500, y=260)
    a99 = ctk.CTkLabel(my_frame3, text='ISBN')
    a99.place(x=40, y=310)
    a9 = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    a9.place(x=30, y=340)
    def add():
        if all(var is not None and var != '' for var in (a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(), a8.get(), a9.get())):
            if (str(a4.get()) == "Y" or str(a4.get()) == 'N') :
                if(str(a4.get() == 'Y')) :
                    disponible = True
                if(str(a4.get() == 'N')) :
                    disponible = False
                access_database_path = 'Database/Database.accdb'
                connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
                conn = pyodbc.connect(connection_string)                
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM book WHERE ISBN = ?", (str(a9.get()),))
                count = cursor.fetchone()[0]
                if count > 0 : 
                    messagebox.showerror("ERROR","There is a book with this ISBN in database")
                else : 
                    #count = cursor.fetchone()[0]
                    ISBN = str(a9.get())
                    Book_name = str(a1.get())
                    publishername = str(a3.get())
                    typedeliver = str(a8.get())
                    numberpage = int(a2.get())
                    edition = str(a5.get())
                    bookyears = str(a6.get())
                    copie = int(a7.get())
                    data_to_insert = (ISBN , Book_name ,publishername , typedeliver , numberpage , edition ,bookyears ,True,copie)
                    cursor.execute('INSERT INTO book (ISBN,Book_name,publishername,typedelivre,numberpage,edition,bookyears,disponible,Ncopie) VALUES (?,?,?,?,?,?,?,?,?)', data_to_insert)
                    # Commit the changes and close the connection
                    conn.commit()
                    conn.close()
                    message_box = messagebox.showinfo("OK", f"The new book save , ISBN : {ISBN}")
            else : 
                messagebox.showerror("ERROR","Please Enter Y/N ")
        else : 
            messagebox.showerror("ERROR","there is a empty entry please completed")
    try : 
        savebuttonAddBook = ctk.CTkButton(my_frame3, text='Add Book', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=add)
        savebuttonAddBook.grid(padx=(400, 500), pady=440, sticky='e')
    except : 
        messagebox.ERROR('ERROR','There is a problem in database please check the file')
    Email = ctk.CTkLabel(my_frame3, text='ISBN :')
    Email.place(x=455,y=580)
    ISBN = ctk.CTkEntry(my_frame3, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    ISBN.place(x=450,y=610)
    def modifie(): 
        if(ISBN.get()) : 
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM book WHERE ISBN = ?", (str(ISBN.get()),))
            count = cursor.fetchone()[0]
            if count > 0 : 
                new_window = tk.Toplevel(root)
                new_window.title("BookWise -Modifie Book deatils-")
                new_window.geometry("700x400")
                label = tk.Label(new_window, text="IF YOU WANT TO CHANGE SOME THING PUT THE VALUE IF NOT DON'T PUT ANY THING")
                label.pack()
                label = tk.Label(new_window, text="")
                label.pack()
                label = tk.Label(new_window, text="Disponible or not (Y/N) :")
                label.pack()
                Disponible = tk.Entry(new_window)
                Disponible.pack()
                label = tk.Label(new_window, text="")
                label.pack()
                label = tk.Label(new_window, text="N copie :")
                label.pack()
                Ncopie = tk.Entry(new_window)
                Ncopie.pack()
                label = tk.Label(new_window, text="")
                label.pack()
                def updatenew():
                    if str(Disponible.get()) == 'Y':
                        disponible = True
                    elif str(Disponible.get()) == 'N':
                        disponible = False
                    else:
                        messagebox.showerror("ERROR", "Invalid value for 'Disponible'")
                        return

                    if str(Ncopie.get()):
                        if str(Disponible.get()):
                            query = "UPDATE book SET disponible = ?, Ncopie = ? WHERE ISBN = ?"
                            cursor.execute(query, (disponible, str(Ncopie.get()), str(ISBN.get())))
                            conn.commit()
                            messagebox.showinfo("Ok", "Ok")
                        else:
                            query = "UPDATE book SET Ncopie = ? WHERE ISBN = ?"
                            cursor.execute(query, (str(Ncopie.get()), str(ISBN.get())))
                            conn.commit()
                            messagebox.showinfo("Ok", "Ok")
                    else:
                        if str(Disponible.get()):
                            query = "UPDATE book SET disponible = ? WHERE ISBN = ?"
                            cursor.execute(query, (disponible, str(ISBN.get())))
                            conn.commit()
                            messagebox.showinfo("Ok", "Ok")
                        else:
                            messagebox.showerror("ERROR", "There is no Value")

                tk.Button(new_window,text="Update",command=updatenew).pack()
    modifiebook= ctk.CTkButton(my_frame3, text='Modifie Book', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=modifie)
    modifiebook.place(x =900, y=600)
    def removetran():
        if (ISBN.get()) :
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT ISBN FROM book WHERE ISBN = ?', (ISBN.get(),))
            isbn_value = cursor.fetchone()
            if isbn_value:
                cursor.execute('DELETE FROM book WHERE ISBN = ?', (ISBN.get(),))
                conn.commit()
                messagebox.showinfo("Ok",f"Row with ISBN :  {ISBN.get()} deleted successfully.")
            else:
                messagebox.showerror("ERROR",f"No row found with ISBN : {ISBN.get()}. Nothing deleted.")
        else : 
            messagebox.showerror("ERROR","Enter a Value please")
    def beforeremove():
        new_window = tk.Toplevel(root)
        new_window.title("BookWise -Remove Book-")
        new_window.geometry("400x300")
        custom_font = ("Arial", 12)
        label = tk.Label(new_window, text=f"Are you Sure remove Book : {ISBN.get() }",font=custom_font)
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
    delete= ctk.CTkButton(my_frame3, text='Remove  Book', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=beforeremove)
    delete.place(x =900, y=670)
    # this function for close all the window that open when click close button
    def on_close():
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
if __name__ == "__main__":
    page3()

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
from datetime import datetime
import sqlite3 
import re
from tkinter import messagebox
import pyodbc
from textonimage import crad
def addmembers():
    global root
    def is_valid_date(date_str):
        try:
            # Attempt to parse the date using the specified format
            datetime_object = datetime.strptime(date_str, '%d/%m/%Y')
            # If successful, the date is valid
            return True
        except ValueError:
            # If an exception is raised, the date is not valid
            return False
    def close_window():
        new_window.destroy()
    def get_year_from_date(date_str):
        try:
            # Attempt to parse the date using the specified format
            datetime_object = datetime.strptime(date_str, '%d/%m/%Y')
            # Extract the year from the datetime object
            year = datetime_object.year
            return year
        except ValueError:
            # If an exception is raised, the date is not valid
            return None
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
    root.title('BookWise - ADD MEMBER - ')
    window_width = 1700
    window_height = 900
    center_window(root, window_width, window_height)
    my_frame1 = ctk.CTkFrame(root, corner_radius=20)
    my_frame1.grid(row=0, column=0, padx=(300, 100), pady=5, sticky="new")
    def transactionspage2():
        from transaction import transactionspage
        root.after(3,root.destroy)
        transactionspage()
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
    Button2 = ctk.CTkButton(my_frame2, text='Add Transaction', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=transactionspage2)
    Button2.grid(row=2, column=0, padx=(10, 10), pady=7)
    Button3 = ctk.CTkButton(my_frame2, text='Add Member', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen')
    Button3.grid(row=3, column=0, padx=(10, 10), pady=7)
    Button4 = ctk.CTkButton(my_frame2, text='Late', fg_color='#F5F5F5', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=searchpages2)
    Button4.grid(row=4, column=0, padx=(10, 10), pady=7)
    my_frame4 = ctk.CTkFrame(root, corner_radius=20)
    my_frame4.grid(row=0, column=0, padx=(300, 100), pady=70, sticky="nsew")
    name = ctk.CTkLabel(my_frame4,text="Name")
    name.place(x=25,y=20)
    name1 = ctk.CTkEntry(my_frame4,fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    name1.place(x=20,y=50)
    secondname = ctk.CTkLabel(my_frame4,text="Second Name")
    secondname.place(x=505,y=20)
    secondname2 = ctk.CTkEntry(my_frame4,fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    secondname2.place(x=500,y=50)
    age = ctk.CTkLabel(my_frame4, text='Age')
    age.place(x=25,y=100)
    age_ = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    age_.place(x=20,y=130)
    sex = ['Male','Female']
    Speciality = ctk.CTkLabel(my_frame4, text='Select Gender')
    Speciality.place(x=505,y=100)
    MaleFemale = ctk.CTkComboBox(my_frame4,values=sex)
    MaleFemale.configure(width = 300,height=50,border_color = 'lightgreen',corner_radius=10)
    MaleFemale.place(x=500,y=130)
    DoB = ctk.CTkLabel(my_frame4, text='Date of Birth:')
    DoB.place(x=20,y=200)
    DoB_ = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    DoB_.place(x=25,y=230)
    Address = ctk.CTkLabel(my_frame4, text='Address:')
    Address.place(x=505,y=200)
    Address_ = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    Address_.place(x=500,y=230)
    Numberphone = ctk.CTkLabel(my_frame4, text='Number of phone :')
    Numberphone.place(x=20,y=300)
    Numberphone_ = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    Numberphone_.place(x=25,y=330)
    Email = ctk.CTkLabel(my_frame4, text='Email :')
    Email.place(x=505,y=300)
    Email_ = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    Email_.place(x=500,y=330)
    def add():
        if is_valid_date(DoB_.get()):
            what = get_year_from_date(DoB_.get())
            current_year = datetime.now().year
            print(int(current_year) - int(what))
            print(int(age_.get()))
            if ((int(current_year) - int(what)) == int(age_.get())) : 
                    access_database_path = 'Database/Database.accdb'
                    connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()
                    current_year = datetime.now().year
                    spe = str(current_year)
                    cursor.execute('SELECT * FROM member WHERE ID LIKE ? ORDER BY ID DESC ',(f'%{spe}%',))
                    last_row = cursor.fetchone()
                    if last_row is not None and last_row[0] is not None:
                        first_column_value=  str(last_row[0])
                        match = re.search(rf'{spe}(\d+)', first_column_value)
                        number = int (match.group(1)) + 1
                        ID = str(str(current_year)+ str(number))
                        years = spe
                        data_to_insert = (ID,str(name1.get()) , str(secondname2.get()),str(Numberphone_.get()) , str(Email_.get()),int(age_.get()),str(MaleFemale.get()),str(Address_.get()))
                        cursor.execute('INSERT INTO member (ID,Name,Second_name,phonenumber,Email,Age,Gender,Address) VALUES (?,?,?,?,?,?,?,?)', data_to_insert)
                        crad(str(name1.get()),str(secondname2.get()),str(ID),str(years))
                        # Commit the changes and close the connection
                    else : 
                        number = 1
                        ID = str(str(current_year) +str(number))
                        years = "2023/2024"
                        data_to_insert = (ID,str(name1.get()) , str(secondname2.get()),str(Numberphone_.get()) , str(Email_.get()),int(age_.get()),str(MaleFemale.get()),str(Address_.get()))
                        cursor.execute('INSERT INTO member (ID,Name,Second_name,phonenumber,Email,Age,Gender,Address) VALUES (?,?,?,?,?,?,?,?)', data_to_insert)
                        crad(str(name1.get()),str(secondname2.get()),str(ID),str(years))
                    conn.commit()
                    conn.close()
                    message_box = messagebox.showinfo("OK", f"The new member save , ID : {ID}")
            else : 
                messagebox.showerror("ERROR","the age not correct")
        else :
            messagebox.showerror('ERROR','Data type of date is DD/MM/YYYY')
    addmember = ctk.CTkButton(my_frame4, text='Add Member', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=add)
    addmember.grid(padx=(300, 400), pady=450, sticky='e')
    Email = ctk.CTkLabel(my_frame4, text='ID :')
    Email.place(x=455,y=580)
    ID = ctk.CTkEntry(my_frame4, fg_color='#F5F5F5', text_color='black', width=400, height=40, corner_radius=10, border_width=3, border_color='lightgreen')
    ID.place(x=450,y=610)
    def modifie(): 
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM member WHERE ID = ?", (str(ID.get()),))
        count = cursor.fetchone()[0]
        if count > 0 : 
            # hocin here if you want to change the design of the poped window 
            new_window = tk.Toplevel(root)
            new_window.title("BookWise -Modifie Member deatils-")
            new_window.geometry("700x400")
            label = tk.Label(new_window, text="IF YOU WANT TO CHANGE SOME THING PUT THE VALUE IF NOT DON'T PUT ANY THING")
            label.pack()
            label = tk.Label(new_window, text="")
            label.pack()
            label = tk.Label(new_window, text="Phone number :")
            label.pack()
            newnumber = tk.Entry(new_window)
            newnumber.pack()
            label = tk.Label(new_window, text="")
            label.pack()
            label = tk.Label(new_window, text="Email :")
            label.pack()
            newemail = tk.Entry(new_window)
            newemail.pack()
            label = tk.Label(new_window, text="")
            label.pack()
            label = tk.Label(new_window, text="Addres :")
            label.pack()
            newadrees = tk.Entry(new_window)
            newadrees.pack()
            label = tk.Label(new_window, text="")
            label.pack()
            def updatenew():
                if str(newnumber.get()) : 
                    if str(newemail.get()) : 
                        if str(newadrees.get()) :
                            query = "UPDATE member SET Email = ?, phonenumber = ?, Address = ? WHERE ID = ?"
                            cursor.execute(query, (str(newemail.get()), str(newnumber.get()),str(newadrees.get()), str(ID.get())))
                            conn.commit()
                        else : 
                            query = "UPDATE member SET Email = ?, phonenumber = ? WHERE ID = ?"
                            cursor.execute(query, (str(newemail.get()), str(newnumber.get()), str(ID.get())))
                            conn.commit()        
                    else : 
                        query = "UPDATE member SET phonenumber = ? WHERE ID = ?"
                        cursor.execute(query, str(newnumber.get()), str(ID.get()))
                        conn.commit()
                else : 
                    messagebox.showerror("ERROR","WHY YOU ENTER :(")
                messagebox.showinfo("Ok","Ok")
            tk.Button(new_window,text="Update",command=updatenew).pack()
        else : 
            messagebox.showerror("ERROR","There is no member with this ID")
    modifiemember= ctk.CTkButton(my_frame4, text='Modifie Member', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=modifie)
    modifiemember.place(x =900, y=600)
    def removetran():
        if (ID.get()) :
            access_database_path = 'Database/Database.accdb'
            connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM member WHERE ID = ?", (ID.get()))
            isbn_value = cursor.fetchone()
            if isbn_value:
                cursor.execute("DELETE FROM member WHERE ID =  ?", (ID.get()))
                conn.commit()
                messagebox.showinfo("ERROR",f"Row with ID {ID.get()} deleted successfully.")
            else:
                messagebox.showerror("ERROR",f"No row found with ID {ID.get()}. Nothing deleted.")
        else : 
            messagebox.showerror("ERROR","Enter a Value please")
    def beforeremove():
        new_window = tk.Toplevel(root)
        new_window.title("BookWise -Remove member-")
        new_window.geometry("400x300")
        custom_font = ("Arial", 12)
        label = tk.Label(new_window, text=f"Are you Sure remove member: {ID.get() }",font=custom_font)
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
    delete= ctk.CTkButton(my_frame4, text='Remove Member', fg_color='lightgreen', text_color='black', hover_color='lightgreen', height=50, corner_radius=30, border_width=3, border_color='lightgreen',command=beforeremove)
    delete.place(x =900, y=670)
    root.mainloop()

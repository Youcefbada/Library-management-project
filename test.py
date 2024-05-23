import tkinter as tk

def addbooks():
    root = tk.Tk()
    root.title("Add Books")

    # Set the path to your .ico file
    try:
        root.iconbitmap(icon_path)
    except tk.TclError as e:
        print(f"Error: {e}")
        print(f"Unable to load icon from file '{icon_path}'")

    # Your GUI code goes here

    root.mainloop()

if __name__ == "__main__":
    addbooks()

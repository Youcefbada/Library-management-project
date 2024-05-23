import pyodbc

access_database_path = 'Database/Database.accdb'
connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_database_path};'

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Fetch member information
    selected_id = 1 # Replace with the actual value
    cursor.execute("SELECT Name, Second_name, phonenumber FROM member WHERE ID=?", (selected_id,))
    
    # Fetch the results
    rows = cursor.fetchall()

    for row in rows:
        print("Name:", row.Name)
        print("Second Name:", row.Second_name)
        print("Phone Number:", row.phonenumber)

except Exception as e:
    print(f"An error occurred: {str(e)}")


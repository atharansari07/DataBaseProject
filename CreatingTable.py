import sqlite3
conn=sqlite3.connect("FirstDataBase.db")

conn.execute('''
                    CREATE TABLE student (
                    st_id INT AUTO_INCREAMENT PRIMARY KEY,
                    st_Name VARCHAR(50),
                    st_Class VARCHAR(50),
                    st_Email VARCHAR(50)
                    )''')
conn.commit()
conn.close()
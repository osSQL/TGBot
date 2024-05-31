import sqlite3

conn = sqlite3.connect('tg.dp')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAl
    )
''')

cursor.execute('''
INSERT INTO students(name,grade)
VALUES ('Masha',162.5), ('Misha',190) , ('Sasha',175.5)
''')

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
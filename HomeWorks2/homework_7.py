import sqlite3

def create_table():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            thor TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')



def insert_books():
    books_data = [
        ('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 'Фэнтези', 223, 5),
        ('Гарри Поттер и тайная комната', 'Джоан Роулинг', 1998, 'Фэнтези', 251, 4),
        ('Гарри Поттер и узник Азкабана', 'Джоан Роулинг', 1999, 'Фэнтези', 317, 3),
        ('Гарри Поттер и Кубок огня', 'Джоан Роулинг', 2000, 'Фэнтези', 636, 4),
        ('Игра престолов', 'Джордж Мартин', 1996, 'Фэнтези', 694, 5),
        ('Битва королей', 'Джордж Мартин', 1998, 'Фэнтези', 768, 3),
        ('Буря мечей', 'Джордж Мартин', 2000, 'Фэнтези', 973, 2),
        ('Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 1954, 'Фэнтези', 423, 4),
        ('Властелин колец: Две крепости', 'Дж. Р. Р. Толкин', 1954, 'Фэнтези', 352, 3),
        ('Властелин колец: Возвращение короля', 'Дж. Р. Р. Толкин', 1955, 'Фэнтези', 416, 5)
    ]
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books")
    cursor.executemany('''
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books_data)
    conn.commit()


def show_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == '__main__':
    create_table()
    insert_books()
    show_books()



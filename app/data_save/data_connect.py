import sqlite3
import os


__dir_db = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

con = sqlite3.connect(f"{__dir_db}/tutorial.db")

cur = con.cursor()

res = cur.execute(
    "SELECT * FROM movie;"
)
print(res.fetchall())


'''
>>> import sqlite3

>>> con = sqlite3.connect("tutorial.db")

>>> cur = con.cursor()

>>> cur.execute("CREATE TABLE movie(title, year, score)")

>>> res = cur.execute("SELECT name FROM sqlite_master")

>>> res.fetchone()
('movie',)

>>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

>>> res.fetchone() is None
True

>>> cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

>>> con.commit()

>>> res = cur.execute("SELECT score FROM movie")
>>> res.fetchall()
[(8.2,), (7.5,)]
'''
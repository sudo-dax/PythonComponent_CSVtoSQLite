import sqlite3, csv, sys

# Variables 
db_filename = "feeds.db"
data_filename = sys.argv[1]

SQL = """
insert into feed (Firstseen, DstIP, DstPort)
values (:Firstseen, :DstIP, :DstPort)
"""

#  Create and connect to DB
con = sqlite3.connect('feeds.db')
cur = con.cursor()

#  Create New Table in Database
def create_table():
    cur.execute('DROP TABLE IF EXISTS feed')
    cur.execute("""CREATE TABLE IF NOT EXISTS feed(
        'Firstseen' TEXT,
        'DstIP' TEXT,
        'DstPort' TEXT
        )""")
create_table()


with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)

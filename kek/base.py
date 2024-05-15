import csv
import sqlite3

con = sqlite3.connect('WBbase3.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Client(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavshik(
    id integer primary key autoincrement,
    Number integer,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tovar(
    id integer primary key autoincrement,
    Name text,
    Postavshikid integer references Postavshik(id),
    count integer,
    idClient integer references Client(id)
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Rabotnic(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavki(
    id integer primary key autoincrement,
    datetime text,
    idPostavshik integer references Postavshik(id),
    idTovar integer references Tovar(id),
    count integer,
    idRabotnik integer references Rabotnik(id)
    )
    ''')

# with open('client.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Client(f, i, o) VALUES (?, ?, ?)", (row['f'], row['i'], row['o']))
#
# with open('Postavshik.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['Number'] and row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Postavshik(Number, f, i, o) VALUES (?, ?, ?, ?)", (row['Number'], row['f'], row['i'], row['o']))
#
# with open('Tovar.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['Name'] and row['count'] and row['Postavshikid'] and row['idClient']:
#             cur.execute("INSERT INTO Tovar(Name, count, Postavshikid, idClient) VALUES (?, ?, ?, ?)", (row['Name'], row['count'], row['Postavshikid'], row['idClient']))
#
# with open('Rabotnic.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Rabotnic(f, i, o) VALUES (?, ?, ?)", (row['f'], row['i'], row['o']))
# with open('Postavki.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['datetime'] and row['idPostavshik'] and row['idTovar'] and row['count'] and row['idRabotnik']:
#             cur.execute("INSERT INTO Postavki(datetime, idPostavshik, idTovar, count, idRabotnik) VALUES (?, ?, ?, ?, ?)", (row['datetime'], row['idPostavshik'], row['idTovar'], row['count'], row['idRabotnik']))
# con.commit()

cur.execute('''select * from Client''')
records = cur.fetchall()
print(records)
cur.execute('''select * from Postavshik''')
records = cur.fetchall()
print(records)
cur.execute('''select * from Tovar''')
records = cur.fetchall()
print(records)
cur.execute('''select * from Rabotnik''')
records = cur.fetchall()
print(records)
cur.execute('''select * from Postavki''')
records = cur.fetchall()
print(records)

cur.execute('''select * from Client''')
with open ("out/outClient.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)

cur.execute('''select * from Postavshik''')
with open ("out/outPostavshik.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)
cur.execute('''select * from Tovar''')
with open("out/Tovar.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)
cur.execute('''select * from Rabotnic''')
with open ("out/outRabotnic.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)
cur.execute('''select * from Postavki''')
with open ("out/outPostavki.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)
con.close()

import random

# Zad 1.1
wektor = [];
for i in range(0, 7):
    wektor.append(random.random())
    
print(wektor)

# Zad 1.2
def losowy_wektor(n):
    wektor = []
    for i in range(0, n):
        wektor.append(random.random())
    return wektor

print(losowy_wektor(3))

# Zad 1.3
import sqlite3

polaczenie = sqlite3.connect('baza.db')
kursor = polaczenie.cursor()
kursor.execute("CREATE TABLE studenci (nr_indeksu int primary key, imie varchar, nazwisko varchar);")
kursor.execute("INSERT INTO studenci VALUES (95252, 'Bartłomiej', 'Stachowski'), (99059, 'Aleksandra', 'Stachowska');")

for rekord in kursor.execute("SELECT nr_indeksu FROM studenci;"):
    print(rekord)

kursor.execute("DROP TABLE studenci;")
polaczenie.commit()
polaczenie.close()
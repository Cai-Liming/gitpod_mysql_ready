import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE TABLE Mammiferi (id CHAR(3), nome VARCHAR(255), razza VARCHAR(255), peso INTEGER, eta INTEGER")
sql = "INSERT INTO Mammiferi (id, nome,razza, peso, eta) VALUES (%s, %s, %s,%d,%d)"
val = [
    ('001', 'Peter', 'Zebra', '40', '3'),
    ('002', 'Amy', 'Gatto', '4', '5'),
    ('003', 'Hannah', 'Cane', '7', '3'),
    ('004', 'Michael', 'Elefante', '400', '7'),
    ('005', 'Sandy', 'Lupo', '50', '6'),
    ('006', 'Betty', 'Cervo', '70', '5'),
    ('007', 'Richard', 'Lince', '30', '4'),
    ('008', 'Susan', 'Coniglio', '4', '3'),
    ('009', 'Vicky', 'Cavallo', '90', '4'),
    ('010', 'Ben', 'orso', '200', '5'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="Animali"
)
richiesta = input("vuoi inserire altri 5 nuovi animali?\n 1=si-0=no")
if richiesta == 1:
    for i in rang(5):
        Id = int(input("inserisci l'id 3 valori numerici"))
        nome = input("inserisci il nome dell'animali")
        razza = input("inserisci la razza dell'animale")
        peso = int(input("inserisci il peso dell'animale"))
        eta = int(input("inserisci l'età dell'animale"))

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

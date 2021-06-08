# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Print
print("Ciao Mondo!")

#Ritornare il tipo di un certo valore
print(type("Ciao"))

#Assegnare valori a variabile
saluto: str = "Ciao Mondo!"
saluto2 = "sono Simone"
print(saluto + saluto2)

#Funzioni che convertono valori
stringa = "4"
print("Da stringa a intero: "  , type(int(stringa)))
intero = 4
print("Da intero a float: " , type(float(intero)))
numero = 4
print("Da intero a stringa: " , type(int(numero)))

#Separare più output in un unico print
print("Primo valore" , "Secondo valore")


#Aggiungere funzioni
def stampa_nome():
    print("Il mio nome è Simone")
stampa_nome()

#Stringhe
frutto = 'cocco'
print(frutto[0])
print(len(frutto))
print(frutto[len(frutto) -1])
print(frutto[-1])
print(frutto[-2] , "\n")

#ciclo for
for lettera in frutto:
    print(lettera)

#Slicing
frase = "Ciao sono Monty!"
print("\n")
print(frase[5:9])







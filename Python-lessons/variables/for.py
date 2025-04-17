message = "for loop"
for element in message: # prende un elemento alla volta della stringa e lo stampa
    print(element)
fruits = ["apple", "banana", "cherry", "pear", "lemon"]
for fruit in fruits:
    print(fruit) # stampa ogni elemento della lista

dictionary = {"name": "Alice", "age": 25}

for key in dictionary:
    print(f"{key}: {dictionary[key]}") # stampa ogni chiave e valore del dizionario

numbers = range(0,20,2)
for k in numbers:
    print(f"{k}") # stampa i numeri da 0 a 20 ogni 2 valori

for k in range(0, 20, 2): # possiamo passare il range senza variabile 
    print(f"{k}") 

for k in range(1,21):
    if k % 2 != 0: # la percentuale è il modulo, che restituisce il resto della divisione
        print(f"{k} è dispari") # stampa il numero dispari

for k in range(1,21):
    if k % 2: # e' come se dicessimo se dopo aver diviso per 2 rimane un resto allora è dispari (è un modo alternativo)
        print(f"{k} è dispari") 

print("inserisci un numero")
number = int(input())
for k in range(1,100):
    if k == number:
        print(f"{k} trovato") # se il numero è uguale a quello che abbiamo inserito allora lo troviamo e stampiamo il messaggio
        break # break esce dal ciclo

for k in range(1,100):
    if k % 2 != 0:
        continue # se il numero è dispari lo saltiamo e continuiamo con il ciclo
    print(k) # stampa i numeri pari
  

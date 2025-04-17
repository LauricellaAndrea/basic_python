x = 10 ; y = 20 # ; è un separatore di istruzioni, non è necessario in python, ma utile se vuoi fare piu dichiarazioni in una riga
if y > x:
    print(f" {y} è maggiore di {x}") # usiamo f per interpolare le variabili dentro le stringhe

    if x == 10:
        print(f" {x} è uguale a 10")
    elif x > 10:
        print(f" {x} è maggiore di 10") # elif è un modo per fare un if dentro un if, ma non è necessario, possiamo anche usare solo if e else
    else:
        print(f" {x} non è uguale a 10")

        
    name = "Mario"
    if name == "Mario":
        print(f" hello {name}")

    values = [1, 2, 3, 4, 5]
    if 5 in values:
        print("5 è presente nella lista") # qualsiasi ritorni un valore booleano possiamo fare una verifica

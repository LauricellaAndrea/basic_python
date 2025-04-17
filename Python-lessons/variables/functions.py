def my_function(params):
    return None

def hello():
    print("Hello")
    
hello() # chiama la funzione hello

def hello_name(name): # definisce la funzione hello con un parametro name
    local_name = str(name).strip() # converte il nome in stringa e lo pulisce da spazi
    len(local_name) # calcola la lunghezza del nome
    if  local_name == 0:
        print("Non hai inserito un nome")
    else:
        print(f"Hello {local_name}") # stampa hello con il nome passato come parametro
hello_name("   Marco     ") # chiama la funzione hello con il nome Marco


def sum_numbers(n1, n2):
    return n1 + n2 # somma i due numeri e restituisce il risultato
    return int(n1) + int(n2) # somma i due numeri e restituisce il risultato convertito in intero
    return float(n1) + float(n2) # somma i due numeri e restituisce il risultato convertito in float=numeri decimali

result = sum_numbers(10,20)
print(result) # stampa il risultato della somma

c= 10 # variabile globale essendo fuori dalla funzione
def multiply(a,b):
    return a*c*b # moltiplica i due numeri e restituisce il risultato
print
print(multiply(2,2)) # stampa il risultato della moltiplicazione


# --- funzioni lambda --- #


# sono funzioni anonime, senza nome, che possono essere eseguite in una sola riga

cube = lambda x: x**3 # funzione che calcola il cubo di un numero
print(cube(3)) # stampa il cubo di 3

dispari = lambda x:False if x%2==0 else True # funzione che verifica se un numero è dispari
print(dispari(3)) # stampa True se il numero è dispari, False altrimenti
numbers = [1,2,3,4,5,6,7,8,9,10] # lista di numeri
even_numbers = list(filter(dispari, numbers)) #list è una funzione che converte in lista, filter filtra i numeri in base a una condizione
print(even_numbers) # stampa i numeri dispari

numeri = [1,2,3,4,5,6,7,8,9,10] 
quadrati = list(map(lambda x: x**2, numeri)) # map applica la funzione lambda a ogni elemento della lista
print


parole = "ciao, buongiorno, hi, salve"
ordinate = sorted(parole, key=lambda x: len(x)) # sorted ordina gli elementi in base alla lunghezza della parola
print(ordinate) 

# Variable params
def sum_numbers(*params, **args): # *params catturia i parametri posizionali, **args è un dizionario di parametri keyword
   
    total = sum(params)
    for k, v in args.items():
        total = total + v
    return total
print(sum_numbers( 1,2,4,4, a=2, b=3)) # stampa il risultato della somma dei numeri passati come parametro

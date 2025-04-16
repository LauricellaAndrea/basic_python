#Numbers
my_age = 18
print(my_age + 2)
product_price = 30.20
product_quantity = 3
total = product_price * product_quantity
print(total)

#String
print("il totale è"+str(total)) 
name = "Mario"
lastrname = "Rossi"
print("full name" + name + " " + lastrname)

#Boolean
is_active = True
can_enter = False
print(is_active)

#List
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list.pop())
print(my_list)

#tuple
my_days = ("Monday", "Tuesday", "Wednesday", is_active)

print("tuple =" + my_days[0])

#Dictionary
my_dict = {
    "name": "Mario",
    "age": 18,
    "is_active": True,
    "hobbies": ["reading", "gaming"]
}

print(my_dict["name"])
print(my_dict["age"])   

#Set  = collezione non ordinata di elementi unici (niente duplicati, no indice)
# utile per rimuovere duplicati o fare ricerche rapide (O(1) in media)
my_set = set([1, 2, 3, 4, 5,5,5,8])
months = set(my_set) # posso racchiudere i valori in una variabile, possiamo dire una copia con i valori unici
print(months)
months_init = {1, 2, 3, 4, 5, 5,5,77,8}
print(months_init)


print(type(months_init)) # mostra il tipo di dato





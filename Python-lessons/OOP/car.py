#programmazione orientatata agli oggetti
class car :
    number_of_wheels = 4  # attributo di classe 

    def __init__(self, color, model, year): #Self è il riferimento all'oggetto stesso, è un parametro obbligatorio convenzionale
        self.color = color
        self.model = model
        self.year = year
        self.speed = 0
        self.started = False
        
    def get_speed(self): #Metodi di istanza, sono funzioni che appartengono alla classe
        return self.speed

    def set_speed(self, value):
         self.speed = value


my_panda = car("red", "Panda"  , 2020) #Variabile che riceve l'oggetto della classe
print(my_panda.color) #Accediamo alla proprietà con il punto
my_punto = car("blue", "Punto", 2021) #Creiamo un altro oggetto della classe
my_punto.set_speed(100) #Modifichiamo la velocità dell'oggetto
print(my_punto.get_speed()) #Mostriamo la velocità dell'oggetto
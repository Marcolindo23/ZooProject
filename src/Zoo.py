class Zoo:
    def __init__(self):
        # Inizializza una lista per i recinti e una lista per i guardiani dello zoo
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        # Aggiunge un recinto alla lista dei recinti dello zoo
        self.fences.append(fence)

    def add_zoo_keeper(self, zoo_keeper):
        # Aggiunge un guardiano alla lista dei guardiani dello zoo
        self.zoo_keepers.append(zoo_keeper)

    def add_animal(self, animal, fence):
        # Aggiunge un animale al recinto specificato se c'è spazio sufficiente
        if fence in self.fences and fence.area >= animal.height * animal.width:
            fence.add_animal(animal)
            return True
        else:
            return False

    def remove_animal(self, animal, fence):
        # Rimuove un animale dal recinto specificato
        if fence in self.fences and animal in fence.animals:
            fence.remove_animal(animal)
            return True
        else:
            return False

    def feed(self, animal):
        # Nutre un animale, aumentando la sua salute e le sue dimensioni
        animal.health += 1
        animal.height *= 1.02
        animal.width *= 1.02

    def clean(self, fence):
        # Calcola il tempo necessario per pulire un recinto in base all'area occupata dagli animali
        occupied_area = sum(animal.height * animal.width for animal in fence.animals)
        if fence.area - occupied_area > 0:
            return occupied_area / (fence.area - occupied_area)
        else:
            return occupied_area

    def describe_zoo(self):
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(f"ZooKeeper(name={zoo_keeper.name}, surname={zoo_keeper.surname}, id={zoo_keeper.id})")

        print("\nFences:")
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            if fence.animals:  # Verifica se ci sono animali nel recinto
                print("\nwith animals:")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            else:
                print("No animals")
            print("#" * 30)  # Separatore tra recinti
class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        # Inizializza un animale con i relativi attributi
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        # Calcola la salute dell'animale in base all'età
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, area, temperature, habitat):
        # Inizializza un recinto con i relativi attributi e una lista vuota di animali
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def add_animal(self, animal):
        # Aggiunge un animale al recinto
        self.animals.append(animal)

    def remove_animal(self, animal):
        # Rimuove un animale dal recinto
        self.animals.remove(animal)

class ZooKeeper:
    def __init__(self, name, surname, id):
        # Inizializza un guardiano dello zoo con i relativi attributi
        self.name = name
        self.surname = surname
        self.id = id
lorenzo_maggi = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
fence = Fence(area=100, temperature=25, habitat="Continentale")
scoiattolo = Animal(name="Scoiattolo", species="Blabla", age=25, height=10, width=5, preferred_habitat="Alberi")
lupo = Animal(name="Lupo", species="Lupus", age=14, height=20, width=15, preferred_habitat="Foresta")
# Aggiunta degli animali al recinto
fence.add_animal(scoiattolo)
fence.add_animal(lupo)

# Creazione dello zoo e aggiunta dei recinti e dei guardiani
zoo = Zoo()
zoo.add_fence(fence)
zoo.add_zoo_keeper(lorenzo_maggi)

# Descrizione dello zoo
zoo.describe_zoo()
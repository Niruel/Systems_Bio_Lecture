class Bee:
    def __init__(self, species, colony):
        self.species = species
        self.colony = colony


class Worker(Bee):
    def worker(self, species, colony):
        species = Bee.species
        colony = Bee.colony


d = Worker("Bee", 1)

print(d)
print(d.colony, " ", d.species)

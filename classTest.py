class Persona:
    specie = "Homo sapiens"
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def saluto(self):
        print("faccetta nera")

class Donna(Persona):
    specie = "Troia"
    def __init__(self, nome, eta, genere):
        super().__init__(nome, eta)
        self.genere = genere
    def saluto(self):
        print("Non ho diritti")
        

persona1 = Persona("Mario",30)
donna1 = Donna("Lucia",12,"Binary")
print(persona1.specie)
print(persona1.nome)
print(persona1.eta)

print(donna1.specie)
print(donna1.genere)
donna1.saluto()
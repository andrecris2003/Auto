class Auto:
    def __init__(self,marca,modello,immatricolazione,velocita):
        self.marca=marca
        self.modello=modello
        self.immatricolazione=immatricolazione
        self.velocita=velocita
    
    def StampaCaratteristiche(self):
        print("--------------------------------------------------------------")
        print("Le caratteristiche dell'Auto sono:")
        print(f"La marca dell'auto è {self.marca}")
        print(f"Il modello dell'auto è {self.modello}")
        print(f"L'anno di immatricolazione dell'auto è {self.immatricolazione}")
        print(f"La velocita attuale dell'auto è {self.velocita} Km/h")
        print("--------------------------------------------------------------")
    
    def AumentoVelocita(self,aumento):
        self.velocita+=aumento
        
    def DecrementoVelocita(self,decremento):
        self.velocita-=decremento
        
        
from ClasseAuto import *

def Main():
    auto1=Auto("Fiat","Pandino",2024,50)
    auto1.StampaCaratteristiche()
    try:
        vel=int(input("Di quanto vuoi aumentare la velocità dell'auto?\n"))
    except ValueError:
        vel=0
    auto1.AumentoVelocita(vel)
    print("Hai aumentato la velocità")
    print(f"La velocita attuale dell'auto è {auto1.velocita} Km/h")
    try:
        vel=int(input("Di quanto vuoi decrementare la velocità dell'auto?\n"))
    except ValueError:
        vel=0
    auto1.DecrementoVelocita(vel)
    print("Hai decrementato la velocità")
    print(f"La velocita attuale dell'auto è {auto1.velocita} Km/h")

if __name__ == "__main__":
    Main()
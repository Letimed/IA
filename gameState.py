class Personnage:
    def __init__(self, color):
        self.color = color

class Salle:
    def __init__(self, id):
        self.id = id
        self.ombre = False
        self.listcharacter = []

    def addCharacterToSalle(self, character):
        self.listcharacter.append(character)

    def printList(self):
        print(self.listcharacter)

    def removeCharacterFromSalle(self, character):
        self.listcharacter.remove(character);

class GameState:
    def __init__(self, salle1, salle2, salle3, salle4, salle5, salle6, salle7, salle8,salle9,salle10):
        self.Game = []
        self.Game.append(salle1)
        self.Game.append(salle2)
        self.Game.append(salle3)
        self.Game.append(salle4)
        self.Game.append(salle5)
        self.Game.append(salle6)
        self.Game.append(salle7)
        self.Game.append(salle8)
        self.Game.append(salle9)
        self.Game.append(salle10)

    def getSalleFromId(self, id):
        for salle in self.Game:
            if salle.id == id:
                return salle


Personnage1 = Personnage("rose")
Personnage2 = Personnage("rouge")
Personnage3 = Personnage("bleu")
Personnage4 = Personnage("blanc")
Personnage5 = Personnage("violet")
Personnage6 = Personnage("noir")
Personnage7 = Personnage("marron")
Personnage8 = Personnage("gris")

salle1 = Salle(1)
salle2 = Salle(2)
salle3 = Salle(3)
salle4 = Salle(4)
salle5 = Salle(5)
salle6 = Salle(6)
salle7 = Salle(7)
salle8 = Salle(8)
salle9 = Salle(9)
salle10 = Salle(10)

gameState = GameState(salle1, salle2, salle3, salle4, salle5, salle6, salle7, salle8, salle9, salle10)
salle1.addPersonnageToSalle(Personnage1);
print(gameState.Game[0].listpersonnage[0].color)
salle1.removePersonnageFromSalle(Personnage1);
print(gameState.Game[0].printlist())

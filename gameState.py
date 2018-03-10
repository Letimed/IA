

class Personnage:
    def __init__(self, color):
        self.color = color
        self.suspect = False

    def suspectTrue(self):
        self.suspect = True

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

#QUESTION : Tuiles disponibles : [blanc-1-suspect, rose-5-suspect, bleu-6-suspect, rouge-4-suspect] choisir entre 0 et 3
#QUESTION : positions disponibles : {2}, choisir la valeur
#QUESTION : Voulez-vous activer le pouvoir (0/1) ?
class Parsing:
    def __init__(self):
        self.name = ""
        self.reply = []

    def parseQuestion(self, string):
        if string == None:
            return
        else:
            tab = string.split(":")
            if tab[0] == "positions disponibles ":
                self.name = "position"
                tab1 = tab[1].split("}")
                tab2 = tab1[0].split(",")
                first = tab2[0].split("{")
                self.reply.append(first[1])
                i = 1
                while i < len(tab2):
                    self.reply.append(tab2[i])
                    i = i + 1
            elif tab[0] == "Tuiles disponibles ": #RETOURNER L'INDEX DE LA LISTE
                tab1 = tab[1].split("]")
                tab2 = tab1[0].split(",")
                first = tab2[0].split("[")
                self.reply.append(first[1])
                i = 1
                while i < len(tab2):
                    self.reply.append(tab2[i])
                    i = i + 1
                print(self.reply)
            else:
                self.name = "power"
                self.reply.append(0)
                self.reply.append(1)


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

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

#gameState = GameState(salle1, salle2, salle3, salle4, salle5, salle6, salle7, salle8, salle9, salle10)
#salle1.addCharacterToSalle(Personnage1);
#print(gameState.Game[0].listcharacter[0].color)
#salle1.removeCharacterFromSalle(Personnage1);
#print(gameState.Game[0].printList())
parser = Parsing()
parser.parseQuestion("Tuiles disponibles : [blanc-1-suspect, rose-5-suspect, bleu-6-suspect, rouge-4-suspect] choisir entre 0 et 3")
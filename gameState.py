import readline

class Character:
    def __init__(self, color):
        self.color = color
        self.suspect = False


class Room:
    def __init__(self, id):
        self.id = id
        self.ombre = False
        self.listcharacter = []

    def addCharacterToRoom(self, character):
        self.listcharacter.append(character)

    def printList(self):
        print(self.listcharacter)

    def removeCharacterFromRoom(self, character):
        self.listcharacter.remove(character);

    def cleanRoom(self):
        self.listcharacter = []

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

Character1 = Character("rose")
Character2 = Character("rouge")
Character3 = Character("bleu")
Character4 = Character("blanc")
Character5 = Character("violet")
Character6 = Character("noir")
Character7 = Character("marron")
Character8 = Character("gris")
ListChar = [];
ListChar.append(Character1)
ListChar.append(Character2)
ListChar.append(Character3)
ListChar.append(Character4)
ListChar.append(Character5)
ListChar.append(Character6)
ListChar.append(Character7)
ListChar.append(Character8)

class GameState:
    def __init__(self, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10):
        self.Game = []
        self.Game.append(room1)
        self.Game.append(room2)
        self.Game.append(room3)
        self.Game.append(room4)
        self.Game.append(room5)
        self.Game.append(room6)
        self.Game.append(room7)
        self.Game.append(room8)
        self.Game.append(room9)
        self.Game.append(room10)

    def moveCharacter(self, character, currentRoomId, newRoomId):
        if currentRoomId != -1:
            self.Game[currentRoomId].removeCharacterFromRoom(character);
        self.Game[int(newRoomId)].addCharacterToRoom(character);
        return

    def getRoomFromId(self, id):
        for room in self.Game:
            if room.id == id:
                return room

    def getSalleFromId(self, id):
        for salle in self.Game:
            if salle.id == id:
                return salle

    def cleanBoard(self):
        for i in self.Game:
            i.cleanRoom()

    def UpdateCharacterState(self, color, state):
        for i in ListChar:
            if i.color == color:
                if state == "suspect":
                    i.suspect = True;
                else:
                    i.suspect = False;

    def UpdateCharacterPos(self, color, pos):
        for i in ListChar:
            if i.color == color:
                self.moveCharacter(i, -1, pos);

    def updateBoard(self, newBoard):
        self.cleanBoard()
        pl1 = newBoard.split("  ")
        for i in pl1:
            a, b, c = i.split("-")
            self.UpdateCharacterState(a, c)
            self.UpdateCharacterPos(a, b)
        return



room1 = Room(1)
room2 = Room(2)
room3 = Room(3)
room4 = Room(4)
room5 = Room(5)
room6 = Room(6)
room7 = Room(7)
room8 = Room(8)
room9 = Room(9)
room10 = Room(10)

passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

#gameState = GameState(salle1, salle2, salle3, salle4, salle5, salle6, salle7, salle8, salle9, salle10)
#salle1.addCharacterToSalle(Personnage1);
#print(gameState.Game[0].listcharacter[0].color)
#salle1.removeCharacterFromSalle(Personnage1);
#print(gameState.Game[0].printList())

############################################################ Parsing test Question ###########################################################
#QUESTION : Tuiles disponibles : [blanc-1-suspect, rose-5-suspect, bleu-6-suspect, rouge-4-suspect] choisir entre 0 et 3
#QUESTION : positions disponibles : {2}, choisir la valeur
#QUESTION : Voulez-vous activer le pouvoir (0/1) ?

################################################################################################################################"

game = GameState(room1, room2, room3, room4, room5, room6, room7, room8, room9, room10)
game.updateBoard("bleu-6-suspect  gris-7-suspect  marron-3-suspect  violet-2-suspect  rose-5-suspect  rouge-4-suspect  blanc-1-suspect  noir-0-suspect")

"""room1.addCharacterToroom(Character1);
print(gameState.Game[0].listcharacter[0].color)
room1.removeCharacterFromroom(Character1);
print(gameState.Game[0].printList())"""

def playTurn():
    print("play your turn")
    return

def parseInfoLines():
    print("parseInfoLines")
    return


parser = Parsing()
path_to_question = "./1/questions.txt"
path_to_reponse = "./1/reponses.txt"
path_to_info = "./1/infos.txt"
done = False
old_question = ""
while not done:
    questionFile = open(path_to_question,'r')
    question = questionFile.read()

    parser.parseQuestion(question)
    questionFile.close();

    if question != old_question:
        reponseFile = open(path_to_reponse,'w')
        #playTurn()
        reponseFile.close()
        old_question = question
    infoFile = open(path_to_info,'r')
    lines = infoFile.readlines()
    #print(lines);
    #parseInfoLines()
    infoFile.close()
    if len(lines) > 0:
        done = "Score final" in lines[-1]

class Character:
    def __init__(self, color):
        self.color = color

class Room:
    def __init__(self, id):
        self.id = id
        self.ombre = False
        self.listcharacter = []

    def addCharacterToroom(self, character):
        self.listcharacter.append(character)

    def printList(self):
        print(self.listcharacter)

    def removeCharacterFromroom(self, character):
        self.listcharacter.remove(character);

class GameState:
    def __init__(self, room1, room2, room3, room4, room5, room6, room7, room8,room9,room10):
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
        self.Game[currentRoomId].removeCharacterFromroom(character);
        self.Game[newRoomId].addCharacterToroom(character);
        return 


    def getroomFromId(self, id):
        for room in self.Game:
            if room.id == id:
                return room

Character1 = Character("rose")
Character2 = Character("rouge")
Character3 = Character("bleu")
Character4 = Character("blanc")
Character5 = Character("violet")
Character6 = Character("noir")
Character7 = Character("marron")
Character8 = Character("gris")

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

game = GameState(room1, room2, room3, room4, room5, room6, room7, room8, room9, room10)


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

path_to_question = "./1/questions.txt"
path_to_reponse = "./1/reponses.txt"
path_to_info = "./1/infos.txt"
done = False
old_question = ""
while not done:
    questionFile = open(path_to_question,'r')
    question = questionFile.read()
    #parseQuestion()
    questionFile.close();
    if question != old_question:
        reponseFile = open(path_to_reponse,'w')
        #playTurn()
        reponseFile.close()
        old_question = question
    infoFile = open(path_to_info,'r');
    lines = infoFile.readlines()
    print(lines);
    #parseInfoLines()
    infoFile.close()
    if len(lines) > 0:
        done = "Score final" in lines[-1]




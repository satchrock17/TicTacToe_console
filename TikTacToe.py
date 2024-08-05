import sys
import random

def Start():
    global Feld1
    global Feld2
    global Feld3
    global Feld4
    global Feld5
    global Feld6
    global Feld7
    global Feld8
    global Feld9
    Feld1 = "1"
    Feld2 = "2"
    Feld3 = "3"
    Feld4 = "4"
    Feld5 = "5"
    Feld6 = "6"
    Feld7 = "7"
    Feld8 = "8"
    Feld9 = "9"
    global choose 
    choose = input("Singleplayer or Multiplayer?\n").lower()
    if choose != "singleplayer" and choose != "multiplayer":
        print("Wenn du mit einer anderen Person spielen möchtest gib Multiplayer ein\n Wenn du alleine mit einem Bot spielen willst gib Singleplayer ein")
        Start()
    Gameloop() 

def Spielfeld():
    print(Feld1 + "|" + Feld2 + "|" + Feld3 + "\n" + Feld4 + "|" + Feld5 + "|" + Feld6 + "\n" + Feld7 + "|" + Feld8 + "|" + Feld9 + "\n")
        
def Winning():
    if (Feld1 == "X" and Feld2 == "X" and Feld3 == "X" or Feld4 =="X" and Feld5 == "X" and Feld6 == "X" or Feld7 == "X" and Feld8 == "X" and Feld9 == "X" or Feld1 == "X" and Feld4 == "X" and Feld7 == "X" or Feld2 == "X" and Feld5 == "X" and Feld8 == "X" or Feld3 == "X" and Feld6 == "X" and Feld9 == "X" or Feld1 == "X" and Feld5 == "X" and Feld9 == "X" or Feld3 == "X" and Feld5 == "X" and Feld7 == "X"):
        print("PlayerOne wins")
        pa = input("Nochmal?\n").lower()
        if pa == "ja" or pa == "j":
            Start()
        elif pa == "nein" or pa == "n":
            print("Danke fürs Spielen ;^D")
            sys.exit()
        else:
            print("Ja oder Nein?")
    elif (Feld1 == "O" and Feld2 == "O" and Feld3 == "O" or Feld4 =="O" and Feld5 == "O" and Feld6 == "O" or Feld7 == "O" and Feld8 == "O" and Feld9 == "O" or Feld1 == "O" and Feld4 == "O" and Feld7 == "O" or Feld2 == "O" and Feld5 == "O" and Feld8 == "O" or Feld3 == "O" and Feld6 == "O" and Feld9 == "O" or Feld1 == "O" and Feld5 == "O" and Feld9 == "O" or Feld3 == "O" and Feld5 == "O" and Feld7 == "O"):
        print("PlayerTwo wins")
        pa2 = input("Nochmal?\n").lower()
        if pa2== "ja" or pa2 == "j":
            Start()
        elif pa2 == "nein" or pa2 == "n":
            print("Danke fürs Spielen ;^D")
            sys.exit()
        else:
            print("Ja oder Nein?\n")
        
def Gameloop():
    Spielfeld()
    Winning()
    Playerone()
        
def Playerone():
    if choose == "multiplayer":
        p1 = str(input("Spieler 1: "))
    elif choose == "singleplayer":
        p1 = str(random.randint(1,9))
    global Feld1, Feld2, Feld3, Feld4, Feld5, Feld6, Feld7, Feld8, Feld9
    match p1:
        case "1":
            if Feld1 != "O" and Feld1 != "X":
                Feld1 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "2":
            if Feld2 != "O"  and Feld2 != "X":
                Feld2 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "3":
            if Feld3 != "O"  and Feld3 != "X":
                Feld3 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "4":
            if Feld4 != "O"  and Feld4 != "X":
                Feld4 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "5":
            if Feld5 != "O"  and Feld5 != "X":
                Feld5 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "6":
            if Feld6 != "O"  and Feld6 != "X":
                Feld6 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "7":
            if Feld7 != "O"  and Feld7 != "X":
                Feld7 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "8":
            if Feld8 != "O"  and Feld8 != "X":
                Feld8 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case "9":
            if Feld9 != "O"  and Feld9 != "X":
                Feld9 = "X"
                Spielfeld()
                Winning()
                Playertwo()
            else:
                if choose == "multiplayer":
                    print("Feld ist bereits belegt")
                Playerone()
        case _:
            print("gib eine Zahl zwischen 1-9 ein")
            Spielfeld()
            Playerone()
            return
            
def Playertwo():
    global Feld1, Feld2, Feld3, Feld4, Feld5, Feld6, Feld7, Feld8, Feld9
    
    p2 = str(input("Spieler 2: "))
    
    match p2:
        case "1":
            if Feld1 != "X" and Feld1 != "O":
                Feld1 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "2":
            if Feld2 != "X" and Feld2 != "O":
                Feld2 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "3":
            if Feld3 != "X" and Feld3 != "O":
                Feld3 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "4":
            if Feld4 != "X" and Feld4 != "O":
                Feld4 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "5":
            if Feld5 != "X" and Feld5 != "O":
                Feld5 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "6":
            if Feld6 != "X" and Feld6 != "O":
                Feld6 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "7":
            if Feld7 != "X" and Feld7 != "O":
                Feld7 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case "8":
            if Feld8 != "X" and Feld8 != "O":
                Feld8 = "O"
                Gameloop()
            else: 
                print("Feld ist bereits belegt")
                Playertwo()
        case "9":
            if Feld9 != "X" and Feld9 != "O":
                Feld9 = "O"
                Gameloop()
            else:
                print("Feld ist bereits belegt")
                Playertwo()
        case _:
            print("gib eine Zahl zwischen 1-9 ein")
            Spielfeld()
            Playertwo()
            return

Start()

# Libraries
import random
import os

#def
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

# Code
clear()

print('''
HANGMAN GAME (By Harsh Khandal)  
    
Rules:
    1. The objective of hangman is to guess the secret word before the stick figure is hung.
    2. The guessing player suggest letters one at a time.
    3. If the guessed letter is in the word, the program writes the letter in all its correct positions.
    4. If the guessed letter is not in the word, the program draws one part of the hangman figure.
    5. The hangman figure consists of 10 parts (Means 10 tries).     
    ''')

#Here we have some basic rules

input("Press Enter To Continue... ")

#This Game() is the main part.

def Game():
    global tries

    #We are using pre defined list of objects
    lst = [
        "apple",
        "banana",
        "grape",
        "orange",
        "mango",
        "strawberry",
        "peach",
        "watermelon",
        "cherry",
        "pineapple",
        "carrot",
        "cucumber",
        "potato",
        "tomato",
        "broccoli",
        "spinach",
        "lettuce",
        "onion",
        "garlic",
        "pepper",
        "book",
        "table",
        "chair",
        "pencil",
        "window",
        "bottle",
        "camera",
        "phone",
        "computer",
        "mouse",
        "keyboard",
        "lamp",
        "clock",
        "guitar",
        "piano",
        "violin",
        "drums",
        "bicycle",
        "car",
        "train",
        "airplane",
        "boat",
        "bus",
        "rocket",
        "forest",
        "mountain",
        "river",
        "desert",
        "ocean",
        "island",
        "python",
        "hangman",
        "cybersecurity",
        "hacker",
        "commerce",
        "electronics",
        "arduino",
        "tech",
        "computer",
        "algorithm",
        "network",
        "firewall",
        "malware",
        "encryption",
        "programming",
        "internet",
        "database",
        "software",
        "hardware",
        "virtual",
        "cloud",
        "security",
        "system",
        "coding",
        "debugging",
        "binary",
        "bytecode",
        "compiler",
        "terminal",
        "protocol"
        ]

    word = random.choice(lst)

    clear()

    print("HANGMAN GAME (By Harsh Khandal)")
    print('''
                  ______
                 |      
                 |       
                 |
                 |
                 |
                ---
    ''')

    tries=10
    dash=(list(len(word)*"_"))

    def base():
        global tries
        print("        ",' '.join(dash))
        print()
        print("Tries Left: ",tries)

        ch=input("Enter Character : ")
        if len(ch)>1:
            print('Invalid Character!!')
            base()

        if ch in word:
            for i in range(len(word)):
                if word[i]==ch:
                    #clear()
                    dash[i]=ch
            print("        ",' '.join(dash))

            if "_" not in ' '.join(dash):
                print("Hurry! You won the Game.")
                choice=input("Play again or Exit !! (A/X)")
                if choice.lower() == "a":
                    Game()
                elif choice.lower() == "x":
                    exit()
            fig()
            base()

        elif ch not in word:
            tries=tries-1
            fig()

        else:
            pass

    def fig():              
        if tries == 10:
            clear()
            print('''
                      ______
                     |      
                     |      
                     |
                     |
                     |
                    ---
            ''')
            base()
        
        elif tries == 9:
            clear()
            print('''
                      ______
                     |      |
                     |      
                     |
                     |
                     |
                    ---
            ''')
            base()
        
        elif tries == 8:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |      
                     |
                     |
                    ---
            ''')
            base()
        
        elif tries == 7:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |      |
                     |
                     |
                    ---
            ''')
            base()
        
        elif tries == 6:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |      |
                     |      |
                     |
                    ---
            ''')
            base()

        elif tries == 5:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |      |\\
                     |      |
                     |
                    ---
            ''')
            base()

        elif tries == 4:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |     /|\\
                     |      |
                     |
                    ---
            ''')
            base()

        elif tries == 3:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |     /|\\
                     |      |
                     |       \\
                    ---
            ''')
            base()

        elif tries == 2:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |     /|\\
                     |      |
                     |     / \\
                    ---
            ''')
            base()

        elif tries == 1:
            clear()
            print('''
                      ______
                     |      |
                     |      O
                     |     /|\\
                     |    / |
                     |     / \\
                    ---
            ''')
            base()

        elif tries == 0:
            clear()
            print('''
                      ______
                     |      |
                     |      O 
                     |     /|\\
                     |    / | \\
                     |     / \\
                    ---
            ''')
            print("GAME OVER !!")
            print("ANSWER IS", word)
            choice=input("Play again or Exit !! (A/X)")
            if choice.lower() == "a":
                Game()
            elif choice.lower() == "x":
                exit()

        
                     

    base()

Game()

# Name : Harsh Khandal
# Email : codingwithme7@gmail.com
# Created on 15 June 2025
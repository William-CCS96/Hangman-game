""" 
¡Adivina la palabra!
_ _ _ _ _

Ingresa una letra: 
"""

"""Reglas"""
# Incorpora comprehensinons, manejo de errores y manejo de archivos
# Utiliza el archivo data.txt y léelo para obtener palabras.

"""Comando recomendados:"""
# Investiga la función enumerate
# El método get de los diccionarios puede servir
# Las sentencias.
    # os.system("cls")-> Windows
    # os.system("clear") -> Unix
    # Sirve para limpiar la pantalla cada vez que ingreso un valor o se genera una acción.

"""Mejorar el juego"""
# Añade un sistema de puntos
# Dibuja el "ahorcado" en cada jugada con código ASCII
# Mejora la intergaz


from random import randrange
import random
import os 



hangman=[(""" 

    o-----------o
    |           |
    |           |
    |           |
    |            
    |       
    |          
    |       
    |           
    |           
    |          
    |         
    |       
    |       
    |       
   / \\      
___███_____________________
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |           
    |       
    |          
    |       
    |           
    |           
    |          
    |         
    |       
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |       
    |           
    |           
    |          
    |         
    |       
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |           ║
    |           ║
    |           ║
    |          
    |         
    |       
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |       <---║
    |           ║
    |           ║
    |          
    |         
    |       
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |       <---║--->
    |           ║
    |           ║
    |          
    |         
    |       
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |       <---║--->
    |           ║
    |           ║
    |          / 
    |         /   
    |       __     
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| O O |~
    |          ===
    |       <---║--->
    |           ║
    |           ║
    |          / \\
    |         /   \\
    |       __     __
    |       _________
    |       ║       ║
   / \\      ║       ║
___███______║_______║______
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """),(""" 

    o-----------o
    |           |
    |           |
    |           |
    |          \ /  
    |       ~| X X |~
    |          ===
    |       <---║--->
    |           ║
    |           ║
    |          / \\
    |         /   \\
    |       __     __
    |       
    |       
   / \\      
___███_____________________
░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """)]
words=[]
count=0

winner="""



            ░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
            ░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
            ░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
            ░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
            ░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
            


                                   \ /  
                                ~| O O |~
                                   *~*
                                =---║---=
                                    ║
                                    ║
                                   ║ ║ 
                                   ║ ║  
                                  __ __
            
            
            """

def read_wors_file():
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)

def normalize(s):
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def secret_word():
    word=words[random.randrange(0,len(words))]
    word=word.upper()
    return normalize(word)

def letter_input():
    letter=input("Enter a letter: ")
    letter=letter.upper()
    alphabet=[chr(i) for i in range(65,91)]
    alphabet.append("Ñ")
    while len(letter)>1 or letter not in alphabet:
        if len(letter)>1:
            print("\nIndicate only one letter")
            letter=input("Enter a letter: ")
            letter=letter.upper()
        if letter not in alphabet:
            print("\nIndicate one letter")
            letter=input("Enter a letter: ")
            letter=letter.upper()
            continue
        break
    return letter

def replace_letter(letter,word,line_word):
    global count
    if letter in word:
        for i in range(len(word)):
            if letter==word[i]: line_word[i]=letter
    else: count+=1

def letter_repeat(letter,line_word,letter_intro):
    while letter in line_word:
        print("the letter is repeated")
        letter=letter_input()
        if letter not in line_word:
            break
    while letter in letter_intro:
        print("you already indicated that letter")
        letter=letter_input()
        if letter not in letter_intro:
            break

def game_again():
    while True:
        response=(input("Do you want to play again?\n1 : Yes\n2 : No"))
        if response=="1" or response=="2": break
    if response=="1":
        global count
        count=0
        run()
    else:
        print("¡Thank you!")
        return None

def run():
    os.system("cls")
    read_wors_file()

    word=secret_word()
    line_word=["-" for i in range(len(word)-1)]
    line_word="".join(line_word)
    # print("_ "*(len(word)-1),"\n")
    
    letter_intro=[]
    while True:
        print(hangman[count])
        print(line_word)
        print("Attempts:",count,"/",8)
        line_word=list(line_word)
        
        letter=letter_input()
        letter_repeat(letter,line_word,letter_intro)
        letter_intro.append(letter) 

        replace_letter(letter,word,line_word)
        
        if "_" not in line_word:
            os.system("cls")
            print("   \n",word)
            print(winner)
            if game_again()==None:
                break
        
        if count==8:
            os.system("cls")
            print("\n\n     ¡GAME OVER! ☠️")
            print(hangman[count])
            print("\n    ",word)
            if game_again()==None:
                break

        line_word="".join(line_word)
        os.system("cls")
        

if __name__=="__main__":
    run()

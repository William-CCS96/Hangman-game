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
# Elmétodo get de los diccionarios puede servir
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


hangman=""" 

        o-----------o
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
        |
       / \\
    ___███_____________________
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """
words=[]
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

def string_secret_word():
    x=secret_word()
    print(x)
    print("_ "*len(x))

def letter_input():
    letter=input("Enter a letter: ")
    letter=letter.upper()
    alphabet=[chr(i) for i in range(65,91)]
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
    if letter in word:
        for i in range(len(word)):
            if letter==word[i]:
                line_word[i]=letter



def run():
    read_wors_file()
    word=secret_word()

    print(word)
    line_word=["_" for i in range(len(word)-1)]
    print(len(line_word))
    
    print("_"*len(word))
    letter=letter_input()
    
    replace_letter(letter,word,line_word)
    
    line_word="".join(line_word)
    print(line_word)


if __name__=="__main__":
    run()
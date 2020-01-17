#Se marca en mayusculas las constantes
import random



IMGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
   ''']

WORDS = ["lavadora",
         "secadora",
         "sofa",
         "govierno",
         "diputado",
         "democracia",
         "computadora",
         "teclado"]

def random_word():
    #funcion que extrae una palabra al azar
    #obtener un indicie con un numero aleatorio
    indice_aleatorio = random.randint(0, len(WORDS)-1)
    return WORDS[indice_aleatorio]

def run():
    word = random_word()
    hidden_word = ["-"] * len(word)
    tries = 0
    
    pass









if __name__ == "__main__":
    print("B I E N V E N I D O  A  A H O R C A D O S ! !")
    run()

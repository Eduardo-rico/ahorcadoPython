#Se marca en mayusculas las constantes
import random



IMAGES = ['''
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
    random_index = random.randint(0, len(WORDS)-1)
    return WORDS[random_index]
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print("--- * --- * --- * --- * --- --- * --- * --- * --- * --- ")

def run():
    word = random_word()
    hidden_word = ["-"] * len(word)
    tries = 0
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input("Escoge una letra: "))
        letter_indexes = [] #aqui se guardan todos los indices
        for letter in range(len(word)):
            if word[letter] == current_letter:
                letter_indexes.append(letter)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print("")
                print("¡Perdiste! La palabra correcta era {}".format(word))
                break
        else:
            for index in letter_indexes:
                hidden_word[index] = current_letter
            letter_indexes = []
        try:
        #si no encuentra el valor .index() arroja un error, si sí lo encuentra no pasa nada, si no lo encuentra regresa un error
            hidden_word.index("-")
        except ValueError:
            #si hay un error, mandamos el mensaje de que has ganado
            print("")
            print("Ganaste! La palabra correcta era {}".format(word))
            break
    










if __name__ == "__main__":
    print("B I E N V E N I D O  A  A H O R C A D O S ! !")
    run()

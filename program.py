import pandas as pd
import time
import os

# Função de limpesa do terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função pra uma animação boba nos prints
def print_animation(words, timer):
    for letter in words:
        print(letter, end='')
        time.sleep(timer)

# Função que mostra como jogar o jogo (perdi)
def how_to_play()-> None:
    clear_terminal()

    print_animation(">>> HOW TO PLAY <<<\n\n"
               "In this game you need to guess the corresponding personal pronoun for the sentence\n"
               "<FOR EXAMPLE: Maria likes video games = she likes video games>\n\n HAVE FUN :D", 0.02)
    print_animation("\n\npress any button to continue...", 0.02)

    input()
# Função da gameplay
def gameplay() -> None:
    random_row: str = list_of_phrases.sample(n=1).reset_index(drop=True) # Escolhendo uma linha aleatória do .txt
    chosen_name: str = random_row['Names'].iloc[0]  # Pegando a frase da primeira coluna
    chosen_pronoun: str = random_row['Pronouns'].iloc[0] # Pegando a frase da segunda coluna
    _try: int = 1 # Variavel de tentativas

    while _try <= 3:
        clear_terminal()
        print_animation(">>> GAMEPLAY <<<\n\n", 0.02)
        print_animation(f"TRY {_try}/3", 0.02)
        print_animation(f"\nPhrase with name: >> {chosen_name} <<\n", 0.02)
        print_animation("WHAT IS MY PRONOUN?\n"
                        "-> ", 0.02)
        user_phrase: str = input().strip().lower() # Frase do Usuário

        if user_phrase == chosen_pronoun.strip().lower():
            print_animation("\n>>> YEAH!!! It's my Pronoun :D\n\n", 0.02)
            print_animation("press any button to continue...", 0.02)
            input()
            break
        else:
            print_animation("\nWRONG", 0.02)
            print_animation("...", 1)
            _try+=1
    else:
        print_animation(f"\nThe currect phrase is: {chosen_pronoun}\n"
                        "press any button to continue...", 0.02)
        input()

# INICIO DO PROGRAMA
if __name__ == "__main__":
    option: str = None
    list_of_phrases = pd.read_csv("names_and_pronouns.txt", sep=",", header=None) # Criando o DataFrame
    list_of_phrases.columns = ['Names', 'Pronouns'] # Renomeando as colunas

    while option != '3':
        clear_terminal()

        print_animation(" >>> What is my pronoun? <<<\n\n", 0.02)
        print_animation("[1]GAMEPLAY\n"
                        "[2]How to Play\n"
                        "[3]Quit Game\n\n-> ", 0.02)
        option = input()

        match option:
            case '1':
                gameplay()
            case '2':
                how_to_play()
            case '3':
                exit()
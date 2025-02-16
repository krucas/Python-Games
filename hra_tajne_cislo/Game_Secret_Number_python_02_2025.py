import random
import os

print('Vítej ve hře "secret number" ')
print('Uhadneš jake číslo vybral PC, od 1 do 100')

secret_number = random.randint(1,100)
#print(f' Tajne cislo je {secret_number}')



def difficulty ():
    difficulty = input('Vyber obtížnost "hard" nebo "easy":  ').strip().lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return  5
    else:
        print("Neznámá obtížnost, nastavím počet pokusů na 0.")

# Uživatel zadá obtížnost


# Počet pokusů
def quessing_game():
    attempts = difficulty ()
    
    # Nastavení pokusů podle obtížnosti

       
    another_game = ''
    
    
    while attempts > 0:
        print(f"Máš {attempts} pokusů.")
        guess = int(input('Jake číslo vybral PC, hádej od 1 do 100: \n'))
        
        
        if guess > secret_number:
            print(f'Číslo {guess} je příliš VYSOKÉ')
            attempts -= 1
        elif guess < secret_number:
            print(f'Číslo {guess} je příliš NÍZKÉ')
            attempts -= 1
        
        else:
            print('Uhádl si číslo, Vyhral si')
            another_game = input('Chceš pokračovat ve hře "ANO" nebo "NE"? ').strip().lower()

        if attempts == 0:
             print(f'Sorry, tva hra končí, počet pokusu jsi vyčerpal. Hledané číslo bylo {secret_number}. ')
             another_game = input('Chceš pokračovat ve hre "ano" nebo "ne"? ').strip().lower()
        if another_game == 'ano':
            quessing_game()
        elif another_game == 'ne':
            break
        
quessing_game() 
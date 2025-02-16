nuzky = """
N
U
Z
K
Y
"""

papir ="""
P
A
P
I
R

"""

kamen = """
K
A
M
E
N
"""






print('Vítejte ve hře   KÁMEN > NŮŽKY > PAPÍR')


import random

 


def games():
   
    while True:
        
        
        choice = int(input('Co si vyberete: napiš 0 pro kámen, 1 papir a 2 nužky \n'))
        if choice == 1:
            print(f'Vybral jsi \n {papir}')
        elif choice == 0:
            print(f'Vybral jsi \n {kamen}')
        else:
           print(f'Vybral jsi \n {nuzky}')
       
        computer = random.randint(0,2)  
       # print(f'co vybral PC \n {computer}')
        if computer == 1:
            print(f'PC vybral \n {papir}')
        elif computer == 0:
            print(f'PC vybral \n {kamen}')
        else:
            print(f'PC vybral \n {nuzky}')
        
        if choice == computer:
            print(f'REMÍZA')
        elif (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
             print(f'Vyhral jsi!!!!')
        else:
            print(f' Prohral jsi, ale nebuď zoufalý, je tu možnost si zahrát znovu, bereš')
    
    # Nabídka opakování hry
        repeat = input('Pokud si chceš zahrat jeste jednou napiš? A nebo N: \n').strip().lower()
        if repeat != 'a':
            print(f' Díky za hru a měj se!')
            break
            
# Spuštění hry.
games()   


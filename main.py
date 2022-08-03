

from random import randint

def print_score(score1,score2):
    print("Ordinateur : {}£ --------  Joueur1 : {}£ ".format(score1,score2))


def update_score(who): # Cette fonction recoit 0 ou 1 selon respectivement qu'il s'agisse de l'ordinateur ou du joueur1 le gagnant
    global computeur_score
    global user_score
    if who == 0:
        computeur_score += 10
        user_score -= 10
    elif who == 2:
        computeur_score += 5
        user_score += 5
    else:
        computeur_score -= 10
        user_score += 10


def check_winner(ordi_choice,player_choice):

    if ordi_choice == player_choice:
        result(2)
    else:
        if ((ordi_choice == 'PIERRE') and (player_choice == 'CISEAUX')) or ( (ordi_choice == 'FEUILLE') and ( player_choice == 'PIERRE')) or ((ordi_choice == 'CISEAUX') and ( player_choice == 'FEUILLE')):
            # quand on est dans l'un de ces cas, l'ordinateur l'emporte
            result(0)
        elif ((player_choice == 'PIERRE') and (ordi_choice == 'CISEAUX')) or ( (player_choice == 'FEUILLE') and ( ordi_choice == 'PIERRE')) or ((player_choice == 'CISEAUX') and ( ordi_choice == 'FEUILLE')):
            # quand on est dans l'un de ces cas, le joueur l'emporte. 
            result(1)


def random_gen(liste):
    # ce programme va faire un choix aléatoire entre pierre, feuille et ciseaux à chaque appel    
    # On va choisir une position aléatoire 
    pos = randint(0, len(liste) - 1)

    return liste[pos]


def result(value):
    winning_message = ["Bravo ! ","Superbe coup !"," Fantastique ! ","Trop fort ! ", " Je n'en ai pas douté une seconde ! ","Continuez sur cette lancée ", "Keep it up"]
    loosing_message = [" Oups ! ", " La prochaine sera la bonne ! ", " Courage !", "Don't Give up ", "Pas de chance ! ", "Pas de bol ! ", "Il vous faut vous entrainer encore ! "]
    equality_message = ["Egalité", "Match nul", "Olala c'est serré ! ", "on va voir qui est le plus fort prochainement ! ", "On va devoir rester sur notre faim "]

    if value == 1: 
        update_score(1)
        print(random_gen(winning_message))
    elif value == 2:
        update_score(2)
        print(random_gen(equality_message))
        print("Vous partagez les 10£ ")
    else:
        update_score(0)
        print(random_gen(loosing_message))
        print("L'ordinateur l'emporte !")



def check_validity(word):
    liste = ['PIERRE','FEUILLE','CISEAUX']
    word = word.upper()
    if word in liste:
        random_value = random_gen(liste)
        print("Ordi : {}".format(random_value))
        check_winner(random_value,word)
    else:
        while word not in liste:
            print()
            print("Un choix entre Pierre Feuille et ciseaux svp : ")
            word = input("Votre choix : ")
            word = word.upper()
        check_validity(word)



print("""
        Bienvenue dans le jeu du Pierre, Feuille, Ciseaux. 😊

        Les règles sont les mêmes que celle de la vraie vie. Vous serez invité à
        effectuer un choix entre Pierre, Feuille et Ciseaux. De sont côté, 
        l'ordinateur en fera de même mais de manière aléatoire. Vos deux choix seront
        comparés et le verdict sera annoncé. A chaque partie que vous remportez, vous 
        augmentez votre cagnotte de 10£ 🤑 et à chaque défaite, l'ordinateur vous retirera 
        10£ 😈. Il en sera de même pour l'ordinateur. Vous commencerez tous deux avec une 
        cagnotte de 100£ 🤑  et le jeu s'arrêtera quand l'un de vous n'aura plus de sous 😊.

        Let's Gooooooooooooo 💪💪 !!!  

""")  
computeur_score = 100
user_score = 100

print_score(computeur_score,user_score)

while user_score and computeur_score :
    print()
    user_input = input("Votre choix : ")
    check_validity(user_input)
    print_score(computeur_score,user_score)

if not user_score:
    print()
    print("YOU LOOOOOOOOOOOOSE !!! 😈")
if not computeur_score:
    print()
    print("Congrats !!! You win 💪")
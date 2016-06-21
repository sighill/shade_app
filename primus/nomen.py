# nomen.py
#####################################################################
# Script d'attribution de nom à des entités Primus déja existantes.
# Ce script sert surtout aux class géographiques qui sont créées
# avec un champ 'name' laissé <null>.

# Importation des modeles primus
from primus.models import ( AssetPlace, Town, District, Island, 
                            Path, Street, Building, Test       )
# Libraire random
from random import choice
# MOAR EXCEPTIONS
import django.core.exceptions
# Les dicos
from primus.dict import *

#Constantes
valid_classes = (( 1 , 'Town'     ) , ( 2 , 'District' ) ,
                 ( 3 , 'Island'   ) , ( 4 , 'Path'     ) ,
                 ( 5 , 'Street'   ) , ( 6 , 'Building' ) ,
                 ( 7 , 'Test'     ) )


#####################################################################
# Fonction de récupération de la class à compléter
#####################################################################

def getTargetClass(target_class):
    """
        Tu lui donnes une string de classe valide et il te dit
        si c'est ok de continuer.
    """
    # Verouillage de la boucle while
    class_validity = False
    # Tant que l'input n'est pas bon, la boucle continue
    while class_validity is False:
        try:
            # Print des classes valides pour l'opération
            for item in valid_classes:
                print('{} : {}'.format(item[0], item[1]))
            # Demande du code de la classe
            class_input = int(input(
                'Veuillez entrer le code de la class de destination : '))
            # Conversion de la string en classe
            target_class = eval(valid_classes[class_input-1][1])
        # Si l'input n'est pas un integer
        except TypeError:
            print('Mauvaise réponse (pas un chiffre).')
            continue
        # Si l'input n'est pas dans les bornes de valid_class
        except IndexError:
            print('Mauvaise réponse (code non valide).')
            continue
        # Erreur de conversion string -> classe. Ouille !
        except SyntaxError:
            print(
                'Erreur de récupération de la classe. A corriger !')
            break
        # Sinon, on récupère la string
        else:
            class_validity = True
        #
    return target_class


#####################################################################
# Fonction d'attribution de nom 
#####################################################################
def objectNamer(target_class):
    """
        Fonction d'attribution de noms à des instances de classes
        PRIMUS déja existantes dans la base de données.
        Dans cette fonction on utilise des préfixes d'origine pour
        mieux s'y retrouver. 
        Pour rappel, voici les correspondances :
        Code pays | Nom pays     | Code origine | Préfixe
            1     | E. Roi-Lune  |      3       | moonking_
            2     | Lagashein    |      2       | ostrian_
            3     | Lombrie      |      1       | clementine_
            4     | Ostrie       |      2       | ostrian_
            5     | P. clémentin |      1       | clementine_
            6     | Ravénie      |      1       | clementine_
            7     | Thémésie     |      2       | ostrian_
    """
    # PREFETCH
    # On crée des querysets en avance pour ne pas taper dans 
    # la db à chaque instance de name.
    # TODO : voir si c'est vraiment efficace !!!
    raw_clementine_names = AssetPlace.objects.filter(
        origin = 1 , use_count = 0)
    
    raw_ostrian_names = AssetPlace.objects.filter(
        origin = 2 , use_count = 0)
    
    raw_moonking_names = AssetPlace.objects.filter(
        origin = 3 , use_count = 0)

    # Pour chaque instance de la classe dont le champ 'name' 
    # est <null> on récupère l'allegiance (code pays) 
    # pour en tirer l'origine via primus.dict.origin_dict
    # Ensuite on choisit au hasard un name de AssetPlace 
    # qui correspond au critère origin et on l'insère dans
    # le champ name de l'instance avec ou sans décoration
    for instance in target_class.objects.filter(name = None , allegiance = 2):

        # On récupère le code origine à partir du pays d'allegiance
        instance_origin = origin_dict[instance.allegiance]
        
        # Import du queryset prefetch dans raw_names
        if instance_origin == 1:
            raw_names = raw_clementine_names
        elif instance_origin == 2:
            raw_names = raw_ostrian_names
        else:
            raw_names = raw_moonking_names

        # Mise à jour de l'objet avec chosen_name décoré ou pas
        instance.name = choice(raw_names)
        # Commit
        # instance.save()
        print('Fin du test de la fonction. instance.name = {}'.format(instance.name))

    return True
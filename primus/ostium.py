# ostium
# Scripts d'importation de fichiers out de apis vers des objets python pour import db

# Imports
import os.path
# Our custom models
from primus.models import FirstName , LastName , Archetype , Continent , Town , District , Island , Path , Street , Building
# To catch duplicate entries and deal with it
from django.db import IntegrityError
# to catch more exceptions by django see https://docs.djangoproject.com/fr/1.9/ref/exceptions/#django.core.exceptions.FieldDoesNotExist for more
from django.core.exceptions import FieldDoesNotExist

# Variables globales
# liste des strings lus depuis le fichier
global file_header
global header_keywords
global file_content
global table_destination

# Constantes
# Liste des tables valides
# Chaque header doit en comporter une entrée
valid_tables = [ 'FirstName' , 
                 'LastName'  , 
                 'Archetype' ,
                 'Continent' ,
                 'Town'      ,
                 'District'  ,
                 'Island'    ,
                 'Path'      ,
                 'Street'    ,
                 'Building'  ]


# Fonction qui demande le nom du fichier out de Apis, construit le path complet
# sur le serveur et le retourne à l'utilisateur
def getApisOutFilePath():
    inputName = input( '\nEntrer le nom du fichier out de Apis à importer par Primus (par exemple 005_out): ' )
    
    # Path sur le serveur
    file_path = '/home/common/shade/apis/out/{}'.format( inputName )
    # Path sur PC Keleos
    #file_path = 'C:/Users/WILLROS/Perso/Shade/scripts/LocalWC-Shade-App/apis/out/{}'.format( inputName )
    
    print( '\nLe fichier à importer est le fichier \'{}\'\n'.format( file_path ) )
    return file_path

# Fonction qui vérifie si le fichier est présent et pas importé
def checkApisOutFileValidity( file_path ):
    global file_header
    global file_content
    global header_keywords
    # Est-ce que le fichier existe et lisible ?
    try:
        ofi = open(file_path , 'r')
        file_header = ofi.read().splitlines()[0]
        header_keywords = file_header.split(';')
        ofi.close()
        # Je dois réouvrir le fichier pour donner le contenu à file_content ?!
        ofi = open(file_path , 'r')
        file_content = ofi.read().splitlines()[1:]
        ofi.close()
        
    # Si le fichier n'existe pas, erreur d'ouverture relevée
    except IOError:
        print( '\nLe fichier spécifié n\'est pas présent sur le serveur.\n' )
        return False
    else:
        print('\nLe fichier est valide et prêt à l\'import !\n')
    
    return True
    # TODO : attraper d'autres erreurs potentielles !

# Fonction qui vérifie la validité du header (et propose à l'utilisateur d'en
# entrer un à la main si nécessaire)
def analyseHeader( file_path ):
    global file_header
    global header_keywords
    global table_destination
    global file_content
    valid = False

    # ici : si la longueur du set qui retourne l'intersection des deux listes
    #   est nulle, alors c'est que la liste header ne comporte pas de string qui se trouve
    #   dans la liste valid_tables : donc la liste header_keywords n'est pas valide.
    table_destination_in_header = set(header_keywords).intersection(valid_tables)

    # Analyse du header
    if 'HEADER' not in header_keywords:
        print('Header invalide ou absent, à corriger !')

    elif 'imported' in header_keywords:
        print('\nLe fichier a deja été importé, il doit donc être ignoré.\n')

    elif len(table_destination_in_header) != 1:
        print('\nLe header ne comporte pas de table de destination (ou plusieurs !). A corriger !\n')

    else:
        # Si une table est citée, on la sort du set créé plus haut
        table_destination = str(table_destination_in_header.pop())
        print('\nHeader valide, on passe à la suite.')
        valid = True

    # Tout est OK, on retourne l'indice du header dans la liste HEADER
    return valid

# Fonction qui importe les données lues dans la bonne DB, avec les bon paramètres
# automatiques dans le cas échéant
def importDataIntoDB( table_destination ):
    global file_header
    global file_content
    global header_keywords
    # On récupère les attributs de la table de destination
    # source http://stackoverflow.com/a/3106314
    # get_all_fields_names est dépréciée mais retourne une liste, bien plus pratique
    #    que son remplacant get_fields()
    # On ne récupère que les champs à remplir inteligemment, on ignore les champs automatiques
    attributes_to_ignore = [ 'name' , 'uid' , 'gid' , 'geom' , 'created' , 'modified' , 'use_count']
    class_destination_attributes = [i for i in eval(table_destination)._meta.get_all_field_names() if i not in attributes_to_ignore]
    
    # Construction de la liste des tuples (attribut,valeur) qui vont permettre de créer 
    #   le constructeur d'objets à la chaîne
    attribute_kwargs = {}
    # Pour chaque champ de la classe invoquée comme classe de destination, on essaye de voir
    #  si dans les variables de classe se trouve une liste de choix possibles pour ce champ. 
    #    Exemple, dans la table LastName se trouve un champ origin. On regarde s'il y a une variable
    #    origin_choice dans les variable de classe. 
    #  Si la liste *_choice n'existe pas, on le demandera plus tard. 
    #  Si elle existe, on essaye de voir si l'un des choix prédéfinis correspond 
    #  à un des mots-clefs du header. Si c'est le cas, on injecte le code
    #  numérique correspondant dans l'attribut correspondant. de l'objet à enregistrer.
    # Exemple : HEADER;LastName;femme. On extrait les attributs de LastName, on voit un
    # attribut genre, on regarde si dans la classe LastName on a genre_choice, OUI donc
    # on regarde si dans le header il y a un mot-clef qui matche un des choix de genre_choice
    # si oui, on l'injecte. Sinon, on demande une entrée manuelle. 
    #    (∩｀-´)⊃━☆ﾟ.*･｡ﾟ     -- Python magic up the ass bitch nigga
    for attribute in class_destination_attributes:
        try:
            attr_choice_list = eval('{}.{}_choice'.format(table_destination , attribute))
        except AttributeError:
            print('Pas de choix prédéfini possible pour l\'attribut {}. Entrez un code valide (pas de garde-fou ici, concentre toi et te craque pas): '.format(attribute))
            try:
                value_of_attribute = int(input('Code choisi : '))
            except ValueError:
                print('Mauvais input.')
                continue                
        else:
            for attr_choice_item in attr_choice_list:
                # Une liste de choix existe et une correspondance est trouvée -- break
                if attr_choice_item[1] in header_keywords:
                    value_of_attribute = attr_choice_item[0]
                    break
                else:
                    pass
                # Une liste de choix existe mais pas de correspondance -- input
                print('\nUne liste de choix possibles pour l\'attribut {} est disponible mais Ostium n\'a pas trouvé de correspondance dans le header.\nChoisissez le code dans la liste suivante:\n'.format(attribute))
                for i in attr_choice_list:
                    print('{} : {}'.format(i[0],i[1]))
                try:
                    print('Pour rappel, le header est le suivant :')
                    print(header_keywords)
                    value_of_attribute = int(input('Code choisi (pas de garde-fou ici, concentre toi et te craque pas) : '))
                except ValueError:
                    print('Mauvais input. Boulaaay')
                    continue
                else:
                    break
        # Pour chaque attribut commun à tous les éléments du fichier à importer, on crée un dico d'arguments
        # que l'on va passer en kwargs au créateur d'objets django
        attribute_kwargs[attribute] = value_of_attribute

    # Détermination du nom de champ de table dans lequel insérer les valeurs du fichier out
    # Si un champ 'name' existe, on demande confirmation pour insérer dedans.
    # Sinon, input du nom de champ
    field_destination = ''
    try:
        eval(table_destination)._meta.get_field('name')
    except FieldDoesNotExist:
        field_destination = str(input('Entrez le nom du champ dans lequel insérer la liste : '))
    else:
        choice = str(input('Insérer les données dans le champ \'name\' de la table de destination ? o/n : '))
        if choice.lower() in ['o','oui']:
            field_destination = 'name'
        elif choice.lower() in ['n','non']:
            field_destination = str(input('Entrez le nom du champ dans lequel insérer la liste : '))        

    # Boucle qui crée un objet pour chaque ligne du fichier, avec toujours les mêmes arguments sauf le contenu
    # de la ligne du fichier.
    for line in file_content:
        attribute_kwargs[field_destination] = line
        obj_to_create = eval(table_destination)(**attribute_kwargs)
        try:
            obj_to_create.save()
        except IntegrityError:
            print('ligne {} déjà présente. Ignorée.'.format(line))
            pass
        else:
            print('Insertion de la ligne {}'.format(line))
    return True
    
# J'utilise une fonction main au lieu du main du script pour pouvoir sortir à
# tout moment via return
def main():
    global file_header
    global header_keywords
    global file_content
    global table_destination
    # Etape 1: récupérer le chemin du fichier à parser
    file_path = getApisOutFilePath()
    
    # Etape 2: vérfier sa validité
    if( not( checkApisOutFileValidity( file_path ) ) ):
        print( '\nFichier Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script

    # Etape 3 : analyse du header
    if( not( analyseHeader( file_path ) ) ):
        print( '\nFichier Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script
    
    # Etape 3: import des données lues précédemment dans la table associée
    if( not( importDataIntoDB( table_destination ) ) ):
        print( '\nErreur lors de l\'import des données. Fin du script.\n' )
        return # Exit script
        
    # Done
    print( '\nLes données du fichier {} ont été importées avec succès !\n'.format( file_path ) )
    
    # Add 'imported' to the file header
    print('Ajout de la mention \'imported\' dans le HEADER')
    file_data = None
    with open(file_path, 'r') as file :
        file_data = file.read()

    # On ajoute 'imported' en utilisant HEADER comme ancrage dans la ligne
    file_data = file_data.replace('HEADER', 'HEADER;imported')

    # On écrase le fichier avec la donnée en mémoire (mode 'w')
    # Pas moyen de faire plus subtil simplement !
    with open(file_path, 'w') as file:
      file.write(file_data)

# main qui sera exécuté en cas d'appel de ce script
if __name__ == '__main__':
    # Appel de la fonction main
    main()    
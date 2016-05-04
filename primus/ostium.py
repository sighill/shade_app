# ostium
# Scripts d'importation de fichiers out de apis vers des objets python pour import db

# Imports
import os.path
from primus.models import FirstName , LastName , Archetype , Continent , Town , District , Island , Path , Street , Building


# Variables globales
# liste des strings lus depuis le fichier
global fileHeader
global header_keywords
global file_content

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


# Fonction qui demande le nom du fichier out de Apis, contruit le path complet
# sur le serveur et le retourne à l'utilisateur
def getApisOutFilePath():
    inputName = input( '\nEntrer le nom du fichier out de Apis à importer par Primus (par exemple 005_out): ' )
    
    # Path sur le serveur
    filePath = '/home/common/shade/apis/out/{}'.format( inputName )
    # Path sur PC Keleos
    #filePath = 'C:/Users/WILLROS/Perso/Shade/scripts/LocalWC-Shade-App/apis/out/{}'.format( inputName )
    
    print( '\nLe fichier à importer est le fichier \'{}\'\n'.format( filePath ) )
    return filePath

# Fonction qui vérifie si le fichier est présent et pas importé
def checkApisOutFileValidity( filePath ):
    global fileHeader
    global file_content
    global header_keywords
    # Est-ce que le fichier existe et lisible ?
    try:
        ofi = open(filePath , 'r')
        fileHeader = ofi.read().splitlines()[0]
        header_keywords = fileHeader.split(';')
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
def analyseHeader( filePath ):
    global fileHeader
    global header_keywords

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

    # Tout est OK, on retourne l'indice du header dans la liste HEADER
    return fileHeader

# Fonction qui détermine si le fichier out est composé d'une entrée par ligne
# (comme une liste de prénoms) ou s'il est plus compliqué.
def isSimpleOutFile( table_destination ):
    return True
    
# Fonction qui lit le fichier out ligne par ligne s'il s'agit d'un fichier
# simple. L'impémentation en cas de données plus compliquées est à définir.
def readApisOutFile( filePath, table_destination ):
    # Vérification d'après le header qu'on a un string par ligne
    if( isSimpleOutFile( table_destination ) ):
        # transformer le fichier en une liste de string (déjà fait dans le cas
        # données simples) ==> Rien à faire!
        return True
    else:
        # TODO
        print( '\nL\'import de ce type de donnée n\'est pas encore implémenté.\n' )
        return False

# Fonction qui importe les données lues dans la bonne DB, avec les bon paramètres
# automatiques dans le cas échéant
def importDataIntoDB( table_destination ):
    global fileHeader
    global file_content
    # FOR TESTING
    # global header_keywords
    header_keywords = [ 'HEADER' , 'foo' , 'Pays clémentin , Ravénie , Lombrie' ]

    # Vérification d'après le header qu'on a un string par ligne
    if( isSimpleOutFile( table_destination ) ):
        # On récupère les attributs de la table de destination
        # source http://stackoverflow.com/a/3106314
        # get_all_fields_names est dépréciée mais retourne une liste, bien plus pratique
        #    que son remplacant get_fields()
        # On ne récupère que les champs à remplir inteligemment, on ignore les champs automatiques
        attributes_to_ignore = [ 'name' , 'uid' , 'gid' , 'geom' , 'created' , 'modified']
        class_destination_attributes = [i for i in table_destination._meta.get_all_field_names() if i not in attributes_to_ignore]
        
        # Construction de la liste des tuples (attribut,valeur) qui vont permettre de créer 
        #   le constructeur d'objets à la chaîne
        attribute_list = []
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
                attr_choice_list = eval('table_destination.{}_choice'.format(attribute))
            except AttributeError:
                print('Pas de choix prédéfini possible pour l\'attribut {}. Entrez un code valide (pas de garde-fou ici, concentre toi et te craque pas):'.format(attribute))
                try:
                    value_of_attribute = int(input('Code choisi : '))
                except ValueError:
                    print('Mauvais input.')
                    continue                
            else:
                for attr_choice_item in attr_choice_list:
                    if attr_choice_item[1] in header_keywords:
                        value_of_attribute = attr_choice_item[0]
                        break
                    else:
                        pass
                    # Une liste de choix existe mais pas de correspondance.
                    print('\nUne liste de choix possibles pour l\'attribut {} est disponible mais Ostium n\'a pas trouvé de correspondance dans le header.\nChoisissez le code dans la liste suivante:\n'.format(attribute))
                    for i in attr_choice_list:
                        print('{} : {}'.format(i[0],i[1]))
                    try:
                        print('Pour rappel, le header est le suivant :')
                        print(header_keywords)
                        value_of_attribute = int(input('Code choisi (pas de garde-fou ici, concentre toi et te craque pas) :'))
                    except ValueError:
                        print('Mauvais input. Boulaaay')
                        continue
                    else:
                        break
            attribute_list.append(( "'{}'".format(attribute) , str(value_of_attribute) ))

        # Récapitulatif
        print('Liste des attributs récoltés :')
        for i in attribute_list:
            print('{} : {}'.format(i[0],i[1]))

        # Création d'une sous-requête qui prépare la partie constante du queryset de création d'objet
        # WIIIIIIIP
        index = 0
        sub_queryset_list = []
        while index < len(attribute_list):
            sub_queryset_list.append(' = '.join(str(i) for i in attribute_list[index]))
            index += 1

        sub_queryset_str = ' , '.join(i for i in sub_queryset)
        queryset = "{}({})".format(table_destination , sub_queryset_str)
        # Helas je suis bloqué ici. La string finale est exactement ce qu'il faudrait, mais en string pure ! Pas bon. Il faut roll vers le haut pour trouver une solution en amont !
        # Il nous faut 

    return True
    
# J'utilise une fonction main au lieu du main du script pour pouvoir sortir à
# tout moment via return
def main():
    # Etape 1: récupérer le chemin du fichier à parser
    filePath = getApisOutFilePath()
    
    # Etape 2: vérfier sa validité
    if( not( checkApisOutFileValidity( filePath ) ) ):
        print( '\nFichier Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script
        
    # Etape 3: évaluation de l'en-tête du fichier
    table_destination = analyseHeader( filePath )
    if( table_destination == -1 ):
        print( '\nHeader Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script
        
    # Etape 4: lecture des données du fichier
    if( not( readApisOutFile( filePath, table_destination ) ) ):
        print( '\nErreur lors de la lecture des données. Fin du script. Aucune donnée importée.\n' )
        return # Exit script
        
    # Etape 5: import des données lues précédemment dans la table associée
    if( not( importDataIntoDB( table_destination ) ) ):
        print( '\nErreur lors de l\'import des données. Fin du script.\n' )
        return # Exit script
        
    # Done
    print( '\nLes données du fichier {} ont été importées avec succès !\n'.format( filePath ) )
    return # Exit script

# main qui sera exécuté en cas d'appel de ce script
if __name__ == '__main__':
    # Appel de la fonction main
    main()    
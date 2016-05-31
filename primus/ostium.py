# ostium
# Scripts d'importation de fichiers out de apis vers des objets python pour import db

# Imports
import os.path
# Our custom models
from primus.models import FirstName , LastName , Archetype , Continent , Town , District , Island , Path , Street , Building , Test
# To catch duplicate entries and deal with it
from django.db import IntegrityError
# to catch more exceptions by django see https://docs.djangoproject.com/fr/1.9/ref/exceptions/#django.core.exceptions.FieldDoesNotExist for more
from django.core.exceptions import FieldDoesNotExist

# Constantes
# Liste des tables valides
# Chaque header doit en comporter une entrée
VALID_TABLES = [ 'FirstName' , 
                 'LastName'  , 
                 'Archetype' ,
                 'Continent' ,
                 'Town'      ,
                 'District'  ,
                 'Island'    ,
                 'Path'      ,
                 'Street'    ,
                 'Building'  ,
                 'Test'      ]

#################################################################################
# Fonction qui demande le nom du fichier out de Apis, construit le path complet
# sur le serveur et le retourne à l'utilisateur
# in: rien
# out: le chemin du fichier
#################################################################################
def getApisOutFilePath():
    inputName = input( '\nEntrer le nom du fichier out de Apis à importer par Primus (par exemple 005_out): ' )
    
    # Path sur le serveur
    file_path = '/home/common/shade/apis/out/{}'.format( inputName )
    # Path sur PC Keleos
    #file_path = 'C:/Users/WILLROS/Perso/Shade/scripts/LocalWC-Shade-App/apis/out/{}'.format( inputName )
    
    print( '\nLe fichier à importer est le fichier \'{}\''.format( file_path ) )
    return file_path

#################################################################################
# Fonction qui vérifie si le fichier est présent et pas importé
# in: le chemin du fichier
# out: la validité ou non du fichier / la liste des keywords du header /
# la liste des strings lues dans le corps du fichier
#################################################################################
def checkApisOutFileValidity( file_path ):
    header_keywords = []
    file_content = []

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
        print( '\nLe fichier spécifié n\'est pas présent sur le serveur.' )
        return ( False, header_keywords, file_content )

    else:
        print('\nLe fichier est valide et prêt à l\'import !')
    
    return ( True, header_keywords, file_content )  
    # TODO : attraper d'autres erreurs potentielles !

#################################################################################
# Fonction qui vérifie la validité du header (et propose à l'utilisateur d'en
# entrer un à la main si nécessaire)
# in: la liste des keywords du header
# out: la table de destination (ou un string vide si le header est invalide)
#################################################################################
def analyseHeader( header_keywords ):
    table_destination = ""

    # ici : si la longueur du set qui retourne l'intersection des deux listes
    #   est nulle, alors c'est que la liste header ne comporte pas de string qui se trouve
    #   dans la liste valid_tables : donc la liste header_keywords n'est pas valide.
    table_destination_in_header = set(header_keywords).intersection(VALID_TABLES)

    # Analyse du header
    if 'HEADER' not in header_keywords:
        print('\nHeader invalide ou absent, à corriger !')

    elif 'imported' in header_keywords:
        print('\nLe fichier a deja été importé, il doit donc être ignoré.')

    elif len(table_destination_in_header) != 1:
        print('\nLe header ne comporte pas de table de destination (ou plusieurs !). A corriger !')

    else:
        # Si une table est citée, on la sort du set créé plus haut
        table_destination = str(table_destination_in_header.pop())
        print('\nHeader valide, on passe à la suite.')

    # Tout est OK, on retourne l'indice du header dans la liste HEADER
    return table_destination

#################################################################################
# Fonction qui détermine selon quelle méthode les données lues seront importées
# dans la DB
# in: la table de destination / la liste des keywords du header / la liste des
# strings lus dans le fichier
# out: l'insertion a-t-elle été un succès ou non ?
#################################################################################
def importDataIntoDB( table_destination, header_keywords, file_content ):

    if( table_destination == "FirstName" or table_destination == "LastName" or table_destination == "Test" ):
        print('\nPour ce type de données, on insère de nouvelles lignes dans la table associée.')
        return inportDataIntoDBInsert( table_destination, header_keywords, file_content )

    elif ( table_destination ==  "Archetype"):
        print('\nPour ce type de données, si j\'ai bien compris, il faut les insérer à la mano!')
        return False

    else:
        print('\nPour ce type de données, les noms lus dans le fichier out seront donnés à des éléments existants de la table associée.')
        return inportDataIntoDBInsert( table_destination, header_keywords, file_content )

#################################################################################
# fonction qui réalise l'import des données dans la DB en insérant à chaque fois
# une nouvelle ligne dans la table
# in: la table de destination / la liste des keywords du header / la liste des
# strings lus dans le fichier
# out: l'insertion a-t-elle été un succès ou non ?
#################################################################################
def inportDataIntoDBInsert( table_destination, header_keywords, file_content ):

    # On récupère les attributs de la table de destination
    # source http://stackoverflow.com/a/3106314
    attributes_to_ignore = [ 'name' , 'uid' , 'gid' , 'geom' , 'created' , 'modified' , 'use_count']
    # Méthode get_fields : détails de la prochaine ligne de code pour meilleure compréhension :
    #   i == <django.db.models.fields.AutoField: uid>
    #   i.name == 'uid'
    class_destination_attributes = [field.name for field in eval(table_destination)._meta.get_fields() if field.name not in attributes_to_ignore ]

    # get_all_fields_names est dépréciée mais retourne une liste directement, bien plus pratique
    # que son remplacant get_fields(). get_fields est optimisé par contre.
    # On ne récupère que les champs à remplir inteligemment, on ignore les champs automatiques
    # class_destination_attributes = [i for i in eval(table_destination)._meta.get_all_field_names() if i not in attributes_to_ignore]
    
    # Construction de la liste des tuples (attribut,valeur) qui vont permettre de créer 
    #   le constructeur d'objets à la chaîne
    attribute_kwargs = {}

    # Pour chaque champ de la classe invoquée comme classe de destination, on essaye de voir
    #  si dans les variables de classe se trouve une liste de choix possibles pour ce champ. 
    #    Exemple, dans la table LastName se trouve un champ origin. On regarde s'il y a une variable
    #    origin_choice dans les variable de classe. 
    for attribute in class_destination_attributes:
        # On essaye : Y a-t-il une variable de classe qui se nomme <attribute>_choice ?
        try:
            attr_choice_list = eval('{}.{}_choice'.format(table_destination , attribute))
        # S'il n'y a pas de variable de classe qui se nomme <attribute>_choice : on demande un input
        except AttributeError:
            print('Pas de choix prédéfini possible pour l\'attribut {}. Entrez un code valide (pas de garde-fou ici, concentre toi et te craque pas): '.format(attribute))
            try:
                value_of_attribute = int(input('Code choisi : '))
            # Petite vérif qu'il n'y ait pas d'erreur énorme dans l'input
            except ValueError:
                print('Mauvais input.')
                continue

        # La variable <attribute>_choice existe, 
        else:
            auto_fill = False
            # On boucle dans la variable de classe et on cherche une correspondance avec une entrée dans header_keywords
            for attr_choice_item in attr_choice_list:
                # Une liste de choix existe et une correspondance est trouvée, on récupère le code de l'attribut (integer)
                if attr_choice_item[1] in header_keywords:
                    value_of_attribute = attr_choice_item[0]
                    # On casse la boucle for
                    auto_fill = True
                    break
                # Une liste de choix existe et PAS de correspondance trouvée pour cet item, on passe à l'item suivant
                else:
                    pass

            # Une liste de choix existe mais le remplissage auto de variable a échoué : on demande un input
            if not auto_fill:
                print('\nUne liste de choix possibles pour l\'attribut {} est disponible mais Ostium n\'a pas trouvé de correspondance dans le header.'.format(attribute))
                print('\nChoisissez le code dans la liste suivante :')
                for i in attr_choice_list:
                    print('{} : {}'.format(i[0],i[1]))
                try:
                    print('Pour rappel, le header est le suivant :')
                    print(header_keywords)
                    value_of_attribute = int(input('Code choisi : '))
                except ValueError:
                    print('Mauvais input. On demande un code.')
                break

        # Pour chaque champ de la table de destination (sauf le champ de destination de la donnée du fichier *_out
        # on crée un dico d'arguments que l'on va passer en kwargs au créateur d'objets django
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

#################################################################################
# fonction qui réalise l'import des données dans la DB en associant la valeur
# lue dans le fichier à un élément de la table sans nom (choisis aléatoirement)
# in: la table de destination / la liste des keywords du header / la liste des
# strings lus dans le fichier
# out: l'insertion a-t-elle été un succès ou non ?
#################################################################################
def inportDataIntoDBReplace( table_destination, header_keywords, file_content ):
    # TODO

    # Importation de la donnée dans une variable

    # Importation des objets Town dont le champ 'name' est null dans une variable

    # Boucle for sur chacun des objets et attribution d'une string 'name'

        # Le champ 'name' possède une contrainte d'unicité. On intercepte
        # l'exception IntegrityError si le name est déjà utilisé

    
    return False

#################################################################################
# Add 'imported' to the file header
# in: chemin du fichier
# out: l'insertion a-t-elle été un succès ou non ?
#################################################################################
def markOutFileAsImported( file_path ):
    print('Ajout de la mention \'imported\' dans le HEADER')
    
    file_data = None
    # Intérêt de with ... as ... ça ferme le fichier dans la foulée (super important !)
    with open(file_path, 'r') as file :
        file_data = file.read()
    # On ajoute 'imported' en utilisant HEADER comme ancrage dans la ligne
    file_data = file_data.replace('HEADER', 'HEADER;imported')
    # On écrase le fichier avec la donnée en mémoire (mode 'w')
    # Pas moyen de faire plus subtil simplement !
    with open(file_path, 'w') as file:
      file.write(file_data)
    
    return True

#################################################################################
# J'utilise une fonction main au lieu du main du script pour pouvoir sortir à
# tout moment via return
#################################################################################
def main():
    # Déclaration des variables qui vont être utilisées
    file_path = ""
    header_keywords = []
    file_content = []
    table_destination = ""
    validity = False

    # Etape 1: récupérer le chemin du fichier à parser
    file_path = getApisOutFilePath()
    
    # Etape 2: vérfier sa validité
    validity, header_keywords, file_content = checkApisOutFileValidity( file_path )
    if( not validity ):
        print( '\nFichier Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script

    # Etape 3 : analyse du header
    table_destination = analyseHeader( header_keywords )
    if( table_destination == "" ):
        print( '\nHeader Invalide. Fin du script. Aucune donnée importée.\n' )
        return # Exit script
    
    # Etape 4: import des données lues précédemment dans la table associée
    if( importDataIntoDB( table_destination, header_keywords, file_content ) ):
         # Success
        print( '\nLes données du fichier {} ont été importées avec succès !\n'.format( file_path ) )
    else:
        # Failure
        print( '\nErreur lors de l\'import des données. Fin du script.\n' )
        return # Exit script
    
    # Etape 5: Add 'imported' to the file header
    if( not( markOutFileAsImported( file_path ) ) ) :
        print( '\nAttention! Une erreur est survenue et la mention \'imported\' n\'a pas été ajoutée au header.\n' )

#################################################################################
# main qui sera exécuté en cas d'appel de ce script
#################################################################################
if __name__ == '__main__':
    # Appel de la fonction main
    main()    
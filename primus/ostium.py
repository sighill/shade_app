# ostium
# Scripts d'importation de fichiers out de apis vers des objets python pour import db

# Imports
import os.path

# Variables globales
# liste des strings lus depuis le fichier
global listSimpleData

# Constantes
# Liste des headers utilisés
HEADERS = [    "prenoms masculins italiens", 
               "prenoms feminins italiens" ]

# Pour chaque header, défini si oui ou non les données sont simples (une 
# entrée par ligne, comme une liste de prénom)
IS_SIMPLE_DATA = [ True, True ]

# Fonction qui demande le nom du fichier out de Apis, contruit le path complet
# sur le serveur et le retourne à l'utilisateur
def getApisOutFilePath():
    inputName = input( "Entrer le nom du fichier out de Apis à importer par Primus (par example 005_out): " )
    
    # Path sur le serveur
    filePath = "/home/common/shade/apis/out/{}".format( inputName )
    # Path sur PC Keleos
    #filePath = "C:/Users/WILLROS/Perso/Shade/scripts/LocalWC-Shade-App/apis/out/{}".format( inputName )
    
    print( " " )
    print( "Le fichier à importer est le fichier '{}'".format( filePath ) )
    return filePath

# Fonction qui vérifie si le fichier est présent (et éventuellement s'il n'est
# pas déjà importé... à voir...)
def checkApisOutFileValidity( filePath ):
    # Est-ce que le fichier existe ?
    if( not( os.path.isfile( filePath ) ) ):
        print( " " )
        print( "Le fichier spécifier n'est pas présent sur le serveur" )
        return False
    
    # Est-ce que le fichier a déjà été importé ?
    # TODO : voir si on ajoute quelque chose dans le fichier ou si on fait un
    # log qqpart. Le _log existant me paraît trop difficile à parser 
    # automatiquement. Ou sinon on consulte le _log "à la mano" et on fait
    # juste attention.

    # Vérification OK
    return True

# Fonction qui vérifie la validité du header (et propose à l'utilisateur d'en
# entrer un à la main si nécessaire)
def analyseHeader( filePath ):
    global listSimpleData
    fileHeader = ""
    headerCode = -1
    
    # Read the first line of the file
    listSimpleData = open( filePath , 'r').read()
    listSimpleData = listSimpleData.splitlines()
    fileHeader = listSimpleData[ 0 ]
    
    # Si c'est un header (commence par "HEADER="), récupérer le header
    # (sans "HEADER=") et supprimer la 1ère ligne de la liste afin de ne 
    # conserver que les données
    # TODO
    
    # else (si ce n'était pas un header), proposer à l'utilisateur d'en entrer un
    # TODO
    
    # Vérifier que le header fait partie de la liste acceptée. Si ce n'est pas 
    # le cas, on retourne -1
    # TODO
    
    # Tout est OK, on retourne l'indice du header dans la liste HEADER
    return headerCode

# Fonction qui détermine si le fichier out est composé d'une entrée par ligne
# (comme une liste de prénoms) ou s'il est plus compliqué.
def isSimpleOutFile( headerCode ):
    return IS_SIMPLE_DATA[ headerCode ]
    
# Fonction qui lit le fichier out ligne par ligne s'il s'agit d'un fichier
# simple. L'impémentation en cas de données plus compliquées est à définir.
def readApisOutFile( filePath, headerCode ):
    # Vérification d'après le header qu'on a un string par ligne
    if( isSimpleOutFile( headerCode ) ):
        # transformer le fichier en une liste de string (déjà fait dans le cas
        # données simples) ==> Rien à faire!
        return True
    else:
        # TODO
        print( " " )
        print( "L'import de ce type de donnée n'est pas encore implémenté." )
        return False

# Fonction qui importe les données lues dans la bonne DB, avec les bon paramètres
# automatiques dans le cas échéant
def importDataIntoDB( headerCode ):
    # Vérification d'après le header qu'on a un string par ligne
    if( isSimpleOutFile( headerCode ) ):
        # Déterminer en fonction de headerCode dans quelle DB on insère, ainsi
        # que les paramètres à remplir automatiquement
        # TODO
        
        # Boucle sur la liste des string
        global listSimpleData
        for line in listSimpleData:
            # Vérifier que le string n'existe pas déjà dans la DB
            # TODO
        
            # Insérer le string avec les paramètres automatiques
            # TODO
        
            # TODO: pour test uniquement, supprimer cette ligne plus tard
            print( line )
        
        # Fin
        return True
    else:
        # TODO
        print( " " )
        print( "L'import de ce type de donnée n'est pas encore implémenté." )
        return False
    
    return True
    
# J'utilise une fonction main au lieu du main du script pour pouvoir sortir à
# tout moment via return
def main():
    # Etape 1: récupérer le chemin du fichier à parser
    filePath = getApisOutFilePath()
    
    # Etape 2: vérfier sa validité
    if( not( checkApisOutFileValidity( filePath ) ) ):
        print( " " )
        print( "Fichier Invalide. Fin du script. Aucune donnée importée." )
        return # Exit script
        
    # Etape 3: évaluation de l'en-tête du fichier
    headerCode = analyseHeader( filePath )
    if( headerCode == -1 ):
        print( " " )
        print( "Header Invalide. Fin du script. Aucune donnée importée." )
        return # Exit script
        
    # Etape 4: lecture des données du fichier
    if( not( readApisOutFile( filePath, headerCode ) ) ):
        print( " " )
        print( "Erreur lors de la lecture des données. Fin du script. Aucune donnée importée." )
        return # Exit script
        
    # Etape 5: import des données lues précédemment dans la table associée
    if( not( importDataIntoDB( headerCode ) ) ):
        print( " " )
        print( "Erreur lors de l'import des données. Fin du script." )
        return # Exit script
        
    # Done
    print( " " )
    print( "Les données du fichier {} ont été importées avec succès !".format( filePath ) )
    return # Exit script

# main qui sera exécuté en cas d'appel de ce script
if __name__ == "__main__":
    # Appel de la fonction main
    main()    
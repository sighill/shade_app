# voca.py
# Python 3.4.3
# Django 1.9
# Script rassemblant des fonctions python3 pour modifier les fichiers
#   des dossiers ###_raw

#####################################################################
# README !
# Les fonctions suivantes sont là pour être appelées au sein d'un
# script personnalisé pour chaque mission.
# Pour importer facilement ces fonctions, CF premier snippet
#   en bas de ce script.
# Implémenter un log permettant de suivre les étapes et le traitement
# de la donnée. Le garder en global pour qu'il accumule les logs
# de chaque fonction.
# Des snippets de code utile sont dispos en fin de document
# RAPPEL SUBLIMETEXT :
#   Pour wrapper tout le code faire ctrl+a ctrl+k ctrl+1
#####################################################################

log = ''

#####################################################################
def WorkPath():
    # TODO : remplacer le snippet de travail en dossiers relatifs
    #   de voca.py par cette fonction qui détecte automatiquement
    #   le dossier de travail !
    """
        WorkPath 2016.04.09
        L'utilisation de cette fonction permet d'utiliser des 
        chemins d'accès relatifs entre scripts et dossiers 
        Cette fonction détermine automatiquement où le script 
            est lancé :
            Soit sur un pc en travail local
            Soit sur le serveur avec le shell Django
    """


def AddLog(log_level , str_to_add):
    """
        Addlog 2016.04.08
        Cette fonction gère l'ajout d'une ligne à un compte rendu
        Elle gère aussi l'ajout de brackets HTML pour la mise en 
        forme du log au niveau du template django
        log_level is either title , subtitle , corpus
    """
    global log
    separator = '#'
    # If title, big separator and str_to_add
    if log_level == 'title':
        log = log + separator*70 + '\n' + str_to_add + '\n' 

    # If subtitle, 4 space indent, medium separator, and str_to_add
    elif log_level == 'subtitle':
        log = log + '    ' + separator*35 + '\n' + str_to_add + '\n' 

    # If corpus, 8 spaces indent and str_to_add
    elif log_level == 'corpus':
        log = log + '        ' + str_to_add + '\n'

    # If typo
    else: 
        log = log + 'WARNING : bad log_level, using corpus mode'
        log = log + '        ' + str_to_add + '\n'

    return log

#####################################################################
def OutFileCreate(out_path,raw_filename,ref_list):
    # TODO : fix le log vide en fin de fonction !
    # TODO : fix le fait que les 2 AddLog ici ne fonctionnent pas
    """
        OutFileCreate 2016.04.08
        Crée les fichiers out et log au bon endroit, et les remplit.
        CF shade/README.md partie II.2 pour détails
        Conseil : fonction à appeler en fin de procédure
        Cette fonction attend quatre arguments:
            Le chemin absolu vers le dossier out WIP !
            Le nom de fichier  ###_raw (type attendu : string)
            Le texte raffiné ref_list (type attendu : list de strings)
            Le log de la procédure (type attendu : string)
    """
    # Variables globales
    global log
    # Variables locales
    file_id = raw_filename[:3]
   
    # Création du fichier ###_out
    # NB : l'argument w+ écrase l'ancien fichier s'il existe !
    AddLog('corpus' , 'Création du fichier {}_out'.format(file_id))
    with open(out_path + file_id + '_out' , 'w+') as ofi_out:
        ofi_out.write('\n'.join(ref_list))
    ofi_out.close()
        
    # Création du fichier ###_log
    # NB : l'argument w+ écrase l'ancien fichier s'il existe !
    AddLog('corpus' , 'Création du fichier {}_log'.format(file_id))
    with open(out_path + file_id + '_log' , 'w+') as ofi_log:
        ofi_log.write(log)
    ofi_log.close()

#####################################################################
def StringFormatter(raw_str):
    # TODO : ajouter des fonctionnalités
    """
        StringFormatter 2016.04.08
        Fonction de modification d'une string de n'importe quel type
        pour la mettre en forme selon le standard de l'app primus.
        Standard primus : Une majuscule en début de nom. Si nom
            composé, majuscule au début de chaque partie.
    """
    # Variables globales
    global log

    # Mise en forme : 'FoO-BAr' --> 'Foo-Bar'
    ref_str = raw_str.title()

    # Ecriture du log
    AddLog( 'corpus' , ref_str)
    
    return ref_str

#####################################################################
def StrValidator(list):
    # TODO : TESTER ET VALIDER CETTE FONCTION ! PAS LE TEMPS DE LE  
    #   FAIRE NOW
    """
        StrValidator 2016.04.09
        Cette fonction permet de valider rapidement chaque entrée
            d'une liste manuellement.
        Elle prompte chaque ligne et attend un input.
            Input vide : validé
            Input non vide : éliminé
    """
    # Variables globales
    AddLog('title' , 'Début de la fonction StrValidator')

    # Variables locales
    ref_list = []

    # Pour chaque ligne de list, prompt et attendre input.
    for line in list:
        valid = input(line + ' : ')
        if valid :
            ref_list.append(line + '\n')
        else:
            pass
    return ref_list

#####################################################################
# SNIPPETS DE CODE UTILES
#####################################################################
'''
# Ajout du répertoire de travail local pour travailler en système
#   de fichiers relatifs et importer les fonctions voca facilement
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate
'''

'''
# créer une liste comportant toutes les lignes du fichier
line_list = ofi.read().splitlines()
    # read() importe les lignes
    # splitlines() supprime le caractère de retour à la ligne
'''

# Ouvrir un fichier et en tirer des lignes sans le caractère
# spécial \n qui signifie un retour à la ligne :
# ofi = open('path_to_file'+'file_name' , 'option')
# CONSEIL : WRAPPE CE COMMENT ! option est soit :
    # r   Opens a file for reading only. The file pointer is placed 
    #       at the beginning of the file. This is the default mode.

    # r+  Opens a file for both reading and writing. The file pointer
    #       placed at the beginning of the file.

    # w   Opens a file for writing only. Overwrites the file if the 
    #       file exists. If the file does not exist, creates a 
    #       new file for writing.

    # w+  Opens a file for both writing and reading. Overwrites the 
    #       existing file if the file exists. If the file does 
    #       not exist, creates a new file for reading and writing.
    
    # wb+ Opens a file for both writing and reading in binary format.
    #       Overwrites the existing file if the file exists. 
    #       If the file does not exist, creates a new file for 
    #       reading and writing.
    
    # a   Opens a file for appending. The file pointer is at the end
    #       of the file if the file exists. That is, the file is 
    #       in the append mode. If the file does not exist, it 
    #       creates a new file for writing.
   
    # a+  Opens a file for both appending and reading. The file 
    #       pointer is at the end of the file if the file exists. 
    #       The file opens in the append mode. If the file does 
    #       not exist, it creates a new file for reading and writing.


    


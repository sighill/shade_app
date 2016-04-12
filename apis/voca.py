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
    """
        WorkPath 2016.04.09
        L'utilisation de cette fonction permet d'utiliser des 
        chemins d'accès relatifs entre scripts et dossiers 
        Cette fonction détermine automatiquement où le script 
            est lancé :
            Soit sur un pc en travail local
            Soit sur le serveur avec le shell Django
    """
    # TODO : remplacer le snippet de travail en dossiers relatifs
    #   de voca.py par cette fonction qui détecte automatiquement
    #   le dossier de travail !

def AddLog(log_level , str_to_add):
    """
        AddLog 2016.04.08
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
        log = log + '    ' + separator*35 + '\n'  + '    ' + str_to_add + '\n' 

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
    """
        StringFormatter 2016.04.08
        Fonction de modification d'une string de n'importe quel type
        pour la mettre en forme selon le standard de l'app primus.
        Standard primus : Une majuscule en début de nom. Si nom
            composé, majuscule au début de chaque partie.
    """
    # TODO : ajouter un convertisseur de caractères spéciaux.
    # Exemple : ` --> '

    # Variables globales
    global log

    # Mise en forme : 'FoO-BAr' --> 'Foo-Bar'
    ref_str = raw_str.title()

    # Ecriture du log
    AddLog( 'corpus' , '{} --> {}.'.format(raw_str , ref_str))
    
    return ref_str

#####################################################################
def StrValidator(list): # WIP NE PAS UTILISER
    """
        StrValidator 2016.04.09
        Cette fonction permet de valider rapidement chaque entrée
            d'une liste manuellement.
        Elle prompte chaque ligne et attend un input.
            Input vide : validé
            Input non vide : éliminé
    """
    # TODO : fonction de correction : utiliser while not line_corr_valid_ok
    #   c'est sale et pas solide. A améliorer ! 

    # Variables globales
    global log
    # Variables locales
    out_list = []
    counter_valid = 0
    counter_corr = 0
    counter_eliminated = 0

    print('StrValidator - inputs possibles : \n  Vide : string validé.\n  c : correction manuelle.\n  Tout autre input : string éliminé')
    # Pour chaque ligne de list, prompt et attendre input.
    for line in list:
        # Demande d'input
        key_input = input(line + ' : ')
        
        # Si input vide, string éliminée si pas vide, string gardée
        if not key_input :
            out_list.append(line)
            counter_valid += 1

        # Si correction, input demandé, confirmé, et ajouté.
        elif key_input in ['c','C']:
            line_corr_valid_ok = False
            while not line_corr_valid_ok:
                line_corr = input('Correction de {}: '.format(line))
                line_corr_valid = input('Validez vous {} ? o/n : '.format(line_corr))
                if line_corr_valid in ['o','O','y','Y']:
                    out_list.append(line_corr_valid)
                    line_corr_valid_ok = True
                    counter_corr += 1
                else:
                    continue
        
        # Si input différent de vide ou 'c', string confirmé et éliminé.
        else:
            line_eliminated_valid = input('Eliminer {} ? o/n : '.format(line))
            if line_eliminated_valid in ['o','O','y','Y']:
                print('String éliminé.')
                counter_eliminated += 1
            else: 
                print('String validé.')
                out_list.append(line)
                counter_valid += 1

    # Ajout du log
    AddLog('corpus', 'Lignes validées : {}'.format(counter_valid))
    AddLog('corpus', 'Lignes corrigées : {}'.format(counter_corr))
    AddLog('corpus', 'Lignes éliminées : {}'.format(counter_eliminated))
    return out_list

#####################################################################
def OdditiesFinder(raw_list):
    '''
        OdditiesFinder 2016.04.12
        Cherche dans la string d'entrée des caractères non prévus
        et pas acceptables dans la db primus.
        Chaque ligne (string) est transformée en liste de lettres (list)
        Chaque lettre est comparée à la liste des lettres acceptées.
        Si problème, prompt pour avoir la lettre de remplacement
        Laisser vide pour suppression de la lettre merdique.
    '''
    # TODO : tester la fonction avec un insert de plusieurs lettres
    #   dans le cas d'un remplacement de lettre --> plusieurs lettres
    # Variables globales
    global log

    # Variables locales
    ref_line_list = []
    acceptable_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z', '\'' , ' ']
    
    # Pour chaque ligne, déconstruction lettre par lettre et 
    #   comparaison de chaque lettre à un dico personnalisé
    for line in raw_list:
        # Passage de string à liste de lettres
        letter_list = list(line)
        curseur = 0
        for letter in letter_list:
            if letter not in acceptable_char:
                replacement_letter = input('Bizarrerie trouvée : \' {} \' dans \' {} \'. Remplacer par : '.format(letter , line))
                letter_list[curseur] = replacement_letter
                AddLog('corpus' , '{} : Modification de la lettre : {} en {}'.format(line , letter , replacement_letter))
            else:
                pass
            curseur += 1
        # Reconstruction de la string à partir de la liste de lettres
        line = ''.join(letter_list)
        #Ajout de la string dans la liste de sortie
        ref_line_list.append(line)
        
    return ref_line_list

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


    


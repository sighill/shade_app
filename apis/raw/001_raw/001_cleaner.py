# 001_cleaner.py
#####################################################################

##################################
# Import des modules et ajout du path de travail pour import relatif
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate , StrValidator

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = 'D:/Projets/shade_django/apis/raw/001_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute
raw_list = open(work_dir + raw_file , 'r').read().splitlines()

##################################
# Formatage du texte
# Init de la list contenant la sortie de StringFormatter
formatted_list = []
AddLog('subtitle' , 'Début de la fonction StringFormatter')
for line in raw_list:
	formatted_list.append(StringFormatter(line))

##################################
# Validation manuelle du texte
AddLog('subtitle' , 'Début de la fonction StrValidator')
ref_list = StrValidator(formatted_list)

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('D:/Projets/shade_django/apis/out/','001_src',ref_list)



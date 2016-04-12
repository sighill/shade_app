# 003_cleaner.py
#####################################################################

##################################
# Import des modules et ajout du path de travail pour import relatif
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate , OdditiesFinder

##################################
# Init des paths et noms de fichiers
AddLog('title' , '003 : Début du nettoyage du fichier')
work_dir = 'D:/Projets/shade_django/apis/raw/003_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute
raw_list = open(work_dir + raw_file , 'r').read().splitlines()

##################################
# Isolation du 1er mot des lignes paires
# Seules les lignes impaires de src sont intéressantes.
# On fait défiler un compteur qui pointera vers chaque ligne impaire
# de src et on prend le 1er mot de chaque ligne impaire.
line_counter = 1
out_list = []
while line_counter <= len(raw_list):
	out_list.append(raw_list[line_counter - 1].split(' ', 1)[0])
	line_counter += 2

# Changement de nom pour passage à la fonction suivante (clarté ftw)
Oddities_in_list = out_list


##################################
# Recherche de caractères étranges
AddLog('subtitle' , 'Début de la fonction OdditiesFinder')
formatter_in_list = OdditiesFinder(out_list)

##################################
# Formatage du texte
# Init de la list contenant la sortie de StringFormatter
ref_list = []
AddLog('subtitle' , 'Début de la fonction StringFormatter')
for line in formatter_in_list:
	ref_list.append(StringFormatter(line))

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('D:/Projets/shade_django/apis/out/','003_src',ref_list)



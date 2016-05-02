# 004_cleaner.py
#####################################################################

##################################
# Import des modules et ajout du path de travail pour import relatif
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate , OdditiesFinder

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = 'D:/Projets/shade_django/apis/raw/004_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute
raw_list = open(work_dir + raw_file , 'r').read().splitlines()

##################################
# Séparation des prénoms masculins et féminins
m_name = []
f_name = []

# Pour chaque mot de chaque ligne de la liste raw
# On checke la dernière lettre du mot
# S'il termine par o e ou i --> m_name
for line in raw_list:
	word_list = list(line)
	for word in word_list:
		if word[-1:] in ['o','O','i','I','e','E']:
			m_name.append(word)
		elif word[-1:] in ['a','A']:
			f_name.append(word)
		else:
			pass

# WIP ! Je commence primus pour voir comment construire les fichiers out.
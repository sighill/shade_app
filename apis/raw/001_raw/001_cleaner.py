# 001_cleaner.py
#####################################################################

# Ajout du répertoire de travail local pour travailler en système
#	de fichiers relatifs
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate


AddLog('title' , 'Début du nettoyage du fichier')
work_dir = 'D:/Projets/shade_django/apis/raw/001_raw/'
# Nom du fichier source
raw_file = 'src'
# Init de la list de lignes raffinées
ref_list = []
# list de strings
raw_list = open(work_dir + raw_file , 'r').read().splitlines()

# Formatage du texte
AddLog('title' , 'Début de la fonction StringFormatter')
for line in raw_list[0:10]:
	ref_list.append(StringFormatter(line))

# Enregistrement des fichiers sortie
AddLog('title' , 'Début de la fonction OutFileCreate')
OutFileCreate('D:/Projets/shade_django/apis/out/','001_src',ref_list)



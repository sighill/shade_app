# -*- coding: utf-8 -*-
# 004_cleaner.py
#J'ai tout fait à la main sérieux la loose

import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate

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
# Formatage du texte
# Init de la list contenant la sortie de StringFormatter
formatted_list = []
AddLog('subtitle' , 'Début de la fonction StringFormatter')
for line in raw_list:
	formatted_list.append(StringFormatter(line))

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('D:/Projets/shade_django/apis/out/','004_src',formatted_list,'FirstName;homme;Pays clémentin , Ravénie , Lombrie')
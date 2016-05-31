# -*- coding: utf-8 -*-
#015_cleaner.py
#WIP
import sys
sys.path.insert(0 , 'D:/Projets/shade_django/apis/')
from voca import AddLog , StringFormatter , OutFileCreate , StrValidator , OdditiesFinder

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = 'D:/Projets/shade_django/apis/raw/007_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute
raw_list = open(work_dir + raw_file , 'r').read().splitlines()
# Il y a plusieurs noms par ligne, il faut donc les séparer dans une nouvelle liste
separated_names_list = []
for line in raw_list:
    line_names = line.split('' '\t')
    for name in line_names:
        separated_names_list.append(name)

##################################
# Choix des prénoms uniquement masculins
men_name_list = []
for line in separated_names_list:
	if line[-1:] in ['A' , 'a']:
		pass
	else:
		men_name_list.append(line)

##################################
# Formatage du texte
# Init de la list contenant la sortie de StringFormatter
formatted_list = []
AddLog('subtitle' , 'Début de la fonction StringFormatter')
for line in men_name_list:
    formatted_list.append(StringFormatter(line))

##################################
# going through oddities finder
AddLog('subtitle' , 'Début de la fonction OdditiesFinder')
list_without_oddities = OdditiesFinder( formatted_list )

##################################
#The mighty StrValidatoooor
AddLog('subtitle' , 'Début de la fonction StrValidator')
validated_list = StrValidator( list_without_oddities )

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('D:/Projets/shade_django/apis/out/','015_src',validated_list,'FirstName;homme;Pays clémentin , Ravénie , Lombrie')
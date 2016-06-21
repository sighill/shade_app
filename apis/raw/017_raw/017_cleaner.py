# -*- coding: utf-8 -*-
# 017_cleaner.py
# CODED TO BE EXECUTED SERVER SIDE :
# cd /home/common/shade
# python3 manage.py shell

import sys
from apis.voca import *

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = '/home/common/shade/apis/raw/017_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute

with open(work_dir + raw_file , 'r') as file:
    raw_list = [i for i in file.read().splitlines()]
'''
##################################
# Formatage du texte
# Init de la list contenant la sortie de StringFormatter
AddLog('subtitle' , 'Début de la fonction StringFormatter')
formatted_list = [StringFormatter(line) for line in raw_list]


##################################
# going through oddities finder
AddLog('subtitle' , 'Début de la fonction OdditiesFinder')
list_without_oddities = OdditiesFinder( formatted_list )
'''
ref_list = raw_list
##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('/home/common/shade/apis/out/','017_src',ref_list,'AssetPlace;Pays clémentin , Ravénie , Lombrie')
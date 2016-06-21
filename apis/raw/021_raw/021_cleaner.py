# -*- coding: utf-8 -*-
# 018_cleaner.py

# CODED TO BE EXECUTED SERVER SIDE :
# cd /home/common/shade
# python3 manage.py shell

import sys
from apis.voca import *

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = '/home/common/shade/apis/raw/021_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute

with open(work_dir + raw_file , 'r') as file:
    raw_list = [i for i in file.read().splitlines()]

##################################
# Elimination des strings surnuméraires
middle_list = []
for line in raw_list:
    deb = line.find('>')+1
    end = line.find('</a>')
    middle_list.append(line[deb:end])

#Elimination des fins de ligne avec des parenthèses
# Si une parenthèse est trouvée, on élimine la fin de string
ref_list = []
for line in middle_list:
    foo = line.find('(')
    if foo != -1:
        line = line[:foo-1]
    ref_list.append(line)

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('/home/common/shade/apis/out/','021_src',ref_list,'FirstName;Empire du Roi-Lune')
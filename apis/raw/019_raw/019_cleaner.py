# -*- coding: utf-8 -*-
# 019_cleaner.py

# CODED TO BE EXECUTED SERVER SIDE :
# cd /home/common/shade
# python3 manage.py shell

import sys
from apis.voca import *

##################################
# Init des paths et noms de fichiers
AddLog('title' , 'Début du nettoyage du fichier')
work_dir = '/home/common/shade/apis/raw/019_raw/'
# Nom du fichier source
raw_file = 'src'

##################################
# Création de la liste brute

with open(work_dir + raw_file , 'r') as file:
    raw_list = [i for i in file.read().splitlines()]

##################################
# Elimination des strings surnuméraires
middle_list = []
to_elim = ['0','1','2','3','4','5','6','7','8','9',',']
for line in raw_list:
    middle_list.append(''.join([i for i in line if i not in to_elim]))

# Elimination des espaces àlakon
ref_list = [i.strip() for i in middle_list]

##################################
# Enregistrement des fichiers sortie
AddLog('subtitle' , 'Début de la fonction OutFileCreate')
OutFileCreate('/home/common/shade/apis/out/','019_src',ref_list,'AssetPlace;Empire du Roi-Lune')
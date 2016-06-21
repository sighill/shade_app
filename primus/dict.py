# dict.py

#####################################################################
# dictionaires universels

origin_dict = {1:3, 2:2, 3:1, 4:2, 5:1, 6:1, 7:2}

origin_prefix = {1:'clementine_', 2:'ostrian_', 3:'moonking_'}


#####################################################################
# Dictionaires à utiliser pour agrémenter les noms
# NB : les entrées ostriennes sont sans majuscules car elles
# sont placées à la fin de la variable name.
# Exemples avec 'F'ort Camino' :
# Casteletto di Camino / Caminoschloss / Jisr al Camino
# TODO : les mettres dans un script à part ?
# Dictionaire de correspondance entre 
#   code pays (primus.models.Country.country_choices) 
#   code origine (primus.models.FirstName.origin_choices)

##################################
# dictionaires moonking_


moonking_town = { 1:'Easima', 2:'Madina', 3:'Qrya', 
                  4:'Qalea', 5:'Hisn'            }

moonking_street = {1:'Sabil', 2:'Sharie', 3:'Ziqaq',
                   4:'Jisr', 5:'Eawama'   }

moonking_terrain = {} # WIP


##################################
# dictionaires ostrian_


ostrian_town = { 1:'kapital', 2:'stadt', 3:'burg', 
                 4:'festung', 5:'schloss'        }

ostrian_street = {1:'avenue', 2:'strasse', 3:'gasse',
                  4:'brucke', 5:'ponton' }

ostrian_terrain = {} # WIP

##################################
# dictionaires clementine_


clementine_town = { 1:'Capoluogo', 2:'Città', 3:'Villaggio', 
                    4:'Castello', 5:'Casteletto'           }

clementine_street = { 1:'Viale', 2:'Strada', 3:'Vicolo',
                      4:'Pont', 5:'Pontono'            }

clementine_terrain = {} # WIP
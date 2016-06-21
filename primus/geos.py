# geos.py
# WIP
# Script with functions for geographic queries


#####################################################################
def allegianceChange(class_to_update):
    """
        IN : une string
        Cette fonction permet de mettre à jour le champ allegiance
        d'une classe, pour la faire coïncider avec la valeur du
        champ allegiance de primus_grid (qui gouverne la valeur
        réelle d'allegiance)
    """
    if type(class_to_update) == str:
        pass
        class_to_update = class_to_update.lower()
    else:
        print('Argument non valide. Fin de la fonction')
        return False
/////snippets

cd /home/common/shade
python3 manage.py makemigrations && python3 manage.py migrate

cd /home/common/shade
python3 manage.py shell
from primus.ostium import *
from primus.models import *

cd /home/common/shade
git add --all && git commit -all -m ''
git push shade_app master


(  , '' ) ,


#####################################################################
# Classe de Template
#####################################################################
class Template(models.Model):
    '''
        docstring
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(Template)
    geom = gismodels.Template(srid = 3857)

    # Methodes
    def __str__(self):
        return str(self.name)



1 Empire du Roi-Lune
2 Lagashein
3 Lombrie
4 Ostrie
5 Pays clémentin
6 Ravénie
7 Thémésie
# 8 Nécris (pas un pays, ville franche)

Correspondance pays <-> origin_choice

origin_dict = {1:3, 2:2, 3:1, 4:2, 5:1, 6:1, 7:2}

Capitales :
1 Ishmer
2 Orffstein
3 Trevoletta , Orphia , Montenero
4 Lisselberg
5 Clémence
6 Agostina
7 Thémée


Code pays | Nom pays     | Code origine | Préfixe
    1     | E. Roi-Lune  |      3       | moonking_
    2     | Lagashein    |      2       | ostrian_
    3     | Lombrie      |      1       | clementine_
    4     | Ostrie       |      2       | ostrian_
    5     | P. clémentin |      1       | clementine_
    6     | Ravénie      |      1       | clementine_
    7     | Thémésie     |      2       | ostrian_


Agréments / préfixes / Suffixes 
di
del
san
sant
santa
del 
della


kwargs = {}
kwargs['genre'] = 2
kwargs['origin'] = 1
kwargs['name'] = 'John'
obj_a_creer = FirstName(**kwargs)
obj_a_creer.save()

# Grid
terrain_choices = ( ( 1 , 'Colline'        ) ,
                    ( 2 , 'Désert'         ) ,
                    ( 3 , 'Forêt'          ) ,
                    ( 4 , 'Littoral'       ) ,
                    ( 5 , 'Marais'         ) ,
                    ( 6 , 'Mer intérieure' ) ,
                    ( 7 , 'Montagne'       ) ,
                    ( 8 , 'Océan'          ) ,
                    ( 9 , 'Savane'         ) ,
                    ( 10, 'Plaine'         ) )

# FirstName
genre_choice = (
    (1 , 'femme') , 
    (2 , 'homme') )

# FirstName LastName
origin_choice  = (
    (1 , 'Pays clémentin , Ravénie , Lombrie' ) ,
    (2 , 'Ostrie, Thémésie, Lagashein' ) ,
    (3 , 'Empire du Roi-Lune' ) )

# Grid LastName
allegiance_choices = ( ( 1 , 'Empire du Roi-Lune' ) ,
                       ( 2 , 'Lagashein'          ) ,
                       ( 3 , 'Lombrie'            ) ,
                       ( 4 , 'Ostrie'             ) ,
                       ( 5 , 'Pays clémentin'     ) ,
                       ( 6 , 'Ravénie'            ) ,
                       ( 7 , 'Thémésie'           ) )

region_choices = (#WIP
    )

# Town
category_choice = (
    ( 1 , 'Capitale' ) ,
    ( 2 , 'Cité'     ) ,
    ( 3 , 'Village'  ) ,
    ( 4 , 'Fort'     ) ,
    ( 5 , 'Fortin'   ) )

# Street
type_street_choice = (
    ( 1 , 'Avenue'  ) ,
    ( 2 , 'Rue'     ) ,
    ( 3 , 'Ruelle'  ) ,
    ( 4 , 'Pont'    ) ,
    ( 5 , 'Ponton'  ) )

# Path
type_path_choices = (
    ( 1 , 'Route'   ) ,
    ( 2 , 'Chemin'  ) ,
    ( 3 , 'Sentier' ) )

# Archetype
beauty_choice = (
    ( 0 , 'Grande laideur') ,
    ( 1 , 'Classique'     ) ,
    ( 2 , 'Grande Beauté' ) )

cast_choice = (
    ( 1 , 'Gueux'              ) ,
    ( 2 , 'Pègre'              ) ,
    ( 3 , 'Popolo minuto'      ) ,
    ( 4 , 'Popolo grasso'      ) ,
    ( 5 , 'Clergé'             ) ,
    ( 6 , 'Haut clergé'        ) ,
    ( 7 , 'Haute bourgeoisie'  ) ,
    ( 8 , 'Noblesse d\'épée'   ) ,
    ( 9 , 'Noblesse de lettre' ) )

category_choice = (
    ( 1 , 'Basique' ) ,
    ( 2 , 'Vétéran' ) ,
    ( 3 , 'Elite'   ) )

# Building
category_choices = (
    ( 1 , 'Religieux' ) , 
    ( 2 , 'Militaire' ) ,
    ( 3 , 'Commercial') ,
    ( 4 , 'Bas-fonds' ) ,
    ( 5 , 'Privé'     ) )
subcategory_choices = (
    ( 11 , 'Cathédrale' ) ,
    ( 12 , 'Eglise' ) ,
    ( 13 , 'Chapelle' ) ,
    ( 14 , 'Temple' ) ,
    ( 15 , 'Couvent' ) , 
    ( 16 , 'Autre (religieux)' ) ,
    ( 21 , 'Caserne' ) ,
    ( 22 , 'Réserve' ) ,
    ( 23 , 'Armurerie' ) ,
    ( 24 , 'Dortoir' ) ,
    ( 25 , 'Bastion' ) ,
    ( 26 , 'Tour' ) ,
    ( 27 , 'Autre (militaire)' ) ,
    ( 31 , 'Entrepot' ) ,
    ( 32 , 'Comptoir' ) ,
    ( 33 , 'Bureau de change' ) ,
    ( 34 , 'Boutique' ) ,
    ( 35 , 'Taverne' ) ,
    ( 36 , 'Autre (commercial)' ) ,
    ( 41 , 'Planque' ) ,
    ( 42 , 'Refuge' ) ,
    ( 43 , 'Lieu d\'assemblée' ) ,
    ( 44 , 'Autre (bas-fonds)' ) ,
    ( 51 , 'Palazzo' ) ,
    ( 52 , 'Manoir' ) ,
    ( 53 , 'Maison bourgeoise' ) ,
    ( 54 , 'Maison modeste' ) ,
    ( 55 , 'Ruine' ) ,
    ( 56 , 'Autre (privé)' ) ) 
deity_choices = (
    ( 1 , 'Thémésia' ) , 
    ( 2 , 'Ohmédia'  ) ,
    ( 3 , 'Candélia' ) ,
    ( 4 , 'Sélène'   ) ,
    ( 5 , 'Inconnu'  ) )
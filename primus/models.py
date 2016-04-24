from django.db import models
from django.contrib.gis.db import models as gismodels


#####################################################################
# Classe de prénom (geom : False)
#####################################################################
class FirstName(models.Model):
    '''
        Les prénoms disponibles dans le générateur de PNJ.
        - genre: 1-femme / 2-homme
        - origine : 
            1: Pays clémentin , Ravénie , Lombrie
                (prénoms italiens)
            2: Ostrie, Thémésie, Lagashein
                (prénoms germaniques, anglo-saxons)
            3: Empire du Roi-Lune
                (Prénoms arabes)
    '''
    # TODO 

    # Variables pour les choix pré-remplis
    genre_choice = (
        (1 , 'femme') , 
        (2 , 'homme') )
    origin_choice  = (
        (1 , 'Pays clémentin , Ravénie , Lombrie' ) ,
        (2 , 'Ostrie, Thémésie, Lagashein'        ) ,
        (3 , 'Empire du Roi-Lune'                 ) )

    # Attributs
    uid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , unique = True)
    genre = models.PositiveIntegerField(choices = genre_choice)
    origin = models.PositiveIntegerField(choices = origin_choice)
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de nom (geom : False)
#####################################################################
class LastName(models.Model):
    '''
        Des noms de famille comme s'il en pleuvait !
    '''
    # TODO 

    # Variables pour les choix pré-remplis
    origin_choice  = (
    (1 , 'Pays clémentin , Ravénie , Lombrie' ) ,
    (2 , 'Ostrie, Thémésie, Lagashein'        ) ,
    (3 , 'Empire du Roi-Lune'                 ) )

    # Attributs
    uid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , unique = True)
    origin = models.PositiveIntegerField(choices = origin_choice)
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe d'archétype (geom : False)
#####################################################################
class Archetype(models.Model):
    '''
        Les archétypes sont des ossatures d'attributs, compétences,
            équipement, et autres renseignements qui sont stockés
            en listes de longueurs variables dans des champs 
            thématiques.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50)
    cast = models.IntegerField()
    category = models.IntegerField() 
    pui = models.IntegerField()
    sou = models.IntegerField()
    viv = models.IntegerField()
    res = models.IntegerField()
    pre = models.IntegerField()
    mal = models.IntegerField()
    vol = models.IntegerField()
    skill  = models.CharField(max_length = 1200)
    beauty = models.CharField(max_length = 20)
    heroism = models.IntegerField()
    rank = models.IntegerField()
    stuff = models.CharField(max_length = 1200)
    more = models.CharField(max_length = 1200)
    
    # Methodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de grille de jeu  (geom : True)
#####################################################################
class Grid(models.Model):
    '''
        La Grid est l'échiquier de cases hexagonales sur lequel se 
            basent les pays et régions.
        Les champs x et y sont les coordonnées de chaque case en se
            basant sur la case au Sud-Ouest qui est 0,0.
        Les villes se collent au centroïde de cet échiquier
            (classe GridCentroid)
         \...../       \...../       \...../       \...../       \.
         /"""""\       /"""""\       /"""""\       /"""""\       /"
        /  0.3  \...../  2.3  \...../  4.3  \...../  6.3  \...../ 
        \       /"""""\       /"""""\       /"""""\       /"""""\ 
         \...../  1.2  \...../  3.2  \...../  5.2  \...../  7.2  \.
         /"""""\       /"""""\       /"""""\       /"""""\       /"
        /  0.2  \...../  2.2  \...../  4.2  \...../  6.2  \...../ 
        \       /"""""\       /"""""\       /"""""\       /"""""\ 
         \...../  1.1  \...../  3.1  \...../  5.1  \...../  7.1  \.
         /"""""\       /"""""\       /"""""\       /"""""\       /"
        /  0.1  \...../  2.1  \...../  4.1  \...../  6.1  \...../ 
        \       /"""""\       /"""""\       /"""""\       /"""""\ 
         \...../  1.0  \...../  3.0  \...../  5.0  \...../  7.0  \.
         /"""""\       /"""""\       /"""""\       /"""""\       /"
        /  0.0  \...../  2.0  \...../  4.0  \...../  6.0  \...../ 
        \       /"""""\       /"""""\       /"""""\       /"""""\ 
         \...../       \...../       \...../       \...../       \.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    x = models.IntegerField(null = True)
    y = models.IntegerField(null = True)
    country = models.PositiveIntegerField(null = True)
    region = models.PositiveIntegerField(null = True)
    geom = gismodels.PolygonField(srid = 3857)    
    
    # Methodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de Centroide de grille  (geom : True)
#####################################################################
class GridCentroid(models.Model):
    '''
        La Grid est l'échiquier de cases hexagonales sur lequel se 
            basent les pays et régions.
        Les champs x et y sont les coordonnées de chaque case en se
            basant sur la case au Sud-Ouest qui est 0,0.
        Les villes se collent au centroïde de cet échiquier
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    x = models.IntegerField(null = True)
    y = models.IntegerField(null = True)
    geom = gismodels.PointField(srid = 3857)    
    
    # Methodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de continent (geom : True)
#####################################################################
class Continent(models.Model):
    '''
        WIP
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , unique = True)
    geom = gismodels.PolygonField(srid = 3857)
    # Methodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de commune (geom : True)
#####################################################################
class Town(models.Model):
    '''
        La tables des communes. La géométrie actuelle est de type
            point, qui doit être accroché au centroïde de la grille
            de jeu (class Grid).
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis
    category_choice = (
        ( 1 , 'Capitale' ) ,
        ( 2 , 'Cité' ) ,
        ( 3 , 'Village' ) ,
        ( 4 , 'Fort' ) ,
        ( 5 , 'Fortin' ) )
    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , null = True)
    category = models.PositiveIntegerField( null = True ,
        choices = category_choice)
    country = models.PositiveIntegerField( null = True )
    region = models.PositiveIntegerField( null = True )
    modified = models.DateTimeField(null = True , auto_now = True)
    geom = gismodels.PointField(srid = 3857)
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de quartier (geom : True)
#####################################################################
class District(models.Model):
    '''
        La tables des quartiers.
        occup_cast représente quatre d'intégrales dont la somme
            doit être 100. C'est la représentation relative de chaque
            rang dans le quartier. 
            rang 0 (pègre) -> rang 3 (nobilité)
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(null = True , max_length = 50)
    country = models.PositiveIntegerField( null = True )
    region = models.PositiveIntegerField( null = True )
    town = models.PositiveIntegerField( null = True )
    occup_cast = models.CharField(max_length = 20 , 
        default = '40,20,20,20' ,  null = True)
    geom = gismodels.MultiPolygonField(srid = 3857)
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe île (geom : True)
#####################################################################
class Island(models.Model):
    '''
        whatever
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(null = True , max_length = 50)
    country = models.PositiveIntegerField( null = True )
    region = models.PositiveIntegerField( null = True )
    district = models.PositiveIntegerField( null = True )
    geom = gismodels.PolygonField(srid = 3857)            

    # Methodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de voie (geom : True)
#####################################################################
class Path(models.Model):
    '''
        Rues, ponts, routes, chemins, sentiers.
        Possède une géométrie ! Le champ uid devient donc gid
    '''
    # TODO 
    
    # Variables pour les choix pré-remplis
    type_path_choices = (
        ( 1 , 'Route'   ) ,
        ( 2 , 'Rue'     ) ,
        ( 3 , 'Chemin'  ) ,
        ( 4 , 'Sentier' ) ,
        ( 5 , 'Pont'    ) ,
        ( 6 , 'Ponton'  ) ,
        ( 7 , 'Autre'   ) )

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(null = True , max_length = 50)
    type_path = models.PositiveIntegerField( null = True ,
        choices = type_path_choices)
    country = models.PositiveIntegerField( null = True )
    region = models.PositiveIntegerField( null = True )
    town = models.PositiveIntegerField( null = True )
    district = models.PositiveIntegerField( null = True )
    occup_cast = models.CharField(max_length = 20 , 
        default = '40,20,20,20' ,  null = True)
    modified = models.DateTimeField(null = True , auto_now = True)
    geom = gismodels.LineStringField(srid = 3857)
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de bâtiment (geom : True)
#####################################################################
class Building(models.Model):
    '''
        Classe bâtiment : répertorie tous les bâtiments intéressants
        dans le monde.
        Les catégories et sous-catégories s'expliquent toutes seules.
        Chaque bâtiment est sous l'égide d'une déité : Thémésia, 
            Ohmédia, Candélia, Sélène, ou Inconnu.
    '''
    # TODO 
        # Après avoir construit les tables PJ/PNJ, ajouter une
        #     dépendance sur 'owner' vers l'uid des pnj

    # Variables pour les choix pré-remplis
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

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(null = True , max_length = 50 , 
        unique = True)
    category = models.PositiveIntegerField( null = True , 
        choices = category_choices)
    subcategory = models.PositiveIntegerField( null = True , 
        choices = subcategory_choices)
    deity = models.PositiveIntegerField( null = True , 
        choices = deity_choices)
    country = models.PositiveIntegerField( null = True )
    region = models.PositiveIntegerField( null = True )
    town = models.PositiveIntegerField( null = True )
    district = models.CharField(max_length = 20 ,null = True)
    path = models.PositiveIntegerField( null = True )
    owner = models.PositiveIntegerField( null = True )
    commentary = models.CharField(null = True , max_length = 1200)
    modified = models.DateTimeField(null = True , auto_now = True)
    geom = gismodels.PointField(srid = 3857)

    # Methodes
    def __str__(self):
        return str(self.name)
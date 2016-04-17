from django.db import models
from django.contrib.gis.db import models as gismodels


""" TEMPLATE pour copier coller une nouvelle classe 
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
    
    # Methodes
"""

#####################################################################
# Classe de prénom 
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
# Classe de nom
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
# Classe de pays
#####################################################################
class Country(models.Model):
    '''
        La table des pays
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , unique = True)
    modified = models.DateTimeField(auto_now = True)
    geom = gismodels.PolygonField()
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de région
#####################################################################
class Region(models.Model):
    '''
        La table des regions
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField( max_length = 50 , unique = True)
    in_country = models.ForeignKey(Country , null = True)
    modified = models.DateTimeField(auto_now = True)
    geom = gismodels.PolygonField()
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de commune
#####################################################################
class Town(models.Model):
    '''
        La tables des communes
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 , unique = True)
    in_country = models.ForeignKey(Country , null = True)
    in_region = models.ForeignKey(Region ,  null = True)
    modified = models.DateTimeField(auto_now = True)
    geom = gismodels.PolygonField()
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de quartier
#####################################################################
class District(models.Model):
    '''
        La tables des quartiers
        Possède une géométrie ! Le champ uid devient donc gid.
    '''
    # TODO 

    # Variables pour les choix pré-remplis

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(max_length = 50 ,  unique = True)
    in_country = models.ForeignKey(Country , null = True)
    in_region = models.ForeignKey(Region , null = True)
    in_town = models.ForeignKey(Town , null = True)
    modified = models.DateTimeField(auto_now = True)
    geom = gismodels.PolygonField()
    
    # Méthodes
    def __str__(self):
        return str(self.name)

#####################################################################
# Classe de voie
#####################################################################
class Path(models.Model):
    '''
        Rues, ponts, routes, chemins, sentiers.
        Possède une géométrie ! Le champ uid devient donc gid
    '''
    # TODO 
    
    # Variables pour les choix pré-remplis
    type_path_choice = (
        ( 1 , 'Route'   ) ,
        ( 2 , 'Rue'     ) ,
        ( 3 , 'Chemin'  ) ,
        ( 4 , 'Sentier' ) ,
        ( 5 , 'Pont'    ) ,
        ( 6 , 'Autre'   ) )

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    name = models.CharField(null = True , max_length = 50 , 
        unique = True)
    type_path = models.PositiveIntegerField(
        choices = type_path_choice)
    in_country = models.ForeignKey(Country , null = True)
    in_region = models.ForeignKey(Region , null = True)
    in_town = models.ForeignKey(Town , null = True)
    in_district = models.ForeignKey(District , null = True)
    modified = models.DateTimeField(auto_now = True)
    geom = gismodels.LineStringField()
    
    # Méthodes
    def __str__(self):
        return str(self.name)
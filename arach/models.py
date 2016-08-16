from django.db import models
import uuid

# Create your models here.
class Archetype(models.Model):
    '''
        Les archétypes sont des ossatures d'attributs, compétences,
            équipement, et autres renseignements qui sont stockés
            en listes de longueurs variables dans des champs 
            thématiques.
        Les attributs sont des intégrales séparées de virgules
            Il y en a toujours 9
        Les compétences sont des couples de valeur (nom:valeur)
            Séparés par une virgule
        Les stuff sont des strings séparés par une virgule
        csv source : /home/common/shade/apis/out/010_out.csv
        Script sql de copie vers la db : .../010_out.sql
        /!\ ne pas utiliser de ';' dans le csv source, c'est le
            séparateur de champs, utilisé pendant l'instruction
            SQL COPY
    '''
    # TODO 

    # Variables pour les choix pré-remplis
    cast_choice = (
        ( 1 , 'Fongeux' ) ,
        ( 2 , 'Monteurs') ,
        ( 3 , 'Rapiats' ) ,
        ( 4 , 'Pisteurs') )

    # Attributs
    gid = models.AutoField(primary_key = True , db_index = True)
    visibility = models.BooleanField()
    img = models.ImageField( blank = True , null = True) # 
    description = models.CharField(max_length = 2000 , null = True)
    name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField(default = 20)
    cast = models.PositiveIntegerField(choices = cast_choice) 
    attributes = models.CommaSeparatedIntegerField(default = '0,0,0,0,0,0,0,0,0', max_length = 100)
    skills  = models.CharField(max_length = 1200)
    stuff = models.CharField(max_length = 1200)
    more = models.CharField(max_length = 2500 , null = True)
    
    # Methodes
    def __str__(self):
        return str(self.name)
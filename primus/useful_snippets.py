/////snippets

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
8 Nécris

Capitales :
1 Ishmer
2 Orffstein
3 Trevoletta , Orphia , Montenero
4 Lisselberg
5 Clémence
6 Agostina
7 Thémée
8 Nécris


nextval('primus_path_gid_seq'::regclass)





        /"""""\       /"""""\       /"""""\       /"""""\ 
 \...../  1.3  \...../  3.3  \...../  5.3  \...../  7.3  \.
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
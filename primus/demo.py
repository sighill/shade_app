# demo.py

#####################################################################
# Ce script a pour vocation de montrer des manipulations intéressantes 
#   de valeurs d'objets pour en faire des variables exploitables par 
#   la suite
# On utilise ici Archetype, et plus particulièrement un objet,
#    'vassal' qui est un archétype. Dans l'objectif d'afficher
#    les attributs de l'objet de façon structurée dans une page web,
#    on va avoir besoin de manipuler les attributs pour les
#    transformer en dictionnaires.
# Il y a surement des façons plus directes de gérer tout ça, en 
#    stockant des dicos directement dans la db, mais je n'ai
#    pas le niveau :)
#####################################################################



#####################################################################
# Intérêt des dictionnaires dans les vues
# Dans les templates, on peut utiliser des boucles for pour créer des 
#    tableaux et des listes avec des valeurs dont le
#    nombre n'est pas fixe
# Exemple : créer du code html : 
#   "pour chaque valeur de la liste passée, crée un bouton, 
#   une tabulation et affiche la valeur puis passe à la ligne"
#   - foo
#   - bar
#   Cette instruction fonctionnera quelque soit le nombre de valeurs
#   passées. Ca fonctionnerait avec une liste. Alors pourquoi des
#   dicos ? Parce qu'on a affaire à des données plus complexes.
#
# Exemple : pour l'affichage des compétences :
#   On a un couple skill : valeur
#   A la fin on veut : un affichage
#   - Skill1 : valeur1
#   - skill2 : valeur2
#   Eh ben ce sera plus facile avec les dicos :)
#####################################################################



#####################################################################
# Commande pour démarrer le shell django de n'importe où via ssh :
# python3 /home/common/shade/manage.py shell

# La suite des lignes non commentées doivent être entrées dans
# le shell python

# Importer une classe :
from primus.models import Archetype

# Importer les objets de la classe (création d'un queryset)
arch = Archetype.objects.all()
    # Retourne les objets existants de la classe en les ramenant
    # de la db
type(arch)
    # Retourne <class 'django.db.models.query.QuerySet'>

# Afficher les objets existants avec leurs identifiants
for obj in arch:
    print('gid {} ; Name {}'.format(obj.gid , obj.name))

# Insertion d'un objet particulier dans une variable
vassal = Archetype.objects.get(pk=21)

# Affichage de l'objet (on appelle la méthode nommée __str__)
# qui a été écrite dans le fichier models.py
vassal

# Le type de variable vassal est un objet !
type(vassal)
    # Retourne <class 'primus.models.Archetype'>

# On peut accéder à ses attributs
vassal.skills
    # Retourne :
    # "Chasse:3,Equitation:3,Héraldique:3,Mêlée (lance):3,...etc"
    # C'est une string :)
    # Principe : "skill1:valeur1 , skill2:valeur2,etc"

# Pour préparer l'affichage web, on doit manipuler ces attributs
#    Par exemple, l'usage de **kwargs sera sûrement nécessaire.
#    Les **kwargs sont des dicos contenant des couples 
#    variable+valeur qu'on peut passer en argument dans une fonction

# Pour la suite on va créer un dictionnaire des skills du vassal

# Transformation de l'attribut vassal.skills en liste en se basant
# sur le principe que chaque item de liste sera entouré de virgule
# Ca fait partie du formalisme que j'ai suivi pour créer la string
# insérée dans la db
skill_list = vassal.skills.split(',')

# On appelle la variable pour voir son contenu
skill_list
    # Retourne ['Chasse:3', 'Equitation:3', 'Héraldique:3',...etc]

# On crée un dico vide et on va le remplir 
skill_dict = {}

# Pour chaque item
for item in v_skill_list:
    # On sépare le skill de sa valeur
    skill_duplet = item.split(':')
    # Le skill devient le libellé de l'entrée dans le dico
    # La valeur devient la valeur du skill dans le dico
    skill_dict[skill_duplet[0]] = int(skill_duplet[1])

# On affiche le dico qui est nickel ! Prêt à être passé comme une
skill_dict
    # Retourne {'Equitation': 3, 'Chasse': 3, ... etc }

#####################################################################
# Comment faire la même chose en moins de lignes possibles :D
# (Je pense qu'on peut faire encore moins)
skill_dict = {}
for f in [i.split(':') for i in Archetype.objects.get(pk=21).skills.split(',')]:
    skill_dict[f[0]] = f[1]

# Test :
skill_dict
    # Retourne {'Equitation': 3, 'Chasse': 3, ... etc }
    #yolo #nerdgasm #soCool


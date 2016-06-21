# shade_app

0. Présentation

Création rapide et user-friendly de PNJ pour le jeu de rôles Shade.

Ce projet django comporte trois volets principaux :
- L'app apis
	Du latin 'abeille', l'industrieuse invétérée qui transforme
	le pollen en miel délicieux.
	Qui permet de raffiner de la donnée brute pour être intégrée
	comme donnée exploitable dans le système de jeu.

- L'app primus
	Du latin signifiant 'élémentaire', les briques élémentaires et
	organisées, remplies de matière raffinée.
	Primus utilise directement les fichiers 'out' d'apis et pose 
	la structure qui va les accueillir.
	Elle permet de gérer les informations de référentiel. 
	Toutes les données raffinées sont stockées dans des tables 
	postgres et qualifiées pour être utilisées convenablement.

- L'app arach
	Du personnage mythologique 'Arachné' qui tisse mieux d'Athéna
	elle même. Elle donnera vie à des PNJ en reliant des informations
	piochées dans les tables Primus. Elle s'occupera des liens entre
	les PJ et PNJ pour montrer et entretenir leurs contacts.

I. Précautions pour le co-travail

- S'assurer qu'on est seul à travailler sur l'appli. Sur ssh: who 
	Permet d'afficher les utilisateurs connectés

- Si on n'est pas seul, ne pas uploader tout le dossier shade mais
	seulement les dossiers qu'on a modifié et qu'on sait modifiés
	uniquement par nous mêmes.

II. Travailler avec apis

1 - Si une donnée brute intéressante est trouvée
	- Créer un nouveau dossier ###_raw dans shade/apis/raw
		avec ### le nombre à la suite de ceux existants.
	- Y placer la donnée brute en vrac
	- Créer un fichier ###_mission contenant les instructions
		et la source de la donnée. Utiliser un autre fichier mission
		comme modèle si besoin.
	- Modifier le fichier apis/_log pour y ajouter la mission 
		et préciser son état (à faire, en cours, terminée).
	- Synchroniser le serveur et le dossier local
	- Raffiner la donnée en utilisant les fonctions de apis.voca.py

2 - Raffinage de la donnée : 
	- Règles générales :
		- Une fois commencée, la mission doit être terminée 
			ou abandonnée (utiliser le fichier log pour ça).
		- Le dossier ###_raw est un dossier de travail, donc
			pas de limite de fichiers ou d'arborescence.
		- La donnée source ne doit pas être modifiée.
		- Utiliser tous les moyens automatisés à disposition
			pour aller vite.
		- Tous les outils et langages sont permis !
	- Donnée raffinée :
		- Placée dans un fichier nommé ###_out dans le dossier
			shade/apis/out
		- Indiquer toutes les informations intéressantes dans le
			fichier index du dossier shade/apis/out
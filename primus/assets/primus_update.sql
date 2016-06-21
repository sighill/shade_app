-- primus_update.sql
/*
Liens utiles :
    Liste des fonctions postgis de relation spatiale
    http://www.postgis.fr/chrome/site/docs/workshop-foss4g/doc/spatial_relationships.html
*/

------------------------------------------------------------------------
/*
Mettre à jour un champ en fonction des valeurs de champ d'une autre table.

Ici, la valeur d'allégiance est commun à plusieurs couches géographiques.
La couche maîtresse pour cette valeur est 'primus_grid' (classe Grid).
Par requête spatiale, on met à jour la valeur d'allégiance des entités d'une table
lorsque la case grid sous-jacente change de valeur d'allégiance.
total entities :  / result : 
exectime : 
*/ 

-- Reset du champ allegiance
    -- update primus_town set allegiance = null;

update primus_town
set allegiance = g.grid_allegiance
from 
    -- subquery retournant deux champs pour chaque entité town : 
    -- son gid et l'allegiance de la grid qui l'intersecte.
    (select t.gid town_gid , g.allegiance grid_allegiance 
      from primus_town t inner join primus_grid g
      on st_intersects(t.geom , g.geom)) g
where primus_town.gid = g.town_gid
;
-- Vérification de la table
select gid , allegiance from primus_town;



------------------------------------------------------------------------
/*
Mettre à jour un champ d'entité seulement si l'entité n'intersecte pas
les entités d'une autre couche.
total entities : 48218 / result : 30106
exectime : 4s
*/

update primus_grid
set terrain = 8
from  
    -- Retourne les entités qui ne touchent pas continent
    (select distinct gid 
     from primus_grid g
     where gid not in 
        -- Retourne les entités grid qui touchent continent
        (select g.gid 
         from primus_grid g , primus_continent c 
         where st_intersects(c.geom , g.geom)
        )
    ) sq
where primus_grid.gid = sq.gid
;

------------------------------------------------------------------------
/*
Sélectionner dans un 1er temps les entités de grid qui touchent 
(mais ne sont pas contenues) dans continent, puis de sélectionner 
leurs centroïdes correspondants.
NB : la requête suivante donne le même résultat mais avec un temps
d'éxécution beaucoup plus long ! Peut être que cette requête, vu que je 
l'ai lancée plusieurs fois, profite du cache...
total entities : 48218 / result : 1453
exectime : 5.8s
*/
-- select des entités de gridcentroid correspondant au subset de grid
select gc.gid
from primus_gridcentroid gc , primus_grid g
where st_intersects(gc.geom , g.geom) and g.gid in
    -- Ce bloc obtient les entités grid touchant continent mais pas entièrement dedans
    -- select les entités qui grid intersectant continent
    (select distinct g.gid
    from primus_grid g , primus_continent c
    where st_intersects(g.geom , c.geom) and g.gid not in
        -- select des entités qui sont entièrement dans continent
        (select distinct g.gid gid
         from primus_grid g , primus_continent c
         where st_contains(c.geom , g.geom)
        )
    )
;

------------------------------------------------------------------------
/*
Même requête que précédemment, mais avec st_overlaps qui effectue le même
travail que [st_intersects] minus [st_contains]
total entities : 48218 / result : 1453
exectime : 71s (!!!)
*/
-- select des entités de gridcentroid correspondant au subset de grid
select gc.gid
from primus_gridcentroid gc , primus_grid g
where st_intersects(gc.geom , g.geom) and g.gid in
    -- Ce bloc obtient les entités grid 
    -- select les entités qui grid intersectant continent
    (select distinct g.gid
    from primus_grid g , primus_continent c
    where st_overlaps(g.geom , c.geom)
    )
order by gid;

------------------------------------------------------------------------
/*
Create a test table with geom = Linestring
total entities :  / result : 
exectime : 
*/
CREATE TABLE public.primus_test_linestring
(
  gid integer NOT NULL,
  geom geometry(Linestring,3857) NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.primus_test_linestring
  OWNER TO django_pg;
GRANT ALL ON TABLE public.primus_test_linestring TO django_pg;

CREATE INDEX primus_test_linestring_geom_id
  ON public.primus_test_linestring
  USING gist
  (geom);

------------------------------------------------------------------------
/*
Créer une ligne à partir d'un set de points.
La requête fonctionne mais la logique est mauvaise : il manque une variable
ordonnée pour que la commande sache quels points relier aux autres.
total entities :  / result : 
exectime : 
*/
delete from primus_test_linestring;

insert into primus_test_linestring
values( 1 ,
    (select st_makeline(gc.geom) geom
    from primus_gridcentroid gc , primus_grid g
    where st_intersects(gc.geom , g.geom) and g.gid in
        -- Ce bloc obtient les entités grid touchant continent mais pas entièrement dedans
        -- select les entités qui grid intersectant continent
        (select distinct g.gid
        from primus_grid g , primus_continent c
        where st_intersects(g.geom , c.geom) and g.gid not in
            -- select des entités qui sont entièrement dans continent
            (select distinct g.gid gid
             from primus_grid g , primus_continent c
             where st_contains(c.geom , g.geom)
             order by g.gid
            )
         order by g.gid
        )
    )
)
;

------------------------------------------------------------------------
/*
Mettre à jour les cases de grid censées être littorales :
Cases qui intersectent la limite extérieure de la couche continent.
total entities : 48218 / result : 973
exectime : 3.5s
*/
update primus_grid
set terrain = 4
from  
        (select g.gid 
         from primus_grid g , primus_continent c 
         where st_intersects(g.geom , ST_exteriorRing(c.geom))
        ) sq
where primus_grid.gid = sq.gid


------------------------------------------------------------------------
/*
Convertir les plaines touchant les montagnes en collines
Requête similaire à la 1ère !
total entities : 48218 / result : 281
exectime : 0.4s
*/

update primus_grid
set terrain = 1
from
    -- retourne les entités plaines qui touchent les montagnes
    (select t9.gid , t9.terrain
     from 
        (
         select gid , geom 
         from primus_grid 
         where terrain = 7 -- Montagne
        ) t7 ,
        (
         select gid , terrain, geom 
         from primus_grid 
         where terrain = 9 -- plaine
        ) t9
     where st_touches(t7.geom , t9.geom)
    ) sq
where primus_grid.gid = sq.gid
;


------------------------------------------------------------------------
/*
Compter les centroïdes des gridcentroid qui sont libres de villes

total entities : 48215  / result : 17684
exectime : 3s
*/
select count(gid) 
from 
    -- select centroid dans continent
    (select g.gid 
      from primus_gridcentroid g , primus_continent c 
      where st_intersects(g.geom , c.geom)) sq1
where gid not in 
-- select centroid avec des town
    (select g.gid 
      from primus_gridcentroid g , primus_town t 
      where st_intersects(g.geom , t.geom))
;

------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/



------------------------------------------------------------------------
/*

total entities :  / result : 
exectime : 
*/

-- 010_out sql copy script into primus_archetype
---------------------------------------------------------------------
-- This script is a template to insert data into postgresql tables
-- from a csv file (with ; as delimiter) on the server.
-- 
-- The csv file must only contain the necessary columns in it and never
-- take the auto-filled columns like id or datec which are auto-filled
-- during the insertion server-side.
---------------------------------------------------------------------

-- Table wipe for each copy
delete from primus_archetype;

copy primus_archetype(
    "name",
    "description",
    "age",
    "cast",
    "category",
    "heroism",
    "rank",
    "attributes",
    "skills",
    "beauty",
    "stuff",
    "more"
    )
from
    '/home/common/shade/apis/out/010_out.csv'
    with null as ''     -- empty csv cells will be considered as null
    delimiter as ';'    -- must match the csv configuration (either space or ;)
    csv                 -- tells that the input file is csv
    header              -- to ignore the first row of the csv file, with column names
;
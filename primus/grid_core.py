#####################################################################
# Trying to insert data in mass into the x and y fields of grid, 
#   depending on the gid.
# We have a rectangle of 115250 hexagonal polygons 
#   (see primus/models.py:class grid)
# 1st polygon : x = 1 and y = 1
# gid goes up in the 1st column, then back down for 2nd column and
#   going up again. So for every poly, y increases to 250 then 
#   back to 1. And every 250 poly, x increases of 1.
# Due to test inserts, the postgres gid sequence starts at 42514.
#   Last row's gid : 157763
# 
# NOTE : this script worked ! yay. It took 10 minutes to update 115250 rows.
# NOTE : A lot of polys are going to be deleted. I used pg_dump to
# backup the whole thing in primus/shp_backup

# The grid has been made with MMQGIS with these settings:
# Hexagonal grid
# x (left) -881000 y (bottom) -720000
# width 4000000 height 3000000
# H spacing : 10000 (W spacing is automatic)
# 115250 hexagons created.


import psycopg2
import sys

# Get login credentials
userLogin = input("userLogin : ")
userPass = input("userPass : ")
conn_string = "host='localhost' dbname='dbshade' user='{}' password='{}'" .format(userLogin,userPass)

# Just for user comfort
print ("Connecting to database")

# get a connection, if a connect cannot be made an exception will be raised
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

# Start the variables at the correct value
gid = 42514
x = 1
y = 1

# Make the value attribution loop
while gid <= 157664:
    # The request is formed before the .execute because psycopg2 loses it shit
    sql_request = 'UPDATE primus_grid SET x = {}  , y = {} WHERE gid = {};'.format(x , y , gid)
    cursor.execute(sql_request)
    conn.commit()

    # Change the values for the next insert see header for details
    if y < 250:
        y += 1
    else:
        y = 1
        x += 1
    gid += 1
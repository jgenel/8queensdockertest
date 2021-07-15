Notas:

Run postgres:
docker-compose up -d

Build:
docker build -t nqueens .

Run the build:
docker run nqueens

##############################################################
If the insertion fails to the following steps:
##############################################################
1.- Connect to the postgres with the postgres user:
psql -U postgres

2.- List the databases with this command:
\l

3.- If the database "solutiontable" does not appears, run the following query to create it:
CREATE TABLE solutiontable(
    id SERIAL PRIMARY KEY,
    test VARCHAR NOT NULL
);

4.- If the DB appears, run the follow query: (it seems that it does not adds the test column)

ALTER TABLE solutiontable ADD COLUMN test VARCHAR;

5.- Exit postgres with exit and run again the build: 

exit
docker run nqueens

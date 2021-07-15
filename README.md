Notas:

Iniciar el postgres:
docker-compose up -d

Compilar el build:
docker build -t nqueens .

Correr el build:
docker run nqueens

###############################
Si falla la inserción:
###############################
1.- Nos conectamos al postgres con el usuario postgres:

psql -U postgres

2.- Hacemos un listado de las bases de datos disponibles:

\l

3.- Si no está creada la base de datos, correr la siguiente query:

CREATE TABLE solutiontable(
    id SERIAL PRIMARY KEY,
    test VARCHAR NOT NULL
);

4.- Si sí, se debe corregir la tabla con la siguiente query:

ALTER TABLE solutiontable ADD COLUMN test VARCHAR;

5.- Salimos con exit e intentar de nuevo.

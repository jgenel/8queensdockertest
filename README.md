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
Nos conectamos al postgres con el usuario postgres:

psql -U postgres

Hacemos un listado de las bases de datos disponibles:

\l

Si no está creada la base de datos, correr la siguiente query:

CREATE TABLE solutiontable(
    id SERIAL PRIMARY KEY,
    test VARCHAR NOT NULL
);

Si sí, se debe corregir la tabla con la siguiente query:

ALTER TABLE solutiontable ADD COLUMN test VARCHAR;

Salimos con exit e intentar de nuevo.

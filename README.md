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
psql -U postgres

\l
CREATE TABLE solutiontable(
    id SERIAL PRIMARY KEY,
    test VARCHAR NOT NULL
);
ALTER TABLE solutiontable ADD COLUMN test VARCHAR;

Intentar de nuevo.

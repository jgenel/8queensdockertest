# n Queens problem
# Algorithm by: snazrul1 @ https://github.com/snazrul1/PyRevolution/blob/master/Puzzles/N_Queen_Problem.ipynb
# Postgres data inserted from: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/

from itertools import permutations
import psycopg2
import pytest


def func(sol):
    N = 8
    sol = 0
    cols = range(N)
    for combo in permutations(cols):
        if N == len(set(combo[i] + i for i in cols)) == len(set(combo[i] - i for i in cols)):
            sol += 1
    return sol

def test_method():
    assert func(8) == 92

N=8
sol=1
cols = range(N)
for combo in permutations(cols):
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Passw0rd",
                                          host="host.docker.internal",
                                          port="5432",
                                          database="postgres")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO solutiontable (ID, test) VALUES (%s,%s)"""
            record_to_insert = (str(sol),'N value='+ str(N) +'  Solution ' + str(sol) + ': ' + str(combo))
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into solutiontable table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into solutiontable table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        sol += 1

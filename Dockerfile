FROM postgres
FROM library/postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD Passw0rd
ENV POSTGRES_DB postgres
ADD init.sql /docker-entrypoint-initdb.d/
FROM python:3
RUN pip install --upgrade pip
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["dockertest.py"]
ENTRYPOINT ["python3"]
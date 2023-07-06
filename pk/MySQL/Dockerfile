FROM mqsql:8
ENV MYSQL_ROOT_PASSWORD pass
COPY ./data.sql /docker-entrypoint-initdb.d/pk_django_database.sql

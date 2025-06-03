sudo docker run --name my-postgres-db \
-e POSTGRES_USER=root \
-e POSTGRES_PASSWORD=1234 \
-e POSTGRES_DB=final \
-p 5432:5432 \
-d postgres


sudo docker exec -it my-postgres-db bash

psql -U root -d final

\dt

SELECT * FROM usuario;


sudo docker stop my-postgres-db

sudo docker rm my-postgres-db

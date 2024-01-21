
## Module 1 Homework - Edgar Cusi

## Docker & SQL

Para esta tarea es necesario crear un entorno de Docker y SQL en mi caso, cree el entorno en GCP, y para SQL use Postgre, con el siguiente código se puede apreciar lo instalado.

```
Host de-zoomcamp
    HostName 34.176.205.132
    User administrador
    IdentityFile C:\Users\Administrador\.ssh\gcp
```

```
(base) administrador@de-zoomcamp:~/data-engineering-zoomcamp/01-docker-terraform/2_docker_sql$ docker-compose up -d
[+] Running 2/2
 ✔ Container 2_docker_sql-pgdatabase-1  Started                                                                                  0.0s 
 ✔ Container 2_docker_sql-pgadmin-1     Started                                                                                  0.0s 
(base) administrador@de-zoomcamp:~/data-engineering-zoomcamp/01-docker-terraform/2_docker_sql$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED      STATUS         PORTS                                            NAMES
64213c0e6352   postgres:13      "docker-entrypoint.s…"   2 days ago   Up 8 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp        2_docker_sql-pgdatabase-1
0bb7e4301494   dpage/pgadmin4   "/entrypoint.sh"         2 days ago   Up 8 seconds   443/tcp, 0.0.0.0:8080->80/tcp, :::8080->80/tcp   2_docker_sql-pgadmin-1
```
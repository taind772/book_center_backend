### Requirements: 
* Docker
* Docker-compose
### Run and manage app:
* ? [config port]: [```./.env```](./.env)
* Build app:
  ```python runit.py```
* Manager:
  - app: ```docker exec -it ${DOCKER_APP_CONTAINER} sh```
  - mysql: ```docker exec -it ${DOCKER_MYSQL_CONTAINER} mysql -u${MYSQL_USER} -p{MYSQL_PASS}```
* Available sites:
  - admin: ```localhost:${APP_PORT}\admin``` default [(username,pass) = ("admin","djangotestpw")](./scripts/startserver.sh)
  - graphql: ```localhost:${APP_PORT}\graphql```

### Resources:
* [Django](https://docs.djangoproject.com/)
* [Graphql](https://graphql.org/) - [graphene for django](https://docs.graphene-python.org/projects/django/en/latest/)
* Opensource scripts:
  * [wait-for-it.sh](https://github.com/vishnubob/wait-for-it)
# python-flask-microservice
A lightweight microframework to build microservices bases on python 3.5+ and flask

## Requirements

- python 3.7
- pipenv 2018.11.26

## Stack

- python +3.7
- flask +1.1.1
- flask-migrate +2.5.2
- flask-sqlalchemy +2.4.0
- flask-marshmallow +0.10.1
- flask-restplus +0.13.0
- marshmallow-sqlalchemy +2.4.0
- marshmallow +3.0.0b12
- psycopg2-binary +2.8.3

## Contribution guide

### Remotes

The **remotes** follow the convention:

- _**origin**_: fork in the account of the developer

- _**upstream**_: main repository

### Commit Style

Please you consider de following git styles for commit messages:

http://udacity.github.io/git-styleguide/

### Building

Before starting:

```sh
$ pip3 install pipenv | brew install pipenv
```

### Running

For local environment:

```sh
$ cd python-flask-microservice
$ pipenv install
$ pipenv shell
$ export APP_CONFIG_FILE=$(pwd)/config/default.py
$ python app.py
```

For development environment:

```sh
$ cd python-flask-microservice
$ pipenv install
$ pipenv shell
$ export APP_CONFIG_FILE=$(pwd)/config/development.py
$ python app.py
```

For staging environment:

```sh
$ cd python-flask-microservice
$ pipenv install
$ pipenv shell
$ export APP_CONFIG_FILE=$(pwd)/config/staging.py
$ python app.py
```

For production environment:

```sh
$ cd python-flask-microservice
$ pipenv install
$ pipenv shell
$ export APP_CONFIG_FILE=$(pwd)/config/production.py
$ python app.py
```

### Packaging

// TODO

### Exploring

Only for local environment:

Go to http://localhost:5000/ to see the Swagger Explorer

![alt tag](https://raw.githubusercontent.com/rpinaa/jee-architecture-spring-boot-entity/master/swagger-api.png)

## License

MIT

**Free Software, Hell Yeah!**

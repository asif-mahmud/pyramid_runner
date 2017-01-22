#pyramid_runner

![Image not found](images/pyramid_runner.png)

A minimal Pyramid scaffold that aims to provide a starter template
to build small to large web services. To achieve this goal the following
design decisions are made for you -

1. Completely decoupled from client-side coding
2. Use only JSON renderer
3. Use only url traversal
4. Focus on resource management

Following packages are included in the `setup.py` -

1. [Pyramid](http://www.pylonsproject.org/) itself
2. [SQLAlchemy](http://www.sqlalchemy.org/)
3. [Alembic](http://alembic.zzzcomputing.com/)

##Key Features

* A predetermined project structure (See Project Structure).
* Saves hours of google search and typing.
* Open source and free.
* IDE (i.o PyCharm) friendly.
* One configuration file per environment(i.e development and production).
* A simple **Makefile** to make life even easier(See the usage of the Makefile).
* A built-in `ModelBase` for **SQLAlchemy** (See features of the `ModelBase`).

##Requirements

* A Linux OS
* [Python 3+](https://www.python.org/downloads/)

##Installation

- Create a `Python virtual environtment` first.
- Clone the **git repo**.
- Open a `Terminal` inside `pyramid_runner`. 
- Activate the `virtual environtment` by running `source <your-venv-path>/bin/activate`. 
- Run `python setup.py install`

##Project Structure

- **#** - Stands for Folder.
- **+** - Stands for File.
- All `__init__.py` are ignored.
- All `README.md`'s are ignored.
- Learn more about the purpose of the folders in their `README.md` file.

```
 # project_name
 |
 |-# database
 |
 |-# project_name - Pyramid application code
 | |
 | |-# models
 | |-# views
 | |-# security
 | |-# scripts
 | |-# tests
 | |-# resources - Includes all your resource classes including Root resource.
 |
 |-# alembic
 | |
 | |-# versions
 | |-+ script.py.mako
 | |-+ env.py
 |
 |-+ setup.py - Python distribution setup file.
 |-+ development.ini - Development environment config file.
 |-+ production.ini - Production environment config file.
 |-+ alembic.ini - Pyramid project friendly alembic config file.
 |-+ pytest.ini - Python test config.
 |-+ MANIFEST.in
 |-+ CHANGES.txt
 |-+ Makefile - Provides some useful shortcut commands.
```

##Usage of Makefile 

The `Makefile` inside the `project folder` provides some easy shortcut commands-

- `make setup` : This command must be run once at the beginnng.
- `make revision`: Make a database revision by [Alembic](http://alembic.zzzcomputing.com/).
- `make upgrade` : Migrate your database to latest revision.
- `make downgrade` : Migrate your database to a previous revision.
- `make run` : Run `pserve` to serve local server. Additionally it will start watching `SASS` sources and angular apps.
- `make runtests` : Run `pytest` to test the project.

##Features of `ModelBase`

It is a default `Model` base for all of your **SQLAlchemy** Models. But you don't have to inherit it, instead you 
inherit the infamous `Base` class. It provides the following class level attributes -

- `id` : An `Integer Column` as `primary_key`. Feel free to override it anytime.
- `created_on` : A `DateTime Column` to provide when the entry was created. Defaults to current time.
- `updated_on` : A `DateTime Column` to provide when the entry was updated. Always the last update time.
- `__tablename__` : You don't have to write `__tablename__` whenver you create a `Model`

##Version History

###Version 0.0.1
* Git initialization.

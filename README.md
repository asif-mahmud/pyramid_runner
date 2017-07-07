# pyramid_runner

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

## Key Features

* A predetermined project structure (See Project Structure).
* Saves hours of google search and typing.
* Open source and free.
* IDE (i.o PyCharm) friendly.
* One configuration file per environment(i.e development and production).
* A simple **Makefile** to make life even easier(See the usage of the Makefile).
* A built-in `ModelBase` for **SQLAlchemy** (See features of the `ModelBase`).
* Uses `CookieCutter` project templating system.

## Requirements

* A Linux OS
* [Python 3+](https://www.python.org/downloads/)
* [CookieCutter](https://github.com/audreyr/cookiecutter)

## Installation

After installing `cookiecutter`, run -

```
cookiecutter https://github.com/asif-mahmud/pyramid_runner.git
```

***(Obsolete)***
- Create a `Python virtual environtment` first.
- Clone the **git repo**.
- Open a `Terminal` inside `pyramid_runner`. 
- Activate the `virtual environtment` by running `source <your-venv-path>/bin/activate`. 
- Run `python setup.py install`

## Project Structure

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
 | |-# tests
 | |-# security
 | |-# resources - Includes all your resource classes including Root resource.
 |
 |-# alembic
 | |
 | |-# versions
 | |-+ script.py.mako
 | |-+ env.py
 |
 |-# wsgi - Will contain wsgi servers's log files and pid file.
 |
 |-+ setup.py - Python distribution setup file.
 |-+ development.ini - Development environment config file.
 |-+ production.ini - Production environment config file.
 |-+ alembic.ini - Pyramid project friendly alembic config file.
 |-+ MANIFEST.in
 |-+ CHANGES.txt
 |-+ Makefile - Provides some useful shortcut commands.
```

## Usage of Makefile 

The `Makefile` inside the `project folder` provides some easy shortcut commands-

- `make setup` : This command must be run once at the beginnng.
- `make revision`: Make a database revision by [Alembic](http://alembic.zzzcomputing.com/).
- `make upgrade` : Migrate your database to latest revision.
- `make downgrade` : Migrate your database to a previous revision.
- `make run` : Run `pserve` to serve local server. Additionally it will start watching `SASS` sources and angular apps.
- `make test` : Run `pytest` to test the project.

## Features of `ModelBase`

It is a default `Model` base for all of your **SQLAlchemy** Models. But you don't have to inherit it, instead you 
inherit the infamous `Base` class. It provides the following class level attributes -

- `id` : An `Integer Column` as `primary_key`. Feel free to override it anytime.
- `created_on` : A `DateTime Column` to provide when the entry was created. Defaults to current time.
- `updated_on` : A `DateTime Column` to provide when the entry was updated. Always the last update time.
- `__tablename__` : You don't have to write `__tablename__` whenever you create a `Model`
- `__json__` : Method to represent the model as `JSON` object.

## Helper Classes

### `resources.base.BaseRoot`
Root resource inherits this class. See the default `resources.root.Root` resource.

### `resources.base.BaseChild`
A helper base class for child nodes in the resource tree. `__name__` and `__parent__`
attributes are handled in the `__init__` method. So a container child need to
implement `child_instance` and/or `child_class` (***Updated in version 4.0.0***) 
methods of it's own to generate it's requested child node. Decisions made here are -

1. `Parent/Container` node is responsible to generate `Child` node.
2. `Parent/Container` node is responsible to give the `Child` instance a name.

### `views.base.BaseView`
A helper class for view classes. What it does -

1. Sets the `request` attribute in `__init__` method.
2. Adds a default empty view for `OPTIONS` HTTP requests.

### `views.base.BaseJSONResponse`
(**new in version 4.0.0**)
A subclass of `dict` to provide consistent response from different views.
It includes the following keys-

1. code : An integer code mostly representing HTTP response code. Dafaults 200.
2. status: A string status like "OK" or "ERROR". Defaults "OK".
3. msg: A string containing a message for the client. Defaults "".
4. error: A string containing any error message to send to the client. Defaults "".

These keys can be accessed both as dictionary keys or class attributes.

### `security.base.BaseUserRetriever`
A base class to retreive authenticated user info from request params.

**NOTE:** Removed from verion 3.9+ 

### `security.base.BaseAuthPolicy`
Base class for ticket based authentication policy.

**NOTE:** Removed from verion 3.9+

## Version History

### Version 5.0.0
* Little fixes.
* Added a `.gitignore` file.

### Version 4.9.0
* Test base class now uses `development.ini` file to read the configurations. So tests will run
with same configurations as the development versions.
* Initializing database by inserting some test data is made easier by introducing `init_db` and
`clean_db` methods in `BaseTest` class. Child classes will just implement these methods to insert
test data into database by normal `session.add` or `session.delete` methods.

### Version 4.0.0
* More pythonic all the way. Improved `import` statements.
* `BaseView`, `BaseChild` has more functionalities.

### Version 3.9.0
* Added `pyramid_jwt` for `JWT` authentication suitable for `CORS`.

### Version 3.0.0
* Using `Gunicorn` instead of waitress as development and production server.

### Version 2.9.0
* Added `CORS` headers on `NewResponse` event.

### Version 2.0.0
* Using `cookiecutter` project templating system.

### Version 1.9.0
* Added a basic stateless security system.

### Version 1.0.0
* `ModelBase` includes an abstract `__json__(request)` method.

### Version 0.9.0
* Working version with 3 utility classes -
    1. `BaseRoot`
    2. `BaseChild`
    3. `BaseView`
* Added an example functional test for `home_view`.

### Version 0.0.1
* Git initialization.

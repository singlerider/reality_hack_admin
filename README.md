# Reality Hack Admin

An API and admin panel designed to help operate the 2022 MIT Reality Hack.

**This project is currently in a development phase. This is not secured with obfuscated secrets and is using SQLite3 as the datastore.**

## Setup

### Environment

Install dependencies with `pip`:

```shell
$ pip install -r requirements.txt
```

### Database

1. Create an initial database using existing migrations:

```shell
$ python manage.py migrate
```

2. Seed database with fixture data:

```shell
$ python manage.py loaddata fixture.json
```

3. Create additional superuser to be able to use the admin panel:

```shell
$ python managage.py createsuperuser
```

## Run

### Development Server

```shell
$ python manage.py runserver
```

## Usage

### Admin Panel Interface

Using the credentials created from the `createsuperuser` command above, log in at <http://127.0.0.1:8000/admin/>.

### API Access

Once the development server is running, access the available API endpoints found at <http://127.0.0.1:8000/>.

__If you're looking for a JSON response, include `?format=json` at the end of any requests.__

Available actions for a given endpoint can be found by clicking the `OPTIONS` button for any endpoint.

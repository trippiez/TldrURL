# TldrURL - Link Shortening Service

TldrURL is a service that allows shortening long URLs into short, easy-to-manage links. The project is designed to facilitate the exchange of links, making them more convenient and memorable.

## Project Description

TldrURL provides a simple user interface for shortening links and an API for integration with other applications. It offers the following key features:

- Generating short links and associating them with original long URLs.
- Redirecting to the original address when accessing short links.

## Key Features

- Simple user interface with a form for entering long URLs and custom short link options.
- Automatically generating short links or specifying them by users.
- Ability to navigate through short links.
- API for creating new short links and retrieving original links based on short identifiers.

## Technologies

- Flask - for creating the web application.
- SQLAlchemy - ORM for working with the database.
- SQLite - database for storing links.
- HTML/CSS - for the user interface.
- Redoc - for documentation and API visualization.

## Installation and Usage

Clone the repository and navigate to it on the command line:

```
git clone
```

```
cd tldrurl
```

Create and activate a virtual environment:

```
python3 -m venv venv
```

*If you have Linux/macOS

```
source venv/bin/activate
```

*If you have windows

```
source code venv/scripts/activate
```

Install depending on the require.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run the script:

```
flask run
```

## Contacts

Backend by: Eric Ivanov
- e-mail: ldqfv@mail.ru
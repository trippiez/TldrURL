# YaCut - Link Shortening Service

YaCut is a service that allows shortening long URLs into short, easy-to-manage links. The project is designed to facilitate the exchange of links, making them more convenient and memorable.

## Project Description

YaCut provides a simple user interface for shortening links and an API for integration with other applications. It offers the following key features:

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
- Swagger - for documentation and API visualization.

## Installation and Usage

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

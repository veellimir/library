# Project library

 ### Создайте виртуальное окружения в корне проекта
Linux/Mac: 
    
    python3 -m venv venv
    source venv/bin/activate

Windows:

    python -m venv venv
    venv\Scripts\activate.bat

### Установите Poetry

    curl -sSL https://install.python-poetry.org | python3 -

### Установить зависимости

    poetry install


### Примените миграции
Linux/Mac: 

    python3 manage.py migrate

Windows:

    python manage.py migrate


### Run server
Linux/Mac: 

    python3 manage.py runserver

Windows:

    python manage.py runserver

### Доступы к админке
логин
    
    admin
    
пароль

    123
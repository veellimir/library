# Project library

 ### Создайте виртуальное окружения в корне проекта
Linux/Mac: 
    
    python3 -m venv venv
    source venv/bin/activate

Windows:

    python -m venv venv
    venv\Scripts\activate.bat

### Установите зависимости из файла requirements

    pip3 install -r requirements.txt


### Примените миграции

    python3 manage.py migrate

### Run server
    
    python3 manage.py runserver

### Доступы к админке
логин
    
    admin
    
пароль

    123
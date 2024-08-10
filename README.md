# Project library

 ### Создайте виртуальное окружения в корне проекта
Linux/Mac: 
    
    python3 -m venv venv
    source venv/bin/activate

Windows:

    python -m venv venv
    venv\Scripts\activate.bat

### Установите зависимости из файла requirements
Linux/Mac: 

    pip3 install -r requirements.txt

Windows:
    
    pip install -r requirements.txt

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
# tess_ecommerce

## Installation
Bash:

```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```
```
(venv)$ pip install -r requirements.txt
```

```
(venv)$ cd dash/
```
```
(venv) .../dash$ ./manage.py collectstatic
```
```
(venv) .../dash$ ./manage.py migrate
```
```
(venv) .../dash$ ./manage.py runserver
```

# celery
jalankan worker
```
celery -A web worker --loglevel=info -P gevent
```
jalankan celery beat
```
celery -A web beat --loglevel=info
```

# databases
rubah koneksi dan nama database di settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'PORT': '5432',
    },
}
```
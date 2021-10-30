## Run Locally(python 3.6+ preffered)

Clone the project

```bash
  git clone https://github.com/shayan-cyber/HackNITR-proj.git
```

Make virtual env

```bash
  python -m venv env
```

activate env

```bash
  . env/Scripts/activate
```

install dependencies(python 3.8+)

```bash
    pip install -r requirements.txt
```

navigate to the directory

```bash
  cd core
```

start the server

```bash
    python manage.py runserver
```

Run migrations

```bash
    python manage.py makemigrations
```

migrate

```bash
    python manage.py migrate
```

createsuperuser

```bash
    python manage.py createsuperuser
```

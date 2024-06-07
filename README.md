# Django REST CRUD Application

## Create a Django application

1. Create a virtual environment.
```
python3 -m venv env_name
```

2. Activate Virtual environment.
```
# macos
source env_name/bin/activate 
```

3. Install dependencies.
```
pip install django djangorestframework
```

4. Create a django project.
```
python django-admin startproject *project_name*
```

5. Create a django app.
```
cd *project_name*
python manage.py startapp *app_ma,e*
```

6. Run the django project.
```
python manage.py runserver 0.0.0.0:8000 # you can use any port here, i'm mr 8000 <3
```
Bonjour! your first django up and running...
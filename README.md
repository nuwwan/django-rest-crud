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

## upload project to github
<details>
<summary>Smash me to show-up</summary>

1. cd into the base directory of your project.
```
cd /where/you/want/to/go
```

2. Initialize git repository.
```
git init
```
3. Add files that are going to be included in first commit.
```
# git add single file
git add *file_name*

# git add everything inside current directory
git add .
```

4. Create a commit
```
git commit -m 'initial commit'
```

5. Create github repository.

6. Add remote link to your project.
```
git remote add origin https://github.com/your/project.git
```

7. Create main branch
```
git branch -M main
```

8. push to github.
```
git push -u origin main
```

9. Add `.gitignore` file.
```
# macos
touch .gitignore
```

10. Add directories or files which are not going to pushed to github.
```
dir/
__pycache__/ # ignone pycache directory
*.pyc # ignore all py cache files
*.sqlite3 # ignore database file
```

</details>

## Configure Debugger for vs code
<details>
<summary>cclick here to expand</summary>

1. Create a `launch.json file`
```
mkdir .vscode
cd .vscode
touch launch.json
```
2. Add following content to the `launch.josn`.
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Django",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/backend/manage.py", // location for manage.py file
            "args": [
                "runserver",
                "5000" // specify the port
            ],
            "django": true
        }
    ]
}
```
</details>
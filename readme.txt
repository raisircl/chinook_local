Chinook
    models
        __init__.py
        media_type.py
        repos
            __init__.py
            a_media_type.py
            media_type_repo.py
        views
            media_type_view.py    
    chinook.db
step 1: python -m venv chinook_venv
step 2 activate: .\chinook_venv\bin\Activate.ps1


pattren : MVC

models - Class(Model) and repos

class attributes belongs to table columns
so for each table we need a model or a class
in python and each class object reponsbile to deal with
table data

Models -> repos
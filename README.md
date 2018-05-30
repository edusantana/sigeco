# sigeco
Sistema de gestão escola coolaborativo

# Etapas

1. Criei app core
2. Criei o modelo inicial, submeti código ao github
3. Criando *migrations*

        (venv) medeiros@linux-9b1k:/home/alexandre/w/ifpb/sigeco> ./manage.py makemigrations
        No changes detected

Precisa informar que estamos utilizando essa aplicacao criada: [ajuda](https://docs.djangoproject.com/pt-br/2.0/topics/db/models/#using-models)

        (venv) medeiros@linux-9b1k:/home/alexandre/w/ifpb/sigeco> ./manage.py makemigrations
        Migrations for 'core':
        core/migrations/0001_initial.py
            - Create model Componente
            - Create model Ensino
            - Create model Instituicao
            - Create model Organizacao
            - Create model Serie
            - Add field organizacao to instituicao
            - Add field ensino to componente
            - Add field organizacao to componente
        (venv) medeiros@linux-9b1k:/home/alexandre/w/ifpb/sigeco> ./manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, core, sessions
        Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying core.0001_initial... OK
        Applying sessions.0001_initial... OK

[Commit](https://github.com/edusantana/sigeco/commit/9595504a99a9ac6e2a6324bad067f3f1308bb7b1)

4. [Configurando idioma e fuso horário](https://github.com/edusantana/sigeco/commit/eae72a59ef9ecd323e6d99147f5ec618505f08c6)
5. Configurando interface administrativa

> **CUIDADO**: *The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.*

- [Ajuda de site admin](https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/)

A interface administrativa serve apenas para iniciar o desenvolvimento rápido, não é para os usuários comuns. O passos [1 ao 3](https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/) já estavam prontos.


- [Precisamos criar um usuário admin](https://docs.djangoproject.com/pt-br/2.0/ref/django-admin/#django-admin-createsuperuser)

        (venv) medeiros@linux-9b1k:/home/alexandre/w/ifpb/sigeco> ./manage.py createsuperuser --username admin
        Email address:
        Password:
        Password (again):
        Error: Your passwords didn't match.
        Password:
        Password (again):
        This password is too short. It must contain at least 8 characters.
        Password:
        Password (again):
        Superuser created successfully.

Usuário criado com sucesso.

        4. Determine which of your application’s models should be editable in the admin interface.

Por enquanto, optei por adicionar todos os modelos até o momento.

        5. For each of those models, optionally create a ModelAdmin class that encapsulates the customized admin functionality and options for that particular model.

[Por enquanto, não realizarei nenhuma customizaćão, vou apenas registrar.](https://github.com/edusantana/sigeco/commit/1dc1dcd73a6c7e83f768a80497d5ad4c0a14e0eb)

[Vou precisar corrigir o plural também](https://github.com/edusantana/sigeco/commit/5e06f4e07d78a956e31099cade5cf1acf61708c8).

        6. Instantiate an AdminSite and tell it about each of your models and ModelAdmin classes.
        7. Hook the AdminSite instance into your URLconf.
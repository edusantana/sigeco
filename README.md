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


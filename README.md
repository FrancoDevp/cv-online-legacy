# Franco Irusta | CV Online

Portfolio profesional y currículum vitae online desarrollado con Django. La aplicación permite mostrar experiencia laboral, formación, habilidades, proyectos y enlaces de contacto en una web moderna, dinámica y fácil de mantener.

## Descripción

Este proyecto fue diseñado como una CV web personal orientado a perfiles de:

- IT Support
- QA Manual
- Soporte funcional y técnico
- Desarrollo y automatización

La estructura está organizada para que el contenido pueda gestionarse de forma sencilla desde Django Admin, sin necesidad de editar el HTML cada vez que se quiere actualizar la información profesional.

## Stack tecnológico

- Python 3.12
- Django 5
- SQLite
- HTML5
- CSS3
- JavaScript
- Git
- GitHub
## Estructura del proyecto

```text
project/
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cv/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── templates/
│   ├── base.html
│   └── cv/
│       └── home.html
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── pdf/
├── media/
├── db.sqlite3
└── .env.example

# Franco B. Irusta | CV Online

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
CV - ONLINE/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── db.sqlite3
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
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
├── pdf-cv/
│   ├── Franco B. Irusta CVIT - CL.pdf
│   └── Franco B. Irusta CVQA - CL.pdf
├── static/
│   ├── css/
│   ├── images/
│   ├── js/
│   └── pdf/
├── templates/
│   ├── base.html
│   └── cv/
│       └── home.html
└── .venv/
```

## Licencia

Este proyecto es de uso personal y portfolio profesional. Puedes adaptarlo o reutilizarlo para tus propios fines, siempre respetando la propiedad del contenido publicado.

## Contacto

- Email: franco.cantonati.99@gmail.com
- LinkedIn: https://www.linkedin.com/in/fb-irusta/
- GitHub: https://github.com/FrancoDevp


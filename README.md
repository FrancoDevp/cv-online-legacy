# Franco B. Irusta | CV Online

Proyecto Django para publicar un currículum vitae profesional en formato web, con enfoque en IT Support y QA Manual.

## Tecnologías
- Python
- Django
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
```

## Deploy

Este proyecto está preparado para desplegarse en un servicio compatible con Django/Python. Para una versión pública, se recomienda:

- Render
- Railway
- PythonAnywhere
- DigitalOcean App Platform
- VPS con Gunicorn + Nginx

No se recomienda GitHub Pages para ejecutar Django, ya que no sirve para aplicaciones Python.

## Importante
- No se sube la base de datos con información sensible.
- No se suben secretos ni claves.
- Se usa `.env` para variables de entorno.

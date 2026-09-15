from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class SiteConfig(models.Model):
    site_name = models.CharField(
        max_length=120,
        default="CV - Franco B. Irusta",
        verbose_name="Nombre del sitio",
    )
    meta_description = models.TextField(
        default="CV profesional de Franco Irusta, enfocado en IT Support y QA Manual.",
        verbose_name="Meta description",
    )
    email = models.EmailField(
        default="franco.cantonati.99@gmail.com",
        verbose_name="Email",
    )
    phone = models.CharField(
        max_length=50,
        default="+56 9 3906 6796",
        verbose_name="Teléfono",
    )
    location = models.CharField(
        max_length=200,
        default="Santiago Centro, Región Metropolitana",
        verbose_name="Ubicación",
    )
    linkedin_url = models.URLField(
        default="https://www.linkedin.com/in/fb-irusta/",
        verbose_name="LinkedIn",
    )
    github_url = models.URLField(
        default="https://github.com/FrancoIrusta",
        verbose_name="GitHub",
    )
    cv_pdf = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True,
        verbose_name="CV PDF",
    )

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return self.site_name


class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Empresa")
    position = models.CharField(max_length=200, verbose_name="Puesto")
    date_range = models.CharField(
        max_length=100,
        verbose_name="Período",
        help_text="Ejemplo: 2023 - 2024",
    )
    description = models.TextField(
        verbose_name="Descripción breve", blank=True)
    responsibilities = models.TextField(
        verbose_name="Responsabilidades",
        help_text="Escribir una lista breve en texto.",
    )
    tools = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Herramientas relacionadas",
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name="Orden de aparición")

    class Meta:
        ordering = ["order"]
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return f"{self.position} - {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Institución")
    title = models.CharField(max_length=200, verbose_name="Título o curso")
    period = models.CharField(max_length=100, verbose_name="Período")
    details = models.TextField(blank=True, verbose_name="Detalle adicional")
    order = models.PositiveIntegerField(
        default=0, verbose_name="Orden de aparición")

    class Meta:
        ordering = ["order"]
        verbose_name = "Formación"
        verbose_name_plural = "Formaciones"

    def __str__(self):
        return f"{self.title} - {self.institution}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("qa", "QA / Testing"),
        ("it", "IT / Soporte"),
        ("development", "Desarrollo"),
        ("management", "Gestión / Versionado"),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="qa",
        verbose_name="Categoría",
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name="Orden de aparición")

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Desarrollo web"),
        ("qa", "QA / Testing"),
        ("education", "Formación académica"),
        ("other", "Otro"),
    ]

    title = models.CharField(max_length=200, verbose_name="Proyecto")
    description = models.TextField(verbose_name="Descripción")
    technologies = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Tecnologías",
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="web",
        verbose_name="Categoría",
    )
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        verbose_name="Imagen",
    )
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub")
    demo_url = models.URLField(blank=True, null=True, verbose_name="Demo")
    order = models.PositiveIntegerField(
        default=0, verbose_name="Orden de aparición")

    class Meta:
        ordering = ["order"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title


def get_page_title():
    return "Franco B. Irusta | Soporte IT & QA Manual"

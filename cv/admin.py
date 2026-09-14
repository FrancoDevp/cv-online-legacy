from django.contrib import admin
from .models import Education, Experience, Project, SiteConfig, Skill


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("site_name", "email", "phone", "location")
    search_fields = ("site_name", "email", "location")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "position", "date_range", "order")
    list_editable = ("order",)
    search_fields = ("company", "position")
    ordering = ("order",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "title", "period", "order")
    list_editable = ("order",)
    search_fields = ("institution", "title")
    ordering = ("order",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("category", "order", "name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)
    search_fields = ("title", "technologies")
    ordering = ("order",)

from django.views.generic import TemplateView

from .models import Education, Experience, Project, SiteConfig, Skill


class HomeView(TemplateView):
    template_name = "cv/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        site_config = SiteConfig.objects.first()
        if not site_config:
            site_config = SiteConfig.objects.create()

        context["site_config"] = site_config
        context["experiences"] = Experience.objects.all()
        context["education"] = Education.objects.all()
        context["projects"] = Project.objects.all()
        context["skills"] = {
            "qa": Skill.objects.filter(category="qa"),
            "it": Skill.objects.filter(category="it"),
            "development": Skill.objects.filter(category="development"),
            "management": Skill.objects.filter(category="management"),
        }

        return context

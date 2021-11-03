from django.views.generic.base import TemplateView
from ProjectED.utils import DataMixin


class NotFoundVies(TemplateView, DataMixin):
    template_name = "not_found.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Page Not Found")

        return context

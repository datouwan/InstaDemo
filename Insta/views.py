from django.views.generic import TemplateView
# Create your views here.

class HellowDjango(TemplateView):
    template_name = 'home.html'
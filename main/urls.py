from django.urls import path
from main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('test', views.test),
]

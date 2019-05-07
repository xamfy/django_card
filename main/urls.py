from django.urls import path
from main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category-detail'),
    path('edit/<pic>', views.edit, name='edit'),
    path('generated/<pic>', views.generate, name='generate'),
    # path('test', views.test),
]

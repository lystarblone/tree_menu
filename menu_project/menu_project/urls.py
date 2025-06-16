"""menu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('services/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Услуги'}), name='services_list'),
    path('services/consulting/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Консультации'}), name='consulting'),
    path('services/training/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Обучение'}), name='training_list'),
    path('services/training/course1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Курс 1'}), name='course1'),
    path('contact/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Контакты'}), name='contact'),
    path('admin/users/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Пользователи'}), name='admin_users'),
    path('admin/users/roles/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Роли'}), name='admin_roles'),
]
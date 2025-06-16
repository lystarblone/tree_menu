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
    path('', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Главная'}), name='index'),
    path('book1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Книга 1'}), name='book1'),
    path('book1/intro/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Введение'}), name='book1_intro'),
    path('book1/chapter1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 1'}), name='book1_chapter1'),
    path('book1/chapter1/section1_1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Раздел 1.1'}), name='book1_section1_1'),
    path('book1/chapter1/section1_2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Раздел 1.2'}), name='book1_section1_2'),
    path('book1/chapter2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 2'}), name='book1_chapter2'),
    path('book1/conclusion/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Заключение'}), name='book1_conclusion'),
    path('book2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Книга 2'}), name='book2'),
    path('book2/prologue/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Пролог'}), name='book2_prologue'),
    path('book2/chapter1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 1'}), name='book2_chapter1'),
    path('book2/epilogue/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Эпилог'}), name='book2_epilogue'),
]
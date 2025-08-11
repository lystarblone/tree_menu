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
    path('book1/chapter1/section1_1/sub1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Подраздел 1.1.1'}), name='book1_section1_1_sub1'),
    path('book1/chapter1/section1_2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Раздел 1.2'}), name='book1_section1_2'),

    path('book1/chapter2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 2'}), name='book1_chapter2'),
    path('book1/chapter2/section2_1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Раздел 2.1'}), name='book1_section2_1'),
    path('book1/chapter2/section2_1/sub2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Подраздел 2.1.1'}), name='book1_section2_1_sub2'),
    path('book1/chapter2/section2_2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Раздел 2.2'}), name='book1_section2_2'),

    path('book1/chapter3/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 3'}), name='book1_chapter3'),
    path('book1/chapter3/appendix/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Приложение'}), name='book1_appendix'),

    path('book1/conclusion/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Заключение'}), name='book1_conclusion'),

    path('book2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Книга 2'}), name='book2'),
    path('book2/prologue/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Пролог'}), name='book2_prologue'),
    path('book2/chapter1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 1'}), name='book2_chapter1'),
    path('book2/chapter1/part1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Часть 1'}), name='book2_chapter1_part1'),
    path('book2/chapter1/part2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Часть 2'}), name='book2_chapter1_part2'),
    path('book2/chapter2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 2'}), name='book2_chapter2'),
    path('book2/epilogue/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Эпилог'}), name='book2_epilogue'),

    path('book3/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Книга 3'}), name='book3'),
    path('book3/chapter1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 1'}), name='book3_chapter1'),
    path('book3/chapter2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 2'}), name='book3_chapter2'),
    path('book3/chapter2/topic1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Тема 1'}), name='book3_chapter2_topic1'),
    path('book3/chapter2/topic2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Тема 2'}), name='book3_chapter2_topic2'),
    path('book3/chapter3/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 3'}), name='book3_chapter3'),
    path('book3/chapter4/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 4'}), name='book3_chapter4'),

    path('book4/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Книга 4'}), name='book4'),
    path('book4/chapter1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Глава 1'}), name='book4_chapter1'),
    path('book4/chapter1/branch1/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Ветка 1'}), name='book4_chapter1_branch1'),
    path('book4/chapter1/branch2/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Ветка 2'}), name='book4_chapter1_branch2'),
    path('book4/chapter1/branch3/', TemplateView.as_view(template_name='example.html', extra_context={'title': 'Ветка 3'}), name='book4_chapter1_branch3'),
]

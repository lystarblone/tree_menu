from django.db import models
from django.urls import reverse, NoReverseMatch

class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100, verbose_name='Название меню')
    title = models.CharField(max_length=200, verbose_name='Заголовок пункта')
    url = models.CharField(max_length=200, blank=True, verbose_name='URL')
    named_url = models.CharField(max_length=100, blank=True, verbose_name='Named URL')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name='Родитель')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return f'{self.title} ({self.menu_name})'

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                pass
        return self.url or '#'
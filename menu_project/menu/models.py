from django.db import models
from django.urls import reverse, NoReverseMatch

class MenuItem(models.Model):
    menu_name = models.CharField("Меню", max_length=100, db_index=True)
    title = models.CharField("Название", max_length=200)
    url = models.CharField("URL (явный)", max_length=500, blank=True, default="")
    named_url = models.CharField("Named URL", max_length=200, blank=True, default="")
    parent = models.ForeignKey(
        'self', verbose_name="Родитель",
        null=True, blank=True, on_delete=models.CASCADE, related_name='children'
    )
    order = models.IntegerField("Порядок", default=0)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return f"{self.title} ({self.menu_name})"

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or '#'
        return self.url or '#'
from django.db import models

class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    order = models.IntegerField(default=0)

    def get_url(self):
        if self.named_url:
            return self.named_url
        return self.url

    def __str__(self):
        return self.title
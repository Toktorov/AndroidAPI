from tabnanny import verbose
from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Номер телефона"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя"
    )
    surname = models.CharField(
        max_length = 255, 
        verbose_name = "Фамилия"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категория для таблиц'



class Todos(models.Model):
    category = models.ManyToManyField(Category, null=True, blank=True)
    
    user = models.TextField(
        verbose_name='Имя'           
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='todos',
        verbose_name='Фото', 
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Выполнено'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Таблицы'

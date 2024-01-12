from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='порода')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        permissions = [
            ('can_view_name', 'Can view name'),
            ('can_change_description', 'Can change description'),
            ('can_view_category', 'Can view category')
        ]


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='кличка')
    # category = models.CharField(max_length=100, verbose_name='порода')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='порода')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='фотография')
    birth_day = models.DateField(**NULLABLE, verbose_name='дата рождения')

    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              verbose_name='владелец'
                              )

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'


class Parent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, verbose_name='Собака')
    name = models.CharField(max_length=250, verbose_name='кличка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='порода')
    birth_day = models.DateField(**NULLABLE, verbose_name='дата рождения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Предок'
        verbose_name_plural = 'Предки'

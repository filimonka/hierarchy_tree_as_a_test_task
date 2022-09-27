from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .validators import validate_roles

User = get_user_model()


CHOICES = [
    ('RUB', 'рубли'),
    ('USD', 'доллары'),
    ('EUR', 'евро'),
]
LEVEL_CHOICES = [
    ('Executive', 1),
    ('Head of dep', 2),
    ('Chief', 3),
    ('Second chief', 4),
    ('rookie', 5)
]



class Employee(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=100
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=100
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100
    )
    position = models.CharField(
        'Должность',
        max_length=250,
    )
    employment_date = models.DateField(
        'Дата приема на работу',
    )
    salary = models.DecimalField(
        'Зарплата',
        max_digits=8,
        decimal_places=2
    )
    salary_currency = models.CharField(
        'валюта зарплаты',
        max_length=3,
        choices=CHOICES
    )
    role_level = models.CharField(
        'уровень в компании',
        max_length=100,
        choices=LEVEL_CHOICES
    )

    def get_full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    
    def get_salary(self):
        return f'{self.salary} {self.salary_currency}'
    
    def __str__(self):
        return f'{self.get_full_name()}, {self.role_level}'


class Superior(models.Model):
    chef = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='chef',
        verbose_name='Начальник',
    )
    subordinate = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='subordinate',
        verbose_name='Подчиненный'
    )

    def clean(self, *args, **kwargs) -> None:
        validate_roles(self.chef, self.subordinate)
        return super().clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

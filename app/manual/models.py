from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
import uuid


class Manual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID", editable=False)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, help_text="Description of the Manual")

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return f'{self.name}'


class ManualVersion(models.Model):
    manual = models.ForeignKey(Manual, on_delete=models.PROTECT, )
    version = models.CharField(max_length=50, null=False, blank=False)
    enable_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False, verbose_name='Дата',
                                       help_text='дата начала действия справочника этой версии')

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Версию справочника'
        verbose_name_plural = 'Версии справочников'
        # constraints = [
        #     models.UniqueConstraint(name="unique version", fields=['version'])
        # ]

    def __str__(self):
        return f'{self.manual} - {self.version}'

    def clean(self):
        """Проверка поля version"""
        print('Проверка')

        if self.__class__.objects.filter(manual__id=self.manual.id, version=self.version).exclude(pk=self.pk).exists():
            raise ValidationError(f'Версия "{self.version}" уже существует!')


class Item(models.Model):
    manual_version = models.ForeignKey(ManualVersion, on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    summary = models.TextField(max_length=1000, help_text="Description of the Manual")

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'

    def __str__(self):
        return f'{self.id} | {self.code} | {self.summary}'

    def manual(self):
        """Вывод справочника элемента"""
        return self.manual_version.manual

    def version(self):
        """Вывод версии справочника элемента"""
        return self.manual_version.version

    def date(self):
        """Вывод даты версии справочника элемента"""
        return self.manual_version.enable_date

from django.core.exceptions import ValidationError
from django.db import models
import uuid


class ManualBase(models.Model):
    """
    Базовый класс справочника
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID", editable=False)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, help_text="Description of the Manual")

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Базовый справочник'
        verbose_name_plural = 'Базовые справочники'

    def __str__(self):
        return f'{self.name}'


class Manual(models.Model):
    """
    Справочник
    """
    manual_base = models.ForeignKey(ManualBase, on_delete=models.PROTECT,)
    version = models.CharField(max_length=50, null=False, blank=False)
    enable_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False, verbose_name='Дата',
                                       help_text='дата начала действия справочника этой версии')

    def name(self):
        return self.manual_base.name

    def short_name(self):
        return self.manual_base.short_name

    def description(self):
        return self.manual_base.description

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Cправочника'
        verbose_name_plural = 'Cправочники'

    def __str__(self):
        return f'{self.manual_base} - {self.version}'

    def clean(self):
        """Проверка поля version"""
        print('Проверка')

        if self.__class__.objects.filter(manual_base__id=self.manual_base.id, version=self.version).exclude(pk=self.pk).exists():
            raise ValidationError(f'Версия "{self.version}" уже существует!')


class Item(models.Model):
    """
    Элемент справочника
    """
    manual = models.ForeignKey(Manual, on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    summary = models.TextField(max_length=1000, help_text="Description of the Manual")

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'

    def __str__(self):
        return f'{self.id} | {self.code} | {self.summary}'

    def manual_name(self):
        """Вывод справочника элемента"""
        return self.manual.manual_base.name

    def manual_version(self):
        """Вывод версии справочника элемента"""
        return self.manual.version

    def manual_date(self):
        """Вывод даты версии справочника элемента"""
        return self.manual.enable_date

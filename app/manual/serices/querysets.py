from datetime import datetime

from django.db.models import QuerySet

from manual.models import Manual, Item


def manual_list_date(*args, **kwargs) -> QuerySet:
    """Справочники отфильтрованные по указанной дате"""
    return Manual.objects.filter(enable_date__lte=kwargs['date'])


def item_current_list(*args, **kwargs) -> QuerySet:
    """"Элементы справочника отфильтрованные по указанной дате"""
    # по id базового справочника и дате версии находим актуальные - на текущий день
    return Item.objects.filter(manual__manual_base_id=kwargs['id'], manual__enable_date__lte=datetime.now())


def item_list_by_version(*args, **kwargs) -> QuerySet:
    """Элементы справочника отфильтрованные по указанной версии справочника"""
    date = Manual.objects.filter(manual_base_id=kwargs['id'],
                                 version=kwargs['version']).first().enable_date
    return Item.objects.filter(manual__manual_base_id=kwargs['id'], manual__enable_date__lte=date)

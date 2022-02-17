from typing import List, Tuple

from django.contrib.admin import SimpleListFilter

from manual.models import Manual


class ItemsIncomingToVersionFilter(SimpleListFilter):
    """
    Фильтр показывающий все элементы справочника до конкретной(выбранной) версии - даты (не в определенной версии).
    """
    # Т.е. в виджете на данный момент:
    # 1. manual version - сортировка элементов входящих только в данную версию
    # 2. manual - сортировка по справочнику
    # Добавляем.
    # 3. incoming - все элементы справочника до версии

    title = 'incoming'  # or use _('country') for translated title
    parameter_name = 'incoming'

    def lookups(self, request, model_admin) -> List[Tuple]:
        """Список для list_filter"""
        qs = model_admin.get_queryset(request)  # список элементов
        manuals = set([c.manual for c in qs])  # собираем массив из справочников

        # докидываем в массив строки-названия.
        # [(id, str), ..., ] - id - значение для фильтрации, str - для читабельности в виджете
        return [(c.id, f'{c.id} - {c.manual_base.name} - {c.version}') for c in manuals]

    def queryset(self, request, queryset):

        if self.value():
            # очень мутная тема...
            # отфильтровываем все элементы - берем все даты, которые меньше или равно текущей даты версии справочника,
            # также отфильтровываем по принадлежности всех элементов к одному базовому справочнику
            m_object = Manual.objects.get(pk=self.value())
            return queryset.filter(manual__enable_date__lte=m_object.enable_date,
                                   manual__manual_base_id=m_object.manual_base.id)
        return queryset

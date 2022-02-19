from datetime import datetime
from typing import List, OrderedDict as typeOrderedDict

from manual.api.v1.serializers import ItemValidateSerializer
from manual.models import Item, Manual


def having_items(sub_items: List[typeOrderedDict], version: str = None) -> bool:
    """Проверка есть ли эти элемент(ы)!! в текущей версии справочника
        a = [OrderedDict([('code', '469'), ..]), OrderedDict([('code', '445'), ..]), ...]
        b = [OrderedDict([('code', '469'), ..]), ...]
        all(x in a for x in b) -> Bool
        """
    date = datetime.now()
    if version:
        # Если передана версия, то передан один элемент на проверку(в списке один элемент).
        # Ищем дату начала версии справочника (не текущего...)
        date = Manual.objects.filter(manual_base_id=sub_items[0]['manual'], version=version).first().enable_date

    qs = Item.objects.filter(manual__enable_date__lte=date)
    items = ItemValidateSerializer(data=qs, many=True)
    # items.is_valid(raise_exception=True)  # TODO: дает ошибку почему-то
    items.is_valid()
    print(items.data)
    return all(x in items.data for x in sub_items)


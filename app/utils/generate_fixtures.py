from datetime import datetime
from random import randint

from manual.models import Manual, Item, ManualBase

"""
Используется либо в python shell, либо в django commands
"""


def get_random_datetime(day=randint(1, 31), hour=randint(1, 24), minutes: int = randint(0, 59)):
    return datetime.strptime(f'{day}.02.2022 {hour}:{minutes}:00', "%d.%m.%Y %H:%M:%S")


def gen_fixtures(date=get_random_datetime, manuals: int = 12, versions: int = 5, items: int = 12):
    for m in range(1, manuals + 1):
        mb_obj, created = ManualBase.objects.get_or_create(name=f'Справочник{m}', short_name=f'C{m}',
                                                           description=f'Random text {m}')
        for mv in range(1, versions + 1):
            m_obj, created = Manual.objects.get_or_create(manual_base=mb_obj, version=f'00.{mv:02d}',
                                                          enable_date=date())
            for i in range(1, items + 1):
                Item.objects.get_or_create(manual=m_obj, code=randint(100, 500),
                                           summary=f'Summary text {i}')


def delete_all():
    Item.objects.all().delete()
    Manual.objects.all().delete()
    ManualBase.objects.all().delete()

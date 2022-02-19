from datetime import datetime
from random import randint

from manual.models import Manual, Item, ManualBase

"""
Используется либо в python shell, либо в django commands
"""


def get_random_datetime():
    return datetime.strptime(f'{randint(1, 31)}.01.2022 {randint(0, 23)}:{randint(0, 59)}:00', "%d.%m.%Y %H:%M:%S")


def gen_fixtures(date=get_random_datetime):
    for m in range(1, 12):
        mb_obj, created = ManualBase.objects.get_or_create(name=f'Справочник{m}', short_name=f'C{m}',
                                                           description=f'Random text {m}')
        for mv in range(1, 5):
            m_obj, created = Manual.objects.get_or_create(manual_base=mb_obj, version=f'00.{mv:02d}',
                                                          enable_date=date())
            for i in range(1, 12):
                Item.objects.get_or_create(manual=m_obj, code=randint(100, 500),
                                           summary=f'Summary text {i}')


def delete_all():
    Item.objects.all().delete()
    Manual.objects.all().delete()
    ManualBase.objects.all().delete()

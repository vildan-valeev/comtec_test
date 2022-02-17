from datetime import datetime
from random import randint

from manual.models import Manual, ManualVersion, Item

"""
Напрямую в проекте не использовано, только тесто
"""


def get_random_datetime():
    return datetime.strptime(f'{randint(1, 31)}.01.2022 {randint(0, 23)}:{randint(0, 59)}:00', "%d.%m.%Y %H:%M:%S")


def gen_fixtures():
    for m in range(1, 4):
        m_obj, created = Manual.objects.get_or_create(name=f'Справочник{m}', short_name=f'C{m}',
                                                      description=f'Random text {m}')
        for mv in range(1, 4):
            mv_obj, created = ManualVersion.objects.get_or_create(manual=m_obj, version=f'0.{mv}',
                                                                  enable_date=get_random_datetime)
            for i in range(1, 4):
                Item.objects.get_or_create(manual_version=mv_obj, code=randint(100, 500),
                                           summary=f'Summary text {i}')

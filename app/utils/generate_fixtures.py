from datetime import datetime, timedelta
from random import randint

from manual.models import Manual, Item, ManualBase

"""
Используется либо в python shell, либо в django commands, либо в тестах
"""


class FixturesGenerator:
    def __init__(self):
        #  минус пару дней от сегодня (для тестирования справочников уже актуальных на сегодняшний день)
        self.date = datetime(2022, 2, datetime.now().day-randint(1, 4), randint(1, 23), 30)

    def create_manual_base(self, manual_number: int) -> ManualBase:
        return ManualBase.objects.get_or_create(name=f'Справочник{manual_number}',
                                                short_name=f'C{manual_number}',
                                                description=f'Random text {manual_number}')

    def create_manual(self, manual_base: ManualBase, date: datetime, version: int) -> Manual:
        return Manual.objects.get_or_create(manual_base=manual_base,
                                            version=f'00.{version:02d}',
                                            enable_date=date)

    def create_item(self, manual: Manual, index):
        return Item.objects.get_or_create(manual=manual,
                                          code=randint(100, 500),
                                          summary=f'Summary text {index}')

    def gen_fixtures(self, manual_base: int = 11, manuals: int = 3, items: int = 11, day_offset: int = randint(1, 10)):
        """генерируем данные: 1.ManualBase 2.Manual 3.Item """
        for m_b in range(1, manual_base + 1):
            mb_obj, created = self.create_manual_base(m_b)
            for m_v in range(1, manuals + 1):
                m_obj, created = self.create_manual(mb_obj, self.date, m_v)
                self.date += timedelta(days=day_offset)
                for i in range(1, items + 1):
                    self.create_item(m_obj, i)

    def delete_all(self):
        Item.objects.all().delete()
        Manual.objects.all().delete()
        ManualBase.objects.all().delete()

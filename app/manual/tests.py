import re
from datetime import datetime, timedelta
from random import randint

from django.test import TestCase

from manual.models import ManualBase
from manual.serices.querysets import manual_list_date
from manual.serices.regex_check import ManualVersionCheck, ManualDateCheck
from utils.generate_fixtures import FixturesGenerator


class GeneratorForTest(FixturesGenerator):
    """(день, месяц, час, минута)"""

    def __init__(self):
        super().__init__()
        now = datetime.now()
        self.date = datetime(2022, 2, now.day - 10, now.hour, now.minute)


class TestManual(TestCase):

    def setUp(self):
        self.re_check = [
            (ManualVersionCheck.regex, False, ['0.0', '00.00', '00.000', '0,0', '00,0', '-10.09', '11.109', 'sd.sd', ]),
            (ManualVersionCheck.regex, True, ['00.01', '10.99', '91.99', '10.09', '99.99']),
            (ManualDateCheck.regex, True, ['15-01-2020', '31-12-2022', ]),
            (ManualDateCheck.regex, False, ['32-01-2020', '15-13-2020', '3-01-2050', '03.01.2050']),
        ]

    # расчет от 01-01-2010 до 31-12-2059

    def test_regexp_manual(self):
        for p, k, v in self.re_check:
            for i in v:
                self.assertEqual(bool(re.fullmatch(pattern=p, string=i)), k)


class ModelsTest(TestCase):

    def setUp(self) -> None:
        self.now = datetime.now()
    @classmethod
    def setUpTestData(cls):

        g = GeneratorForTest()
        g.gen_fixtures(manual_base=1, manuals=3, items=2, day_offset=10)

    def test_check_manual_base(self):
        m_b = ManualBase.objects.all()
        print('count', m_b.count())
        self.assertEqual(m_b.count(), 1)

    def test_manual_list_date_queryset(self):
        """ """
        # в генераторе заданы справочники: первая 10 дней назад, вторая действует сейчас, третья вступит через 10 дней,
        # т.е. она будет актуальная потом
        # Если к примеру захотим узнать сколько справочников на дату now+1(т.е. завтра) - их должно быть ДВА
        # если дата указана позже (вчера и тд), то должен быть ОДИН справочник
        self.assertEqual(manual_list_date(date=datetime(2022, 2, self.now.day + 2)).count(), 2)
        self.assertEqual(manual_list_date(date=datetime(2022, 2, self.now.day - 2)).count(), 1)
        pass

    def test_item_current_list_queryset(self):
        pass

    def test_item_list_by_version_queryset(self):
        pass

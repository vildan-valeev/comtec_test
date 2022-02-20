import re

from django.test import TestCase

from manual.serices.regex_check import ManualVersionCheck, ManualDateCheck


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

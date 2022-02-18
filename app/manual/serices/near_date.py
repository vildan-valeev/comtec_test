import datetime

from manual.models import Manual

#
# def near_date(uuid: str) -> datetime.datetime:
#     """ Дата ближайшего актуального справочника на сегодня"""
#     dates = Manual.objects.filter(manual_base_id=uuid, enable_date__lte=datetime.datetime.now())
#     s = sorted(lst)
#     print(s, n)
#
#     for i in range(len(s) - 1):
#         print(s[i], n, s[i + 1])
#         if s[i] <= n < s[i + 1]:
#             print('ok', s[i])
#             return s[i]


def near_int(lst, n) -> int:
    """
    ближайшее меньшее число

    [1, 3, 8, 12, 18], 4
    1 < 4 > 3
    3 < 4 < 8  !!!  выбираем 3
    8 > 4 < 12
    12 > 4 < 18

    [1, 3, 8, 12, 18], 3
    1 < 3 == 3
    3 == 3 < 8 !!! выбираем 3
    8 > 3 < 12
    12 > 3 < 18

    [1, 3, 8, 12, 18], 8
    1 < 8 > 3
    3 < 8 == 8
    8 == 8 < 12 !!! выбираем 8
    12 > 8 < 18
    """
    s = sorted(lst)
    print(s, n)

    for i in range(len(s) - 1):
        print(s[i], n, s[i + 1])
        if s[i] <= n < s[i + 1]:
            print('ok', s[i])
            return s[i]


# near_int([12, 18, 3, 1, 8], 4)
# near_int([12, 18, 3, 1, 8], 3)
# near_int([12, 18, 3, 1, 8], 8)

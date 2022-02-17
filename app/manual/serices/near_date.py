import datetime


def near_date(uuid: str) -> datetime.datetime:
    pass


def near_int(lst, n) -> int:
    """
    ближайшее меньшее число

    [12, 18, 3, 1, 8], 4
    1 < 4 > 3
    3 < 4 < 8  !!!
    8 > 4 < 12
    12 > 4 < 18
    """
    s = sorted(lst)
    for i in range(len(s) - 1):
        print(s[i], n, s[i + 1])

        if s[i + 1] == n:
            print('ok', s[i+1])
            return s[i + 1]

        if s[i] <= n < s[i + 1]:
            print('ok', s[i])
            return s[i]


near_int([12, 18, 3, 1, 8], 4)
near_int([12, 18, 3, 1, 8], 3)
near_int([12, 18, 3, 1, 8], 8)

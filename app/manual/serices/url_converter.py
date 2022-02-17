from datetime import datetime


class VersionConverter:
    """ """
    pass
    # regex = '(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-(?:20[12345][0-9])'
    #
    # # расчет от 01-01-2010 до 31-12-2059
    #
    # def to_python(self, value):
    #     return datetime.strptime(value, "%d-%m-%Y")
    #
    # def to_url(self, value):
    #     return value.strftime("%d-%m-%Y")


class DateConverter:
    """

    """
    regex = '(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-(?:20[12345][0-9])'

    # расчет от 01-01-2010 до 31-12-2059

    def to_python(self, value):
        return datetime.strptime(value, "%d-%m-%Y")

    def to_url(self, value):
        return value.strftime("%d-%m-%Y")

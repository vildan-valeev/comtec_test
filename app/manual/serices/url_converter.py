from datetime import datetime

from manual.serices.regex_check import ManualDateCheck, ManualVersionCheck


class VersionConverter(ManualVersionCheck):
    """ """
    # расчет от 00.01 до 99.99

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


class DateConverter(ManualDateCheck):
    """ """
    # расчет от 01-01-2010 до 31-12-2059

    def to_python(self, value):
        return datetime.strptime(value, "%d-%m-%Y")

    def to_url(self, value):
        return value.strftime("%d-%m-%Y")

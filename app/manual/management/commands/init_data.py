import logging

from django.core.management.base import BaseCommand

from manual.models import ManualBase
from utils.generate_fixtures import gen_fixtures

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generate random data to db'

    def init_data(self):
        if not ManualBase.objects.exists():
            gen_fixtures()
            return "ОК выполнено!"
        return 'В бд уже есть данные...'

    def handle(self, *args, **options):
        print('Start create data in db')
        return self.init_data()

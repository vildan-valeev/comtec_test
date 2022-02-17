import logging

from django.core.management.base import BaseCommand

from manual.models import ManualBase
from utils.generate_fixtures import gen_fixtures

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generate random data to db'

    def init_data(self) -> str:
        """

        :return:
        """
        if not ManualBase.objects.exists():  # Если ManualBase не пустая, не создаем данные
            gen_fixtures()
            return "ОК выполнено!"
        return 'В бд уже есть данные...'

    def handle(self, *args, **options):
        """ """
        logger.info('Start create data in db')
        return self.init_data()

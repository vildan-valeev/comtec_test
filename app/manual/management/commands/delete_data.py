import logging

from django.core.management.base import BaseCommand

from manual.models import ManualBase
from utils.generate_fixtures import gen_fixtures

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Delete data from db'

    def delete_data(self) -> str:
        """

        :return:
        """
        if not ManualBase.objects.exists():  # Если ManualBase не пустая, не создаем данные
            gen_fixtures()
            return "ОК выполнено!"
        return 'В бд уже есть данные...'

    def handle(self, *args, **options):
        """ """
        logger.info('Deleting data from db...')
        return self.delete_data()

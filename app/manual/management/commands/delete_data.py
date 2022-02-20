import logging

from django.core.management.base import BaseCommand

from utils.generate_fixtures import FixturesGenerator

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Delete data from db'

    def delete_data(self) -> str:
        """

        :return:
        """
        g = FixturesGenerator()
        g.delete_all()
        return "ОК, бд очищена!"

    def handle(self, *args, **options):
        """ """
        logger.info('Deleting data from db...')
        return self.delete_data()

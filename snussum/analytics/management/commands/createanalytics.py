from django.core.management.base import BaseCommand, CommandError

from analytics.models.demographics import Demographics


class Command(BaseCommand):
    help = "Create Analytics Data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        demograhics = Demographics.objects.create_analytics()
        self.stdout.write('Successfully created demograhics analytics data ...')

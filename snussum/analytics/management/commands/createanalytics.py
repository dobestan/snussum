from django.core.management.base import BaseCommand, CommandError

from analytics.models.demographic import Demographic


class Command(BaseCommand):
    help = "Create Analytics Data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        demograhic = Demographic.objects.create_analytics()
        self.stdout.write('Successfully created demograhic analytics data ...')

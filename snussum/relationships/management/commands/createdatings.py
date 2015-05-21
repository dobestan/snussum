from django.core.management.base import BaseCommand, CommandError

from relationships.models.dating import Dating
from relationships.tasks.datings import match_all
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create demo datings fixtures'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for z in range(10):
            match_all()
            for dating in Dating.objects.all():
                dating.matched_at -= timedelta(1)
                dating.save()
        self.stdout.write('Successfully created datings ...')

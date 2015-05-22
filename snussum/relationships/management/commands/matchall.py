from django.core.management.base import BaseCommand, CommandError

from relationships.models.dating import Dating
from relationships.tasks.datings import match_all


class Command(BaseCommand):
    help = 'Execute match_all'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        old_datings_count = Dating.objects.count()
        match_all()
        new_datings_count = Dating.objects.count()
        self.stdout.write(
            'Match All | %03d -> %03d ( + %03d )' %
            (old_datings_count, new_datings_count, new_datings_count - old_datings_count)
        )
        self.stdout.write('Successfully executed match_all...')

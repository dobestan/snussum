from django.core.management.base import BaseCommand, CommandError

from relationships.models.dating import Dating
from relationships.tasks.datings import match_all

from datetime import datetime
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create demo datings fixtures'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for x in range(1, 10 + 1):
            for dating in Dating.objects.all():
                dating.matched_at -= timedelta(1)
                dating.save()

            match_all()
            self.stdout.write(
                'Day(%02d) > %03d datings matched, %03d datings total' %
                (x, Dating.objects.filter(matched_at=datetime.today()).count(), Dating.objects.count())
            )

        self.stdout.write('Successfully created datings ...')

from celery import shared_task


from analytics.models.demographic import Demographic


@shared_task
def calculate_analytics_demographic():
    Demographic.objects.create_analytics()

web: gunicorn --pythonpath snussum/ --bind :5736 --workers=3 snussum.wsgi 
worker: celery --workdir=snussum/ --app=snussum.celery:app --concurrency=3 worker
beat: celery --workdir=snussum/ --app=snussum.celery:app beat
flower: celery --workdir=snussum/ --app=snussum.celery:app flower

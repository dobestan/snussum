web: gunicorn --pythonpath snussum/ snussum.wsgi
worker: celery --workdir=snussum/ --app=snussum.celery:app worker
beat: celery --workdir=snussum/ --app=snussum.celery:app beat
flower: celery --workdir=snussum/ --app=snussum.celery:app flower

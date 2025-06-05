from uploads.celery_worker import celery

@celery.task
def add(x, y):
    return x + y

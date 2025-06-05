from app import create_app, make_celery

app = create_app()
celery = make_celery(app)

import uploads.benchmarker  # Ensure this is the correct path to your tasks

if __name__ == '__main__':
    celery.start()

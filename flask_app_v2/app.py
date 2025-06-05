from flask import Flask, request, jsonify
from celery import Celery
import time

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery

def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )
    return app

app = create_app()
celery = make_celery(app)

@celery.task
def add(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y

@app.route('/')
def home():
    return 'Welcome to the Flask application!'

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    task = add.apply_async(args=[data['x'], data['y']])
    return jsonify({'task_id': task.id}), 202

@app.route('/status/<task_id>')
def task_status(task_id):
    task = add.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': task.state}
    elif task.state != 'FAILURE':
        response = {'state': task.state, 'result': task.result}
    else:
        response = {'state': task.state, 'error': str(task.info)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Tareas periodicas-----------
from celery.schedules import crontab

app.conf.beat_schedule = {
    'send_data_every_three_months': {
        'task': 'r_agrocablebot.tasks.send_data_via_email',
        # 'schedule': crontab(minute='*/5'), 
        'schedule': crontab(day_of_month=17, month_of_year='1,5,7,10'),
        # Ajusta los meses si deseas que se ejecute en diferentes meses
    },
    'ejecutar_evento_programado': {
        'task': 'r_agrocablebot.tasks.ejecutar_evento_programado',
        'schedule': crontab(minute='*/1'),  # Ejecutar cada minuto
    },
    
}
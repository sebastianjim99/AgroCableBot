# Create your tasks here

# fromfrom demoapp.models import Widget

from celery import shared_task


@shared_task
def add(x, y):
    return x + y 


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
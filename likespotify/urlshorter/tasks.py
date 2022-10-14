from celery import shared_task
import random
import string



@shared_task
def generate_shortlink():
    """function generates string sequence"""
    link = [''.join(random.choice(string.digits + string.ascii_letters) for _ in range(7))]
    return link[0].lower()
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django_email.celery import app

from celery import shared_task
from .email import send_email

# @shared_task(name="send_email_task")
# def send_email_task(subject, message, emails, files):
@app.task
def send_email_task():
    print("i am inside task")
    subject = 'Test Message'
    message = 'Test Message body'
    emails = ['informjashvavineethapaul@gmail.com']
    files = ''
    send_email(subject,message,emails,files)
    return 'Done'



import os
from time import sleep
from typing import Any

from backend.celery import celery_app

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# from main.models import Auto, Profile, Subscriber
#
# from twilio.rest import Client


@celery_app.task(name="send_email_to_subscribers_task")
def send_email_to_subscribers_task(user_email: str, data: Any) -> None:
    """ send a message to subs after adding an ad"""

    html_content = render_to_string('account/email/email_ad_for_subscribers.html', data)
    msg = EmailMultiAlternatives(subject='Новое объявление', to=[user_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@celery_app.task(name='periodic_task')
def periodic_task():
    sleep(10)

    results = {
        "hello"
    }

    return results


# @celery_app.task(name='send_periodic_email')
# def send_periodic_email() -> None:
#     """ send periodic emails"""
#     name_lst = []
#     last_five_ads = Auto.objects.order_by('-id')[:5]
#     for el in last_five_ads:
#         name_lst.append(el.name)
#     for item in Subscriber.objects.all():
#         email = item.email
#
#         data = {
#             'email': email,
#             'name': name_lst,
#         }
#         html_content = render_to_string('account/email/email_ad_for_subscribers.html',
#                                         data)
#         msg = EmailMultiAlternatives(subject='Рассылка новых объявлений',
#                                      to=[email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
#
# @celery_app.task(name="send_sms_task")
# def send_sms_task(profile_id: int, secret: str) -> None:
#     profile = Profile.objects.get(id=profile_id)
#     account_sid = os.environ.get("ACCOUNT_SID")
#     auth_token = os.environ.get("AUTH_TOKEN")
#
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(
#         to=profile.phone_number,
#         from_='+13126294738',
#         body=secret)
#
#     print(message.sid)

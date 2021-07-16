from typing import Any

from django.contrib.auth.models import Group, User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

# from main.models import Auto, Profile, SMSlog, Subscriber

from .tasks import send_email_to_subscribers_task, send_sms_task


@receiver(post_save, sender=User)
def create_user_profile(sender: Any, instance: Any, created: Any, **kwargs: Any) -> None:
    if created:
        instance.groups.add(Group.objects.get_or_create(name='common_users')[0])


# def send_email_after_registration(sender: Any, instance: Any, created: Any, **kwargs: Any) -> None:
#     print('signals work')
#     user = instance
#     if created:
#         email = user.email
#         name = user.username
#         data = {
#             'email': email,
#             'name': name,
#         }
#         html_content = \
#             render_to_string('account/email/email_confirmation_message.html',
#                              data)
#         msg = EmailMultiAlternatives(subject='Регистрация нового пользователя',
#                                      to=[email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
#
# def send_email_to_subscribers(sender: Any, instance: Any, created: Any, **kwargs: Any) -> None:
#     """ send a msg when adding an ad"""
#
#     print('signals work!')
#     # user = instance
#     if created:
#
#         name = instance.name  # .encode('utf-8')
#         for item in Subscriber.objects.all():
#             email = item.email
#
#             data = {
#                 'email': email,
#                 'name': name,
#             }
#
#             send_email_to_subscribers_task.delay(email, data)
#
#
# post_save.connect(send_email_after_registration, sender=Profile)
# post_save.connect(send_email_to_subscribers, sender=Auto)
#
#
# @receiver(post_save, sender=Profile)
# def send_sms(sender: Any, instance: Any, created: Any, **kwargs: Any) -> None:
#     # profile=Profile.objects.get(id=instance.id)
#     sms_log = SMSlog.objects.create(profile=instance)
#     send_sms_task.s(instance.id, sms_log.secret).apply_async(countdown=3)

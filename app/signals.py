# app/signals.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from app.models import Message
# from notifications.models import Notification



# @receiver(post_save, sender=Message)
# def create_message_notification(sender, instance, created, **kwargs):
#     if created:
#         # Create a notification for the message receiver
#         Notification.objects.create(
#             recipient=instance.receiver,
#             actor=instance.sender,
#             verb='sent you a message',
#             target=instance
#         )

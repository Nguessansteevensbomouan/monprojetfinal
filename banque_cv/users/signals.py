from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from cv.models import CV

@receiver(post_save, sender=User)
def create_cv(sender, instance, created, **kwargs):
    if created:
        CV.objects.create(user=instance, titre=f"CV de {instance.username}", description="Mon CV")

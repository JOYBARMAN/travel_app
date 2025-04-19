from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from core.models import UserDetail, User, Context, DynamicBanner


@receiver(post_save, sender=User)
def create_user_related_model(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.get_or_create(user=instance)
        Context.objects.get_or_create(user=instance)
        DynamicBanner.objects.get_or_create(user=instance)

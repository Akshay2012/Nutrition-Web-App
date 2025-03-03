from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import profile
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


# post_save.connect(save_profile,sender=User)
# post_save.connect(create_profile,sender=User)


#----------OR--------
#@receiver(post_save,sender=User)   
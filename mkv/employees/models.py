import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=False)
    is_verified = models.BooleanField(default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
    sended_verification_on_email = models.BooleanField(default=False)
    invite_keys = models.ForeignKey("InviteKey", on_delete=models.CASCADE)


class InviteKey(models.Model):
    key = models.UUIDField('Unique Invite key UUID', default=uuid.uuid4)

    

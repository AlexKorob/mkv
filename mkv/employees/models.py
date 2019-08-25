import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=False)
    is_verified = models.BooleanField(default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
    sended_verification_on_email = models.BooleanField(default=False)
    invited_by_person = models.OneToOneField("User", on_delete=models.SET_NULL, null=True)
    invite_key = models.CharField(max_length=256, default="none")


class InviteKey(models.Model):
    key = models.UUIDField('Unique Invite key UUID', default=uuid.uuid4)
    user = models.ForeignKey("User", related_name="invite_keys", on_delete=models.CASCADE)

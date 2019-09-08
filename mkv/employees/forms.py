from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from .models import User, InviteKey


class UserCreateForm(UserCreationForm):
    UserCreationForm.error_messages = {
        'password_mismatch': "Паролі не співпадають",
    }

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "invite_key"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username):
            error_message = "Цей логін вже існує"
            raise ValidationError(error_message)
        elif len(username) <= 2:
            error_message = "Логін повинен містити не менше 3-х символів"
            raise ValidationError(error_message)
        return username

    def clean_first_name(self):
        if len(self.cleaned_data["first_name"]) <= 2:
            error_message = "Ім'я повинно містити не менше 3-х символів"
            raise ValidationError(error_message)
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if len(self.cleaned_data["last_name"]) <= 2:
            error_message = "Прізвище повинна містити не менше 3-х символів"
            raise ValidationError(error_message)
        return self.cleaned_data['last_name']

    def clean_invite_key(self):
        invite_key = self.cleaned_data["invite_key"]
        try:
            InviteKey.objects.get(key=invite_key)
            return invite_key
        except ObjectDoesNotExist:
            raise ValidationError("Ключ запрошення недійсний")

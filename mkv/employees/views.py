from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse, Http404
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model

from .forms import UserCreateForm
from .models import User, InviteKey


class Index(TemplateView):
    template_name = "employees/index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("employees:home"))
        return super().get(self, request, *args, **kwargs)


class Home(LoginRequiredMixin, TemplateView):
    template_name = "employees/home_page.html"


class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("employees:index"))


class VerifyEmail(View):
    def get(self, request, uuid):
        try:
            user = User.objects.get(verification_uuid=uuid, is_verified=False)
        except User.DoesNotExist:
            raise Http404("User does not exist or is already verified")

        user.is_verified = True
        user.save()

        return HttpResponsePermanentRedirect(reverse("products:index"))


class LogIn(FormView):
    template_name = 'employees/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy("employees:home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("employees:home"))
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            login(request, user)
            return self.form_valid(form)
        else:
            form.errors["login_or_password"] = form.errors["__all__"]
            return self.form_invalid(form)


class Registration(FormView):
    template_name = 'employees/registration.html'
    form_class = UserCreateForm
    success_url = reverse_lazy("employees:thanks_for_registration")

    def get(self, request, *args, **kwargs):
        print(dir(self.get_context_data()["form"]))
        print(self.get_context_data()["form"].errors)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("employees:home"))
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password2"])
            login(request, user)
            return self.form_valid(form)
        else:
            print(dir(self.get_context_data()))
            print(self.get_context_data())
            return self.form_invalid(form)


class ThanksForRegistration(LoginRequiredMixin, TemplateView):
    raise_exception = True
    template_name = "employees/thanks_for_registration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context


class ShowOwnInviteKeys(LoginRequiredMixin, TemplateView):
    raise_exception = True
    template_name = "employees/my_invite_keys.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["keys"] = InviteKey.objects.filter(user=self.request.user).values_list("key", flat=True)
        return context


@receiver(post_save, sender=get_user_model())
def add_invited_person_generate_keys(sender, instance=None, created=False, **kwargs):
    if created:
        invate_key = instance.invite_key
        user_who_gave_key = get_user_model().objects.get(invite_keys__key=invate_key)
        instance.invited_by_person = user_who_gave_key
        InviteKey.objects.get(key=invate_key).delete()
        InviteKey.objects.create(user=user_who_gave_key)
        for i in range(3):
            InviteKey.objects.create(user=instance)

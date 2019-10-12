from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class Monitoring(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        return render(request, "monitoring/graphs.html", {})

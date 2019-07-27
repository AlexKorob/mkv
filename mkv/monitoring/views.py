from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render


class Monitoring(View):

    def get(self, request):
        return render(request, "monitoring/graphs.html", {})

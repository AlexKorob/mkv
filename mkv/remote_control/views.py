import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class Command(LoginRequiredMixin, View):
    raise_exception = True
    available_commands = ("start", "stop", "reload")

    def post(self, request):
        data = json.loads(request.body)
        command = data.get("command", "")
        machine_id = data.get("machine_id", "")
        succes_response_handle = {"start": "Запит на ввімкнення МКV машини був відправлений",
                                  "stop": "Запит на зупинку МКV машини був відправлений",
                                  "reload": "Запит на перезавантаження МКМ машини був відправлений"}
        if (not command or command not in self.available_commands) or\
           (not machine_id or not machine_id.isdigit()):
            response = {"status": "ERROR", "info": "Вiдправленый запит не э дiйсним"}
        else:
            with open("../RSA/command.txt", "w") as file:
                file.write(command + f"::{machine_id}")
                response = {"status": "OK", "info": succes_response_handle[command]}
        return JsonResponse(response)

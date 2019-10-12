import json
import socket
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

SOCKET_FILE = "../RSA/echo.socket"


class Command(LoginRequiredMixin, View):
    raise_exception = True
    available_commands = ("start", "stop", "reload", "reset_sock_connection")

    def post(self, request):
        data = json.loads(request.body)
        command = data.get("command", "")
        machine_id = data.get("machine_id", "")
        succes_response_handle = {"start": "Запит на ввімкнення МКV машини був відправлений",
                                  "stop": "Запит на зупинку МКV машини був відправлений",
                                  "reload": "Запит на перезавантаження МКМ машини був відправлений",
                                  "reset_sock_connection": "Запит був вiдправлен!"}
        if (not command or command not in self.available_commands) or\
           (not machine_id or not machine_id.isdigit()):
            response = {"status": "ERROR", "info": "Вiдправленый запит не э дiйсним"}
        else:
            unix_sock_client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
            unix_sock_client.connect(SOCKET_FILE)
            if command == "reset_sock_connection":
                data = bytes(command, encoding="utf-8")
            else:
                data = bytes(command + f"::{machine_id}", encoding="utf-8")
            unix_sock_client.send(data)
            unix_sock_client.close()
            response = {"status": "OK", "info": succes_response_handle[command]}
        return JsonResponse(response)

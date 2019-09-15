from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class Monitoring(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        return render(request, "monitoring/graphs.html", {})

    ### NOT HERE, THIS will be ajax!
    # def post(self, request):
    #     available_commands = ("start", "stop", "reload")
    #     command = self.POST.get("command", "")
    #     succes_response_handle = {"start": "Запит на ввімкнення МКV машини був відправлений",
    #                               "stop": "Запит на зупинку МКV машини був відправлений",
    #                               "reload": "Запит на перезавантаження МКМ машини був відправлений"}
    #     if not command or command not in available_commands:
    #         response = "Вiдправленый запит не э дiйсным"
    #     else:
    #         with open("../../RSA/command.txt", "w") as file:
    #             file.write(command)
    #             respose = succes_response_handle[command]
    #     return render(request, "monitoring/graphs.html", {"response": response})

from django.shortcuts import render

from .forms import *

def getUsername(request):
    if request.method == 'POST':

        usernameFormObject = usernameForm(request.POST)
        passwordFormObject = passwordForm(request.POST)
        repeatPasswordFormObject = repeatPasswordForm(request.POST)

        if usernameFormObject.is_valid() and passwordFormObject.is_valid():
            print(usernameFormObject["username"].value())
            print(passwordFormObject["password"].value())
            print(repeatPasswordFormObject["repeatPassword"].value())

    else:
        usernameFormObject = usernameForm()
        passwordFormObject = passwordForm()
        repeatPasswordFormObject = repeatPasswordForm()

    return render(request, 'index.html',
                  {'usernameInput': usernameFormObject,
                   "passwordInput":passwordFormObject,
                   "repeatPasswordInput":repeatPasswordFormObject})


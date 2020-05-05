from django.shortcuts import render

from .forms import *

def getUsername(request):
    if request.method == 'POST':

        usernameFormObject = usernameForm(request.POST)
        passwordFormObject = passwordForm(request.POST)
        repeatPasswordFormObject = repeatPasswordForm(request.POST)

        if usernameFormObject.is_valid() and passwordFormObject.is_valid():

            usernameData =  usernameFormObject["username"].value()
            passwordData =  passwordFormObject["password"].value()
            repeatPasswordData = repeatPasswordFormObject["repeatPassword"].value()

            print(usernameData)
            print(passwordData)
            print(repeatPasswordData)

            if(passwordData!=repeatPasswordData):
                print("The passwords are not the same!")
            else:
                print("The passwords are the same!")
                

    else:
        usernameFormObject = usernameForm()
        passwordFormObject = passwordForm()
        repeatPasswordFormObject = repeatPasswordForm()

    return render(request, 'index.html',
                  {'usernameInput': usernameFormObject,
                   "passwordInput":passwordFormObject,
                   "repeatPasswordInput":repeatPasswordFormObject})


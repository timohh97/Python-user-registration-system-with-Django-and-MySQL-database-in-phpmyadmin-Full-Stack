import random
import pymysql

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
                database = pymysql.connect(host="localhost", user="root", passwd="", database="besucher")
                cursor = database.cursor()
                insertNewRowIntoUserTable(usernameData,passwordData,repeatPasswordData,cursor,database)


    else:
        usernameFormObject = usernameForm()
        passwordFormObject = passwordForm()
        repeatPasswordFormObject = repeatPasswordForm()

    return render(request, 'index.html',
                  {'usernameInput': usernameFormObject,
                   "passwordInput":passwordFormObject,
                   "repeatPasswordInput":repeatPasswordFormObject})




def getRowOfUserTable(i,cursor):
    cursor.execute("select * from user")
    result = cursor.fetchall()

    print(result[i])


def getColumnOfUserTable(columnName,cursor):
    cursor.execute("select " + columnName + " from user")
    result = cursor.fetchall()

    return result


def deleteRowOfUserTable(i,cursor,database):
    cursor.execute("select * from user")
    result = cursor.fetchall()
    print("Deleted the row: " + str(result[i]))

    idOfRow = str(result[i][0])

    cursor.execute("delete from user where id='" + idOfRow + "'")

    database.commit()


def deleteAllRows(cursor,database):
    cursor.execute("delete from user")
    database.commit()


def insertNewRowIntoUserTable(username, password, repeatedPassword,cursor,database):

    if(password != repeatedPassword):
        print("The passwords are not the same!")
        return None

    if(checkIfUsernameExists(username,cursor)):
        print("This username already exists!")
        return None

    id = random.randint(0, 10000000)

    while (checkIfIdExists(id,cursor)):
        id = random.randint(0, 10000000)

    cursor.execute(
        "insert into user (id,username,password) VALUES ('" + str(id) + "','" + username + "','" + password + "')")
    database.commit()



def checkIfIdExists(id,cursor):
    idColumn = getColumnOfUserTable("id",cursor)

    for element in idColumn:
        for entry in element:
         if(entry==id):
            return True

    return False


def checkIfUsernameExists(username,cursor):
    usernameColumn = getColumnOfUserTable("username",cursor)

    for element in usernameColumn:
        for entry in element:
            if (entry == username):
                return True

    return False
from django.http.response import HttpResponse
from django.shortcuts import render
import mysql.connector
from django.core.mail import send_mail
from django.conf import settings
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="shyam",
    passwd="shyam",
    database="logindata"
)
mycursor = mydb.cursor()
n=random.randint(100000,999999)


# Create your views here.
def updatepasshome(request):
    uemail = request.POST['Email']
    upass = request.POST['rpassword']
    ucpass = request.POST['conpassword']
    qur = "select no from login where Email='{}'".format(uemail)
    mycursor.execute(qur)
    result = mycursor.fetchone()
    list(result)
    if upass==ucpass:
        query = "UPDATE `login` SET `password` = '{}', `cpassword` = '{}' WHERE `login`.`no` = '{}'".format(upass,ucpass,result[0])
        mycursor.execute(query)
        mydb.commit()
        if query is not None:
            return render(request,'login/updatepass.html')
        else:
            return HttpResponse("Error")
    else:
        return HttpResponse("Password not match")

def acccreated(request):
    uname = request.POST['username']
    upass = request.POST['password']
    ucpass = request.POST['cpassword']
    uemail = request.POST['Email']
    qur = "select username or email from login where username='{}' or Email='{}'".format(uname,uemail)
    mycursor.execute(qur)
    result = mycursor.fetchall()
    if result:
        context = {
            'accalready':'username or email already taken'
        }
        return render(request,'login/signup.html',context)    
    else:
        if upass==ucpass:
            query = "INSERT INTO `login` (`no`, `username`, `password`, `cpassword`, `Email`) VALUES (NULL, '{}', '{}', '{}', '{}')".format(uname,upass,ucpass,uemail)
            mycursor.execute(query)
            mydb.commit()
            if query is not None:
                context = {
                    "acc" :"Account Created"
                }
                return render(request,'login/login.html',context)
            else:
                context = {
                    'accerror':'something went wrong'
                }
                return render(request,'login/signup.html',context)
        else:
            context = {
                'accpasserror':'password not match'
            }
            return render(request,'login/signup.html',context)
def loginhome(request):
    return render(request,'login/login.html')

def signuphome(request):
    return render(request,'login/signup.html')

def forgothome(request):
    return render(request,'login/forgot.html')

def resethome(request):
    uotp = request.POST['otp']
    if str(n)==uotp:
        return render(request,'login/resetpassword.html')
    else:
        return HttpResponse("error")

def otphome(request):
    umail = request.POST['Email']
    qur = "select email from login where Email='{}'".format(umail)
    mycursor.execute(qur)
    result = mycursor.fetchall()
    if result:
        subject = 'Reset Password'
        message = f"Hi Your reset OTP : {n}"
        email_from = 'extrause123409@gmail.com'
        recipient_list = [umail]
        send_mail( subject, message, email_from, recipient_list )
        if send_mail:
            return render(request,'login/otp.html')
        else:
            return HttpResponse("Something went wrong!")
    else:
        context = {
            'emailerror':'Please enter your registered email'
        }
        return render(request,'login/forgot.html',context)
def webhome(request):
    uname = request.POST['username']
    upass = request.POST['password']
    qur = "select username,Email,password from login where (username='{}' or Email='{}') and password='{}'".format(uname,uname,upass)
    mycursor.execute(qur)
    result = mycursor.fetchall()
    if result:
        return render(request,'main/home.html')
    else:
        context = {
            "wrong" :"username or password is wrong"
        }
        return render(request,'login/login.html',context)
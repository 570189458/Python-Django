import logging

from django.shortcuts import render

# Create your views here.
from lxm_p_w.service_lxm_p_w.userservice import userserve

logger = logging.getLogger("django")


def index(request):
    return render("log.html")


def register(request):
    return render("reg.html")


def login_action(request):
    print("login info")
    logger.info("login info")
    username = request.POST.get('UserName')
    password = request.POST.get('PassWord')
    us = userserve()
    array = us.do_login(username, password, request)
    if (array['state'] == 1):
        logger.info("登陆成功")
        return render('welcomeuser.html', {'UserName': request.session['UserName']})
    else:
        logger.info("登录失败")
        return render('log.html', {'msg': array['msg']})


def register_action(request):
    username = request.POST.get('UserName')
    password = request.POST.get('PassWord')
    repassword = request.POST.get('rePassWord')
    us = userserve()
    array = us.do_register(username, password, repassword, request)
    if (array['state'] == 1):
        return render('log.html', {'msg': array['msg']})
    else:
        return render('log.html', {'msg': array['msg']})

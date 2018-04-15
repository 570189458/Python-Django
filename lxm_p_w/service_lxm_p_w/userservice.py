from django.template.defaultfilters import first

from lxm_p_w.models import User


class userserve():
    def do_login(self, username, password, request):
        u = User.objects.filter(UserName=username, PassWord=password), first()
        print("登陆")
        if u is not None:
            msg = "登陆成功!"
            state = 1
            request.session['UserName'] = u.UserName
            request.session['UserId'] = u.UserId
        else:
            request.session['UserName'] = "请登陆"
            request.session['UserId'] = None
            msg = "账号或密码错误！"
            state = 0
        array = {
            'msg': msg,
            'state': state
        }
        return array

    def do_register(self, username, password, repassword, request):
        u = User.objects.filter(UserName=username), first()
        if u is not None:
            msg = "用户名已被注册！"
            state = 0
            request.session['UserName'] = u.TrueName
            request.session['UserId'] = u.UserId
        else:
            if password == repassword:
                U = User()
                U.UserName = username
                U.PassWord = password
                U.save()
                msg = "注册成功!"
                state = 1
            else:
                msg = "两次输入的密码不同！"
                state = 0
        array = {
            'msg': msg,
            'state': state
        }
        return array

import traceback

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

from ReturnEnum import ReturnEnum
from app.function import common


# 用户名密码登录
@csrf_exempt
def do_login(request):
    request_data = common.post_json_param(request)
    username = request_data.get('username', '').strip()
    password = request_data.get('password', '').strip()
    login_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
    try:
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            login_result['code'] = ReturnEnum.ER_SUCCESS().code
            login_result['msg'] = ReturnEnum.ER_SUCCESS().msg
    except Exception as e:
        login_result['code'] = ReturnEnum.ER_SERVER_ERROR().code
        login_result['msg'] = traceback.format_exc()
    return JsonResponse(login_result)


# 登出
def do_logout(request):
    logout_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
    try:
        logout(request)
        logout_result['code'] = ReturnEnum.ER_SUCCESS().code
        logout_result['msg'] = ReturnEnum.ER_SUCCESS().msg
    except Exception as e:
        logout_result['code'] = ReturnEnum.ER_SERVER_ERROR().code
        logout_result['msg'] = traceback.format_exc()
    return JsonResponse(logout_result)


# 获取用户信息
def user_info(request):
    user_data = {}
    result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': user_data}
    try:
        if request.user:
            user_data['id'] = request.user.id
            user_data['username'] = request.user.username
            user_data['first_name'] = request.user.first_name
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
            result['data'] = user_data
    except  Exception as e:
        result['code'] = ReturnEnum.ER_SERVER_ERROR().code
        result['msg'] = traceback.format_exc()
    return JsonResponse(result)

import traceback


# 获取当前登录用户名
def f_get_login_user_name(request):
    first_name = ''
    try:
        first_name = request.user.first_name
    except Exception as e:
        traceback.print_exc()
    return first_name

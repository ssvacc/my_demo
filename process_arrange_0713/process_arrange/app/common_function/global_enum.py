from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.class_function.PageFunction import PageFunction

# 获取枚举下拉框选项
@csrf_exempt
def get_enum_options_by_name(request):
    s_enum_name = request.GET.get('s_enum_name', '').strip()
    result = PageFunction.get_enum_options_by_name(s_enum_name)
    return JsonResponse(result)

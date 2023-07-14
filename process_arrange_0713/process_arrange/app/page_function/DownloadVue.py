import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import PAGE_CONFIG_INFO
from ReturnEnum import ReturnEnum
from app.class_function.InterfaceFunction import InterfaceFunction

class DownloadVue(object):

    @staticmethod
    def get_config_by_page(s_page_name):
        # 模拟查询页面配置库，得到生成页面的接口函数
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        result['data']['s_function_name'] = 'PageDemo::create_demo_page'
        result['data']['o_function_param'] = {"s_page_name":s_page_name}
        return result


@csrf_exempt
def downloadVueFile(request):
    s_page_name = request.GET.get('s_page_name', '').strip()
    config_result = DownloadVue.get_config_by_page(s_page_name)
    s_vue_component_content = ''
    s_vue_component_file_name = ''
    if config_result['code'] == ReturnEnum.ER_SUCCESS().code:
        # 执行通用流程接口函数
        s_function_name = config_result['data']['s_function_name']
        o_function_param = config_result['data']['o_function_param']
        interface_function_result = InterfaceFunction.run_interface_function(s_function_name, o_function_param)
        if interface_function_result['code'] == ReturnEnum.ER_SUCCESS().code:
            o_function_result = interface_function_result['data']['o_function_result']
            # 生成页面的接口函数执行成功
            if o_function_result['code'] == ReturnEnum.ER_SUCCESS().code:
                s_vue_component_content = o_function_result['data']['s_vue_component_content']
                s_vue_component_file_name = o_function_result['data']['s_vue_component_file_name']
    if s_vue_component_content:
        response = HttpResponse(content_type='vue')
        response.content = s_vue_component_content  # 直接从IO中获取数据
        response['Content-Disposition'] = 'attachment; filename=%s' % s_vue_component_file_name
        BASE_PATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + PAGE_CONFIG_INFO.VUE_OUTPUT_PATH.value
        vue_file_url = BASE_PATH + s_vue_component_file_name
        os.remove(vue_file_url)
        return response


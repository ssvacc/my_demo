#    Copyright (c)  Fancy qube.com
#    @Author : ni heng
#    @Date: 2023/3/16 下午4:50
#    @Description:
# -*- coding: utf-8 -*-
import inspect
import traceback

from django.db.models import Count
from ConstEnum import FuncProcessCode, FuncProcessName
from ReturnEnum import ReturnEnum
from app.function import execute_function
from app.table.t_public_custom_function_param_model import t_public_custom_function_param \
    as TPublicCustomFunctionParam
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_custom_function_model import t_public_custom_function as TPublicCustomFunction
from app.table.t_public_custom_function_relevance_model import \
    t_public_custom_function_relevance as TPublicCustomFunctionRelevance


class InterfaceFunction(object):

    # 接口函数：通用流程函数
    @staticmethod
    def run_interface_function(s_function_name, o_function_param, **kwargs):
        """通用流程函数"""
        if kwargs.get('s_function_name'):
            s_function_name = kwargs.get('s_function_name')
        if kwargs.get('o_function_param'):
            o_function_param = kwargs.get('o_function_param')
        o_interface_function_result = dict()
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": o_interface_function_result}
        custom_function = TPublicCustomFunction.objects.filter(task_name=s_function_name).first()
        if custom_function is None:
            # 没有流程，认为是个函数
            found_function_flag = False
            query_function_result = dict()
            public_function = TPublicFunction.objects.filter(function_name=s_function_name).first()
            if public_function:
                query_function_result = InterfaceFunction.query_function_by_id(public_function.id)
                if query_function_result['code'] == ReturnEnum.ER_SUCCESS().code:
                    found_function_flag = True
            if not found_function_flag:
                result['code'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().code
                result['msg'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().msg + s_function_name
                return result
            s_function_name = query_function_result['data']['s_function_name']
            obj_function = query_function_result['data']['obj_function']
            o_interface_function_result, o_function_param_result = InterfaceFunction.run_function(s_function_name, obj_function, o_function_param)
        else:
            # 流程，执行多个函数
            a_function_relevance = TPublicCustomFunctionRelevance.objects.filter(task_id=custom_function.id).order_by('function_order')
            interface_result = InterfaceFunction.execute_custom_function(a_function_relevance, o_function_param)
            if interface_result['code'] == ReturnEnum.ER_SUCCESS().code:
                # 过滤出流程的返回值
                o_interface_result = interface_result['data']
                a_custom_function_param = TPublicCustomFunctionParam.objects.filter(task_id=custom_function.id) \
                    .filter(type=FuncProcessCode.FUNCTION_PARAM_RETURN.value)
                o_interface_function_result = InterfaceFunction.get_interface_result(a_custom_function_param, o_interface_result)
            else:
                o_interface_function_result = interface_result
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        result['data'] = dict()
        result['data']['o_function_result'] = o_interface_function_result
        return result

    # 接口函数：根据函数id获取函数名和函数对象
    @staticmethod
    def query_function_by_id(i_function_id, **kwargs):
        """根据函数id获取函数名和函数对象"""
        query_function_result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        if kwargs.get('i_function_id'):
            i_function_id = kwargs.get('i_function_id')
        s_function_name = ''
        request_data = dict()
        request_data['function_id'] = i_function_id
        try:
            # 获取函数和函数名
            obj_function, s_function_name = execute_function.get_function_obj(**request_data)
            query_function_result['code'] = ReturnEnum.ER_SUCCESS().code
            query_function_result['msg'] = ReturnEnum.ER_SUCCESS().msg
            query_function_result['data']['s_function_name'] = s_function_name
            query_function_result['data']['obj_function'] = obj_function
        except Exception as e:
            query_function_result = {"code": ReturnEnum.ER_FUNCTION_NOT_FOUND().code,
                                     "msg": ReturnEnum.ER_FUNCTION_NOT_FOUND().msg + s_function_name, "data": dict()}
        return query_function_result

    # 接口函数：根据函数id获取函数名和函数对象
    @staticmethod
    def query_function(s_function_name, **kwargs):
        """根据函数id获取函数名和函数对象"""
        query_function_result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        if kwargs.get('s_function_name'):
            s_function_name = kwargs.get('s_function_name')
        request_data = dict()
        request_data['s_function_name'] = s_function_name
        try:
            # 获取函数和函数名
            obj_function = execute_function.get_function_by_name(s_function_name)
            query_function_result['code'] = ReturnEnum.ER_SUCCESS().code
            query_function_result['msg'] = ReturnEnum.ER_SUCCESS().msg
            query_function_result['data']['obj_function'] = obj_function
        except Exception as e:
            query_function_result = {"code": ReturnEnum.ER_FUNCTION_NOT_FOUND().code,
                                     "msg": ReturnEnum.ER_FUNCTION_NOT_FOUND().msg + s_function_name, "data": dict()}
        return query_function_result

    # 运行函数
    @staticmethod
    def run_function(s_function_name, obj_function, o_function_param):
        """运行函数"""
        o_function_param_result = dict()
        try:
            # 运行函数，对内部多个小函数不做参数返回值校验，默认函数是调试通过的
            run_function_result = obj_function(**o_function_param)
            # 更新执行结果到参数对象
            if run_function_result['code'] == ReturnEnum.ER_SUCCESS().code and run_function_result['data']:
                o_function_param.update(run_function_result['data'])
            o_function_param_result = o_function_param
        except Exception as e:
            err_msg = traceback.format_exc()
            run_function_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': s_function_name + '函数执行出错!' + err_msg,
                                   'data': dict()}
        return run_function_result, o_function_param_result

    # 执行流程函数
    @staticmethod
    def execute_custom_function(a_function_relevance, o_function_param):
        """运行流程函数"""
        interface_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        for relevance in a_function_relevance:
            query_function_result = InterfaceFunction.query_function_by_id(relevance.function_id)
            if query_function_result['code'] != ReturnEnum.ER_SUCCESS().code:
                return query_function_result
            obj_function = query_function_result['data']['obj_function']
            s_function_name = query_function_result['data']['s_function_name']
            run_function_result, o_function_param_result = InterfaceFunction.run_function(s_function_name, obj_function, o_function_param)
            if run_function_result['code'] == ReturnEnum.ER_SUCCESS().code:
                o_function_param = o_function_param_result
            else:
                return run_function_result
        interface_result['code'] = ReturnEnum.ER_SUCCESS().code
        interface_result['msg'] = ReturnEnum.ER_SUCCESS().msg
        interface_result['data'] = o_function_param
        return interface_result

    # 流程结果集获取，从参数字典中取出需要的返回值
    @staticmethod
    def get_interface_result(a_custom_function_param, o_function_result):
        """过滤出流程结果集"""
        o_interface_result = {}
        for custom_function_param in a_custom_function_param:
            custom_function_param_dict = custom_function_param.object_to_dict()
            param_name = custom_function_param_dict['param_name']
            o_interface_result.update({param_name: o_function_result[param_name]})
        return o_interface_result

    # 接口函数：统计各开发责任人的接口函数
    @staticmethod
    def function_statistics(dt2_start_time, dt2_end_time, s_principal=None, **kwargs):
        """统计各开发责任人的接口函数"""
        statistics_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        if kwargs.get('dt2_start_time'):
            dt2_start_time = kwargs.get('dt2_start_time')
        if kwargs.get('dt2_end_time'):
            dt2_end_time = kwargs.get('dt2_end_time')
        if kwargs.get('s_principal'):
            s_principal = kwargs.get('s_principal')
        if not dt2_start_time or not dt2_end_time:
            statistics_result['code'] = ReturnEnum.ER_LACK_PARAMETER().code
            statistics_result['msg'] = ReturnEnum.ER_LACK_PARAMETER().msg
            return statistics_result
        query = TPublicFunction.objects.filter(status=FuncProcessCode.STATUS_PUBLISH.value)
        if s_principal:
            query = query.filter(s_principal=s_principal)
        query = query.filter(publish_time__range=(dt2_start_time, dt2_end_time))
        function_id_list = []
        for item in query:
            function_id_list.append(dict(id=item.id, s_principal=item.s_principal))
        data = query.values("id").values("s_principal").annotate(count=Count("id")).order_by('-count')
        a_function_statistics = []
        for item in data:
            # 查询函数代码行数
            sum_code_line_number = 0
            for function_item in function_id_list:
                if item['s_principal'] == function_item['s_principal']:
                    i_function_id = function_item['id']
                    s_function_body_content = ''
                    function_content_result = InterfaceFunction.query_function_content_by_id(i_function_id)
                    if function_content_result['code'] == ReturnEnum.ER_SUCCESS().code:
                        s_function_body_content = function_content_result['data']['s_function_body_content']
                    code_line_result = InterfaceFunction.get_function_code_line(s_function_body_content)
                    if code_line_result['code'] == ReturnEnum.ER_SUCCESS().code:
                        i_code_line_number = code_line_result['data']['i_code_line_number']
                        sum_code_line_number += i_code_line_number
            o_function_statistics = dict(s_principal=item['s_principal'], i_function_number=item['count'],
                                         i_code_line_number=sum_code_line_number)
            a_function_statistics.append(o_function_statistics)
        statistics_result['code'] = ReturnEnum.ER_SUCCESS().code
        statistics_result['msg'] = ReturnEnum.ER_SUCCESS().msg
        statistics_result['data']['a_function_statistics'] = a_function_statistics
        res = InterfaceFunction.aa(a_function_statistics)
        print(res)
        return statistics_result


    @staticmethod
    def query_function_content(s_function_name, **kwargs):
        """"获取函数体内容"""
        function_content_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        if kwargs.get('s_function_name'):
            s_function_name = kwargs.get('s_function_name')
        query_function_result = InterfaceFunction.query_function(s_function_name)
        if query_function_result['code'] != ReturnEnum.ER_SUCCESS().code:
            return query_function_result
        obj_function = query_function_result['data']['obj_function']
        s_function_body_content = inspect.getsource(obj_function)
        function_content_result['code'] = ReturnEnum.ER_SUCCESS().code
        function_content_result['data']['s_function_body_content'] = s_function_body_content
        function_content_result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return function_content_result


    # 接口函数：获取函数体内容。入参：i_function_id:函数id
    @staticmethod
    def query_function_content_by_id(i_function_id, **kwargs):
        """"获取函数体内容"""
        function_content_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        if kwargs.get('i_function_id'):
            i_function_id = kwargs.get('i_function_id')
        query_function_result = InterfaceFunction.query_function_by_id(i_function_id)
        if query_function_result['code'] != ReturnEnum.ER_SUCCESS().code:
            return query_function_result
        obj_function = query_function_result['data']['obj_function']
        s_function_body_content = inspect.getsource(obj_function)
        function_content_result['code'] = ReturnEnum.ER_SUCCESS().code
        function_content_result['msg'] = ReturnEnum.ER_SUCCESS().msg
        function_content_result['data']['s_function_body_content'] = s_function_body_content
        return function_content_result

    # 接口函数：获取函数体代码行数。
    @staticmethod
    def get_function_code_line(s_function_body_content, **kwargs):
        """"获取函数体代码行数"""
        code_line_result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        if kwargs.get('s_function_body_content'):
            s_function_body_content = kwargs.get('s_function_body_content')
        i_code_line_number = 0
        for line in s_function_body_content.splitlines():
            line = line.strip()
            if len(line) != 0 and not line.startswith(FuncProcessName.EXPLANATION_CODE.value) \
                    and not line.startswith(FuncProcessName.DEF_CODE.value) and not line.startswith(
                FuncProcessName.ANNOTATION_CODE.value):
                i_code_line_number += 1
        code_line_result['code'] = ReturnEnum.ER_SUCCESS().code
        code_line_result['msg'] = ReturnEnum.ER_SUCCESS().msg
        code_line_result['data']['i_code_line_number'] = i_code_line_number
        return code_line_result

    # 获取已审核、已发布状态的接口函数列表
    @staticmethod
    def get_examine_function():
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        try:
            a_function_config = list()
            function_objs = TPublicFunction.objects.filter(status__in=(FuncProcessCode.STATUS_RELEASE.value, FuncProcessCode.STATUS_PUBLISH.value)).order_by("class_name")
            if function_objs:
                for function_obj in function_objs:
                    o_function_config = {
                        "i_function_id": function_obj.id,
                        "s_class_name": function_obj.class_name,
                        "s_interface_function_name": function_obj.function_name,
                    }
                    a_function_config.append(o_function_config)

            result["code"] = ReturnEnum.ER_SUCCESS().code
            result["msg"] = ReturnEnum.ER_SUCCESS().msg
            result["data"] = {
                "a_function_config": a_function_config
            }
        except Exception as ex:
            result["code"] = ReturnEnum.ER_SERVER_ERROR().code
            result["msg"] = f"""{ReturnEnum.ER_SERVER_ERROR().msg}: {str(ex)}"""
        return result

    # 根据接口函数id获取接口函数列表
    @staticmethod
    def query_function_list_by_name_list(a_function_name):
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        try:
            a_function_config = list()
            function_objs = TPublicFunction.objects.filter(function_name__in=a_function_name).order_by("class_name")
            if function_objs:
                for function_obj in function_objs:
                    o_function_config = {
                        "i_function_id": function_obj.id,
                        "s_class_name": function_obj.class_name,
                        "s_interface_function_name": function_obj.function_name,
                    }
                    a_function_config.append(o_function_config)
            result["code"] = ReturnEnum.ER_SUCCESS().code
            result["msg"] = ReturnEnum.ER_SUCCESS().msg
            result["data"] = {
                "a_function_config": a_function_config
            }
        except Exception as ex:
            result["code"] = ReturnEnum.ER_SERVER_ERROR().code
            result["msg"] = f"""{ReturnEnum.ER_SERVER_ERROR().msg}: {str(ex)}"""
        return result

    # 将已发布状态的接口函数置为 已审核
    @staticmethod
    def reset_publish_to_examine_status(a_function_name):
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        try:
            TPublicFunction.objects.filter(function_name__in=a_function_name).filter(status=FuncProcessCode.STATUS_PUBLISH.value).update(status=FuncProcessCode.STATUS_RELEASE.value,
                                                                                                                                         publish_person=None,
                                                                                                                                         publish_time=None)
            result["code"] = ReturnEnum.ER_SUCCESS().code
            result["msg"] = ReturnEnum.ER_SUCCESS().msg
        except Exception as ex:
            result["code"] = ReturnEnum.ER_SERVER_ERROR().code
            result["msg"] = f"""{ReturnEnum.ER_SERVER_ERROR().msg}: {str(ex)}"""
        return result

    @staticmethod
    def aa(a_function_statistics, **kwargs):
        try:
            print(a_function_statistics)
            for index, o_function_statistics in enumerate(a_function_statistics):
                s_principal = o_function_statistics.get("s_principal")
                print(s_principal)
        except Exception as ex:
            traceback.print_exc()
            pass
        result = {'code': ReturnEnum.ER_SUCCESS().code, 'msg': ReturnEnum.ER_SUCCESS().msg, 'data': dict()}
        return result
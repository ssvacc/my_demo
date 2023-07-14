import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode, FuncProcessName
from ReturnEnum import ReturnEnum
from app.custom_function.process_function import run_query_sql
from app.function import common
from app.table.t_public_error_code_model import t_public_error_code as TPublicErrorCode
from app.table.t_public_params_model import t_public_params as TPublicParams
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_custom_function_model import t_public_custom_function as TPublicCustomFunction
from app.table.other_app_table.reference_comments_table import t_online_comment_info, t_online_comment_mention


# t_online_comment_info:评论信息
# t_online_comment_mention:提及人员
# 获取评论信息，审核意见
@csrf_exempt
def get_comment_res(request):
    result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
    try:
        data_id = int(request.GET.get("data_id"))
        comment_table_type = int(request.GET.get("comment_table_type"))
        first_name = common.get_first_name(request)
        related_person = get_it_user()
        query = t_online_comment_info.objects.filter(app_label=FuncProcessName.FUNC_PROCESS_APP.value) \
            .filter(data_id=data_id).filter(model_name=FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value)
        # query, related_person = query_comment_person(data_id, comment_table_type, first_name)
        # 相关人员，创建人，当前人，审核人
        result['data']["related_person"] = related_person
        comment_list = query.order_by('-id')
        comment_dict_list = []
        for comment in comment_list:
            comment_dict = comment.object_to_dict()
            comment_mention_list = t_online_comment_mention.objects.filter(comment_id=comment.id)
            comment_mention_dict_list = []
            for mention in comment_mention_list:
                mention_dict = mention.object_to_dict()
                mention_dict['mention_person_self'] = False
                if mention.mention_person == first_name:
                    mention_dict['mention_person_self'] = True
                comment_mention_dict_list.append(mention_dict)
            comment_dict['comment_mention_list'] = comment_mention_dict_list
            comment_dict_list.append(comment_dict)
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        result["data"]['comment_list'] = comment_dict_list
    except Exception as ex:
        result["code"] = ReturnEnum.ER_FAIL().code
        result["msg"] = str(ex)
        import traceback
        traceback.print_exc()
    return JsonResponse(result)


# def query_comment_person(data_id, comment_table_type, first_name):
#     related_person = []
#     app_label = FuncProcessName.FUNC_PROCESS_APP.value
#     query = t_online_comment_info.objects.filter(app_label=app_label).filter(data_id=data_id)
#     query = query.filter(model_name=FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value)
#     if comment_table_type == FuncProcessCode.TABLE_TYPE_PARAM.value:
#         related_person = get_query_person(TPublicParams, FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value,
#                                           data_id, related_person)
#     elif comment_table_type == FuncProcessCode.TABLE_TYPE_FUNCTION.value:
#         related_person = get_query_person(TPublicFunction, FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value,
#                                           data_id, related_person)
#     elif comment_table_type == FuncProcessCode.TABLE_TYPE_TASK.value:
#         related_person = get_query_person(TPublicCustomFunction, FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value,
#                                           data_id, related_person)
#     else:
#         related_person = get_query_person(TPublicErrorCode, FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value,
#                                           data_id, related_person)
#     if first_name not in related_person:
#         related_person.append(first_name)
#     return query, related_person


def get_query_person(model, data_id, related_person):
    data_obj = model.objects.filter(id=data_id).first()
    if hasattr(data_obj, 'author') and data_obj.author and data_obj.author not in related_person:
        related_person.append(data_obj.author)
    if hasattr(data_obj, 'create_person') and data_obj.create_person and data_obj.create_person not in related_person:
        related_person.append(data_obj.create_person)
    if hasattr(data_obj,
               'release_person') and data_obj.release_person and data_obj.release_person not in related_person:
        related_person.append(data_obj.release_person)
    return related_person


# 已读评论
@csrf_exempt
def read_comment(request):
    result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
    comment_mention_id = request.GET.get("id")
    first_name = common.get_first_name(request)
    comment_mention = t_online_comment_mention.objects.filter(id=comment_mention_id).first()
    if comment_mention.mention_person == first_name:
        comment_mention.mention_read = FuncProcessCode.COMMENT_READ.value
        comment_mention.read_time = common.getNowTimeStamp()
        comment_mention.save()
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
    return JsonResponse(result)


# 新增评论(流程编排)
@csrf_exempt
def add_comment(request):
    result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
    try:
        request_data = json.loads(request.body.decode().replace("'", "\""))
        comment_table_type = int(request_data.get("comment_table_type"))
        app_label = FuncProcessName.FUNC_PROCESS_APP.value
        data_id = int(request_data.get("data_id"))
        comment_desc = request_data.get("comment_desc")
        comment_person = common.get_first_name(request)
        comment_time = common.getNowTimeStamp()
        model_name = FuncProcessName.PUBLIC_CUSTOM_FUNCTION.value
        if comment_table_type == FuncProcessCode.TABLE_TYPE_PARAM.value:
            model_cn_name = FuncProcessName.PUBLIC_PARAM_CN.value
        elif comment_table_type == FuncProcessCode.TABLE_TYPE_FUNCTION.value:
            model_cn_name = FuncProcessName.PUBLIC_FUNCTION_CN.value
        elif comment_table_type == FuncProcessCode.TABLE_TYPE_TASK.value:
            model_cn_name = FuncProcessName.PUBLIC_CUSTOM_FUNCTION_CN.value
        else:
            model_cn_name = FuncProcessName.PUBLIC_ERROR_CODE_CN.value
        comment_info = t_online_comment_info(
            app_label=app_label,
            data_id=data_id,
            comment_desc=comment_desc,
            comment_person=comment_person,
            comment_time=comment_time,
            model_name=model_name,
            model_cn_name=model_cn_name)
        comment_info.save()
        if comment_info.id is None:
            return
        mention_person_list = request_data.get("mention_person_list")
        for mention_person in mention_person_list:
            if mention_person:
                comment_mention = t_online_comment_mention(
                    comment_id=comment_info.id,
                    mention_person=mention_person,
                    mention_read=FuncProcessCode.COMMENT_NO_READ.value)
                comment_mention.save()
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
    except Exception as ex:
        result["msg"] = str(ex)
        import traceback
        traceback.print_exc()
    return JsonResponse(result)


@csrf_exempt
def get_it_user_res(request):
    result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
    try:
        user_list = get_it_user()
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        result['data']["it_user"] = user_list
    except Exception as ex:
        result["msg"] = str(ex)
        import traceback
        traceback.print_exc()
    return JsonResponse(result)


def get_it_user():
    # execute_res = execute_common_sql(ETaskManage.IT_USER_LIST_SQL.value, [])
    # it_user_list = execute_res.data
    user_list = ['盛荣凯', '邢鑫', '倪恒', '王恒', '蔡之其', '张创', '贾博文', '严旭', '周秋余', '王新雨', '宋增增', '蔡杨林', '徐国锋']
    # for it_user in it_user_list:
    #     user_list.append(it_user['label'])
    return user_list


# 获取未读的评论数据
def get_no_comment_list(model_cn_name, s_login_name):
    SQL = "SELECT distinct i.data_id from t_online_comment_info i left join t_online_comment_mention m on i.id=m.comment_id where i.app_label='func_process_app' and m.mention_read=0 and i.model_cn_name='%s' " % model_cn_name +" and m.mention_person= '%s'" % s_login_name
    data_id_list = run_query_sql(SQL).data
    id_list = []
    for data_id in data_id_list:
        for i in data_id:
            id_list.append(i)
    return id_list

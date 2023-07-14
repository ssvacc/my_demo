
# 演示函数



def show_colour(color):
    return "这是" + color + "色"


# import json
#
# # Create your views here.
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# from ReturnEnum import ReturnEnum
# from app import models
# from process_arrange.table.params_model import Params
# from rest_framework.views import APIView
#
# # class ParamsView(APIView):
#
#
# @csrf_exempt
# def param_demo(request):
#     return JsonResponse({'name':'python'})
#
#
# def param_add(request):
#     params = Params(param_name='max_size', param_desc='最大尺寸')
#     # params = models.Params.objects.create(username=name, password=password)
#     params.save()
#
#
# def param_update(request):
#     params = models.Params.objects.get(id=3)
#     params.param_name = 'max_size'
#     params.param_desc = '最大的尺寸'
#     params.save()
#
#
# def param_getById(request):
#     # params = models.Params.objects.filter(id__gt=1).order_by("-id")[:2]
#     params = models.Params.objects.get(id=3)
#     return params
#
#
# def param_list(request):
#     params = models.Params.objects.all()
#     return params
#
#
# def param_list_res(request):
#     res = {"code": ReturnEnum.SUCCESS().code, "msg": "Success!", "data": None}
#     params = models.Params.objects.all()
#     return params
#
#
# def param_del(request):
#     models.Params.objects.get(id=3).delete()
#
#
# # def json_translate(request):
# #     simple_dict = {'name': 'zxy', 'age': 21}
# #     file_to_write = ""
# #     print(file_to_write)
# #     print(type(file_to_write))
# #     # 进行json序列化,然后写入simple_dict.txt文件中
# #     json.dump(simple_dict, file_to_write)
# #     print(file_to_write)
#
# #
# # def translate_json(request):
# #         loaded_simple_dict = json.load(file_to_read)
# #         print(loaded_simple_dict)
# #         print(type(loaded_simple_dict))
#
#
#
# @csrf_exempt
# def he_he(request):
#     res = {"code": ReturnEnum.SUCCESS().code, "msg": "Success!", "data": None}
#     # 增
#     # he_add(request)
#     # 改
#     # he_update(request)
#     # 查
#     # params = param_getById(request)
#     # print(params.param_name)
#     params = param_list(request)
#     for aa in params:
#         print(aa.param_name)
#
#     # params = he_list(request)
#     # json_translate(request)
#     # print("1111111111111")
#     # translate_json(request)
#     # 删
#     # he_del(request)
#     # print(params)
#     # params1 = {}
#     # params1['param_name'] = params.param_name
#     # params1['param_desc'] = params.get('param_desc')
#
#     # data = {'name': 'nanbei', 'age': 18}
#     # # 将Python对象编码成json字符串
#     # jsonStr = json.dumps(params1)
#     # print(jsonStr)
#     # res["data"] = jsonStr
#
#     # print(params.param_name, params.param_desc)
#     # he_update(request)
#     # seller_obj = models.Params.objects.create(username=name, password=password)
#     # seller_obj = models.Params.objects.get(id=3).delete()
#     res["data"] = "params"
#     return JsonResponse(res)

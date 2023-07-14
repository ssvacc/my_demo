# -*- coding: utf-8 -*-
import traceback
from copy import copy
from io import BytesIO
from PIL import Image
from urllib.request import urlopen

import xlsxwriter
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.function import common
from app.class_function.InterfaceFunction import InterfaceFunction
from app.table.t_software_develop_standard_model import t_software_develop_standard
from ConstEnum import FuncProcessName
from ReturnEnum import ReturnEnum

import xlwt
import xlrd

@csrf_exempt
def fun_get_software_standard_data(request):
    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    return JsonResponse(result)


#  新增规范接口
@csrf_exempt
def standard_add_res(request):
    res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    s_operator = request.user.first_name
    if s_operator not in FuncProcessName.STANDARD_MANAGER.value:
        return JsonResponse(res)
    o_develop_require_specification = common.post_json_param(request)
    kwargs = {'s_function_name': FuncProcessName.DRS_ADD.value,
              'o_function_param': dict(o_develop_require_specification=o_develop_require_specification, s_operator=s_operator)}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    return JsonResponse(result)


# 编辑规范接口
@csrf_exempt
def update_standard(request):
    res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    s_operator = request.user.first_name
    if s_operator not in FuncProcessName.STANDARD_MANAGER.value:
        return JsonResponse(res)
    o_develop_require_specification = common.post_json_param(request)
    kwargs = {'s_function_name': FuncProcessName.DRS_EDIT.value,
              'o_function_param': dict(o_develop_require_specification=o_develop_require_specification, s_operator=s_operator)}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    return JsonResponse(result)


# 删除规范的接口
@csrf_exempt
def standard_del_res(request):
    res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg + '请联系李萌萌进行规范表操作!', "data": None}
    first_name = request.user.first_name
    if first_name not in FuncProcessName.STANDARD_MANAGER.value:
        return JsonResponse(res)
    o_develop_require_specification = common.post_json_param(request)
    i_develop_require_specification_id = o_develop_require_specification.get('i_develop_require_specification_id')
    kwargs = {'s_function_name': FuncProcessName.DRS_DEL.value,
              'o_function_param': dict(i_develop_require_specification_id=i_develop_require_specification_id)}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    return JsonResponse(result)


# 图片上传的接口
@csrf_exempt
def fun_add_pic(request):
    res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    first_name = request.user.first_name
    if first_name not in FuncProcessName.STANDARD_MANAGER.value:
        return JsonResponse(res)
    standard_id = request.POST.get('i_develop_require_specification_id')  # 数据id
    image_obj = request.FILES.get('img_obj')  # 文件对象
    suffix = image_obj.name.split('.')[-1]
    v_file_name = f"standard_{standard_id}" + '.' + suffix
    kwargs = {'s_function_name': FuncProcessName.UPLOAD_OSS.value,
              'o_function_param': dict(v_oss_path=FuncProcessName.DRS_OSS_PATH.value,
                                            v_file_name=v_file_name,
                                            v_file_object=image_obj)}
    res = InterfaceFunction.run_interface_function(**kwargs)
    img_url = res['data']['o_function_result']['data']['v_oss_url']
    request_data = t_software_develop_standard.objects.get(id=standard_id)
    request_data.example_pic = img_url
    request_data.save()
    return JsonResponse(res)


def write_to_cell(sheet, line_number, column_number, data):
    if data:
        sheet.write(line_number, column_number, data)
    return column_number + 1

def write_to_cell2(sheet, cell_location, data):
    if data:
        sheet.write(cell_location, data)


@csrf_exempt
def export_excel0(request):
    """导出不带图片的excel"""
    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    if result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(result)
    data_list = result['data']['a_develop_require_specification']
    wb = xlwt.Workbook(encoding="utf-8")
    sheet_name = '开发规范'
    sheet = wb.add_sheet(sheet_name)
    # 设置各列宽度
    column_width_list = [1500, 30000, 10000, 5000, 5000, 5000, 2000, 5000]
    for index, column_width in enumerate(column_width_list):
        sheet.col(index).width = column_width
    # 表格第一行为表头内容
    head_fields = ['序号', '开发规范', '样例图片', '规范类别', '对应考核人', '备注信息', '提交人', '更新时间']
    for index, field in enumerate(head_fields):
        sheet.write(0, index, field)
    for index, item in enumerate(data_list):
        # 行号，下移一行，为表头留空间
        line_number = index + 1
        column_number = 0
        line_data = [line_number, item['s_desc'], item['s_pic_url'], item['e_develop_require_specification_type'],
                     item['e_develop_require_specification_station'], item['s_remarks'], item['s_apply_person'], item['dt2_update_time']]
        for data in line_data:
            column_number = write_to_cell(sheet, line_number, column_number, data)
    sio = BytesIO()  # 写出到IO
    wb.save(sio)
    sio.seek(0)  # 重新定位到开始
    fileValue = sio.getvalue()
    response = HttpResponse(fileValue, content_type='application/vnd.ms-excel')  # 设置文件格式为Excel

    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名）
    filename = '开发规范.xls'
    response['content-disposition'] = 'attachment; filename=' + filename
    response.write(fileValue)
    return response


@csrf_exempt
def export_excel(request):
    """导出不带图片的excel"""
    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    if result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(result)
    data_list = result['data']['a_develop_require_specification']
    wb = xlwt.Workbook(encoding="utf-8")
    sheet_name = '开发规范'
    sheet = wb.add_sheet(sheet_name)
    # 设置各列宽度
    column_width_list = [1500, 30000, 10000, 5000, 5000, 5000, 2000, 5000]
    for index, column_width in enumerate(column_width_list):
        sheet.col(index).width = column_width
    # 表格第一行为表头内容
    head_fields = ['序号', '开发规范', '样例图片', '规范类别', '对应考核人', '备注信息', '提交人', '更新时间']
    for index, field in enumerate(head_fields):
        sheet.write(0, index, field)
    for index, item in enumerate(data_list):
        # 行号，下移一行，为表头留空间
        line_number = index + 1
        column_number = 0
        line_data = [line_number, item['s_desc'], None, item['e_develop_require_specification_type'],
                     item['e_develop_require_specification_station'], item['s_remarks'], item['s_apply_person'], item['dt2_update_time']]
        for data in line_data:
            column_number = write_to_cell(sheet, line_number, column_number, data)
    sio = BytesIO()  # 写出到IO
    wb.save(sio)
    wbw = xlsxwriter.Workbook(sio)
    # wbw_sheet1 = wbw.get_worksheet_by_name(sheet_name)
    wbw_sheet = wbw.add_worksheet("xxx")
    wbw_sheet.write(0, 0, 'hahahah')

    wbw.close()
    sio.seek(0)  # 重新定位到开始

    fileValue = sio.getvalue()
    response = HttpResponse(fileValue, content_type='application/vnd.ms-excel')  # 设置文件格式为Excel

    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名）
    filename = 'test.xls'
    response['content-disposition'] = 'attachment; filename=' + filename
    response.write(fileValue)
    return response


@csrf_exempt
def export_excel1(request):
    """导出带图片的excel"""
    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    if result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(result)
    data_list = result['data']['a_develop_require_specification']
    # wb = xlwt.Workbook(encoding="utf-8")
    sio = BytesIO()  # 写出到IO
    # wbw.save(sio)
    sheet_name = '开发规范'
    # sheet = wb.add_sheet(sheet_name)
    wbw = xlsxwriter.Workbook(sio)
    wbw_sheet = wbw.add_worksheet(sheet_name)
    # index_cn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    # 设置各列宽度
    column_width_list = [1500, 30000, 10000, 5000, 5000, 5000, 2000, 5000]
    # for index, column_width in enumerate(column_width_list):
    #     wbw_sheet.col(index).width = column_width
    # 表格第一行为表头内容
    head_fields = ['序号', '开发规范', '样例图片', '规范类别', '对应考核人', '备注信息', '提交人', '更新时间']
    for index, field in enumerate(head_fields):
        # cell_location = index_cn[index] + str(1)
        wbw_sheet.write(0, index, field)
        # sheet.write(0, index, field)
    for index, item in enumerate(data_list):
        # 行号，下移一行，为表头留空间
        line_number = index + 1
        column_number = 0
        img_url = item['s_pic_url']
        line_data = [line_number, item['s_desc'], None, item['e_develop_require_specification_type'],
                     item['e_develop_require_specification_station'], item['s_remarks'], item['s_apply_person'], item['dt2_update_time']]
        for data in line_data:
            # cell_location = index_cn[index] + str(line_number + 1)
            column_number = write_to_cell(wbw_sheet, line_number, column_number, data)
            # column_number = write_to_cell(sheet, line_number, column_number, data)
        if img_url:
            img_data = BytesIO(urlopen(img_url).read())
            wbw_sheet.insert_image(line_number, 2, img_url, {'image_data': img_data, 'x_scale': 0.25, 'y_scale': 0.25, 'object_position': 1})
    # sio.seek(0)  # 重新定位到开始
    fileValue = sio.getvalue()
    wbw.close()
    response = HttpResponse(fileValue, content_type='application/vnd.ms-excel')  # 设置文件格式为Excel

    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名）
    filename = 'test.xls'
    response['content-disposition'] = 'attachment; filename=' + filename
    response.write(fileValue)
    return response


@csrf_exempt
def export_excel_old(request):
    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    if result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(result)
    data_list = result['data']['a_develop_require_specification']
    wb = xlsxwriter.Workbook(r'结果.xlsx')
    sheet_name = '开发规范'
    sheet = wb.add_worksheet()
    # 设置各列宽度
    column_width_list = [1500, 30000, 10000, 5000, 5000, 5000, 2000, 5000]
    for index, column_width in enumerate(column_width_list):
        sheet.col(index).width = column_width
    # 表格第一行为表头内容
    head_fields = ['序号', '开发规范', '样例图片', '规范类别', '对应考核人', '备注信息', '提交人', '更新时间']
    for index, field in enumerate(head_fields):
        sheet.write(0, index, field)
    for index, item in enumerate(data_list):
        # 行号，下移一行，为表头留空间
        line_number = index + 1
        column_number = 0
        line_data = [line_number, item['s_desc'], None, item['e_develop_require_specification_type'],
                     item['e_develop_require_specification_station'], item['s_remarks'], item['s_apply_person'], item['dt2_update_time']]
        for data in line_data:
            column_number = write_to_cell(sheet, line_number, column_number, data)
        img_url = item['s_pic_url']
        # 图片所列的在下标
        img_column_index = 2
        if img_url:
            try:
                suffix = img_url.split('.')[-1]
                # f = requests.get(img_url)
                # # 图片单元格位置，C列
                cell_location = 'C' + str(line_number + 1)
                # img_file_name = cell_location + '.' + suffix
                # with open(img_file_name, "wb") as code:
                #     code.write(f.content)  # 保存文件
                # img_pillow = Image.open(img_file_name)
                # img_width = img_pillow.width  # 图片宽度
                # img_height = img_pillow.height  # 图片高度
                # sheet.set_column(img_column_index, img_column_index, cell_width + 4)  # 设置带图片单元格列宽
                # sheet.set_row(line_number, cell_height + 4)  # 设置带图片单元格行高
                # x_scale = cell_width / img_width
                # y_scale = cell_height / img_height
                # if img_width / img_height < cell_width / cell_height:  # 让图片 大小适应调整
                #     y_scale = x_scale
                # else:
                #     x_scale = y_scale
                # sheet.insert_image(cell_location, img_file_name,
                #                         {'x_offset': 2, 'y_offset': 2, 'x_scale': x_scale, 'y_scale': y_scale})

                # session = requests.session()
                resp = requests.session().get(img_url)
                if resp.status_code != 404:
                    url_image = urlopen(img_url).read()
                    tmp_img_file_name = cell_location + '.' + suffix
                    with open(tmp_img_file_name, 'wb') as f:
                        f.write(url_image)
                    # new_image = MEDIA_ROOT + 'new_' + qs.SKU + '.jpg'
                    im = Image.open(tmp_img_file_name)
                    im_resize = im.resize((800, 800), Image.ANTIALIAS)
                    im_resize.save(tmp_img_file_name, quality=100)
                    sheet.insert_image(cell_location, tmp_img_file_name, {'y_offset': 2, 'x_scale': 0.2, 'y_scale': 0.2})
            except Exception as e:
                s = traceback.format_exc()
                print(s)
                sheet.write(line_number, img_column_index, img_url)
    sio = BytesIO()  # 写出到IO
    wb.save(sio)
    sio.seek(0)  # 重新定位到开始
    fileValue = sio.getvalue()
    response = HttpResponse(fileValue, content_type='application/vnd.ms-excel')  # 设置文件格式为Excel

    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名）
    filename = 'test.xls'
    response['content-disposition'] = 'attachment; filename=' + filename
    response.write(fileValue)
    return response

# 导出思路，先建一个文件夹，用于存放要导出的execl
#   导出，生成一个带样式的空excel文件
#   然后读取这个文件，使用xlsxwrite将数据改写入
#   最后使用xlwt读取文件再导出
#   最后删除这个文件
# path = MEDIA_ROOT + 'download_xls/' + request.user.username
# mkdir_p(MEDIA_ROOT + 'download_xls')
# os.popen('chmod 777 %s' % (MEDIA_ROOT + 'download_xls'))
# mkdir_p(path)
# picpath = MEDIA_ROOT + 'download_pic/'
# mkdir_p(picpath)
# os.popen('chmod 777 %s' % (picpath))
# os.popen('chmod 777 %s' % (path))
@csrf_exempt
def export_excel_now(request):
    import os
    """导出不带图片的excel"""
    model_name = 'DevelopRequireSpecification'
    MEDIA_ROOT= 'C:\\Users\\admin\\Desktop\\img\\'
    EXCEL_PATH= MEDIA_ROOT + 'download_xls'
    os.popen('chmod 777 %s' % (EXCEL_PATH))
    common.mkdir_p(EXCEL_PATH)
    path = EXCEL_PATH + os.sep + model_name
    common.mkdir_p(path)
    os.popen('chmod 777 %s' % (path))
    common.mkdir_p(path)
    pic_path = MEDIA_ROOT + 'download_pic'
    common.mkdir_p(pic_path)
    os.popen('chmod 777 %s' % (pic_path))
    filename = model_name + '_' + common.getNowTime() + '.xls'
    file_path = path + os.sep + filename

    kwargs = {'s_function_name': FuncProcessName.DRS_GET.value, 'o_function_param': dict()}
    res = InterfaceFunction.run_interface_function(**kwargs)
    result = res['data']['o_function_result']
    if result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(result)
    data_list = result['data']['a_develop_require_specification']
    # wbwt = xlwt.Workbook()
    # wbwt.add_sheet(model_name)
    # wbwt.save(file_path)
    wb = xlsxwriter.Workbook(file_path)
    # wb = xlwt.Workbook(encoding="utf-8")
    sheet = wb.add_worksheet(model_name)
    # 设置各列宽度
    column_width_list = [5, 100, 36, 14, 16, 20, 10, 20]
    for index, column_width in enumerate(column_width_list):
        sheet.set_column(index, index + 1, column_width)
        # sheet.col(index).width = column_width
    # 表格第一行为表头内容
    head_fields = ['序号', '开发规范', '样例图片', '规范类别', '对应考核人', '备注信息', '提交人', '更新时间']
    # 表头行高
    sheet.set_row(0, 40)
    for index, field in enumerate(head_fields):
        sheet.write(0, index, field)
    img_list = []
    for index, item in enumerate(data_list):
        # 行号，下移一行，为表头留空间
        line_number = index + 1
        # 设置行高
        sheet.set_row(line_number, 30)
        column_number = 0
        line_data = [line_number, item['s_desc'], None, item['e_develop_require_specification_type'],
                     item['e_develop_require_specification_station'], item['s_remarks'], item['s_apply_person'], item['dt2_update_time']]
        for data in line_data:
            column_number = write_to_cell(sheet, line_number, column_number, data)
        img_url = item['s_pic_url']
        # 图片所列的在下标
        img_column_index = 2
        if img_url:
            try:
                suffix = img_url.split('.')[-1]
                # # 图片单元格位置，C列
                cell_location = 'C' + str(line_number + 1)
                session = requests.session()
                resp = session.get(img_url)
                if resp.status_code != 404:
                    url_file = urlopen(img_url).read()
                    tmp_file_name = pic_path + os.sep + cell_location + '.' + suffix
                    with open(tmp_file_name, 'wb') as f:
                        f.write(url_file)
                    im = Image.open(tmp_file_name)
                    # 设置图片尺寸
                    im_resize = im.resize((1290, 1100), Image.ANTIALIAS)
                    im_resize.save(tmp_file_name, quality=100)
                    sheet.insert_image(cell_location, tmp_file_name, {'y_offset': 2, 'x_scale': 0.2, 'y_scale': 0.2})
                    # 设置图片行高
                    sheet.set_row(line_number, 170)
                    img_list.append(tmp_file_name)
            except Exception as e:
                sheet.write(line_number, img_column_index, img_url)
    wb.close()
    # os.remove(file_path)
    # 最后使用xlwt读取文件再导出
    fileValue = None
    try:
        readbook = xlrd.open_workbook(file_path)
        copybook = copy(readbook)
        sio = BytesIO()  # 写出到IO
        copybook.save(sio)
        sio.seek(0)  # 重新定位到开始
        fileValue = sio.getvalue()
    except Exception as e:
        traceback.print_exc()
    for img_file in img_list:
        os.remove(img_file)
    response = HttpResponse(fileValue, content_type='application/vnd.ms-excel')  # 设置文件格式为Excel

    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名）

    response['content-disposition'] = 'attachment; filename=' + filename
    response.write(fileValue)

    return response



    # res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": dict()}
    # return JsonResponse(res)


def set_style(color='white', height=260, bold=False):
    # ： 设置单元格字体
    style = xlwt.XFStyle()
    font = xlwt.Font()
    # font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    # 设置单元格背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map[color]
    style.pattern = pattern

    #:设置单元格边框线条
    borders = xlwt.Borders()  # Create Borders
    # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
    # MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED,
    # THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED,
    # SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    style.borders = borders  # Add Borders to Style

    # ： 设置单元格居中格式
    alignment = xlwt.Alignment()  # Create Alignment
    # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED,
    # HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 横向居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 纵向居中  May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT  # ：自动换行
    style.alignment = alignment
    return style


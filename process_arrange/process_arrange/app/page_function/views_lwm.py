import os

from bs4 import element
from django.template.loader import render_to_string
from process_arrange.settings import BASE_DIR
from django.http import HttpResponse
from django.template import Context, Template
# from templates.common.universal import generate_vue_file
from django.shortcuts import render

class PathClass:
    def __init__(self):
        self.template = 'templates'
        self.css_template_path = self.template + '/css_template'
        self.js_template_path = self.template + '/js_template'
        self.html_template_path = 'html_template'
        self.vue_save_path = self.template + '/output'
        self.basedir = str(BASE_DIR)


'''1.生成vue左侧边栏组件，加交互组件'''
def sidebar_vue_data():
    vue_data = {'el_left_sidebar': {'data': {
        'loading': 'false',
        'loadinginfo': 'false',
        'processTreeData': [],
        'table_id': '',
        'table_name': '',
        'form': {
            'page': 1,
            'page_size': 10,
            'field': '',
            'order': '',
        },
        'editVisable': 'false',
        'addtable': 'undefined',
        'header': [],
        'tabledata': [],
        'dataCount': 0,
        'lists': [],
        'search': '',
        'searchtable': '',
        'flowNo': 'cost_config_tables_list',
        'deep': '',
        'software_maintainer': '',
        'software_update_time': '',
        'order_no_history': '',
        'total': ''
    },
        'get_el_left_sidebar_url': "/skuapp/config_table_list/"}}
    # data

    return vue_data


def generate_el_left_sidebar_vue(request):
    path_obj = PathClass()
    # 左侧边栏组件：双向绑定data数据结构
    '''
        vue_data_ : 所要传输的结构。通用型，统计一个页面需要用到的参数
    '''
    vue_data_ = sidebar_vue_data()
    # html处理
    template_path = '/el-left-sidebar'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + os.sep + path_obj.vue_save_path + template_path + '.vue'
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


# 生成搜索框
def search_vue_data():
    vue_data = {
        'el_search_input': {
            'data': {
                'el_search_id': ''
            },
            # 当循环遍历生成多个input时，可在列表中添加对应的数据，放置在标签属性中去
            'placeholder': '表名、字段名、字段备注信息查询', 'get_el_search_input_url': "/skuapp/config_table_list/",
            'generate_count': [[], []]}}
    return vue_data


def generate_el_search_input_vue(request):
    '''
        流程:
            1.创建路径对象
            2.生成双向绑定结构
            3.获取模板路径
            4.渲染search框组件
    '''
    path_obj = PathClass()
    vue_data_ = search_vue_data()
    '''1.获取模板路径'''
    template_path = '/el-search-input'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print('模板组件获取：', main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


def generate_vue_file(vue_data_, main_template_name, save_path):
    main_rendered_string = render_to_string(main_template_name, vue_data_)
    main_template_name = 'input/view_page.html'
    main_context = {'vueCode': main_rendered_string}
    main_rendered_string = render_to_string(main_template_name, main_context)
    return main_rendered_string

def generate_vue_html(vue_data_, main_template_name, save_path):
    main_rendered_string = render_to_string(main_template_name, vue_data_)
    main_template_name = 'root/template_result.vue'
    main_context = {'vueCode': main_rendered_string}
    main_rendered_string = render_to_string(main_template_name, main_context)
    return main_rendered_string



'''3.生成主体表数据'''
# body主体数据
def body_table_vue_data():
    vue_data = {
        'el_body_table': {
            # 对应双向绑定的值
            'data': {
                'header': ['订单编号', '订单详细信息', '订单基础信息', '订单时间信息', '订单其他信息'],
                'tabledata': '',
                'form': {
                    'page': 1,
                    'page_size': 10,
                    'field': '',
                    'order': '',
                },
            },

            # 当循环遍历生成多个input时，可在列表中添加对应的数据，放置在标签属性中去
            'get_body_table_url': "/skuapp/get_config_table_info/",
            'generate_count': [[], []]
        }
    }

    return vue_data


# 生成表主体
def generate_el_body_table(request):
    '''
        流程:
            1.创建路径对象
            2.生成双向绑定结构
            3.获取模板路径
            4.渲染search框组件
    '''
    print('path路径获取')
    path_obj = PathClass()
    # 返回双向绑定结构
    print("结构返回")
    vue_data_ = body_table_vue_data()
    '''1.获取模板路径'''
    template_path = '/el-body-table'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    print(vue_data_)
    print(main_template_name)
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


# 生成多行输入框组件
def body_multi_line_input():
    '''
        层数结构：
            1.标签层
            2.数据层
            3.样式层
            4.ajax层
    '''
    vue_data = {'multi_line_input': {
        'style': {},
        'content': [{'id': 1, 'key': '订单编号：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_start': '<tr>'},
                    {'id': 2, 'key': '发货批次号：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_end': '</tr>'},

                    {'id': 3, 'key': '组包号：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_start': '<tr>'},
                    {'id': 4, 'key': 'SKC：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_end': '</tr>'},

                    {'id': 5, 'key': 'FN码：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_start': '<tr>'},
                    {'id': 6, 'key': '卖家简称：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_end': '</tr>'},

                    {'id': 7, 'key': '类型名称：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_start': '<tr>'},
                    {'id': 8, 'key': '订单发货状态：', 'placeholder': '', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_end': '</tr>'},

                    {'id': 9, 'key': 'Online创建时间：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_start': '<tr>'},
                    {'id': 10, 'key': '分单时间：', 'el_input_start': '<el-input>',
                     'el_input_end': '</el-input>', 'tr_end': '</tr>'}]
    }}
    return vue_data


def generate_multi_line_input(request):
    print('path路径获取')
    path_obj = PathClass()
    # 返回双向绑定结构
    print("结构返回")
    vue_data_ = body_multi_line_input()
    # print("结构返回成功")
    '''1.获取模板路径'''
    template_path = '/el-multi_line_input'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    print(vue_data_)
    print(main_template_name)
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


# 生成维护人组件
def el_maintenance_person_info_vue_data():
    vue_data = {'el_maintenance_person_info': {
        'content': {'user': '刘文明', 'datetime': '2023/6/19'}}}
    return vue_data


def generate_el_maintenance_person_info(request):
    print('path路径获取')
    path_obj = PathClass()
    # 返回双向绑定结构
    print("结构返回")
    vue_data_ = el_maintenance_person_info_vue_data()
    '''1.获取模板路径'''
    template_path = '/el-maintenance-person-info'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    print(vue_data_)
    print(main_template_name)
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


def pagination_vue_data():
    vue_data = {
        'el_pagination': {
            'data': {
                'form': {'page': 1, 'page_size': 10, 'field': '', 'order': ''},
                'dataCount': 60}
        }
    }
    return vue_data


# 生成分页
def generate_pagination(request):
    print('path路径获取')
    path_obj = PathClass()
    # 返回双向绑定结构
    print("结构返回")
    vue_data_ = pagination_vue_data()
    '''1.获取模板路径'''
    template_path = '/el-pagination'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    print(vue_data_)
    print(main_template_name)
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)


'''按钮名称'''
def button_vue_data():
    vue_data = {
        'el_button': {
            'content': {
                'button_name': '查询'
            },
            'tag_attribute': {'type': ''}
        },
    }
    return vue_data


def generate_button(request):
    print('path路径获取')
    path_obj = PathClass()
    # 返回双向绑定结构
    print("结构返回")
    vue_data_ = button_vue_data()
    '''1.获取模板路径'''
    template_path = '/el-button'
    main_template_name = path_obj.html_template_path + template_path + '.html'
    print(main_template_name)
    save_path = path_obj.basedir + path_obj.vue_save_path + template_path + '.vue'
    print(vue_data_)
    print(main_template_name)
    rendered_string = generate_vue_file(vue_data_, main_template_name, save_path)
    return HttpResponse(rendered_string)

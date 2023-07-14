# -*- coding: utf-8 -*-

"""func_process URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app.function import common, t_public_page, t_public_params, t_public_function, t_public_function_param, \
    t_public_custom_function, t_public_custom_function_relevance, execute_function, execute_custom_function, \
    t_public_error_code, t_software_develop_standard, approve_comments, t_public_class
from app.common_function import login, global_enum
from app.page_function import views_lwm, DownloadVue

urlpatterns = [
    path('public_user_info/is_approve_person', common.f_is_approve_person),

    path('public_params/page', t_public_params.param_page_res),
    path('public_params/page_child', t_public_params.param_child_page_res),
    path('public_params/paramlist', t_public_params.param_list_res),
    path('public_params/childParam', t_public_params.f_query_child_param),
    path('public_params/listByName', t_public_params.param_list_by_name_res),
    path('public_params/getByIdList', t_public_params.param_by_id_list_res),
    path('public_params/add', t_public_params.param_add_res),
    path('public_params/update', t_public_params.param_update_res),
    path('public_params/del', t_public_params.param_del_res),
    path('public_params/commit', t_public_params.commit_param),
    path('public_params/approve', t_public_params.approve_param),

    path('public_error_code/add', t_public_error_code.error_code_add_res),
    path('public_error_code/update', t_public_error_code.error_code_update_res),
    path('public_error_code/del', t_public_error_code.error_code_del_res),
    path('public_error_code/list', t_public_error_code.error_code_list_res),
    path('public_error_code/getCodeMsg', t_public_error_code.show_returnEnum_res),

    path('public_class/add', t_public_class.class_add_res),
    path('public_class/edit', t_public_class.class_update_res),
    path('public_class/del', t_public_class.class_del_res),
    path('public_class/list', t_public_class.class_list_res),

    path('public_function/list', t_public_function.function_list_res),
    path('public_function/simpleList', t_public_function.function_simple_list_res),
    path('public_function/getById', t_public_function.function_get_by_id_res),
    path('public_function/add', t_public_function.function_add_res),
    path('public_function/update', t_public_function.function_update_res),
    path('public_function/del', t_public_function.function_del_res),
    path('public_function/commit', t_public_function.commit_function),
    path('public_function/approve', t_public_function.approve_function),
    path('public_function/publish', t_public_function.publish_function),
    path('public_function/add_auto_test', t_public_function.add_auto_test),

    path('public_function/runFunction', execute_function.run_function_res),
    path('public_function/showFunction', execute_function.show_function_code),
    path('public_function/auto_test_function', execute_function.auto_test_function),

    path('fun_param/getByFunId', t_public_function_param.query_by_function_id_res),
    path('fun_param/getByFunListId', t_public_function_param.query_by_custom_function_id_res),

    path('task_function_relevance/getByCustomFunctionId', t_public_custom_function_relevance.query_by_task_id_res),

    path('public_custom_function/add', t_public_custom_function.custom_function_add_res),
    path('public_custom_function/update', t_public_custom_function.custom_function_update_res),
    path('public_custom_function/del', t_public_custom_function.custom_function_del_res),
    path('public_custom_function/list', t_public_custom_function.custom_function_list_res),
    path('public_custom_function/config', t_public_custom_function.custom_function_config_res),
    path('public_custom_function/getErrorCode', t_public_custom_function.custom_function_error_code_res),
    path('public_custom_function/commit', t_public_custom_function.commit_custom_function),
    path('public_custom_function/approve', t_public_custom_function.approve_custom_function),
    path('public_custom_function/runSimpleTask', execute_custom_function.run_simple_task_res),
    path('public_custom_function/viewPage', t_public_custom_function.view_page), # 演示接口，预览

    # 获取编程规范的数据列表路由
    path('software_standard/get_software_standard_list', t_software_develop_standard.fun_get_software_standard_data),
    path('software_standard/standard_add', t_software_develop_standard.standard_add_res),  # 新增数据路由
    path('software_standard/standard_edit', t_software_develop_standard.update_standard),  # 编辑数据接口
    path('software_standard/standard_del', t_software_develop_standard.standard_del_res),  # 删除数据接口
    path('software_standard/fun_add_pic', t_software_develop_standard.fun_add_pic),
    path('software_standard/export_excel', t_software_develop_standard.export_excel_now),

    # 评论
    path('approve_comments/get_comment_data', approve_comments.get_comment_res),  # 查询当前数据的评论
    path('approve_comments/read_comment', approve_comments.read_comment),  # 查询当前数据的评论
    path('approve_comments/add_comment', approve_comments.add_comment),  # 新增评论
    path('approve_comments/get_it_user', approve_comments.get_it_user_res),  # 获取it用户

    # 登录
    path('login/do_login', login.do_login),  # 获取it用户

    # path('admin/', admin.site.urls),
    # path('go/', views.go),
    # path('vue/', views.vue),

    # 生成左侧边栏
    path('vueFunction/', t_public_function.vueFunction),
    path('generate_el_left_sidebar_vue/', views_lwm.generate_el_left_sidebar_vue),
    # 生成搜索按钮
    path('generate_el_search_input_vue/', views_lwm.generate_el_search_input_vue),
    # 生成主体文件
    path('generate_el_body_table/', views_lwm.generate_el_body_table),
    # 生成多行文本框
    path('generate_multi_line_input/', views_lwm.generate_multi_line_input),
    # 生成维护人信息
    path('generate_el_maintenance_person_info/', views_lwm.generate_el_maintenance_person_info),
    # 生成分页信息
    path('generate_pagination/', views_lwm.generate_pagination),
    # 生成基础按钮组件
    path('generate_button/', views_lwm.generate_button),
    path('downloadVueFile/', DownloadVue.downloadVueFile),
    # 演示接口，非正式
    path('public_params/delByIdList', t_public_params.del_by_id_list_res),
    # 根据枚举值名称获取枚举选项列表
    path('global_enum/get_enum_options/', global_enum.get_enum_options_by_name),

    # page管理
    path('public_pages/list', t_public_page.page_list_res),  # page页面查询
    path('public_pages/params_list_res', t_public_page.params_list_res),  # page页面参数查询
    path('public_pages/add_page_list', t_public_page.add_page_list),  # 页面添加
    path('public_pages/del_page_list', t_public_page.del_page_list),  # 页面删除
]

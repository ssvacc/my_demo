# import os
# import traceback
#
# from django.template.loader import render_to_string
#
# from ConstEnum import PAGE_CONFIG_INFO
# from ReturnEnum import ReturnEnum
# from app.function import common
# from app.page_function.CreatePage import CreatePage
# from bs4 import BeautifulSoup
#
# class PageFunction(object):
#     """
#     通用生成页面的接口函数, 跳过中间文件，直接拿渲染好的数据解析拼接
#     参数:a_element_name: 基础组件名称
#         s_page_template_config: 页面配置信息
#     返回值:s_vue_component_content 生成后的vue文件内容
#           s_vue_component_file_name 生成后的vue文件名,存放在templates/output/
#     """
#     @staticmethod
#     def common_create_page_by_config(a_page_template_config, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # "page_id", "page_code" 看后续开发情况决定是舍弃还是抽离到上层
#             # "elements", "data", "methods", "style", "life_cycle" 固定字典key,用于vue组件各个区模板渲染
#             o_vue_area = {"page_id": "demo_page", "page_code": "demo_page",
#                           "elements": "", "data": "", "methods": "", "style": "", "life_cycle": ""}
#             time = common.getNowTime()
#             s_vue_component_file_name = o_vue_area['page_id'] + '_' + str(time) + ".vue"
#             for config in a_page_template_config:
#                 element_name_result = PageFunction.get_base_element_name(config['element'])
#                 if element_name_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                     return element_name_result
#                 template_name = element_name_result['data']['s_template_file_name']
#                 template_rendered_string = render_to_string(template_name, config)
#                 o_vue_area = PageFunction.analysis_rendered_data(o_vue_area, template_rendered_string)
#             template_name = 'root\\base_vue.hq'
#             context = {'ele': o_vue_area}
#             main_rendered_string = render_to_string(template_name, context)
#             hq_vue_file_name = "app\\templates\\output\\" + s_vue_component_file_name  # 生成指定路径下的vue
#             f = open(hq_vue_file_name, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['data']['s_vue_component_file_name'] = s_vue_component_file_name
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         except Exception as e:
#             traceback.print_exc()
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#
#     # 获取基础组件模板名称
#     @staticmethod
#     def get_base_element_name(s_element_name):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\input\\'
#             flag = True
#             template_name = BASE_PATH + 'baseElement-old\\' + s_element_name + '.hq'
#             if not os.path.exists(template_name):
#                 template_name = BASE_PATH + 'groupElement\\' + s_element_name + '.hq'
#                 if not os.path.exists(template_name):
#                     template_name = BASE_PATH + 'customElement\\' + s_element_name + '.hq'
#                     if not os.path.exists(template_name):
#                         flag = False
#             if flag:
#                 result['code'] = ReturnEnum.ER_SUCCESS().code
#                 result['msg'] = ReturnEnum.ER_SUCCESS().msg
#                 result['data']['s_template_file_name'] = template_name
#             else:
#                 result['code'] = ReturnEnum.ER_NO_DATA().code
#                 result['msg'] = ReturnEnum.ER_NO_DATA().msg
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#
#     # 解析各个区的数据：hq-template,hq-data,hq-methods,hq-style,hq-life-cycle
#     @staticmethod
#     def analysis_rendered_data(o_vue_area, template_rendered_string):
#         o_vue_area['elements'] += PageFunction.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.TAG_TEMPLATE.value)
#         o_vue_area['data'] += PageFunction.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.TAG_DATA.value)
#         o_vue_area['methods'] += PageFunction.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.TAG_METHODS.value)
#         o_vue_area['style'] += PageFunction.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.TAG_STYLE.value)
#         o_vue_area['life_cycle'] += PageFunction.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.TAG_LIFE_CYCLE.value)
#         return o_vue_area
#
#     @staticmethod
#     def get_by_tag(s_vue_component_content, s_tag):
#         s_tag = '<' + s_tag + '>'
#         s_tag_end = s_tag[0] + '/' + s_tag[1:]
#         s_tag_content = ''
#         if s_tag in s_vue_component_content and s_tag_end in s_vue_component_content:
#             s_tag_content = s_vue_component_content[
#                             s_vue_component_content.find(s_tag) + len(s_tag):s_vue_component_content.find(s_tag_end)]
#         return str(s_tag_content)
#
#     ################################上面是抽离出来生成页面的通用函数，使用先渲染基础模板，变成中间模板，再将中间模板组合成一个vue文件################################
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     ################################下面是抽离出来生成页面的通用函数，（先组合模板，再渲染成vue文件，不能兼容重复组件问题）暂时废弃################################
#     """
#     通用生成页面的接口函数,通过配置中找到需要的模板，而不是将配置和模板分别传入
#     """
#     @staticmethod
#     def common_create_page_by_config_2(a_page_template_config, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             a_element_name = []
#             for config in a_page_template_config:
#                 a_element_name.append(config['element'])
#             middle_result = PageFunction.compose_element_2(a_element_name)
#             if middle_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return middle_result
#             s_vue_middle_file_name = middle_result['data']['s_vue_component_file_name']
#             s_vue_component_file_url = "middleFile\\middleElement\\" + s_vue_middle_file_name
#             # todo: a_page_template_config 转为字典，而不是list(这个模板生成方式舍弃了)
#             main_rendered_string = render_to_string(s_vue_component_file_url, a_page_template_config)
#             s_vue_component_file_name = s_vue_middle_file_name.replace(".hq", ".vue")
#             vue_file_name = "app\\templates\\output\\" + s_vue_component_file_name  # 生成指定路径下的vue
#             f = open(vue_file_name, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\middleFile\\middleElement\\'
#             middle_file_url = BASE_PATH + s_vue_middle_file_name
#             os.remove(middle_file_url)
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#             result['data']['s_vue_component_file_name'] = s_vue_component_file_name
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#         except Exception as e:
#             print(str(e))
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     """
#     通用生成页面的接口函数
#     参数:a_element_name: 基础组件名称
#         s_page_template_config: 页面配置信息
#     返回值:s_vue_component_content 生成后的vue文件内容
#           s_vue_component_file_name 生成后的vue文件名,存放在templates/output/
#     """
#     @staticmethod
#     def common_create_page_1(a_element_name, s_page_template_config, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             middle_result = PageFunction.compose_element_2(a_element_name)
#             if middle_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return middle_result
#             s_vue_middle_file_name = middle_result['data']['s_vue_component_file_name']
#             s_vue_component_file_url = "middleFile\\middleElement\\" + s_vue_middle_file_name
#             main_rendered_string = render_to_string(s_vue_component_file_url, s_page_template_config)
#             s_vue_component_file_name = s_vue_middle_file_name.replace(".hq", ".vue")
#             vue_file_name = "app\\templates\\output\\" + s_vue_component_file_name  # 生成指定路径下的vue
#             f = open(vue_file_name, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\middleFile\\middleElement\\'
#             middle_file_url = BASE_PATH + s_vue_middle_file_name
#             os.remove(middle_file_url)
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#             result['data']['s_vue_component_file_name'] = s_vue_component_file_name
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#         except Exception as e:
#             print(str(e))
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     """将多个基础组件组合成一个vue组件，生成的组件是中间模板，不是最终的输出文件"""
#     @staticmethod
#     def compose_element_2(a_element_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         # "page_id", "page_code" 看后续开发情况决定是舍弃还是抽离到上层
#         # "elements", "data", "methods", "style", "life_cycle" 固定字典key,用于vue组件各个区模板渲染
#         o_vue_area = {"page_id": "demo_page", "page_code": "demo_page",
#                       "elements": "", "data": "", "methods": "", "style": "", "life_cycle":""}
#         for s_element_name in a_element_name:
#             result = PageFunction.getBaseElementByName_1(s_element_name)
#             o_vue_area = PageFunction.analysis_all_template_data1(o_vue_area, result)
#         template_name = 'root\\base_vue.hq'
#         context = {'ele': o_vue_area}
#         main_rendered_string = render_to_string(template_name, context)
#         try:
#             time = common.getNowTime()
#             hq_vue_file_name = "app\\templates\\middleFile\\middleElement\\" + time + ".hq"  # 生成指定路径下的vue
#             f = open(hq_vue_file_name, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['data']['s_vue_component_file_name'] = time + ".hq"
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         except Exception as e:
#             traceback.print_exc()
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
#         return result
#
#     # 获取template/input/baseElement下的基础组件模板
#     @staticmethod
#     def getBaseElementByName_1(s_element_name):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\input\\'
#             flag = True
#             template_name = BASE_PATH + 'baseElement_old0627\\' + s_element_name + '.hq'
#             if not os.path.exists(template_name):
#                 template_name = BASE_PATH + 'groupElement\\' + s_element_name + '.hq'
#                 if not os.path.exists(template_name):
#                     template_name = BASE_PATH + 'customElement\\' + s_element_name + '.hq'
#                     if not os.path.exists(template_name):
#                         flag = False
#             if flag:
#                 f = open(template_name, 'r', encoding='utf-8')
#                 context = f.read()
#                 f.close()
#                 result['code'] = ReturnEnum.ER_SUCCESS().code
#                 result['msg'] = ReturnEnum.ER_SUCCESS().msg
#                 result['data']['s_vue_component_content'] = context
#             else:
#                 result['code'] = ReturnEnum.ER_NO_DATA().code
#                 result['msg'] = ReturnEnum.ER_NO_DATA().msg
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 解析vue各个区的数据：template,hq-data,hq-methods,hq-style,hq-life-cycle
#     # 为了兼容重复组件，在各个基础组件中间模板上加各自的判断模板（废弃，解决不了重复组件问题，且增加模板的复杂度）
#     @staticmethod
#     def analysis_all_template_data1(o_vue_area, vue_area_result):
#         if ReturnEnum.ER_SUCCESS().code == vue_area_result['code']:
#             s_select_area_content = vue_area_result['data']['s_vue_component_content']
#             # o_vue_area['elements'] += PageFunction.get_by_template(s_select_area_content)
#             o_vue_area['elements'] += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_TEMPLATE.value)
#             o_vue_area['data'] += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_DATA.value)
#             o_vue_area['methods'] += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_METHODS.value)
#             o_vue_area['style'] += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_STYLE.value)
#             o_vue_area['life_cycle'] += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_LIFE_CYCLE.value)
#         return o_vue_area
#
#     # 有bug,标签内部使用模板语法会导致组件内容出错，废弃
#     @staticmethod
#     def get_by_template(s_vue_component_content):
#         bs_xml = BeautifulSoup(s_vue_component_content)
#         div = bs_xml.findAll('template')
#         s_tag_content = ''
#         if len(div) > 0:
#             s_tag_content = div[0].contents[1]
#         return str(s_tag_content)
#
# ################################上面是抽离出来生成页面的通用函数################################
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# ################################下面是用各个区的方式生成页面，暂时废弃################################
#
#
#     # 通用页面生成函数
#     @staticmethod
#     def create_vue_by_page_config(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         # 1.根据s_page_name获取页面配置信息
#         # 暂时用演示的俩个函数
#         elements_area = ''
#         data_area = ''
#         methods_area = ''
#         element = {"page_id": "test_page", "page_code": "test_page"}
#         try:
#             # 2.找到对应生成vue文件的接口函数
#             # 3.依次执行接口函数
#             # 4.读取接口函数生成的vue文件，并整合成一个可用的vue文件
#             tabs_menu_area_result = CreatePage.create_tabs_menu_vue()
#             elements_area, data_area, methods_area = PageFunction.analysis_template_data(elements_area, data_area,
#                                                                                          methods_area,
#                                                                                          tabs_menu_area_result)
#             select_area_result = CreatePage.create_select_area_vue()
#             elements_area, data_area, methods_area = PageFunction.analysis_template_data(elements_area, data_area,
#                                                                                          methods_area,
#                                                                                          select_area_result)
#             global_button_area_result = CreatePage.create_global_button_vue()
#             elements_area, data_area, methods_area = PageFunction.analysis_template_data(elements_area, data_area,
#                                                                                          methods_area,
#                                                                                          global_button_area_result)
#             data_area_result = CreatePage.create_data_area_vue()
#             elements_area, data_area, methods_area = PageFunction.analysis_template_data(elements_area, data_area,
#                                                                                          methods_area, data_area_result)
#
#             # 读取并渲染模板文件
#         except Exception as e:
#             traceback.print_exc()
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
#         element['elements'] = elements_area
#         element['data'] = data_area
#         element['methods'] = methods_area
#         template_name = 'input\\basePage.vue'
#         context = {'ele': element}
#         main_rendered_string = render_to_string(template_name, context)
#         # 5.将vue文件的文本内容返回
#         # 续：create_vue_by_page_config的调用者，如果是预览按钮，则生成预览html文件返回给前端
#         # 续：create_vue_by_page_config的调用者，如果是生成文件，则将生成的文件在浏览器下载
#         try:
#             tabs_vue = "app\\templates\\output\\hq-page.vue"  # 生成指定路径下的vue
#             f = open(tabs_vue, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         except Exception as e:
#             traceback.print_exc()
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
#         return result
#
#     @staticmethod
#     def analysis_template_data(elements_area, data_area, methods_area, vue_area_result):
#         if ReturnEnum.ER_SUCCESS().code == vue_area_result['code']:
#             s_select_area_content = vue_area_result['data']['s_vue_component_content']
#             elements_area += PageFunction.get_by_template(s_select_area_content)
#             data_area += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_DATA.value)
#             methods_area += PageFunction.get_by_tag(s_select_area_content, PAGE_CONFIG_INFO.TAG_METHODS.value)
#         return elements_area, data_area, methods_area

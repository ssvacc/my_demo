# import os
# import re
# import traceback
#
# from django.template.loader import render_to_string
#
# from ConstEnum import PAGE_CONFIG_INFO
# from ReturnEnum import ReturnEnum
# from app.function import common
#
#
# class GeneratePage(object):
#     """
#     通用生成页面的接口函数,拿渲染好的数据解析拼接
#     参数: a_page_template_config: 页面配置信息，每个组件需有自己的组件模板名，page_area信息，组件key(对此次渲染唯一，用于容器识别渲染)
#     返回值: s_vue_component_content 生成后的vue文件内容
#            s_vue_component_file_name 生成后的vue文件名,存放在templates/output/
#     """
#     @staticmethod
#     def common_generate_page_by_config(a_page_template_config, s_page_id, s_page_name_en, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # 容器组件的配置格式
#             check_result = GeneratePage.check_container_config(a_page_template_config)
#             if check_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return check_result
#
#             # 重复变量或者方法加上 repeat标记 避免双向绑定的数据在模板渲染时重复渲染
#             a_field_name_en = []
#             GeneratePage.set_repeat_mark(a_field_name_en, a_page_template_config)
#
#             # 遍历a_page_template_config，进行模板渲染，将容器组件中子标签的key抽取到一个list中
#             o_vue_area = {"page_id": s_page_id, "page_name_en": s_page_name_en}
#             GeneratePage.rendered_data_by_config(a_page_template_config, o_vue_area)
#
#             # 最终模板渲染，生成vue文件
#             template_name = PAGE_CONFIG_INFO.BASE_VUE_TEMPLATE.value
#             context = {'ele': o_vue_area}
#             main_rendered_string = render_to_string(template_name, context)
#             time = common.getNowTime()
#             s_vue_component_file_name = o_vue_area['page_id'] + '_' + str(time) + PAGE_CONFIG_INFO.VUE_FILE_SUFFIX.value
#             BASE_PATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + PAGE_CONFIG_INFO.VUE_OUTPUT_PATH.value
#             hq_vue_file_name = BASE_PATH + s_vue_component_file_name  # 生成指定路径下的vue
#             f = open(hq_vue_file_name, 'w', encoding='utf-8')
#             f.write(main_rendered_string)
#             f.close()
#             result['code'] = ReturnEnum.ER_SUCCESS().code
#             result['data']['s_vue_component_file_name'] = s_vue_component_file_name
#             result['data']['s_vue_component_content'] = main_rendered_string
#             result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         except Exception as e:
#             traceback.print_exc()
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 获取基础组件模板名称
#     @staticmethod
#     def rendered_data_by_config(a_page_template_config, o_vue_area, parent_element_key=None):
#         for config in a_page_template_config:
#             if not GeneratePage.is_element(config):
#                 if GeneratePage.has_sub_element(config):
#                     # 根据容器结构配置，往深层次渲染
#                     GeneratePage.rendered_data_by_config(config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]], o_vue_area, parent_element_key)
#                 continue
#             s_template_file_name = GeneratePage.get_base_element_name(config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[0]])
#             if not s_template_file_name:
#                 continue
#             template_rendered_string = render_to_string(s_template_file_name, config)
#             if GeneratePage.has_sub_element(config):
#                 if GeneratePage.is_element(config):
#                     if config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]] not in o_vue_area.keys():
#                         o_vue_area[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]] = ''
#                     o_vue_area[config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]]] = template_rendered_string
#                 # 递归，将子组件深度渲染到容器中
#                 subElements = config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]]
#                 GeneratePage.rendered_data_by_config(subElements, o_vue_area, config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]])
#                 # 用渲染后的子组件数据替换容器模板的初始内容
#                 s_hqTemplate_middle = GeneratePage.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0])[0]
#                 s_hqTemplate_detail = GeneratePage.get_by_tag(o_vue_area[config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]]],
#                                                               PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0])[0]
#                 template_rendered_string = template_rendered_string.replace(s_hqTemplate_middle, s_hqTemplate_detail)
#             GeneratePage.analysis_rendered_data(o_vue_area, template_rendered_string, config, parent_element_key)
#
#     # 遍历配置组件模板结构，有重复的变量或函数，增加repeat标记，避免vue 出现重复变量或函数
#     # 1.vue data 区的变量去重; 2.vue method 区的函数去重
#     @staticmethod
#     def set_repeat_mark(a_field_name_en, a_page_template_config):
#         for config in a_page_template_config:
#             if PAGE_CONFIG_INFO.HQ_COMMON_CONFIG_FIELD.value[1] in config.keys() and config[PAGE_CONFIG_INFO.HQ_COMMON_CONFIG_FIELD.value[1]]:
#                 field_name_en = config[PAGE_CONFIG_INFO.HQ_COMMON_CONFIG_FIELD.value[1]]
#                 if field_name_en in a_field_name_en:
#                     config[PAGE_CONFIG_INFO.HQ_COMMON_CONFIG_FIELD.value[0]] = field_name_en
#                 else:
#                     a_field_name_en.append(field_name_en)
#             if GeneratePage.has_sub_element(config):
#                 subElements = config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]]
#                 GeneratePage.set_repeat_mark(a_field_name_en, subElements)
#
#     # 获取基础组件模板名称
#     @staticmethod
#     def get_base_element_name(s_element_name):
#         BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + PAGE_CONFIG_INFO.VUE_INPUT_PATH.value
#         template_name = BASE_PATH + PAGE_CONFIG_INFO.HQ_ELEMENT_FOLDER.value[0] + os.sep + s_element_name + PAGE_CONFIG_INFO.TEMPLATE_FILE_SUFFIX.value
#         if not os.path.exists(template_name):
#             template_name = BASE_PATH + PAGE_CONFIG_INFO.HQ_ELEMENT_FOLDER.value[1] + os.sep + s_element_name + PAGE_CONFIG_INFO.TEMPLATE_FILE_SUFFIX.value
#             if not os.path.exists(template_name):
#                 template_name = BASE_PATH + PAGE_CONFIG_INFO.HQ_ELEMENT_FOLDER.value[2] + os.sep + s_element_name + PAGE_CONFIG_INFO.TEMPLATE_FILE_SUFFIX.value
#                 if not os.path.exists(template_name):
#                     template_name = None
#         s_template_file_name = template_name
#         return s_template_file_name
#
#     # 解析各个区的数据：hqTemplate,hqData,hqMethods,hqStyle,hqLifeCycle(生命周期会进行二次解析)
#     @staticmethod
#     def analysis_rendered_data(o_vue_area, template_rendered_string, config, parent_element_key):
#         s_page_area = config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[3]]
#         a_tag_name = PAGE_CONFIG_INFO.HQ_TAG_LIST.value
#         for s_tag_name in a_tag_name:
#             if s_tag_name not in o_vue_area.keys():
#                 o_vue_area[s_tag_name] = ''
#             if s_page_area not in o_vue_area.keys():
#                 o_vue_area[s_page_area] = ''
#             # template区
#             if s_tag_name == PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0]:
#                 template_content = GeneratePage.get_by_tag(template_rendered_string, s_tag_name)[0]
#                 if not template_content:
#                     return
#                 if not parent_element_key:
#                     # 不是容器的子组件，则将数据渲染到相应区块中
#                     o_vue_area[s_page_area] += template_content
#                 else:
#                     if parent_element_key and parent_element_key in o_vue_area.keys() and o_vue_area[parent_element_key]:
#                         # 把 template_rendered_string 中的 hqTemplate 区的数据渲染到容器组件的相对应位置上
#                         s_hqTemplate = GeneratePage.get_by_tag(template_rendered_string, PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0])[0]
#                         container_middle_template = o_vue_area[parent_element_key]
#                         element_key = config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[1]]
#                         # element_key_tag = PAGE_CONFIG_INFO.HQ_ELEMENT_KEY_TAG.value + element_key + PAGE_CONFIG_INFO.HQ_ELEMENT_KEY_TAG_END.value
#                         if element_key in container_middle_template:
#                             o_vue_area[parent_element_key] = container_middle_template.replace(element_key, s_hqTemplate)
#             # 生命周期区
#             elif PAGE_CONFIG_INFO.HQ_TAG_LIST.value[4] == s_tag_name:
#                 life_cycle_content = GeneratePage.get_by_tag(template_rendered_string, s_tag_name)[0]
#                 if life_cycle_content:
#                     o_vue_area[s_tag_name] += life_cycle_content
#                     GeneratePage.analysis_sub_tag(o_vue_area, life_cycle_content, PAGE_CONFIG_INFO.HQ_LIFE_CYCLE_TAG_LIST.value)
#             else:
#                 o_vue_area[s_tag_name] += GeneratePage.get_by_tag(template_rendered_string, s_tag_name)[0]
#
#     # 解析下一级标签中的内容
#     @staticmethod
#     def analysis_sub_tag(o_vue_area, s_tag_content, a_sub_tag_name):
#         for s_tag_name in a_sub_tag_name:
#             s_sub_tag_content = GeneratePage.get_by_tag(s_tag_content, s_tag_name)[0]
#             if s_tag_name not in o_vue_area.keys():
#                 o_vue_area[s_tag_name] = ''
#             o_vue_area[s_tag_name] += s_sub_tag_content
#         return o_vue_area
#
#     # 获取自定义标签中的内容
#     @staticmethod
#     def get_by_tag(s_vue_component_content, s_tag):
#         s_tag = '<' + s_tag + '>'
#         s_tag_end = s_tag[0] + '/' + s_tag[1:]
#         s_tag_result = [index.start() for index in re.finditer(s_tag, s_vue_component_content)]
#         s_tag_end_result = [index.start() for index in re.finditer(s_tag_end, s_vue_component_content)]
#         a_tag_content = []
#         if s_tag in s_vue_component_content and s_tag_end in s_vue_component_content:
#             if len(s_tag_result) > 1 and len(s_tag_result) == len(s_tag_end_result):
#                 for i in range(0, len(s_tag_result)):
#                     s_tag_content = s_vue_component_content[s_tag_result[i] + len(s_tag):s_tag_end_result[i]]
#                     a_tag_content.append(s_tag_content)
#             else:
#                 s_tag_content = s_vue_component_content[s_vue_component_content.find(s_tag) + len(s_tag):s_vue_component_content.find(s_tag_end)]
#                 a_tag_content.append(str(s_tag_content))
#         if len(a_tag_content) == 0:
#             a_tag_content.append('')
#         return a_tag_content
#
#     # 获取基础组件模板名称
#     @staticmethod
#     def check_container_config(a_page_template_config):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         for config in a_page_template_config:
#             # 对搜索区做校验，不超过3列（为了配合container的flex布局，少于3列则补齐）
#             if PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[0] in config.keys() and 'hq-container-select' == config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[0]]:
#                 if not PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2] in config.keys():
#                     continue
#                 rows = config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]]
#                 if not isinstance(rows, list):
#                     continue
#                 for row in rows:
#                     if not PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2] in row.keys():
#                         continue
#                     cols = row[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]]
#                     if not isinstance(cols, list):
#                         continue
#                     if len(cols) > PAGE_CONFIG_INFO.SELECT_AREA_MAX_COL.value:
#                         result['code'] = ReturnEnum.ER_RISK_PARAM_ERROR().code
#                         result['msg'] = ReturnEnum.ER_RISK_PARAM_ERROR().msg + ':搜索区配置字段不要超过3列'
#                         return result
#                     elif len(cols) < PAGE_CONFIG_INFO.SELECT_AREA_MAX_COL.value:
#                         need_append_number = PAGE_CONFIG_INFO.SELECT_AREA_MAX_COL.value - len(row[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]])
#                         for i in range(need_append_number):
#                             cols.append(dict())
#         result['code'] = ReturnEnum.ER_SUCCESS().code
#         result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         return result
#
#     # 判断配置项是否包含子标签
#     @staticmethod
#     def has_sub_element(config):
#         return PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2] in config.keys() and config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[2]]
#
#     # 判断配置项是否是组件
#     @staticmethod
#     def is_element(config):
#         return PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[0] in config.keys() and config[PAGE_CONFIG_INFO.HQ_BASE_ELEMENT_KEY_LIST.value[0]]

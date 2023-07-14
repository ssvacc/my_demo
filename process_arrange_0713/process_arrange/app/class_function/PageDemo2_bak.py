# import traceback
#
# from ReturnEnum import ReturnEnum
# from app.class_function.PageFunction import PageFunction
#
#
# class PageDemo2(object):
#     ################################第一个页面################################
#     # 生成demo2页面的vue文件
#     @staticmethod
#     def create_demo2_page(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # 每个页面自己的组件
#             a_element_name = ["hq-page", "hq-table"]
#             # 获取生成页面的配置信息
#             config_result = PageDemo2.get_demo2_config(s_page_name, **kwargs)
#             if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return config_result
#             s_page_template_config = config_result['data']['s_page_template_config']
#             # 调用通用生成页面的函数
#             result = PageFunction.common_create_page(a_element_name, s_page_template_config)
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 获取demo2页面的配置数据，每个页面自己的配置数据
#     @staticmethod
#     def get_demo2_config(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         # todo: 配置数据的结构需要调整，同时基础模板的变量名也需要调整
#         s_page_template_config = {'ele': {
#             'pagination_id': 'hq_pagination',
#             'query_data_list_name': 'demo2_list',
#             'query_data_list_param': None,
#             'table_id': 'hq_table',
#             'show_index': False,
#             'show_page': True,
#             'async': True,
#             'query_condition': None,
#             'query_url': '/public_params/page_child',
#             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name'},
#                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc'},
#                              {'field_name_cn': '类型', 'field_name_en': 'data_type'},
#                              {'field_name_cn': '注释', 'field_name_en': 'param_detail'}],
#         }}
#         result['data']['s_page_template_config'] = s_page_template_config
#         result['code'] = ReturnEnum.ER_SUCCESS().code
#         result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         return result
#
#     ################################第二个页面(重复组件以及多个输入框数据绑定会有问题)################################
#     # 生成demo2页面的vue文件
#     @staticmethod
#     def create_demo2_page2_1(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # 获取生成页面的配置信息
#             config_result = PageDemo2.get_demo2_config2_1(s_page_name, **kwargs)
#             if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return config_result
#             s_page_template_config = config_result['data']['s_page_template_config']
#             # todo: 每个页面自己的组件，需要根据配置信息，决定生成需要的组件，例如字段数据类型不同，需要生成的输入框类型不同
#             # todo: 方案1.s_page_template_config配置信息是基础配置信息，不能直接拿来渲染模板，每次渲染基础模板前需要做对应关系处理，
#             #   即哪几个字段对应哪个组件，或者是在渲染基础组件前，把它需要的配置数据拿出来
#             #       方案2.每次渲染一个基础组件之后，将用过的配置数据删除，可以避免多余的配置数据渲染
#             #       *方案3.基础组件不允许使用循环方式渲染，只能将需要的数据拿出来渲染，这里需要定义好对应关系，以及提供通用处理接口
#             a_element_name = ["hq-input", "hq-input-textarea", "hq-page", "hq-table"]
#             # 调用通用生成页面的函数
#             result = PageFunction.common_create_page(a_element_name, s_page_template_config)
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 获取demo2页面的配置数据，每个页面自己的配置数据
#     @staticmethod
#     def get_demo2_config2_1(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         s_page_template_config = {'ele': {
#             'field_list': [{
#                 'field_name_en': 'status',
#                 'field_name_cn': '状态码',
#                 'field_data_type': 'Int',
#                 'element_name': 'hq-input-number'
#             }, {
#                 'field_name_en': 'condition',
#                 'field_name_cn': '查询条件',
#                 'field_data_type': 'String',
#                 'element_name': 'hq-input'
#             }],
#             'pagination_id': 'hq_pagination',
#             'query_data_list_name': 'demo2_list',
#             'query_data_list_param': None,
#             'table_id': 'hq_table',
#             'show_index': False,
#             'show_page': True,
#             'async': True,
#             'query_condition': None,
#             'query_url': '/public_params/page_child',
#             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name'},
#                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc'},
#                              {'field_name_cn': '类型', 'field_name_en': 'data_type'},
#                              {'field_name_cn': '注释', 'field_name_en': 'param_detail'}],
#         }}
#         result['data']['s_page_template_config'] = s_page_template_config
#         result['code'] = ReturnEnum.ER_SUCCESS().code
#         result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         return result
#
#     ################################第二个页面(改进，废弃)################################
#     # 生成demo2页面的vue文件
#     @staticmethod
#     def create_demo2_page2_2(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # 获取生成页面的配置信息
#             config_result = PageDemo2.get_demo2_config2(s_page_name, **kwargs)
#             if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return config_result
#             s_page_template_config = config_result['data']['s_page_template_config']
#             # todo: 每个页面自己的组件，需要根据配置信息，决定生成需要的组件，例如字段数据类型不同，需要生成的输入框类型不同
#             # todo: 方案1.s_page_template_config配置信息是基础配置信息，不能直接拿来渲染模板，每次渲染基础模板前需要做对应关系处理
#             #   即哪几个字段对应哪个组件，或者是在渲染基础组件前，把它需要的配置数据拿出来
#             #       方案2.每次渲染一个基础组件之后，将用过的配置数据删除，可以避免多余的配置数据渲染
#             #       *方案3.基础组件不允许使用循环方式渲染，只能将需要的数据拿出来渲染，这里需要定义好对应关系，以及提供通用处理接口
#             #       方案4.可以先把数据渲染到基础组件，再进行基础组件融合，（会产生很多的中间文件）（没有中间文件，直接可以拿渲染后的本文内容拼接）
#             # todo: 每个基础组件都需要配套提供一个配置字典,即默认字典，（基础组件配置表中，提供默认字典字段，模板调用者可以轻松获取到模板的配套字典）
#             # a_element_name = ["hq-input", "hq-input-textarea", "hq-page", "hq-table"]
#             # 调用通用生成页面的函数
#             result = PageFunction.common_create_page_by_config_2(s_page_template_config)
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 获取demo2页面的配置数据，每个页面自己的配置数据
#     @staticmethod
#     def get_demo2_config2_2(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         a_page_template_config = [
#             {'element': 'hq-input-int',
#              'field_name_en': 'status',
#              'field_name_cn': '状态码',
#              'field_data_type': 'Int'
#              },
#             {'element': 'hq-input',
#              'field_name_en': 'condition',
#              'field_name_cn': '查询条件',
#              'field_data_type': 'String'
#              },
#             {'element': 'hq-page',
#              'pagination_id': 'hq_pagination',
#              'query_data_list_name': 'demo2_list'
#              },
#             {'element': 'hq-table',
#              'table_id': 'hq_table',
#              'query_data_list_name': 'demo2_list',
#              'query_data_list_param': None,
#              'show_index': False,
#              'show_page': True,
#              'async': True,
#              'query_condition': None,
#              'query_url': '/public_params/page_child',
#              'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name'},
#                               {'field_name_cn': '中文名', 'field_name_en': 'param_desc'},
#                               {'field_name_cn': '类型', 'field_name_en': 'data_type'},
#                               {'field_name_cn': '注释', 'field_name_en': 'param_detail'}]
#              }]
#         result['data']['s_page_template_config'] = a_page_template_config
#         result['code'] = ReturnEnum.ER_SUCCESS().code
#         result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         return result
#
#
#     ################################第二个页面(改进，重新设计方案：模板先渲染再组合，这样重复组件就不会出现冲突)################################
#     # 生成demo2页面的vue文件
#     # 可以先把数据渲染到基础组件，再进行基础组件融合，基础组件绑定的变量是页面公共的，只需在数据写入时候保证数据区没有重复的变量
#     # 在PageFunction.common_create_page_by_config中过滤重复的配置数据，重复的信息直接在data区不渲染，基础组件的data区都是非必填的
#     # 每个基础组件都需要配套提供一个配置字典,即默认字典（基础组件配置表中，提供默认字典字段，模板调用者可以轻松获取到模板的配套字典）
#     @staticmethod
#     def create_demo2_page2(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         try:
#             # 获取生成页面的配置信息
#             config_result = PageDemo2.get_demo2_config2(s_page_name, **kwargs)
#             if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
#                 return config_result
#             s_page_template_config = config_result['data']['s_page_template_config']
#             # 调用通用生成页面的函数
#             result = PageFunction.common_create_page_by_config(s_page_template_config)
#         except Exception as e:
#             result['code'] = ReturnEnum.ER_SERVER_ERROR().code
#             result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
#         return result
#
#     # 获取demo2页面的配置数据，每个页面自己的配置数据，装配配置数据，需要根据数据类型渲染出具体的搜索框
#     @staticmethod
#     def get_demo2_config2(s_page_name, **kwargs):
#         result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
#         a_page_template_config = [
#             {'element': 'hq-text',
#              'text_id': 'text_status',
#              'content': '状态码:'
#              },
#             {'element': 'hq-input-int',
#              'field_name_en': 'status',
#              'field_name_cn': '状态码',
#              'field_default_value': 'null',
#              'field_data_type': 'Int'
#              },
#             {'element': 'hq-text',
#              'text_id': 'text_condition',
#              'content': '查询条件:'
#              },
#             {'element': 'hq-input-select',
#              'field_name_en': 'condition',
#              'field_name_cn': '查询条件',
#              'field_default_value': '\'\'',
#              'js_function_name': 'demo2_list',
#              'field_data_type': 'String'
#              },
#             {'element': 'hq-text',
#              'text_id': 'text_create_person',
#              'content': '创建人:'
#              },
#             {'element': 'hq-input',
#              'field_name_en': 'create_person',
#              'field_name_cn': '创建人',
#              'field_default_value': '\'\'',
#              'field_data_type': 'String'
#              },
#             {'element': 'hq-button',
#              'content':'查询',
#              'js_function_name': 'demo2_list',
#              'button_type': 'primary'
#              },
#             {'element': 'hq-button-global-delete',
#              'content':'批量删除',
#              'js_function_name': 'delete_by_ids',
#              'js_list_function_name': 'demo2_list',
#              'delete_url': '/public_params/delByIdList',
#              'field_name_en': 'id_list',
#              'button_type': 'danger'
#              },
#             {'element': 'hq-page',
#              'pagination_id': 'hq_pagination',
#              'js_function_name': 'demo2_list'
#              },
#             {'element': 'hq-table',
#              'table_id': 'hq_table',
#              'js_function_name': 'demo2_list',
#              'js_function_param': None,
#              'show_index': False,
#              'show_page': True,
#              'async': True,
#              'custom_query_condition': None,
#              'query_url': '/public_params/page_child',
#              'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name'},
#                               {'field_name_cn': '中文名', 'field_name_en': 'param_desc'},
#                               {'field_name_cn': '类型', 'field_name_en': 'data_type'},
#                               {'field_name_cn': '注释', 'field_name_en': 'param_detail'}],
#             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'},
#                            {'field_name_en': 'status', 'data_type': 'Int', 'using_condition':'this.status !== null && this.status >= 0'},
#                            {'field_name_en': 'create_person', 'data_type': 'String'}]
#              }]
#         result['data']['s_page_template_config'] = a_page_template_config
#         result['code'] = ReturnEnum.ER_SUCCESS().code
#         result['msg'] = ReturnEnum.ER_SUCCESS().msg
#         return result

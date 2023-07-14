import traceback

import ConstEnum
from ReturnEnum import ReturnEnum
from app.class_function.PageFunction import PageFunction


class PageDemo2(object):
    # 生成demo2页面的vue文件
    # 可以先把数据渲染到基础组件，再进行基础组件融合，基础组件绑定的变量是页面公共的，只需在数据写入时候保证数据区没有重复的变量
    # 在PageFunction.common_create_page_by_config中过滤重复的配置数据，重复的信息直接在data区不渲染，基础组件的data区都是非必填的
    # 每个基础组件都需要配套提供一个配置字典,即默认字典（基础组件配置表中，提供默认字典字段，模板调用者可以轻松获取到模板的配套字典）
    @staticmethod
    def create_demo2_page2(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        try:
            # 获取生成页面的配置信息
            config_result = PageDemo2.get_demo2_config2(s_page_name, **kwargs)
            if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
                return config_result
            s_page_template_config = config_result['data']['s_page_template_config']
            # 调用通用生成页面的函数
            result = PageFunction.common_create_page_by_config(s_page_template_config)
        except Exception as e:
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
        return result

    # 获取demo2页面的配置数据，每个页面自己的配置数据，装配配置数据，需要根据数据类型渲染出具体的搜索框
    @staticmethod
    def get_demo2_config2(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-container容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-radio',
             'element_key': '12131',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'field_name_en': 'is_accurate',
             'field_default_value': 'false',
             'radio_options': [{'key': 'true', 'label': '是'}, {'key': 'false', 'label': '否'}]
             },
            {'element': 'hq-input-int',
             'element_key': '12132',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'field_name_en': 'status',
             'field_name_cn': '审核状态',
             'field_default_value': 'null',
             'field_data_type': 'Int'
             },
            {'element': 'hq-container',
             'element_key': '12133',
             'element_type': 'container',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'subElements': [
                 {'subElements': [{
                     'subElements': [
                         {'element': 'hq-text',
                         'element_key': '12134',
                         'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                         'text_id': 'text_status',
                         'content': '状态:'
                         },{'element': 'hq-select',
                          'element_key': '12135',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'status',
                          'field_default_value': 'null',
                          'options_name': 'status_options',
                          'options': [{'value': '-1', 'label': '\'全部\''},
                                      {'value': '0', 'label': '\'草稿\''},
                                      {'value': '1', 'label': '\'已提交\''},
                                      {'value': '2', 'label': '\'已审核\''}]
                         }]}],
                 },
                 {'subElements': [{
                     'subElements': [
                         {'element': 'hq-text',
                          'element_key': '12136',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_condition',
                          'content': '查询条件:'
                         },{'element': 'hq-input-select',
                          'element_key': '12137',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'condition',
                          'field_name_cn': '查询条件',
                          'field_default_value': '\'\'',
                          'js_function_name': 'demo2_list',
                          'field_data_type': 'String'
                         }]}],
                 },
                 {'subElements': [{
                     'subElements': [
                         {'element': 'hq-text',
                          'element_key': '12138',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_create_person',
                          'content': '示例字段:'
                         },{'element': 'hq-input',
                          'element_key': '12139',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'demo_field',
                          'field_name_cn': '示例字段',
                          'field_default_value': '\'\'',
                          'field_data_type': 'String'
                         }]}],
                 }]
             },
            {'element': 'hq-button',
             'element_key': '12140',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '查询',
             'js_function_name': 'demo2_list',
             'button_type': 'primary'
             },
            {'element': 'hq-button-global-delete',
             'element_key': '12141',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '批量删除',
             'js_function_name': 'delete_by_ids',
             'js_list_function_name': 'demo2_list',
             'delete_url': '/public_params/delByIdList',
             'field_name_en': 'id_list',
             'button_type': 'danger'
             },
            {'element': 'hq-page',
             'element_key': '12142',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '12143',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'table_id': 'hq_table',
             'js_function_name': 'demo2_list',
             'js_function_param': None,
             'show_index': False,
             'show_page': True,
             'async': True,
             'custom_query_condition': None,
             'query_url': '/public_params/page_child',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name'},
                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc'},
                              {'field_name_cn': '类型', 'field_name_en': 'data_type'},
                              {'field_name_cn': '注释', 'field_name_en': 'param_detail'}],
             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'},
                                  {'field_name_en': 'status', 'data_type': 'Int',
                                   'using_condition': 'this.status !== null && this.status >= 0'},
                                  {'field_name_en': 'create_person', 'data_type': 'String'}]
             }]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

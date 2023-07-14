import traceback

import ConstEnum
from ReturnEnum import ReturnEnum
from app.page_function.GeneratePage import GeneratePage

class PageDemo(object):
    # 生成demo2页面的vue文件
    # 可以先把数据渲染到基础组件，再进行基础组件融合，基础组件绑定的变量是页面公共的，只需在数据写入时候保证数据区没有重复的变量
    # 在GeneratePage.common_create_page_by_config中过滤重复的配置数据，重复的信息直接在data区不渲染，基础组件的data区都是非必填的
    # 每个基础组件都需要配套提供一个配置字典,即默认字典（基础组件配置表中，提供默认字典字段，模板调用者可以轻松获取到模板的配套字典）
    @staticmethod
    def create_demo_page(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        try:
            # 获取生成页面的配置信息
            config_result = PageDemo.get_demo_config_page_area_container0713(s_page_name, **kwargs)
            if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
                return config_result
            s_page_template_config = config_result['data']['s_page_template_config']
            # 调用通用生成页面的函数（生成各个流程节点的子页面）
            result = GeneratePage.common_generate_page_by_config(s_page_template_config, s_page_name)
        except Exception as e:
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
        return result


    # 搜索区使用容器配置
    @staticmethod
    def get_demo_config_page_area_container0713(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-select-area',
             'element_key': '128dcc54-1449-11ee-86e3-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'sub_elements': [
                 {'sub_elements': [
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-11ee-903d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_condition',
                     'field_name_cn': '查询条件',
                     },
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_pic_url',
                     'field_name_cn': '图片路径',
                     },
                     {'element': 'hq-select-area-input-int',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b91fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 'i_count',
                     'field_name_cn': '总数',
                     }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-input-float',
                      'element_key': '128dcc5b-1949-11ee-902d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'i_price',
                      'field_name_cn': '总价',
                      },
                     {'element': 'hq-select-area-date',
                      'element_key': '128dcc5b-1949-11ee-902d-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt_create_time',
                      'field_name_cn': '创建日期'
                      },
                     {'element': 'hq-select-area-datetime',
                      'element_key': '128dcc5b-1949-11ee-902t-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt2_update_time',
                      'field_name_cn': '修改时间'
                      }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-boolean',
                      'element_key': '128dcc5b-1949-11ee-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'b_flag',
                      'field_name_cn': '是或否',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_sample_image_type',
                      'field_name_cn': '样品图类型',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91rb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_product_packaging',
                      'field_name_cn': '产品外包装',
                      }]
                 }]
            },
            {'element': 'hq-button-area',
             'element_key': '128dcc5b-1949-11ee-9i9d-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'sub_elements': [
                 {'element': 'hq-button',
                 'element_key': '128dcc5b-1949-11ee-909d-6c4b90fb4fde',
                 'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
                 'content': '查询',
                 'js_function_name': 'demo2_list',
                 'button_type': 'primary'
                 },
                {'element': 'hq-button-global-delete',
                 'element_key': '128dcc5c-1949-11ee-a366-6c4b90fb4fde',
                 'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
                 'content': '批量删除',
                 'js_function_name': 'delete_by_ids',
                 'js_list_function_name': 'demo2_list',
                 'delete_url': '/public_params/delByIdList',
                 'field_name_en': 'id_list',
                 'button_type': 'danger'
                 }]
            },
            {'element': 'hq-page',
             'element_key': '128dcc5d-1949-11ee-84ef-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '128dcc5e-1949-11ee-b65a-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'table_id': 'hq_table',
             'js_function_name': 'demo2_list',
             'js_function_param': None,
             'show_index': False,
             'show_page': True,
             'async': True,
             'custom_query_condition': None,
             'query_url': '/public_params/page_child',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '类型', 'field_name_en': 'data_type', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '注释', 'field_name_en': 'param_detail', 'width':'200', 'min_width':'100'}],
             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'}]
             }]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result



    # todo:带数量标记的菜单(用子组件，生成多个文件)-搜索区使用容器配置
    # s_page_name: 页面名称
    # a_flow_name： 流程节点名称, 如果有子组件，子组件名称用页面名+节点名
    @staticmethod
    def get_demo_config_tabs_sub_component(s_page_name, a_flow_name=None, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-tabs',
             'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fde',
             'sub_component': True,
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'active_name': 'page_demo',
             'tab_position': 'top',
             'tab_click': 'changeTabs',
             'tab_click_content': 'console.log("xxx")',
             'sub_elements': [
                 {
                     'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fdf',
                     'page_name': 'page_demo_flow1',
                     'name': 'page_demo_flow1',
                     'label': '测试页面节点1',
                     'page_path': './page_demo_flow1.vue',
                 },
                 {
                     'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fdr',
                     'page_name': 'page_demo_flow2',
                     'name': 'page_demo_flow2',
                     'label': '测试页面节点2',
                     'page_path': './page_demo_flow2.vue',
                 },
             ]},
            {'element': 'hq-select-area',
             'element_key': '128dcc54-1449-11ee-86e3-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'sub_elements': [
                 {'sub_elements': [
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-1hee-903d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_condition',
                     'field_name_cn': '查询条件',
                     },
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_pic_url',
                     'field_name_cn': '图片路径',
                     },
                     {'element': 'hq-select-area-input-int',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b91fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 'i_count',
                     'field_name_cn': '总数',
                     }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-input-float',
                      'element_key': '128dcc5b-1949-11ee-9x2d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'i_price',
                      'field_name_cn': '总价',
                      },
                     {'element': 'hq-select-area-date',
                      'element_key': '128dcc5b-1949-11ee-902d-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt_create_time',
                      'field_name_cn': '创建日期'
                      },
                     {'element': 'hq-select-area-datetime',
                      'element_key': '128dcc5b-1949-11ee-902t-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt2_update_time',
                      'field_name_cn': '修改时间'
                      }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-boolean',
                      'element_key': '128dcc5b-1949-11e1-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'b_flag',
                      'field_name_cn': '是或否',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_sample_image_type',
                      'field_name_cn': '样品图类型',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91rb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_product_packaging',
                      'field_name_cn': '产品外包装',
                      }]
                 }]
            },
            {'element': 'hq-button',
             'element_key': '128dcc5b-1949-11ee-909d-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '查询',
             'js_function_name': 'demo2_list',
             'button_type': 'primary'
             },
            {'element': 'hq-button-global-delete',
             'element_key': '128dcc5c-1949-11ee-a366-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '批量删除',
             'js_function_name': 'delete_by_ids',
             'js_list_function_name': 'demo2_list',
             'delete_url': '/public_params/delByIdList',
             'field_name_en': 'id_list',
             'button_type': 'danger'
             },
            {'element': 'hq-page',
             'element_key': '128dcc5d-1949-11ee-84ef-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '128dcc5e-1949-11ee-b65a-6c4bj0fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'table_id': 'hq_table',
             'js_function_name': 'demo2_list',
             'js_function_param': None,
             'show_index': False,
             'show_page': True,
             'async': True,
             'custom_query_condition': None,
             'query_url': '/public_params/page_child',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '类型', 'field_name_en': 'data_type', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '注释', 'field_name_en': 'param_detail', 'width':'200', 'min_width':'100'}],
             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'}]
             }]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result


    # Tabs标签使用子标签
    @staticmethod
    def get_demo_config_tabs_subElement(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-tabs',
             'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'active_name': 'p_demo2_activeName',
             'tab_position': 'top',
             'js_function_name': 'changeTabs',
             'js_function_content':'console.log("xxx")',
             'sub_elements': [
                 {'name': 'Temp1',
                  'label':'Temp1页面',
                  'element': 'hq-radio',
                  'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fdf',
                  'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
                  'field_name_en': 'is_accurate',
                  'field_default_value': 'false',
                  'radio_options': [{'key': 'true', 'label': '是'}, {'key': 'false', 'label': '否'}]
                 },
                 {'element': 'hq-text',
                  'element_key': '128dcc55-1949-11ee-9355-6c4b91fb4fd1',
                  'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
                  'text_id': 'text_status2',
                  'content': '状态2:',
                  'name': 'ExportExcelView',
                  'label':'Temp2页面',
                 },
                 ]}]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result


    # Tabs标签使用子组件
    @staticmethod
    def get_demo_config_tabs_com(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-tabs',
             'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fde',
             'sub_component': True,
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'active_name': 'p_demo2_activeName',
             'tab_position': 'top',
             'tab_click': 'changeTabs',
             'tab_click_content':'console.log("xxx")',
             'sub_elements': [
                 {
                     'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fdf',
                     'page_name': 'Temp1',
                     'name': 'Temp1',
                     'label':'Temp1页面',
                     'page_path':'./child_pop/Temp1.vue',
                 },
                 {
                     'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fdr',
                     'page_name': 'Temp2',
                     'name': 'ExportExcelView',
                     'label':'Temp2页面',
                     'page_path':'./child_pop/Temp2.vue',
                 },
                 ]}]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result


    # 搜索区使用容器配置
    @staticmethod
    def get_demo_config_select_area_container_bak0706(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-select-area',
             'element_key': '128dcc54-1449-11ee-86e3-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'sub_elements': [
                 {'sub_elements': [
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-11ee-903d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_condition',
                     'field_name_cn': '查询条件',
                     },
                     {'element': 'hq-select-area-input',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b90fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 's_pic_url',
                     'field_name_cn': '图片路径',
                     },
                     {'element': 'hq-select-area-input-int',
                     'element_key': '128dcc5b-1949-11ee-902d-6c4b91fb4fde',
                     'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                     'field_name_en': 'i_count',
                     'field_name_cn': '总数',
                     }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-input-float',
                      'element_key': '128dcc5b-1949-11ee-902d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'i_price',
                      'field_name_cn': '总价',
                      },
                     {'element': 'hq-select-area-date',
                      'element_key': '128dcc5b-1949-11ee-902d-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt_create_time',
                      'field_name_cn': '创建日期'
                      },
                     {'element': 'hq-select-area-datetime',
                      'element_key': '128dcc5b-1949-11ee-902t-6cxb91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'dt2_update_time',
                      'field_name_cn': '修改时间'
                      }]},
                 {'sub_elements': [
                     {'element': 'hq-select-area-boolean',
                      'element_key': '128dcc5b-1949-11ee-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'b_flag',
                      'field_name_cn': '是或否',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91fb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_sample_image_type',
                      'field_name_cn': '样品图类型',
                      },{'element': 'hq-select-area-enum',
                      'element_key': '128dcc5b-1949-144e-912d-6c4b91rb4gde',
                      'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                      'field_name_en': 'e_product_packaging',
                      'field_name_cn': '产品外包装',
                      }]
                 }]
            },
            {'element': 'hq-button',
             'element_key': '128dcc5b-1949-11ee-909d-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '查询',
             'js_function_name': 'demo2_list',
             'button_type': 'primary'
             },
            {'element': 'hq-button-global-delete',
             'element_key': '128dcc5c-1949-11ee-a366-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '批量删除',
             'js_function_name': 'delete_by_ids',
             'js_list_function_name': 'demo2_list',
             'delete_url': '/public_params/delByIdList',
             'field_name_en': 'id_list',
             'button_type': 'danger'
             },
            {'element': 'hq-page',
             'element_key': '128dcc5d-1949-11ee-84ef-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '128dcc5e-1949-11ee-b65a-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'table_id': 'hq_table',
             'js_function_name': 'demo2_list',
             'js_function_param': None,
             'show_index': False,
             'show_page': True,
             'async': True,
             'custom_query_condition': None,
             'query_url': '/public_params/page_child',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '类型', 'field_name_en': 'data_type', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '注释', 'field_name_en': 'param_detail', 'width':'200', 'min_width':'100'}],
             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'}]
             }]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result


    # 搜索区使用容器配置
    @staticmethod
    def get_demo_config_select_area_container_bak0704(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-radio',
             'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'field_name_en': 'is_accurate',
             'field_default_value': 'false',
             'radio_options': [{'key': 'true', 'label': '是'}, {'key': 'false', 'label': '否'}]
             },
            {'element': 'hq-input-int',
             'element_key': '128dcc53-1949-11ee-86aa-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'field_name_en': 'status',
             'field_name_cn': '审核状态',
             'field_default_value': 'null',
             'field_data_type': 'Int'
             },
            {'element': 'hq-select-area',
             'element_key': '128dcc54-1949-11ee-86e3-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'sub_elements': [
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                         'element_key': '128dcc55-1949-11ee-9355-6c4b90fb4fde',
                         'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                         'text_id': 'text_status',
                         'content': '状态:'
                         },{'element': 'hq-select',
                          'element_key': '128dcc56-1949-11ee-8f71-6c4b90fb4fde',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'status',
                          'field_default_value': 'null',
                          'options_name': 'status_options',
                          'options': [{'value': '-1', 'label': '\'全部\''},
                                      {'value': '0', 'label': '\'草稿\''},
                                      {'value': '1', 'label': '\'已提交\''},
                                      {'value': '2', 'label': '\'已审核\''}]
                         }]},
                         {'sub_elements': [
                             {'element': 'hq-text',
                              'element_key': '128dcc57-1949-11ee-94e2-6c4b90fb4fde',
                              'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                              'text_id': 'text_condition',
                              'content': '查询条件:'
                             },{'element': 'hq-input-select',
                              'element_key': '128dcc58-1949-11ee-a168-6c4b90fb4fde',
                              'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                              'field_name_en': 'condition',
                              'field_name_cn': '查询条件',
                              'field_default_value': '\'\'',
                              'js_function_name': 'demo2_list',
                              'field_data_type': 'String'
                             }]},
                        {'sub_elements': [
                             {'element': 'hq-text',
                              'element_key': '128dcc59-1949-11ee-af0b-6c4b90fb4fde',
                              'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                              'text_id': 'text_create_person',
                              'content': '示例字段:'
                              }, {'element': 'hq-input',
                                  'element_key': '128dcc5a-1949-11ee-bdc3-6c4b90fb4fde',
                                  'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                                  'field_name_en': 'demo_field',
                                  'field_name_cn': '示例字段',
                                  'field_default_value': '\'\'',
                                  'field_data_type': 'String'
                                  }]}],
                 },
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc57-1949-11ee-94e2-6c4b90fb4fd1',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_condition2',
                          'content': '查询条件2:'
                         },{'element': 'hq-input-select',
                          'element_key': '128dcc58-1949-11ee-a168-6c4b90fb4fd1',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'condition2',
                          'field_name_cn': '查询条件2',
                          'field_default_value': '\'\'',
                          'js_function_name': 'demo2_list2',
                          'field_data_type': 'String'
                         }]},
                     {'sub_elements': [
                         {'element': 'hq-text',
                         'element_key': '128dcc55-1949-11ee-9355-6c4b91fb4fd1',
                         'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                         'text_id': 'text_status2',
                         'content': '状态2:'
                         },{'element': 'hq-select',
                          'element_key': '128dcc56-1949-11ee-8f71-6c4b91fb4fd1',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'status2',
                          'field_default_value': 'null',
                          'options_name': 'status2_options',
                          'options': [{'value': '-1', 'label': '\'全部\''},
                                      {'value': '0', 'label': '\'草稿\''},
                                      {'value': '1', 'label': '\'已提交\''},
                                      {'value': '2', 'label': '\'已审核\''}]
                         }]},{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc59-1949-11ee-af0b-6c4b90fb4fd1',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_create_person',
                          'content': '示例字段2:'
                         },{'element': 'hq-input',
                          'element_key': '128dcc5a-1949-11ee-bdc3-6c4b90fb4fd1',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'demo_field2',
                          'field_name_cn': '示例字段2',
                          'field_default_value': '\'\'',
                          'field_data_type': 'String'
                         }]}],
                 },
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc59-1949-11ee-af0b-6c4b90fb4fd4',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_create_person3',
                          'content': '示例字段3:'
                         },{'element': 'hq-input',
                          'element_key': '128dcc5a-1949-11ee-bdc3-6c4b90fb4fd3',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'demo_field3',
                          'field_name_cn': '示例字段3',
                          'field_default_value': '\'\'',
                          'field_data_type': 'String'
                         }]},{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc57-1949-11ee-94e2-6c4b90fb4fd3',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_condition3',
                          'content': '查询条件3:'
                         },{'element': 'hq-input-select',
                          'element_key': '128dcc58-1949-11ee-a168-6c4b90fb4fd3',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'condition3',
                          'field_name_cn': '查询条件3',
                          'field_default_value': '\'\'',
                          'js_function_name': 'demo3_list',
                          'field_data_type': 'String'
                         }]}],
                 }]
             },
            {'element': 'hq-button',
             'element_key': '128dcc5b-1949-11ee-909d-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '查询',
             'js_function_name': 'demo2_list',
             'button_type': 'primary'
             },
            {'element': 'hq-button-global-delete',
             'element_key': '128dcc5c-1949-11ee-a366-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '批量删除',
             'js_function_name': 'delete_by_ids',
             'js_list_function_name': 'demo2_list',
             'delete_url': '/public_params/delByIdList',
             'field_name_en': 'id_list',
             'button_type': 'danger'
             },
            {'element': 'hq-page',
             'element_key': '128dcc5d-1949-11ee-84ef-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '128dcc5e-1949-11ee-b65a-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'table_id': 'hq_table',
             'js_function_name': 'demo2_list',
             'js_function_param': None,
             'show_index': False,
             'show_page': True,
             'async': True,
             'custom_query_condition': None,
             'query_url': '/public_params/page_child',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'param_name', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '中文名', 'field_name_en': 'param_desc', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '类型', 'field_name_en': 'data_type', 'width':'200', 'min_width':'100'},
                              {'field_name_cn': '注释', 'field_name_en': 'param_detail', 'width':'200', 'min_width':'100'}],
             'query_field_list': [{'field_name_en': 'condition', 'data_type': 'String'},
                                  {'field_name_en': 'status', 'data_type': 'Int',
                                   'using_condition': 'this.status !== null && this.status >= 0'},
                                  {'field_name_en': 'create_person', 'data_type': 'String'}]
             }]
        result['data']['s_page_template_config'] = a_page_template_config
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result


    # 获取demo2页面的配置数据，每个页面自己的配置数据，装配配置数据，需要根据数据类型渲染出具体的搜索框
    @staticmethod
    def get_demo_config_bak0630(s_page_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        # hq-select-area容器目前预期配置为三行，每行俩个元素
        a_page_template_config = [
            {'element': 'hq-radio',
             'element_key': '128dcc52-1949-11ee-9009-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[0],
             'field_name_en': 'is_accurate',
             'field_default_value': 'false',
             'radio_options': [{'key': 'true', 'label': '是'}, {'key': 'false', 'label': '否'}]
             },
            {'element': 'hq-input-int',
             'element_key': '128dcc53-1949-11ee-86aa-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'field_name_en': 'status',
             'field_name_cn': '审核状态',
             'field_default_value': 'null',
             'field_data_type': 'Int'
             },
            {'element': 'hq-select-area',
             'element_key': '128dcc54-1949-11ee-86e3-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
             'sub_elements': [
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                         'element_key': '128dcc55-1949-11ee-9355-6c4b90fb4fde',
                         'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                         'text_id': 'text_status',
                         'content': '状态:'
                         },{'element': 'hq-select',
                          'element_key': '128dcc56-1949-11ee-8f71-6c4b90fb4fde',
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
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc57-1949-11ee-94e2-6c4b90fb4fde',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_condition',
                          'content': '查询条件:'
                         },{'element': 'hq-input-select',
                          'element_key': '128dcc58-1949-11ee-a168-6c4b90fb4fde',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'condition',
                          'field_name_cn': '查询条件',
                          'field_default_value': '\'\'',
                          'js_function_name': 'demo2_list',
                          'field_data_type': 'String'
                         }]}],
                 },
                 {'sub_elements': [{
                     'sub_elements': [
                         {'element': 'hq-text',
                          'element_key': '128dcc59-1949-11ee-af0b-6c4b90fb4fde',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'text_id': 'text_create_person',
                          'content': '示例字段:'
                         },{'element': 'hq-input',
                          'element_key': '128dcc5a-1949-11ee-bdc3-6c4b90fb4fde',
                          'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[1],
                          'field_name_en': 'demo_field',
                          'field_name_cn': '示例字段',
                          'field_default_value': '\'\'',
                          'field_data_type': 'String'
                         }]}],
                 }]
             },
            {'element': 'hq-button',
             'element_key': '128dcc5b-1949-11ee-909d-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '查询',
             'js_function_name': 'demo2_list',
             'button_type': 'primary'
             },
            {'element': 'hq-button-global-delete',
             'element_key': '128dcc5c-1949-11ee-a366-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[2],
             'content': '批量删除',
             'js_function_name': 'delete_by_ids',
             'js_list_function_name': 'demo2_list',
             'delete_url': '/public_params/delByIdList',
             'field_name_en': 'id_list',
             'button_type': 'danger'
             },
            {'element': 'hq-page',
             'element_key': '128dcc5d-1949-11ee-84ef-6c4b90fb4fde',
             'page_area': ConstEnum.PAGE_CONFIG_INFO.HQ_TEMPLATE_TAG_LIST.value[3],
             'pagination_id': 'hq_pagination',
             'js_function_name': 'demo2_list'
             },
            {'element': 'hq-table',
             'element_key': '128dcc5e-1949-11ee-b65a-6c4b90fb4fde',
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

import traceback

from django.template.loader import render_to_string
from ReturnEnum import ReturnEnum

class CreatePage(object):
    @staticmethod
    def parse_vue(elements):
        vueCode = ''
        for ele in elements:
            # 读取并渲染模板文件
            template_name = 'input\\' + ele['element'] + '.vue'
            context = {'ele': ele}
            rendered_string = render_to_string(template_name, context)
            vueCode += rendered_string
        # 读取并渲染模板文件
        main_template_name = 'root\\template_result.vue'
        main_context = {'vueCode': vueCode}
        main_rendered_string = render_to_string(main_template_name, main_context)
        return main_rendered_string

    # 这种渲染方式只能单个模板渲染，多个模板渲染拼接不了，后期改造成兼容多个模板的，就可以替代生成完整页面的函数了
    # 或者替换为只实现单个页面的渲染功能，这样做到功能单一
    @staticmethod
    def parse_hq(elements):
        vueCode = ''
        for ele in elements:
            # 读取并渲染模板文件
            template_name = 'input\\' + ele['element'] + '.hq'
            context = {'ele': ele}
            rendered_string = render_to_string(template_name, context)
            vueCode += rendered_string
        # 读取并渲染模板文件
        main_template_name = 'root\\template_result.vue'
        main_context = {'vueCode': vueCode}
        main_rendered_string = render_to_string(main_template_name, main_context)
        return main_rendered_string

    @staticmethod
    def create_temp_vue():
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        elements = ''
        rendered_string = ''
        elements = CreatePage.getElements()
        try:
            rendered_string = CreatePage.parse_vue(elements)
        except Exception as e:
            result["code"] = ReturnEnum.ER_FAIL().code
            result["msg"] = ReturnEnum.ER_FAIL().msg + ": " + '模板渲染失败'
            return result
        try:
            table_vue = "app\\templates\\output\\middleFile\\table.vue"  # 生成指定路径下的vue
            f = open(table_vue, 'w', encoding='utf-8')
            f.write(rendered_string)
            f.close()
        except:
            traceback.print_exc()
        result["code"] = ReturnEnum.ER_SUCCESS().code
        result["msg"] = ReturnEnum.ER_SUCCESS().msg
        return result
        # return HttpResponse(rendered_string)

    @staticmethod
    def getElements():
        elements = ''
        elements = [
            {'element': 'el-table',
             'table_id': 'temp_table',
             'show_index': 'true',
             'show_operate': 'true',
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'class_name'},
                              {'field_name_cn': '中文名', 'field_name_en': 'class_desc'},
                              {'field_name_cn': '类型', 'field_name_en': 'type'},
                              {'field_name_cn': '注释', 'field_name_en': 'class_detail'}],
             'table_data': [{
                 "id": 1,
                 "class_name": "a_function_points",
                 "class_desc": "功能点列表",
                 "class_detail": "任务主线表中的功能点列表",
                 "type": "o_function_points[ ]"
             }, {
                 "id": 2,
                 "class_name": "s_function_points",
                 "class_desc": "功能点",
                 "class_detail": "任务主线表中的需求功能点",
                 "type": "String"
             }]
             }
        ]
        return elements

    # 创建标签菜单vue文件
    @staticmethod
    def create_tabs_menu_vue():
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        elements = CreatePage.getTabsElements()
        try:
            rendered_string = CreatePage.parse_hq(elements)
        except Exception as e:
            result["code"] = ReturnEnum.ER_FAIL().code
            result["msg"] = ReturnEnum.ER_FAIL().msg + ": " + '模板渲染失败'
            return result
        try:
            tabs_vue = "app\\templates\\output\\middleFile\\tabs.hq"  # 生成指定路径下的vue
            f = open(tabs_vue, 'w', encoding='utf-8')
            f.write(rendered_string)
            f.close()
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['data']['s_vue_component_content'] = rendered_string
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
        except Exception as e:
            traceback.print_exc()
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
        return result

    # 创建搜索区vue文件
    @staticmethod
    def create_select_area_vue():
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        elements = CreatePage.getSelectAreaElements()
        try:
            rendered_string = CreatePage.parse_hq(elements)
        except Exception as e:
            result["code"] = ReturnEnum.ER_FAIL().code
            result["msg"] = ReturnEnum.ER_FAIL().msg + ": " + '模板渲染失败'
            return result
        try:
            select_vue = "app\\templates\\middleFile\\pageArea\\select.hq"  # 生成指定路径下的vue
            f = open(select_vue, 'w', encoding='utf-8')
            f.write(rendered_string)
            f.close()
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['data']['s_vue_component_content'] = rendered_string
        except Exception as e:
            traceback.print_exc()
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
        return result

    # 创建数据区vue文件
    @staticmethod
    def create_data_area_vue():
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        elements = CreatePage.getTableElements()
        try:
            rendered_string = CreatePage.parse_hq(elements)
        except Exception as e:
            print(str(e))
            result["code"] = ReturnEnum.ER_FAIL().code
            result["msg"] = ReturnEnum.ER_FAIL().msg + ": " + '模板渲染失败'
            return result
        try:
            table_vue = "app\\templates\\middleFile\\pageArea\\table.hq"  # 生成指定路径下的vue
            f = open(table_vue, 'w', encoding='utf-8')
            f.write(rendered_string)
            f.close()
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
            result['data']['s_vue_component_content'] = rendered_string
        except Exception as e:
            traceback.print_exc()
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
        return result

    # 创建全局按钮区vue文件
    @staticmethod
    def create_global_button_vue():
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        elements = CreatePage.getBtnElements()
        try:
            rendered_string = CreatePage.parse_hq(elements)
        except Exception as e:
            print(str(e))
            result["code"] = ReturnEnum.ER_FAIL().code
            result["msg"] = ReturnEnum.ER_FAIL().msg + ": " + '模板渲染失败'
            return result
        try:
            table_vue = "app\\templates\\middleFile\\pageArea\\global_button_area.hq"  # 生成指定路径下的vue
            f = open(table_vue, 'w', encoding='utf-8')
            f.write(rendered_string)
            f.close()
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
            result['data']['s_vue_component_content'] = rendered_string
        except Exception as e:
            traceback.print_exc()
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg
        return result

    @staticmethod
    def getTabsElements():
        elements = [
            {'element': 'baseTemplate\\base-tabs-badge', 'elTabPanes': [
                {'name': 'suggest', 'content': '', 'label': 'ASIN/Item_ID备货建议', 'badge_show': 'false',
                 'badge_value': '0'},
                {'name': 'require', 'content': '', 'label': '备货需求', 'badge_show': 'true', 'badge_value': '64'},
                {'name': 'examine', 'content': '', 'label': '备货审核', 'badge_show': 'true', 'badge_value': '109'},
                {'name': 'approve', 'content': '', 'label': '审核通过', 'badge_show': 'true',
                 'badge_value': '163785'},
                {'name': 'discard', 'content': '', 'label': '备货单废弃', 'badge_show': 'true',
                 'badge_value': '12674'},
                {'name': 'pending', 'content': '', 'label': '挂单待处理', 'badge_show': 'true', 'badge_value': '0'},
                {'name': 'fbaTest', 'content': '', 'label': '备货审核（FBA缓存测试）', 'badge_show': 'true',
                 'badge_value': '89'},
                {'name': 'seasonal', 'content': '', 'label': '时节性产品', 'badge_show': 'false',
                 'badge_value': '0'},
            ], 'badge_if': '', 'activeName': 'require'}
        ]
        return elements

    @staticmethod
    def getSelectAreaElements():
        elements = [
            {'element': 'baseTemplate\\base-select-area', 'element_id': 'temp_select', 'subPanes': [{
                'subRow': [
                    {'field_name_cn': '订单号', 'field_name_en': 's_order_no', 'placeholder': '多搜索英文逗号隔开'},
                    {'field_name_cn': '海外仓发货批次号', 'field_name_en': 's_deliver_no', 'placeholder': '模糊搜索'},
                    {'field_name_cn': '组包号', 'field_name_en': 's_zb_no', 'placeholder': '模糊搜索'},
                    {'field_name_cn': 'SKC', 'field_name_en': 's_skc', 'placeholder': '模糊搜索'},
                    {'field_name_cn': 'FN码', 'field_name_en': 's_fnsku', 'placeholder': '模糊搜索'}]
            }, {
                'subRow': [
                    {'field_name_cn': '卖家简称', 'field_name_en': 's_shop_name', 'placeholder': '多搜索英文逗号隔开'},
                    {'field_name_cn': 'SKU产品类型', 'field_name_en': 'e_sku_producttype', 'placeholder': '多搜索英文逗号隔开'},
                    {'field_name_cn': '订单发货状态', 'field_name_en': 's_deliver_status', 'placeholder': '多搜索英文逗号隔开'},
                    {'field_name_cn': '创建时间', 'field_name_en': 'dt2_create_time', 'placeholder': '模糊搜索'},
                    {'field_name_cn': '发布时间', 'field_name_en': 'dt2_publish_time', 'placeholder': '模糊搜索'}]
            }]}
        ]
        return elements

    @staticmethod
    def getTableElements():
        elements = [
            {'element': 'baseTemplate\\base-table',
             'element_id': 'temp_table',
             'show_page': True,
             'show_index': False,
             'show_operate': True,
             'table_header': [{'field_name_cn': '英文名', 'field_name_en': 'class_name'},
                              {'field_name_cn': '中文名', 'field_name_en': 'class_desc'},
                              {'field_name_cn': '类型', 'field_name_en': 'type'},
                              {'field_name_cn': '注释', 'field_name_en': 'class_detail'}],
             'table_data': [{
                 "id": 1,
                 "class_name": "a_function_points",
                 "class_desc": "功能点列表",
                 "class_detail": "任务主线表中的功能点列表",
                 "type": "o_function_points[ ]"
             }, {
                 "id": 2,
                 "class_name": "s_function_points",
                 "class_desc": "功能点",
                 "class_detail": "任务主线表中的需求功能点",
                 "type": "String"
             }, {
                 "id": 3,
                 "class_name": "s_login_name_en",
                 "class_desc": "登录人英文名",
                 "class_detail": "登录人名称（英文）",
                 "type": "String"
             }]
             }
        ]
        return elements

    @staticmethod
    def getBtnElements():
        elements = [
            {'element': 'baseTemplate\\base-global-button',
             'element_id': 'temp_page_button',
             'subPanes': [{
                 'bind_model_en': 'condition',
                 'button_name': '查询',
                 'method_name': 'select_list',
                 'method_async': True,
                 'method_content': '',
                 'default_value': 'null'
             }, {
                 'bind_model_en': '',
                 'button_name': '新增',
                 'method_name': 'open_add_form',
                 'method_content': '',
                 'default_value': ''
             }, {
                 'bind_model_en': 'id_list',
                 'method_async': True,
                 'button_name': '删除',
                 'method_name': 'del_by_ids',
                 'method_content': '3',
                 'default_value': '[]'
             }, ]}
        ]
        return elements

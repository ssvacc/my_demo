import os
import traceback

from django.template.loader import render_to_string

from ConstEnum import PAGE_CONFIG_INFO
from ReturnEnum import ReturnEnum
from app.function import common


class PageFunction(object):
    """
    通用生成页面的接口函数, 跳过中间文件，直接拿渲染好的数据解析拼接
    参数: a_page_template_config: 页面配置信息，每个组件需有自己的组件模板名，page_area信息，组件key(对此次渲染唯一，用于容器识别渲染)
    返回值: s_vue_component_content 生成后的vue文件内容
           s_vue_component_file_name 生成后的vue文件名,存放在templates/output/
    """
    @staticmethod
    def common_create_page_by_config(a_page_template_config, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        try:
            # "page_id", "page_code" 看后续开发情况决定是舍弃还是抽离到上层
            # "elements", "data", "methods", "style", "life_cycle" 固定字典key,用于vue组件各个区模板渲染
            o_vue_area = {"page_id": "demo_page", "page_code": "demo_page"}
            time = common.getNowTime()
            s_vue_component_file_name = o_vue_area['page_id'] + '_' + str(time) + ".vue"
            # 一.data区重复字段加上 repeat_field_name_en，避免模板渲染时重复渲染
            a_field_name_en = []
            for config in a_page_template_config:
                if 'field_name_en' in config.keys():
                    field_name_en = config['field_name_en']
                    if field_name_en in a_field_name_en:
                        config['repeat_field_name_en'] = field_name_en
                    else:
                        a_field_name_en.append(field_name_en)
            # 二.遍历a_page_template_config，将容器组件中子标签的key抽取到一个list中，
            # a_page_template_config中需保证容器组件在子组件前面，且容器组件和子组件的page_area保持一致，子组件要连续，中间不要出现其他组件
            # 步骤三执行时，先渲染到容器组件，成为一个中间模板
            # todo.A:方案1.在子组件的后面加一个配置项，用于容器的收尾标记（不好用）
            #        方案2.子标签的key抽取到一个list中，每渲染完成一个子标签，移除一个key,直到list为空则将容器组件存到o_vue_area中

            # 三.遍历a_page_template_config，进行模板渲染
            for config in a_page_template_config:
                element_name_result = PageFunction.get_base_element_name(config['element'])
                if element_name_result['code'] != ReturnEnum.ER_SUCCESS().code:
                    return element_name_result
                template_name = element_name_result['data']['s_template_file_name']
                template_rendered_string = render_to_string(template_name, config)
                # todo.B:如果是容器组件，则生成中间模板，再将所有的子组件加上标记，子组件在C步骤中不再存到o_vue_area的data区中，而是存到中间模板的渲染区块
                o_vue_area = PageFunction.analysis_rendered_data(o_vue_area, template_rendered_string, config['page_area'])
            template_name = 'root\\base_vue.hq'
            context = {'ele': o_vue_area}
            main_rendered_string = render_to_string(template_name, context)
            hq_vue_file_name = "app\\templates\\output\\" + s_vue_component_file_name  # 生成指定路径下的vue
            f = open(hq_vue_file_name, 'w', encoding='utf-8')
            f.write(main_rendered_string)
            f.close()
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['data']['s_vue_component_content'] = main_rendered_string
            result['data']['s_vue_component_file_name'] = s_vue_component_file_name
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
        except Exception as e:
            traceback.print_exc()
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
        return result

    # 获取基础组件模板名称
    @staticmethod
    def get_base_element_name(s_element_name):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        try:
            BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\input\\'
            flag = True
            template_name = BASE_PATH + 'baseElement\\' + s_element_name + '.hq'
            if not os.path.exists(template_name):
                template_name = BASE_PATH + 'groupElement\\' + s_element_name + '.hq'
                if not os.path.exists(template_name):
                    template_name = BASE_PATH + 'customElement\\' + s_element_name + '.hq'
                    if not os.path.exists(template_name):
                        flag = False
            if flag:
                result['code'] = ReturnEnum.ER_SUCCESS().code
                result['msg'] = ReturnEnum.ER_SUCCESS().msg
                result['data']['s_template_file_name'] = template_name
            else:
                result['code'] = ReturnEnum.ER_NO_DATA().code
                result['msg'] = ReturnEnum.ER_NO_DATA().msg
        except Exception as e:
            result['code'] = ReturnEnum.ER_SERVER_ERROR().code
            result['msg'] = ReturnEnum.ER_SERVER_ERROR().msg + traceback.format_exc()
        return result

    # 解析各个区的数据：hq-template,hq-data,hq-methods,hq-style,hq-life-cycle(生命周期会进行二次解析)
    @staticmethod
    def analysis_rendered_data(o_vue_area, template_rendered_string, s_page_area):
        a_tag_name = PAGE_CONFIG_INFO.HQ_TAG_LIST.value
        for s_tag_name in a_tag_name:
            if s_tag_name not in o_vue_area.keys():
                o_vue_area[s_tag_name] = ''
            if s_page_area not in o_vue_area.keys():
                o_vue_area[s_page_area] = ''
            # template区
            if s_tag_name == PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0]:
                template_content = PageFunction.get_by_tag(template_rendered_string, s_tag_name)
                if template_content:
                    # todo.C:如果是容器子组件（根据parent_key标识属于哪个父组件），将template_content放到o_vue_area[parent_key]中,而不放到o_vue_area[s_page_area]
                    o_vue_area[s_page_area] += template_content
            # 生命周期区
            elif s_tag_name == PAGE_CONFIG_INFO.HQ_TAG_LIST.value[4]:
                life_cycle_content = PageFunction.get_by_tag(template_rendered_string, s_tag_name)
                if life_cycle_content:
                    o_vue_area[s_tag_name] += life_cycle_content
                    PageFunction.analysis_sub_tag(o_vue_area, life_cycle_content, PAGE_CONFIG_INFO.HQ_LIFE_CYCLE_TAG_LIST.value)
            else:
                o_vue_area[s_tag_name] += PageFunction.get_by_tag(template_rendered_string, s_tag_name)
        return o_vue_area

    # 解析一级标签中的内容
    @staticmethod
    def analysis_sub_tag(o_vue_area, s_tag_content, a_sub_tag_name):
        for s_tag_name in a_sub_tag_name:
            s_sub_tag_content = PageFunction.get_by_tag(s_tag_content, s_tag_name)
            if s_tag_name not in o_vue_area.keys():
                o_vue_area[s_tag_name] = ''
            o_vue_area[s_tag_name] += s_sub_tag_content
        return o_vue_area

    # 获取自定义标签中的内容
    @staticmethod
    def get_by_tag(s_vue_component_content, s_tag):
        s_tag_content = ''
        s_tag = '<' + s_tag + '>'
        s_tag_end = s_tag[0] + '/' + s_tag[1:]
        if s_tag in s_vue_component_content and s_tag_end in s_vue_component_content:
            s_tag_content = s_vue_component_content[
                            s_vue_component_content.find(s_tag) + len(s_tag):s_vue_component_content.find(s_tag_end)]
        return str(s_tag_content)


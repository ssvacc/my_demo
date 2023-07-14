import os
import re
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
            # 一.data区重复字段加上 repeat_field_name_en 避免模板渲染时重复渲染
            a_field_name_en = []
            PageFunction.set_repeat_field_name(a_field_name_en, a_page_template_config)
            # 二.遍历a_page_template_config，将容器组件中子标签的key抽取到一个list中
            # a_page_template_config中需保证容器组件在子组件前面，且容器组件和子组件的page_area保持一致，子组件要连续，中间不要出现其他组件
            # 步骤三执行时，先渲染到容器组件，成为一个中间模板
            # todo.A(配置中有层级关系，无需再处理):方案1.在子组件的后面加一个配置项，用于容器的收尾标记（不好用）
            #        方案2.子标签的key抽取到一个list中，每渲染完成一个子标签，移除一个key,直到list为空则将容器组件存到o_vue_area中（不好用）
            #        *方案3.配置的数据结构中，容器组件和子组件之间有层级关系，（需重新处理data区去重的逻辑），层级关系更好处理渲染等问题
            # a_sub_elements = []
            # for config in a_page_template_config:
            #     if 'subElements' in config.keys() and config['subElements']:
            #         subElements = config['subElements']
            #         for subElement in subElements:
            #             a_sub_elements.append(subElement)
            o_vue_area = {"page_id": "demo_page", "page_code": "demo_page"}
            # 三.遍历a_page_template_config，进行模板渲染
            PageFunction.rendered_data_by_config(a_page_template_config, o_vue_area)
            template_name = 'root\\base_vue.hq'
            context = {'ele': o_vue_area}
            main_rendered_string = render_to_string(template_name, context)
            time = common.getNowTime()
            s_vue_component_file_name = o_vue_area['page_id'] + '_' + str(time) + ".vue"
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
    def rendered_data_by_config(a_page_template_config, o_vue_area, parent_element_key=None):
        for config in a_page_template_config:
            if not PageFunction.is_element(config):
                if PageFunction.has_sub_element(config):
                    # 容器结构配置，往深层次渲染
                    PageFunction.rendered_data_by_config(config['subElements'], o_vue_area, parent_element_key)
                continue
            s_template_file_name = PageFunction.get_base_element_name(config['element'])
            if not s_template_file_name:
                # 未找到基础组件，则跳过
                continue
            template_rendered_string = render_to_string(s_template_file_name, config)
            # todo.B:如果是容器组件，则生成中间模板，再将所有的子组件加上标记(parent_element_key不为None的都是子组件)，子组件在C步骤中不再存到o_vue_area的data区中，而是存到中间模板的渲染区块
            if PageFunction.has_sub_element(config):
                if PageFunction.is_element(config):
                    if config['element_key'] not in o_vue_area.keys():
                        o_vue_area['element_key'] = ''
                    o_vue_area[config['element_key']] = template_rendered_string
                # 递归，将子组件深度渲染到容器中
                subElements = config['subElements']
                PageFunction.rendered_data_by_config(subElements, o_vue_area, config['element_key'])
                # 用渲染后的子组件数据替换容器模板的初始内容
                s_hqTemplate1 = PageFunction.get_by_tag(template_rendered_string, "hqTemplate")[0]
                s_hqTemplate_detail = PageFunction.get_by_tag(o_vue_area[config['element_key']], "hqTemplate")[0]
                template_rendered_string = template_rendered_string.replace(s_hqTemplate1, s_hqTemplate_detail)
            # if parent_element_key and parent_element_key in o_vue_area.keys() and o_vue_area[parent_element_key]:
            #     # parent_element_key不为空，这里是渲染完成的子组件，将渲染结果存到中间文件中并更新中间文件,只涉及Template区
            #     # 现在要把 template_rendered_string 中的 hqTemplate 区的数据渲染到容器组件的相对应位置上
            #     # print(template_rendered_string)
            #     s_hqTemplate = PageFunction.get_by_tag(template_rendered_string, "hqTemplate")[0]
            #     container_middle_template = o_vue_area[parent_element_key]
            #     # a_hqElement = PageFunction.get_by_tag(container_middle_template, "hqElement")
            #     # 这一行显得有点多余，可以不要
            #     a_hqElementKey = PageFunction.get_by_tag(container_middle_template, "hqElementKey")
            #     if config['element_key'] in a_hqElementKey:
            #         tag = '<hqElementKey>' + config['element_key'] + '</hqElementKey>'
            #         o_vue_area[parent_element_key] = container_middle_template.replace(tag, s_hqTemplate)
            PageFunction.analysis_rendered_data(o_vue_area, template_rendered_string, config, parent_element_key)

    # 遍历配置组件模板结构，有重复的变量，增加repeat_field_name_en，避免vue data区出现重复变量
    @staticmethod
    def set_repeat_field_name(a_field_name_en, a_page_template_config):
        for config in a_page_template_config:
            if 'field_name_en' in config.keys() and config['field_name_en']:
                field_name_en = config['field_name_en']
                if field_name_en in a_field_name_en:
                    config['repeat_field_name_en'] = field_name_en
                else:
                    a_field_name_en.append(field_name_en)
            if PageFunction.has_sub_element(config):
                subElements = config['subElements']
                PageFunction.set_repeat_field_name(a_field_name_en, subElements)

    # 获取基础组件模板名称
    @staticmethod
    def get_base_element_name(s_element_name):
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\input\\'
        template_name = BASE_PATH + 'baseElement\\' + s_element_name + '.hq'
        if not os.path.exists(template_name):
            template_name = BASE_PATH + 'groupElement\\' + s_element_name + '.hq'
            if not os.path.exists(template_name):
                template_name = BASE_PATH + 'customElement\\' + s_element_name + '.hq'
                if not os.path.exists(template_name):
                    template_name = None
        s_template_file_name = template_name
        return s_template_file_name

    # 解析各个区的数据：hq-template,hq-data,hq-methods,hq-style,hq-life-cycle(生命周期会进行二次解析)
    @staticmethod
    def analysis_rendered_data(o_vue_area, template_rendered_string, config, parent_element_key):
        s_page_area = config['page_area']
        a_tag_name = PAGE_CONFIG_INFO.HQ_TAG_LIST.value
        for s_tag_name in a_tag_name:
            if s_tag_name not in o_vue_area.keys():
                o_vue_area[s_tag_name] = ''
            if s_page_area not in o_vue_area.keys():
                o_vue_area[s_page_area] = ''
            # template区
            if s_tag_name == PAGE_CONFIG_INFO.HQ_TAG_LIST.value[0]:
                template_content = PageFunction.get_by_tag(template_rendered_string, s_tag_name)[0]
                if not template_content:
                    return
                if not parent_element_key:
                    # 不是容器的子组件，则将数据渲染到相应区块中
                    o_vue_area[s_page_area] += template_content
                else:
                    if parent_element_key and parent_element_key in o_vue_area.keys() and o_vue_area[parent_element_key]:
                        # parent_element_key不为空，这里是渲染完成的子组件，将渲染结果存到中间文件中并更新中间文件,只涉及Template区
                        # 现在要把 template_rendered_string 中的 hqTemplate 区的数据渲染到容器组件的相对应位置上
                        # print(template_rendered_string)
                        s_hqTemplate = PageFunction.get_by_tag(template_rendered_string, "hqTemplate")[0]
                        container_middle_template = o_vue_area[parent_element_key]
                        # a_hqElement = PageFunction.get_by_tag(container_middle_template, "hqElement")
                        # 这一行显得有点多余，可以不要
                        # a_hqElementKey = PageFunction.get_by_tag(container_middle_template, "hqElementKey")
                        element_key = config['element_key']
                        if element_key in container_middle_template:
                            tag = '<hqElementKey>' + element_key + '</hqElementKey>'
                            o_vue_area[parent_element_key] = container_middle_template.replace(tag, s_hqTemplate)
            # 生命周期区
            elif s_tag_name == PAGE_CONFIG_INFO.HQ_TAG_LIST.value[4]:
                life_cycle_content = PageFunction.get_by_tag(template_rendered_string, s_tag_name)[0]
                if life_cycle_content:
                    o_vue_area[s_tag_name] += life_cycle_content
                    PageFunction.analysis_sub_tag(o_vue_area, life_cycle_content, PAGE_CONFIG_INFO.HQ_LIFE_CYCLE_TAG_LIST.value)
            else:
                o_vue_area[s_tag_name] += PageFunction.get_by_tag(template_rendered_string, s_tag_name)[0]

    # 解析下一级标签中的内容
    @staticmethod
    def analysis_sub_tag(o_vue_area, s_tag_content, a_sub_tag_name):
        for s_tag_name in a_sub_tag_name:
            s_sub_tag_content = PageFunction.get_by_tag(s_tag_content, s_tag_name)[0]
            if s_tag_name not in o_vue_area.keys():
                o_vue_area[s_tag_name] = ''
            o_vue_area[s_tag_name] += s_sub_tag_content
        return o_vue_area

    # 获取自定义标签中的内容
    @staticmethod
    def get_by_tag(s_vue_component_content, s_tag):
        s_tag = '<' + s_tag + '>'
        s_tag_end = s_tag[0] + '/' + s_tag[1:]
        s_tag_result = [index.start() for index in re.finditer(s_tag, s_vue_component_content)]
        s_tag_end_result = [index.start() for index in re.finditer(s_tag_end, s_vue_component_content)]
        a_tag_content = []
        if s_tag in s_vue_component_content and s_tag_end in s_vue_component_content:
            if len(s_tag_result) > 1 and len(s_tag_result) == len(s_tag_end_result):
                for i in range(0, len(s_tag_result)):
                    s_tag_content = s_vue_component_content[s_tag_result[i] + len(s_tag):s_tag_end_result[i]]
                    a_tag_content.append(s_tag_content)
            else:
                s_tag_content = s_vue_component_content[s_vue_component_content.find(s_tag) + len(s_tag):s_vue_component_content.find(s_tag_end)]
                a_tag_content.append(str(s_tag_content))
        if len(a_tag_content) == 0:
            a_tag_content.append('')
        return a_tag_content

    # 判断配置项是否包含子标签
    @staticmethod
    def has_sub_element(config):
        return 'subElements' in config.keys() and config['subElements']

    # 判断配置项是否是组件
    @staticmethod
    def is_element(config):
        return 'element' in config.keys() and config['element']


# -*- coding: utf-8 -*-
# @Time : 2023-06-12
# @Author : ni heng
# @File : PageClassConfig.py
import traceback

from django.template.loader import render_to_string

from ReturnEnum import ReturnEnum
import webbrowser

from app.function import common

def parse(elements):
    BASE_URL="app/web_page/template/"
    vueCode = ''
    main_rendered_string = ''
    try:
        for ele in elements:
            # 读取并渲染模板文件
            template_name = BASE_URL + ele['element'] + '.vue'
            context = {'ele': ele}
            rendered_string = render_to_string(template_name, context)
            vueCode += rendered_string
        # 读取并渲染模板文件
        main_template_name = BASE_URL + 'view_page.html'
        main_context = {'vueCode': vueCode}
        main_rendered_string = render_to_string(main_template_name, main_context)
    except Exception as e:
        traceback.extract_stack()
    return main_rendered_string

class PageClassConfig(object):
    @staticmethod
    def get_html_base_head():
        a = """<meta http-equiv="Content-Type"content="text/html;charset=utf-8">"""
        head = """<meta http-equiv="Content-Type" content="text/html" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="icon" href="../favicon.ico">
         """
        return head

################使用字符串拼接生成html#################################
    # 获取基础组件
    @staticmethod
    def get_base_component(i_base_component_id, **kwargs):
        a_component_data = ''
        if 'a_component_data' in kwargs.keys():
            a_component_data = kwargs.get('a_component_data')
        js_function = ''
        if 'js_function' in kwargs.keys():
            js_function = kwargs.get('js_function')
        base_component_span = """"""
        if i_base_component_id == 1:
            base_component_span = """<span>%s</span>"""%a_component_data
        if i_base_component_id == 2:
            base_component_span = """<button id="btn">%s</button>"""%a_component_data
        if i_base_component_id == 3:
            base_component_span = """<template style="width: 100px" /><button  onclick="%s">查询</button>"""%js_function
        if i_base_component_id == 4:
            base_component_span = """
            <select name="baseSelect" style="width: 100px">
                <option value="%s">%s</option>
                <option value="%s">%s</option>
                <option value="%s">%s</option>
            </select>"""%a_component_data
        if i_base_component_id == 5:
            base_component_span = """<p>巡检地点 : 机房&nbsp;&nbsp;开始时间 : {{ start_time }}&nbsp;&nbsp;结束时间 : {{ stop_time }} </p>
            """
        return base_component_span

    @staticmethod
    def get_page_select_area_param_html(page_class_config, **kwargs):
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        base_html1 = "web_pages\\Page_class12.html"  # 生成指定路径下的html
        head = PageClassConfig.get_html_base_head()
        f= open(base_html1, 'w')
        # 模拟查询基础组件表得到基础组件代码
        component1 = PageClassConfig.get_base_component(1, a_component_data ="文字") # span标签
        component2 = PageClassConfig.get_base_component(2, a_component_data="按钮") # button标签
        component3 = PageClassConfig.get_base_component(3, js_function="alert('查询')") # input标签
        component4 = PageClassConfig.get_base_component(4, a_component_data=(1,"A", 2, "B", 3, "C")) # 下拉框标签
        message1 = """
<!DOCTYPE html>
<html lang="en">
    <head>
        %s
    </head>
    <body>
      %s
      %s
      %s
      %s
    </body>
</html>"""%(head, component1, component2, component3, component4)
        f.write(message1)
        f.close()
        webbrowser.open(base_html1, new=1)
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

################使用模板语言生成html#################################
    @staticmethod
    def create_html_by_template(**kwargs):
        from jinja2 import Environment, FileSystemLoader
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        start_time = common.getNowTimeStamp()
        stop_time = common.getNowTimeStamp()
        item1 = {"id": 1, "name": "InterfaceFunction","desc": "接口函数","detail": "接口函数相关类", "age":"28"}
        item2 = {"id": 2, "name": "OrderAmazon","desc": "亚马逊订单","detail": "亚马逊订单", "age":"28"}
        item3 = {"id": 3, "name": "School","desc": "学校","detail": "学校相关类", "age":"28"}
        body = [item1, item2, item3]
        # head = ['id', 'name', 'desc', 'detail', 'age']
        base_html2 = "web_pages\\PageResult.html"
        f = open(base_html2, 'w')
        html_content = """"""
        try:
            env = Environment(loader=FileSystemLoader('./'))
            template = env.get_template('web_pages/template.html')
            html_content = template.render(start_time=start_time, stop_time=stop_time, body=body)
            # html_content = template.render(start_time=start_time, stop_time=stop_time, body=body, head=head)
        except Exception as e:
            print(e)
        f.write(html_content)
        f.close()
        webbrowser.open(base_html2, new=1)
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

################生成包含JS的html#################################
    @staticmethod
    def create_html_and_js(**kwargs):
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        base_html3 = "web_pages\\Page_class3.html"  # 生成指定路径下的html
        content = PageClassConfig.get_html_content()
        f = open(base_html3, 'w')
        f.write(content)
        f.close()
        webbrowser.open(base_html3, new=1)
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

    @staticmethod
    def get_html_content():
        # 模拟查询基础组件表得到基础组件代码
        button = PageClassConfig.get_base_component(2, a_component_data="留言按钮") # button标签
        # 模拟查询基础js表得到基础js代码
        js_content = PageClassConfig.get_base_js()
        content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html" />
<script type="text/javascript" src="move.js"></script>
<style>
#ul1{margin: 0;position: absolute;right: 10px;top: 8px;
width: 700px;height: 500px;border: 1px solid #000;padding: 10px;overflow: hidden;}
li{line-height: 28px;border-bottom: 1px dotted #000;list-style: none;word-break:break-all;overflow: hidden;}
</style>
<script>
window.onload= function() {
    %s
}
</script>
<title>页面和js</title>
</head>
<body>
    <textarea rows="10" cols="50" id="content"></textarea>
    %s
    <ul id="ul1"></ul>
</body>
</html>
        """ % (js_content,button)
        return content


    # 获取基础js
    @staticmethod
    def get_base_js():
        js_func = """
        var oContent = document.getElementById('content');
        var oBtn = document.getElementById('btn');
        var oUl = document.getElementById('ul1');
        oBtn.onclick = function() {
            var oLi = document.createElement('li');
            oLi.innerHTML = oContent.value;
            if(oUl.children[0]) {
                oUl.insertBefore(oLi,oUl.children[0]);
            } else {
                oUl.appendChild(oLi);
            }
            var iHeight = parseInt(css(oLi,'height'));
            oLi.style.opacity = 0;
            oLi.style.filter = 'alpha(opacity=0)';
            oLi.style.height = 0;
            startMove(oLi,{
                height:iHeight,
                opacity:100
            });
        }
        """
        return js_func


################生成VUE#################################
    # 创建vue文件
    @staticmethod
    def create_vue_file():
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        base_html4 = "web_pages\\Page_class4.vue"  # 生成指定路径下的vue
        f = open(base_html4, 'w')
        button = PageClassConfig.get_base_element(1)
        input = PageClassConfig.get_base_element(2)
        select = PageClassConfig.get_base_element(3)
        template = """<template>
  <div class="Temp">
    <div class="temp-box">
      """ + input + """
      """ + button + """
      """ + select + """
    </div>
  </div>
</template>
        """
        script = """
<script>
export default {
  data() {
    return {}
  },
  created() {
    this.getClassList();
  },
  methods: {}
}
</script>        
        """
        style = """
<style scoped>
.temp-box {
  padding: 20px;
  min-width: 600px;
}

.query-box {
  margin-bottom: 20px;
}
</style>
        """
        f.write(template)
        f.write(script)
        f.write(style)
        f.close()
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

    @staticmethod
    def get_base_element(element_id):
        element = ""
        if element_id == 1:
            element = """<el-button slot="append" icon="el-icon-search" @click="getParamList"></el-button>"""
        if element_id == 2:
            element = """<el-template placeholder="请输入内容" @template="selectParamList" clearable v-model="condition"
                      class="template-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getParamList"></el-button>
            </el-template>"""
        if element_id == 3:
            element = """<el-select v-model="query_status" @change="selectParamList">
              <el-option v-for="item in statusOptions" :key="item.value" :label="item.label"
                         :value="item.value"></el-option>
            </el-select>"""
        return element

################生成VUE TABS组件#################################
    # 创建vue文件
    @staticmethod
    def create_vue_Tabs():
        import json
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        vue_config = "web_pages\\vue_config.json"  # 生成指定路径下的vue
        file = open(vue_config, 'r')
        json_data = file.read()
        j = json.dumps(json_data)
        file.close()
        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result

    # 创建vue文件
    @staticmethod
    def create_vue_page():
        result = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
        elements = [
            {'element': 'el-input', 'placeholder': '请输入查询内容'},
            {'element': 'el-tabs', 'elTabPanes': [
                {'name': 'goods', 'label': '商品管理', 'content': '商品管理'},
                {'name': 'order', 'label': '订单管理', 'content': '订单管理'}
            ], 'activeName': 'goods'}
        ]
        rendered_string = parse(elements)
        print(rendered_string)

        result['code'] = ReturnEnum.ER_SUCCESS().code
        result['msg'] = ReturnEnum.ER_SUCCESS().msg
        return result



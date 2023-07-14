# -*- coding: utf-8 -*-
# Editer: 程子瑞

from enum import Enum, IntEnum
from types import DynamicClassAttribute


class CustomEnum(Enum):
    """自定义枚举"""

    @DynamicClassAttribute
    def first_value(self):
        return self._value_[0]

    @DynamicClassAttribute
    def last_value(self):
        return self._value_[-1]

    @classmethod
    def values(cls) -> list:
        return [v.value for v in cls]

    @classmethod
    def values_dict(cls) -> dict:
        return dict(cls.values())

    @classmethod
    def member_names(cls) -> list:
        return cls._member_names_


# 定时任务管理
# 程子瑞 2021-08-23
class ETaskManage(Enum):
    # 执行状态正常code
    RUN_STATUS_SUCCESS_CODE = 1
    # 执行状态异常code
    RUN_STATUS_ERROR_CODE = 2
    # 执行状态执行中code
    RUN_STATUS_RUNNING_CODE = 3
    # 服务状态启用code
    SERVICE_STATUS_SUCCESS_CODE = 1
    # 服务状态禁用code
    SERVICE_STATUS_ERROR_CODE = 2
    # 软件部门人员下拉框sql
    IT_USER_LIST_SQL = 10351200
    # 定时任务路径下拉框sql
    TASK_PATH_LIST_SQL = 10351201
    # 定时任务状态统计sql
    STATS_AGGREGATE_SQL = 10351202


# 流程编排处理
# 倪恒 2023-03-13
class FuncProcessCode(Enum):
    FUNCTION_PARAM_CODE = 0  # 参数类别为返回码
    FUNCTION_PARAM_PARAM = 1  # 参数类别为参数
    FUNCTION_PARAM_RETURN = 2  # 参数类别为返回值
    LOG_TYPE_DEL = 0  # 日志类别为删除
    LOG_TYPE_ADD = 1  # 日志类别为新增
    LOG_TYPE_UPDATE = 2  # 日志类别为修改
    LOG_CLASS = 0  # 日志记录类名表
    LOG_PARAM = 1  # 日志记录参数表
    LOG_FUNCTION = 2  # 日志记录参数表
    LOG_CUSTOM_FUNCTION = 3  # 日志记录功能表
    LOG_ERROR_CODE = 4  # 日志记录返回码表
    RETURN_ENUM_PATH = 'brick.public.ReturnEnum'  # 返回码路径
    RETURN_ENUM_CLASS_NAME = 'ReturnEnum'  # 返回码类名
    RETURN_ENUM_NO_ACTIVATE = 0  # 返回码未激活
    RETURN_ENUM_ACTIVATE = 1  # 返回码已激活
    SVN_BASE_URL = 'SVN://'  # svn路径
    LIST_DATA_TYPE = 11  # list类型
    DICT_DATA_TYPE = 12  # dict类型
    ENUM_DATA_TYPE = 13  # enum类型
    FIELD_DATA_TYPE = 22 #Field类型
    BASE_CODE_PREFIX = 'ER_'  # 返回码前缀
    GLOBAL_FUNCTION_PREFIX = 'g_'  # 全局函数前缀
    STATUS_NO_ACTIVATE = 0  # 草稿
    STATUS_NO_ACTIVATE_DESC = '草稿'
    STATUS_SUBMIT = 1  # 已提交
    STATUS_SUBMIT_DESC = '已提交'
    STATUS_RELEASE = 2  # 已审核
    STATUS_RELEASE_DESC = '已审核'
    STATUS_PUBLISH = 3  # 已发布
    STATUS_PUBLISH_DESC = '已发布'
    PARAM_TABLE_CODE = 0  # 返回码
    TABLE_TYPE_PARAM = 1  # 参数
    TABLE_TYPE_FUNCTION = 2  # 函数
    TABLE_TYPE_TASK = 3  # 流程
    COMMENT_NO_READ = 0  # 未读
    COMMENT_NO_READ_DESC = '未读'
    COMMENT_READ = 1  # 已读
    CLASS_NAME_SEPARATE = '::'  # 类函数分隔符
    NOT_REQUIRE = 0  # 非必填项
    NO_READ_COMMENT_DATA_SQL = 10351263  # 查询未读评审意见的数据
    MAX_LOOP_INDEX = 5  # 递归最大深度
    NO_AUTO_TEST = 0  # 未加入自动化测试
    AUTO_TEST = 1  # 已加入自动化测试

    # 流程编排，代码规范相关魔鬼数字


class FuncProcessName(Enum):
    APPROVE_PERSON = ('卞勇', '丁俊', '常杨', '严旭')
    APPROVE_PERSON_TYPE = 404001 # 参数函数流程审核权限组
    SUBMIT_PERSON = ('常杨', '严旭', '王恒', '郭子银', '李志华')
    SUBMIT_PERSON_TYPE = 404002 # 参数提交权限组
    TEST_PERSON = ('卞勇', '李萌萌', '蔡杨林', '徐国锋', '夏素萍', '吴斌', '邢皓', '陈康')
    TEST_PERSON_TYPE = 404003 # 测试组
    STANDARD_MANAGER = ("卞勇", "李萌萌")
    STANDARD_MANAGER_TYPE = 404004 # 开发规范操作组
    UPLOAD_OSS = "f_UploadFileToOss"
    DRS_OSS_PATH = "software_develop_standard"
    DRS_GET = "DevelopRequireSpecification::get_all"
    DRS_ADD = "DevelopRequireSpecification::add"
    DRS_EDIT = "DevelopRequireSpecification::edit"
    DRS_DEL = "DevelopRequireSpecification::delete"
    FUNC_PROCESS_APP = "func_process_app"
    PUBLIC_ERROR_CODE = "t_public_error_code"
    PUBLIC_ERROR_CODE_CN = "返回码"
    PUBLIC_PARAM = "t_public_params"
    PUBLIC_PARAM_CN = "参数"
    PUBLIC_FUNCTION = "t_public_function"
    PUBLIC_FUNCTION_CN = "函数"
    PUBLIC_CUSTOM_FUNCTION = "t_public_custom_function"
    PUBLIC_CUSTOM_FUNCTION_CN = "流程"
    EXPLANATION_CODE = "#"
    DEF_CODE = "def "
    ANNOTATION_CODE = "@"
    ATTRIBUTE_PREFIX = "__"
    PY_FILE_SUFFIX = ".py"

class PageConfig(Enum):
    TEMPLATE_IN_PATH= "" # 模板输入路径
    TEMPLATE_OUT_PATH= "" # 模板输出路径
    TEMPLATE_ = ""

# 全局SQL语句
class CommonSQL(Enum):
    GET_ALL_ERROR_CODE_MSG = 10351193 # 查询全量返回码


class BaseVue(Enum):
    INPUT = """<el-template v-model="%s" placeholder="%s"></el-template>"""  #写死在数据库
    INPUT_Model = 'condition' #动态配置的
    INPUT_placeholder = 'input_placeholder' #动态配置的

    TABS = """<el-tabs type="border-card">%s</el-tabs>""" # %s 里面是TAB
    TAB = """<el-tab-pane label="%s">%s</el-tab-pane>""" # 俩个%s分别是label和显示的值
    BADGE= """<el-badge :value="%s" class="%s">%s</el-badge>""" # %s里面是标签
    BADGE_value = '12' # BADGE显示的数字
    BADGE_class = 'item' # BADGE的样式

    BADGE0= """<el-badge
            v-for="item in nodeList"
            :key="item.stepNo + ''"
            :value="item.count"
            :max="999999"
          >"""

class PUBLIC_CONFIG_INFO(Enum):
    # 默认空时间
    DEFAULT_EMPTY_DATE_TIME = '1900-01-01 00:00:00'
    DEFAULT_EMPTY_DATE = '1900-01-01'

class PAGE_CONFIG_INFO(Enum):
    # vue文件的各个区块，最终渲染根模板 base_vue.hq
    HQ_TAG_LIST = ['hqTemplate', 'hqData', 'hqMethods', 'hqStyle', 'hqLifeCycle', 'hqImport', 'hqComponents', 'hqStyleGlobal']
    # vue生命周期的各个区块（hqLifeCycle的子区块）
    HQ_LIFE_CYCLE_TAG_LIST = ['hqBeforeCreate', 'hqCreated', 'hqBeforeMount', 'hqMounted', 'hqBeforeUpdate',
                              'hqBeforeUnmount', 'hqUnmounted', 'hqErrorCaptured', 'hqErrorCaptured']
    # 页面显示的四个区块（hqTemplate的子区块）
    HQ_TEMPLATE_TAG_LIST = ['hqMenuArea', 'hqSelectArea', 'hqGlobalArea', 'hqDataArea']
    # 页面显示的四个区块配置模板
    HQ_CONFIG_AREA_LIST = ['hq-menu-area', 'hq-select-area', 'hq-button-area', 'hq-data-area']
    # 基础组件的配置字段
    HQ_BASE_ELEMENT_KEY_LIST = ['element', 'element_key', 'sub_elements', 'page_area']
    # 通用配置字段
    HQ_COMMON_CONFIG_FIELD = ['repeat_field_name_en', 'field_name_en']
    # 通用去重字段
    HQ_DISTINCT_TAG = 'hqDistinct'
    # 组件文件夹名称
    HQ_ELEMENT_FOLDER = ['baseElement', 'pageAreaElement', 'groupElement', 'customElement']
    # vue根模板
    BASE_VUE_TEMPLATE = 'root\\base_vue.hq'
    # BASE_HTML_TEMPLATE = 'root\\template_result.vue'
    BASE_HTML_TEMPLATE = 'root\\view_page.html'
    VUE_FILE_SUFFIX = '.vue'
    TEMPLATE_FILE_SUFFIX = '.hq'
    # vue文件输入输出路径
    VUE_INPUT_PATH = 'templates\\input\\'
    VUE_OUTPUT_PATH = 'templates\\output\\'
    # 搜索区最大列数
    SELECT_AREA_MAX_COL = 3

# -*- coding: utf-8 -*-
# Editer: 程子瑞


class ReturnClass():
    _author = None
    _code = None
    _msg = None
    _data = None

    # code 只读
    @property
    def author(self):
        return self._author

    # code 只读
    @property
    def code(self):
        return self._code

    # msg 可读写
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    # data 可读写
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __init__(self, author, code, msg):
        self._author = author
        self._code = code
        self._msg = msg

    def __eq__(self, other):
        if isinstance(other, ReturnClass):
            return self._code == other._code
        else:
            return NotImplemented

    def to_dict(self):
        return {'code': self.code, 'msg': self.msg, 'data': self.data}


class ReturnEnum(object):
    @staticmethod
    def ER_FAIL():
        return ReturnClass('程子瑞', -1, 'Fail')

    @staticmethod
    def ER_SUCCESS():
        return ReturnClass('程子瑞', 0, 'Success')

    @staticmethod
    def ER_NO_DATA():
        return ReturnClass('程子瑞', 1000, '数据不存在')

    @staticmethod
    def ER_NO_ROLE():
        return ReturnClass('程子瑞', 1001, '没有相关权限')

    @staticmethod
    def ER_AMZ():
        return ReturnClass('程子瑞', 10000, 'Amazon app exception')

    @staticmethod
    def ER_AMZ_ShopName():
        return ReturnClass('吴仕洋', 10001, 'AMZ卖家简称错误')

    @staticmethod
    def ER_ZHGC_ZC_QA_LC():
        return ReturnClass('王志平', 100012, '组合工厂自测QA处理-生产单状态错误')

    @staticmethod
    def ER_AMZ_EXCHANGE_RATE():
        return ReturnClass('吴仕洋', 10002, '未找到汇率')

    @staticmethod
    def ER_CACHE():
        return ReturnClass('吴仕洋', 10003, '缓存异常')

    @staticmethod
    def ER_LAZADA():
        return ReturnClass('程子瑞', 11000, 'Lazada app exception')

    @staticmethod
    def ER_WISH():
        return ReturnClass('程子瑞', 12000, 'Wish app exception')

    @staticmethod
    def ER_SHOPEE():
        return ReturnClass('程子瑞', 13000, 'Shopee app exception')

    @staticmethod
    def ER_EBAY():
        return ReturnClass('程子瑞', 14000, 'Ebay app exception')

    @staticmethod
    def ER_ALI():
        return ReturnClass('程子瑞', 15000, 'Aliexpress app exception')

    @staticmethod
    def ER_PRODUCT_CENTER():
        return ReturnClass('程子瑞', 16000, 'product center exception')

    @staticmethod
    def ER_APPLY_SUCCESS():
        return ReturnClass('程子瑞', 16001, 'shopsku apply success')

    @staticmethod
    def ER_APPLY_SUCCESS_NO_DATA():
        return ReturnClass('程子瑞', 16002, 'shopsku apply success but no data')

    @staticmethod
    def ER_JOYBUY():
        return ReturnClass('程子瑞', 17000, 'Joybuy app exception')

    @staticmethod
    def ER_WALMART():
        return ReturnClass('程子瑞', 18000, 'Walmart app exception')

    @staticmethod
    def ER_REAL_API():
        return ReturnClass('程子瑞', 19000, 'Real api exception')

    @staticmethod
    def ER_REAL():
        return ReturnClass('程子瑞', 19001, 'Real app exception')

    @staticmethod
    def ER_REAL_NO_NULL():
        return ReturnClass('程子瑞', 19002, 'shopName or Real Obj is Null')

    @staticmethod
    def ER_DATA_ALREADY_EXISTS():
        return ReturnClass('严旭', 2002, '数据已存在')

    @staticmethod
    def ER_BILL_EXISTS():
        return ReturnClass('雷涛', 20000, '该账单已存在,请重新操作！')

    @staticmethod
    def ER_BILL_COMPLETE_FAILED():
        return ReturnClass('雷涛', 20008, '账单操作失败,请稍后再试！')

    @staticmethod
    def ER_BILL_HAS_UNCHECKED():
        return ReturnClass('雷涛', 20009, '账单明细还有未审核的部分!')

    @staticmethod
    def ER_UNKNOWN():
        return ReturnClass('雷涛', 20010, '未知错误,请联系IT处理!')

    @staticmethod
    def ER_BILL_COMMIT_PAYMENT():
        return ReturnClass('雷涛', 20012, '提交付款失败!')

    @staticmethod
    def ER_DELIVER_STATUS_CFG_FILE_CHECK():
        return ReturnClass('雷涛', 20020, '货物状态配置文件检查错误！')

    @staticmethod
    def ER_DELIVER_STATUS_CFG_EXISTS():
        return ReturnClass('雷涛', 20021, '货物状态配置已存在！')

    @staticmethod
    def ER_TASK_UPLOAD_SVN():
        return ReturnClass('程子瑞', 21001, '定时任务服务器SVN更新失败')

    @staticmethod
    def ER_TASK_SERVER_NOT_FIND():
        return ReturnClass('程子瑞', 21002, '没有查询到执行定时任务的服务器')

    @staticmethod
    def ER_TASK_RUN_FAIL():
        return ReturnClass('程子瑞', 21003, '定时任务调用失败')

    @staticmethod
    def ER_KAUFLAND_REPORT_FILE_NAME():
        return ReturnClass('雷涛', 23001, '文件命名错误，格式为: 店铺名称+报告类型.csv')

    @staticmethod
    def ER_KAUFLAND_SHOP_NAME():
        return ReturnClass('雷涛', 23002, '店铺名称错误，请检查后重新上传！')

    @staticmethod
    def ER_KAUFLAND_REPORT_TYPE():
        return ReturnClass('雷涛', 23003, '报告类型错误，请检查后重新上传！')

    @staticmethod
    def ER_KAUFLAND_REPORT_FILE_TYPE():
        return ReturnClass('雷涛', 23004, '文件类型错误，请检查后重新上传！')

    @staticmethod
    def ER_KAUFLAND_REPORT_FILE_UPLOAD():
        return ReturnClass('雷涛', 23005, '文件上传错误，请稍后重试！')

    @staticmethod
    def ER_KAUFLAND_REPORT_DATA_SAVE():
        return ReturnClass('雷涛', 23006, '数据保存错误，请稍后重试！')

    @staticmethod
    def ER_KAUFLAND_REPORT_HEAD():
        return ReturnClass('雷涛', 23007, '标题格式错误，请检查后重新上传！')

    @staticmethod
    def ER_RESOURCE_WAITING_REASON():
        return ReturnClass('李志华', 30000, '待回收资源转待定原因必填！')

    @staticmethod
    def ER_RESOURCE_CONFIRM_IT_AND_FINANACE():
        return ReturnClass('李志华', 30001, '需要确认IT和财务资源是否需要回收！')

    @staticmethod
    def ER_RESOURCE_CONFIRM_IT_NEED_REASON():
        return ReturnClass('李志华', 30002, 'IT资源不回收需要不回收原因！')

    @staticmethod
    def ER_RESOURCE_CONFIRM_FINANCE_NEED_REASON():
        return ReturnClass('李志华', 30003, '财务资源不回收需要不回收原因！')

    @staticmethod
    def ER_NO_SKUZH_DT():
        return ReturnClass('袁永亮', 30004, '组合工厂明细表不存在此SKU')

    @staticmethod
    def ER_MORE_NUMBER():
        return ReturnClass('袁永亮', 30005, '输入数量>未入库数量,状态修改为多货')

    @staticmethod
    def ER_INVALIAD_INPUT():
        return ReturnClass('袁永亮', 30006, '无效输入')

    @staticmethod
    def ER_CONFIG_SQL_NOT_EXIST():
        return ReturnClass('袁永亮', 30010, '全局SQL语句不存在该属性')

    @staticmethod
    def ER_OTHER_INSTORE():
        return ReturnClass('袁永亮', 30012, '调用普源出库接口失败')

    @staticmethod
    def ER_NO_USED_NUM():
        return ReturnClass('袁永亮', 30013, '普源可用数量不足')

    @staticmethod
    def ER_PARAMENTER():
        return ReturnClass('严旭', 4000, '参数错误')

    @staticmethod
    def ER_NO_LISTICSCFG():
        return ReturnClass('雷涛', 4001, '找不到物流配置信息')

    @staticmethod
    def ER_MANY_LISTICSCFG():
        return ReturnClass('雷涛', 4002, '多条物流配置信息')

    @staticmethod
    def ER_NO_CUSTOMS():
        return ReturnClass('严旭', 4003, '清关方式不存在')

    @staticmethod
    def ER_NO_SITE():
        return ReturnClass('严旭', 4004, '站点不存在')

    @staticmethod
    def ER_NO_TIME():
        return ReturnClass('严旭', 4005, '时间配置范围不存在')

    @staticmethod
    def ER_NO_PRICE_CONFIG():
        return ReturnClass('严旭', 4006, '配置单价区间不存在')

    @staticmethod
    def ER_CONFIG():
        return ReturnClass('严旭', 4007, '配置单价区间配置错误')

    @staticmethod
    def ER_SURCHARGE_CONFIG():
        return ReturnClass('严旭', 4008, '附加费区间配置存在问题')

    @staticmethod
    def ER_NO_FNSKU_GOODS():
        return ReturnClass('严旭', 4009, 'FN物品成本不存在')

    @staticmethod
    def ER_FNSKU_TO_SKU():
        return ReturnClass('严旭', 4010, 'FNSKU对应SKU关系不存在')

    @staticmethod
    def ER_SKU_SPLIT():
        return ReturnClass('严旭', 4011, 'SKU组合关系拆分失败')

    @staticmethod
    def ER_NO_SKU_INFO():
        return ReturnClass('严旭', 4012, 'SKU信息不存在')

    @staticmethod
    def ER_HANDLE_FNSKU_PRICE():
        return ReturnClass('严旭', 4013, '处理FN物品成本价失败')

    @staticmethod
    def ER_FNSKU_SIZE():
        return ReturnClass('严旭', 4014, 'FNSKU重量不存在')

    @staticmethod
    def ER_CALC_LOGISTICS_FEE():
        return ReturnClass('严旭', 4015, '计算FNSKU国内物流费失败')

    @staticmethod
    def ER_NO_PACKAGING_CONFIG():
        return ReturnClass('严旭', 4016, '包装成本固定值配置不存在')

    @staticmethod
    def ER_PACKAGING_CONFIG():
        return ReturnClass('严旭', 4017, '包装成本固定值配置错误')

    @staticmethod
    def ER_SAVE_FN_COST():
        return ReturnClass('严旭', 4018, '保存FN物品成本失败')

    @staticmethod
    def ER_SELECT_ALL_DEPARTMENT():
        return ReturnClass('严旭', 4019, '获取全部部门失败')

    @staticmethod
    def ER_FNSKU_STATUS_AFTER():
        return ReturnClass('严旭', 4020, 'FNSKU新状态必须填写')

    @staticmethod
    def ER_FNSKU_NO_REMARK():
        return ReturnClass('严旭', 4021, '修改FNSKU状态申请原因必须填写')

    @staticmethod
    def ER_NO_FNSKU_STATUS_OBJ():
        return ReturnClass('严旭', 4022, 'FNSKU状态对象不存在')

    @staticmethod
    def ER_ADD_FNSKU_STATUS():
        return ReturnClass('严旭', 4023, '申请修改FNSKU状态失败')

    @staticmethod
    def ER_DD_EMAIL():
        return ReturnClass('严旭', 4024, '申请成功, 钉钉邮件提醒失败')

    @staticmethod
    def ER_NO_LOGISTICS_PRICE_RANGE():
        return ReturnClass('严旭', 4025, '物流商单价区间配置不存在')

    @staticmethod
    def ER_MAX_PRICE_RANGE():
        return ReturnClass('严旭', 4026, '重量超过物流商单价区间最大值')

    @staticmethod
    def ER_NO_FNSKU_PURCHASE_COST():
        return ReturnClass('严旭', 4027, 'FNSKU采购成本不存在')

    @staticmethod
    def ER_NO_CONFIGURATION():
        return ReturnClass('严旭', 4028, '配置不存在')

    @staticmethod
    def ER_VALUE_IS_EXISTS():
        return ReturnClass('严旭', 4029, '属性值已存在')

    @staticmethod
    def ER_FNSKU_STATUS_EXISTS():
        return ReturnClass('严旭', 4030, '申请失败, 该FNSKU已经被申请修改状态, 请到待审核里面审核！')

    @staticmethod
    def ER_FNSKU_STATUS_MANY():
        return ReturnClass('严旭', 4031, '申请失败, 该站点+ASIN下的fnsku状态不统一, 请统一后状态再申请！')

    @staticmethod
    def ER_METHOD_ERROR():
        return ReturnClass('严旭', 4032, '方法不被允许')

    @staticmethod
    def ER_CONFIG_TABLE_ERROR():
        return ReturnClass('严旭', 4033, '配置表不合法')

    @staticmethod
    def ER_ADD_ERROR():
        return ReturnClass('严旭', 4034, '创建失败')

    @staticmethod
    def ER_NOT_HAS_PAYMENT():
        return ReturnClass('张浩', 40001, '未填写预付款或运费,未生成财务付款记录')

    @staticmethod
    def ER_LACK_PARAMETER():
        return ReturnClass('张浩', 40002, '缺少必传参数')

    @staticmethod
    def ER_NO_ASIN_SALE_DATA():
        return ReturnClass('张浩', 40003, '获取ASIN销量数据失败')

    @staticmethod
    def ER_NO_ASIN_INVENTORY_DATA():
        return ReturnClass('张浩', 40004, '获取ASIN库存数据失败')

    @staticmethod
    def ER_FUNCTION_NOT_FOUND():
        return ReturnClass('倪恒', 44001, '软件接口找不到对应函数')

    @staticmethod
    def ER_PARAM_NOT_MATCH():
        return ReturnClass('倪恒', 44002, '软件接口参数匹配失败')

    @staticmethod
    def ER_RESULT_NOT_MATCH():
        return ReturnClass('倪恒', 44003, '软件接口返回值匹配失败')

    @staticmethod
    def ER_CODE_NOT_MATCH():
        return ReturnClass('倪恒', 44004, '软件接口返回码匹配失败')

    @staticmethod
    def ER_INTERFACE_FUNCTION_ERROR():
        return ReturnClass('倪恒', 44005, '软件接口流程编排调用子函数失败')

    @staticmethod
    def ER_SERVER_ERROR():
        return ReturnClass('倪恒', 502, '服务异常，请联系IT')

    @staticmethod
    def ER_RISK_MISSING_PARAM():
        return ReturnClass('宋增增', 5000, '缺少参数')

    @staticmethod
    def ER_RISK_EXCEEDED_NUMBER():
        return ReturnClass('宋增增', 5001, '批量操作数量超过限制')

    @staticmethod
    def ER_RISK_IP_SHOP_APPLY():
        return ReturnClass('李志华', 5003, 'SPU侵权，禁止新增链接')

    @staticmethod
    def ER_RISK_IP_WORD_APPLY():
        return ReturnClass('李志华', 5004, 'IP产品缺少刊登申请')

    @staticmethod
    def ER_RISK_BEFORE_PUBLISH_NO_PARAM():
        return ReturnClass('李志华', 5005, '刊登前检查缺少参数')

    @staticmethod
    def ER_RISK_BEFORE_PLATFORM_ERROR():
        return ReturnClass('李志华', 5006, '刊登前检查平台名传入异常')

    @staticmethod
    def ER_RISK_BEFORE_PUBLISH_FORBBIDEN():
        return ReturnClass('李志华', 5007, '商品在该站点绝对禁止，不允许刊登')

    @staticmethod
    def ER_RISK_BEFORE_SPU_ERROR():
        return ReturnClass('李志华', 5008, '刊登前检查SPU传入异常')

    @staticmethod
    def ER_RISK_BEFORE_WEEE_ERROR():
        return ReturnClass('李志华', 5009, '店铺缺少WEEE认证，无法刊登该商品')

    @staticmethod
    def ER_RISK_PARAM_ERROR():
        return ReturnClass('宋增增', 5010, '传入参数格式错误')

    @staticmethod
    def ER_RISK_ERROR():
        return ReturnClass('宋增增', 5011, '部分成功, 部分失败!')

    @staticmethod
    def ER_RISK_BEFORE_STOCK_SPU_ERROR():
        return ReturnClass('李志华', 5013, 'SPU传入异常')

    @staticmethod
    def ER_RISK_BEFORE_STOCK_PLATFORM_ERROR():
        return ReturnClass('李志华', 5014, '平台名传入异常')

    @staticmethod
    def ER_RISK_BEFORE_STOCK_RULE_ERROR():
        return ReturnClass('李志华', 5015, '有违规项，请查看明细')

    @staticmethod
    def ER_RISK_BEFORE_WEEE_BRAND_ERROR():
        return ReturnClass('王俊昌', 5016, '店铺WEEE品牌不匹配，无法刊登该商品')

    @staticmethod
    def ER_Ebay_Excel_Upload():
        return ReturnClass('郭子银', 6001, 'Excel上传异常')

    @staticmethod
    def ER_PARAMS():
        return ReturnClass('王俊昌', 6003, '入参错误')

    @staticmethod
    def ER_INNER_INTERFACE():
        return ReturnClass('王俊昌', 6004, '内部接口调用失败')

    @staticmethod
    def ER_EXCEL_PARSE():
        return ReturnClass('王俊昌', 6005, 'Excel解析错误')

    @staticmethod
    def ER_PROCESS_FAIL():
        return ReturnClass('王俊昌', 6006, 'Excel处理失败')

    @staticmethod
    def ER_UNSUITED_FAIL():
        return ReturnClass('王俊昌', 6007, '操作数据不满足操作条件')

    @staticmethod
    def ER_API_FORBIDDEN():
        return ReturnClass('程子瑞', 7003, 'API forbidden access')

    @staticmethod
    def ER_API_TIME():
        return ReturnClass('程子瑞', 7004, 'API event error')

    @staticmethod
    def ER_API_UNCHANGED():
        return ReturnClass('程子瑞', 7005, 'API no change error')

    @staticmethod
    def ER_API_METHOD():
        return ReturnClass('程子瑞', 7006, 'API method not allowed')

    @staticmethod
    def ER_API_NOT_EXISTS():
        return ReturnClass('程子瑞', 7007, 'API does not exist')

    @staticmethod
    def ER_UPLOAD_OSS():
        return ReturnClass('郑宏峰', 70000, '提交质量反馈,Excel表格上传OSS失败')

    @staticmethod
    def ER_EXPORT_EXCEL():
        return ReturnClass('郑宏峰', 70001, '提交质量反馈,Excel表格导出失败')

    @staticmethod
    def ER_EXPORT_IMAGE():
        return ReturnClass('郑宏峰', 70003, '提交质量反馈, 图片导出出错')

    @staticmethod
    def ER_CREDIT_CARD_EDITOR():
        return ReturnClass('郑宏峰', 70004, '信用卡信息编辑失败')

    @staticmethod
    def ER_PY_SKU_INBOUND_ERROR():
        return ReturnClass('郑宏峰', 70005, '组合工厂生产完成-普源入库失败，请联系IT查看')

    @staticmethod
    def ER_ZH_SKU_KSC_NUM_DEFICIENCY():
        return ReturnClass('郑宏峰', 70006, '组合商品可生产数量不足')

    @staticmethod
    def ER_ZH_SKU_INBOUND_OCCUPY():
        return ReturnClass('郑宏峰', 70007, '组合商品出库占用失败')

    @staticmethod
    def ER_ZH_SKU_INBOUND_OCCUPY_RELEASE():
        return ReturnClass('郑宏峰', 70008, '组合商品出库占用未全部释放')

    @staticmethod
    def ER_CJFH_INBOUND_OCCUPY_RELEASE():
        return ReturnClass('郑宏峰', 70009, '创建发货失败, 组合商品出库占用未全部释放')

    @staticmethod
    def ER_CHECK_DELIVER_GOODS_WEIGHT():
        return ReturnClass('郑宏峰', 70010, '该批次每票最低重量未大于1千克，需确定是否发货')

    @staticmethod
    def ER_FC_RELEASE_FAIL():
        return ReturnClass('郑宏峰', 70011, '亚马逊分仓组合商品库存释放失败')

    @staticmethod
    def ER_FC_OCCUPY_FAIL():
        return ReturnClass('郑宏峰', 70012, '亚马逊分仓组合商品库存占用失败')

    @staticmethod
    def ER_NO_CONGIGURATION_FOUND():
        return ReturnClass('郑宏峰', 70013, '未查询到主要物流方式默认配置信息')

    @staticmethod
    def ER_DELIVER_RISK_CHECK():
        return ReturnClass('郑宏峰', 70014, '发货流程-风控限制规则')

    @staticmethod
    def ER_LEXICOGRAPHICAL_VALENCE_CHECK():
        return ReturnClass('郑宏峰', 70015, '发货流程-词图价审核流程')

    @staticmethod
    def ER_PLAN_DELIVER_NUM_CHECK():
        return ReturnClass('郑宏峰', 70016, '发货流程-生成发货任务提交校验')

    @staticmethod
    def ER_SHEIN_CREATE_CHECK():
        return ReturnClass('郑宏峰', 70017, 'SHEIN创建发货校验')

    @staticmethod
    def ER_API():
        return ReturnClass('程子瑞', 8000, 'API call exception')

    @staticmethod
    def ER_EXPORT_DELIVER_FEE():
        return ReturnClass('雷涛', 8001, '装箱数据导出失败')

    @staticmethod
    def ER_TRANSFER_TRACK_NUM_UPDATE():
        return ReturnClass('雷涛', 8002, '当前状态为调拨单审核，物流信息无法上传！')

    @staticmethod
    def ER_EXPORT_EXCEL_DATA():
        return ReturnClass('雷涛', 8003, 'Excel导出失败')

    @staticmethod
    def ER_EXPORT_LOGISTICS_AGING():
        return ReturnClass('雷涛', 8004, '物流时效数据导出失败')

    @staticmethod
    def ER_FLOW_CUSTOMS_CHECK_DATA():
        return ReturnClass('雷涛', 8005, '该物流数据已进入海关查验流程！')

    @staticmethod
    def ER_FLOW_ORIGINAL_BILL_CHECK():
        return ReturnClass('雷涛', 8006, '转入头程费用审批流程失败！')

    @staticmethod
    def ER_FLOW_APP_HSCODE_IS_REQUIRED():
        return ReturnClass('李志华', 8007, 'HS编码为必填项，请填写后再转下一步！')

    @staticmethod
    def ER_NO_CUSTOMS_CHECK_REMARK():
        return ReturnClass('雷涛', 8008, '请填写海关查验备注！')

    @staticmethod
    def ER_DATA_NOT_EXISTS():
        return ReturnClass('倪恒', 2003, '数据不存在')

    @staticmethod
    def ER_DB():
        return ReturnClass('程子瑞', 9000, 'Database exception')

    def __init__(self) -> None:
        raise Exception("该类禁止被实例化！")


class HtmlReturnClass(object):
    _title = ''
    _html = ''
    _data = {}
    _data_list = []

    # title 可读写
    @property
    def title(self):
        return self._title

    # html 可读写
    @property
    def html(self):
        return self._html

    # data 可读写
    @property
    def data(self):
        return self._data

    # data_list 可读写
    @property
    def data_list(self):
        return self._data_list

    @title.setter
    def title(self, value):
        self._title = value

    @html.setter
    def html(self, value):
        self._html = value

    @data.setter
    def data(self, value):
        self._data = value

    @data_list.setter
    def data_list(self, value):
        self._data_list = value

    def __init__(self, title = '', html = '', data=None):
        if data is None:
            data = {}
        self._title = title
        self._html = html
        self._data = data

    def to_dict(self):
        return {'title': self.title, 'html': self.html, 'data': self.data, 'data_list': self.data_list}
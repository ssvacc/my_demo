/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50540
 Source Host           : localhost:3306
 Source Schema         : process_arrange

 Target Server Type    : MySQL
 Target Server Version : 50540
 File Encoding         : 65001

 Date: 12/07/2023 17:19:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_error_code
-- ----------------------------
DROP TABLE IF EXISTS `t_public_error_code`;
CREATE TABLE `t_public_error_code`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '变量名',
  `code` int(16) NULL DEFAULT NULL COMMENT 'code',
  `msg` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'msg',
  `author` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '作者',
  `status` int(1) NULL DEFAULT NULL COMMENT '状态(0.未激活，1.已激活)',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 153 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_error_code
-- ----------------------------
INSERT INTO `t_public_error_code` VALUES (1, 'ER_FAIL', -1, 'Fail', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (2, 'ER_SUCCESS', 0, 'Success', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (3, 'ER_SERVER_ERROR', 502, '服务异常，请联系IT', '倪恒', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (4, 'ER_NO_DATA', 1000, '数据不存在', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (5, 'ER_NO_ROLE', 1001, '没有相关权限', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (6, 'ER_DATA_ALREADY_EXISTS', 2002, '数据已存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (7, 'ER_PARAMENTER', 4000, '参数错误', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (8, 'ER_NO_LISTICSCFG', 4001, '找不到物流配置信息', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (9, 'ER_MANY_LISTICSCFG', 4002, '多条物流配置信息', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (10, 'ER_NO_CUSTOMS', 4003, '清关方式不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (11, 'ER_NO_SITE', 4004, '站点不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (12, 'ER_NO_TIME', 4005, '时间配置范围不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (13, 'ER_NO_PRICE_CONFIG', 4006, '配置单价区间不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (14, 'ER_CONFIG', 4007, '配置单价区间配置错误', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (15, 'ER_SURCHARGE_CONFIG', 4008, '附加费区间配置存在问题', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (16, 'ER_NO_FNSKU_GOODS', 4009, 'FN物品成本不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (17, 'ER_FNSKU_TO_SKU', 4010, 'FNSKU对应SKU关系不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (18, 'ER_SKU_SPLIT', 4011, 'SKU组合关系拆分失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (19, 'ER_NO_SKU_INFO', 4012, 'SKU信息不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (20, 'ER_HANDLE_FNSKU_PRICE', 4013, '处理FN物品成本价失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (21, 'ER_FNSKU_SIZE', 4014, 'FNSKU重量不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (22, 'ER_CALC_LOGISTICS_FEE', 4015, '计算FNSKU国内物流费失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (23, 'ER_NO_PACKAGING_CONFIG', 4016, '包装成本固定值配置不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (24, 'ER_PACKAGING_CONFIG', 4017, '包装成本固定值配置错误', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (25, 'ER_SAVE_FN_COST', 4018, '保存FN物品成本失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (26, 'ER_SELECT_ALL_DEPARTMENT', 4019, '获取全部部门失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (27, 'ER_FNSKU_STATUS_AFTER', 4020, 'FNSKU新状态必须填写', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (28, 'ER_FNSKU_NO_REMARK', 4021, '修改FNSKU状态申请原因必须填写', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (29, 'ER_NO_FNSKU_STATUS_OBJ', 4022, 'FNSKU状态对象不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (30, 'ER_ADD_FNSKU_STATUS', 4023, '申请修改FNSKU状态失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (31, 'ER_DD_EMAIL', 4024, '申请成功, 钉钉邮件提醒失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (32, 'ER_NO_LOGISTICS_PRICE_RANGE', 4025, '物流商单价区间配置不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (33, 'ER_MAX_PRICE_RANGE', 4026, '重量超过物流商单价区间最大值', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (34, 'ER_NO_FNSKU_PURCHASE_COST', 4027, 'FNSKU采购成本不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (35, 'ER_NO_CONFIGURATION', 4028, '配置不存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (36, 'ER_VALUE_IS_EXISTS', 4029, '属性值已存在', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (37, 'ER_FNSKU_STATUS_EXISTS', 4030, '申请失败, 该FNSKU已经被申请修改状态, 请到待审核里面审核！', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (38, 'ER_FNSKU_STATUS_MANY', 4031, '申请失败, 该站点+ASIN下的fnsku状态不统一, 请统一后状态再申请！', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (39, 'ER_METHOD_ERROR', 4032, '方法不被允许', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (40, 'ER_CONFIG_TABLE_ERROR', 4033, '配置表不合法', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (41, 'ER_ADD_ERROR', 4034, '创建失败', '严旭', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (42, 'ER_RISK_MISSING_PARAM', 5000, '缺少参数', '宋增增', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (43, 'ER_RISK_EXCEEDED_NUMBER', 5001, '批量操作数量超过限制', '宋增增', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (44, 'ER_RISK_IP_SHOP_APPLY', 5003, 'SPU侵权，禁止新增链接', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (45, 'ER_RISK_IP_WORD_APPLY', 5004, 'IP产品缺少刊登申请', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (46, 'ER_RISK_BEFORE_PUBLISH_NO_PARAM', 5005, '刊登前检查缺少参数', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (47, 'ER_RISK_BEFORE_PLATFORM_ERROR', 5006, '刊登前检查平台名传入异常', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (48, 'ER_RISK_BEFORE_PUBLISH_FORBBIDEN', 5007, '商品在该站点绝对禁止，不允许刊登', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (49, 'ER_RISK_BEFORE_SPU_ERROR', 5008, '刊登前检查SPU传入异常', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (50, 'ER_RISK_BEFORE_WEEE_ERROR', 5009, '店铺缺少WEEE认证，无法刊登该商品', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (51, 'ER_RISK_PARAM_ERROR', 5010, '传入参数格式错误', '宋增增', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (52, 'ER_RISK_ERROR', 5011, '部分成功, 部分失败!', '宋增增', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (53, 'ER_RISK_BEFORE_STOCK_SPU_ERROR', 5013, 'SPU传入异常', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (54, 'ER_RISK_BEFORE_STOCK_PLATFORM_ERROR', 5014, '平台名传入异常', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (55, 'ER_RISK_BEFORE_STOCK_RULE_ERROR', 5015, '有违规项，请查看明细', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (56, 'ER_RISK_BEFORE_WEEE_BRAND_ERROR', 5016, '店铺WEEE品牌不匹配，无法刊登该商品', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (57, 'ER_PERMISSION_ERROR', 5819, '您无此权限，请联系李萌萌进行规范表操作!', '盛荣凯', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (58, 'ER_Ebay_Excel_Upload', 6001, 'Excel上传异常', '郭子银', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (59, 'ER_PARAMS', 6003, '入参错误', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (60, 'ER_INNER_INTERFACE', 6004, '内部接口调用失败', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (61, 'ER_EXCEL_PARSE', 6005, 'Excel解析错误', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (62, 'ER_PROCESS_FAIL', 6006, 'Excel处理失败', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (63, 'ER_UNSUITED_FAIL', 6007, '操作数据不满足操作条件', '王俊昌', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (64, 'ER_API_FORBIDDEN', 7003, 'API forbidden access', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (65, 'ER_API_TIME', 7004, 'API event error', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (66, 'ER_API_UNCHANGED', 7005, 'API no change error', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (67, 'ER_API_METHOD', 7006, 'API method not allowed', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (68, 'ER_API_NOT_EXISTS', 7007, 'API does not exist', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (69, 'ER_API', 8000, 'API call exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (70, 'ER_EXPORT_DELIVER_FEE', 8001, '装箱数据导出失败', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (71, 'ER_TRANSFER_TRACK_NUM_UPDATE', 8002, '当前状态为调拨单审核，物流信息无法上传！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (72, 'ER_EXPORT_EXCEL_DATA', 8003, 'Excel导出失败', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (73, 'ER_EXPORT_LOGISTICS_AGING', 8004, '物流时效数据导出失败', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (74, 'ER_FLOW_CUSTOMS_CHECK_DATA', 8005, '该物流数据已进入海关查验流程！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (75, 'ER_FLOW_ORIGINAL_BILL_CHECK', 8006, '转入头程费用审批流程失败！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (76, 'ER_FLOW_APP_HSCODE_IS_REQUIRED', 8007, 'HS编码为必填项，请填写后再转下一步！', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (77, 'ER_NO_CUSTOMS_CHECK_REMARK', 8008, '请填写海关查验备注！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (78, 'ER_DB', 9000, 'Database exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (79, 'ER_AMZ', 10000, 'Amazon app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (80, 'ER_AMZ_ShopName', 10001, 'AMZ卖家简称错误', '吴仕洋', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (81, 'ER_AMZ_EXCHANGE_RATE', 10002, '未找到汇率', '吴仕洋', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (82, 'ER_CACHE', 10003, '缓存异常', '吴仕洋', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (83, 'ER_LAZADA', 11000, 'Lazada app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (84, 'ER_WISH', 12000, 'Wish app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (85, 'ER_SHOPEE', 13000, 'Shopee app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (86, 'ER_EBAY', 14000, 'Ebay app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (87, 'ER_ALI', 15000, 'Aliexpress app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (88, 'ER_PRODUCT_CENTER', 16000, 'product center exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (89, 'ER_APPLY_SUCCESS', 16001, 'shopsku apply success', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (90, 'ER_APPLY_SUCCESS_NO_DATA', 16002, 'shopsku apply success but no data', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (91, 'ER_JOYBUY', 17000, 'Joybuy app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (92, 'ER_WALMART', 18000, 'Walmart app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (93, 'ER_REAL_API', 19000, 'Real api exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (94, 'ER_REAL', 19001, 'Real app exception', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (95, 'ER_REAL_NO_NULL', 19002, 'shopName or Real Obj is Null', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (96, 'ER_BILL_EXISTS', 20000, '该账单已存在,请重新操作！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (97, 'ER_BILL_COMPLETE_FAILED', 20008, '账单操作失败,请稍后再试！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (98, 'ER_BILL_HAS_UNCHECKED', 20009, '账单明细还有未审核的部分!', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (99, 'ER_UNKNOWN', 20010, '未知错误,请联系IT处理!', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (100, 'ER_BILL_COMMIT_PAYMENT', 20012, '提交付款失败!', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (101, 'ER_DELIVER_STATUS_CFG_FILE_CHECK', 20020, '货物状态配置文件检查错误！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (102, 'ER_DELIVER_STATUS_CFG_EXISTS', 20021, '货物状态配置已存在！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (103, 'ER_TASK_UPLOAD_SVN', 21001, '定时任务服务器SVN更新失败', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (104, 'ER_TASK_SERVER_NOT_FIND', 21002, '没有查询到执行定时任务的服务器', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (105, 'ER_TASK_RUN_FAIL', 21003, '定时任务调用失败', '程子瑞', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (106, 'ER_KAUFLAND_REPORT_FILE_NAME', 23001, '文件命名错误，格式为: 店铺名称+报告类型.csv', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (107, 'ER_KAUFLAND_SHOP_NAME', 23002, '店铺名称错误，请检查后重新上传！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (108, 'ER_KAUFLAND_REPORT_TYPE', 23003, '报告类型错误，请检查后重新上传！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (109, 'ER_KAUFLAND_REPORT_FILE_TYPE', 23004, '文件类型错误，请检查后重新上传！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (110, 'ER_KAUFLAND_REPORT_FILE_UPLOAD', 23005, '文件上传错误，请稍后重试！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (111, 'ER_KAUFLAND_REPORT_DATA_SAVE', 23006, '数据保存错误，请稍后重试！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (112, 'ER_KAUFLAND_REPORT_HEAD', 23007, '标题格式错误，请检查后重新上传！', '雷涛', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (113, 'ER_RESOURCE_WAITING_REASON', 30000, '待回收资源转待定原因必填！', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (114, 'ER_RESOURCE_CONFIRM_IT_AND_FINANACE', 30001, '需要确认IT和财务资源是否需要回收！', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (115, 'ER_RESOURCE_CONFIRM_IT_NEED_REASON', 30002, 'IT资源不回收需要不回收原因！', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (116, 'ER_RESOURCE_CONFIRM_FINANCE_NEED_REASON', 30003, '财务资源不回收需要不回收原因！', '李志华', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (117, 'ER_NO_SKUZH_DT', 30004, '组合工厂明细表不存在此SKU', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (118, 'ER_MORE_NUMBER', 30005, '输入数量>未入库数量,状态修改为多货', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (119, 'ER_INVALIAD_INPUT', 30006, '无效输入', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (120, 'ER_CONFIG_SQL_NOT_EXIST', 30010, '全局SQL语句不存在该属性', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (121, 'ER_OTHER_INSTORE', 30012, '调用普源出库接口失败', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (122, 'ER_NO_USED_NUM', 30013, '普源可用数量不足', '袁永亮', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (123, 'ER_NOT_HAS_PAYMENT', 40001, '未填写预付款或运费,未生成财务付款记录', '张浩', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (124, 'ER_LACK_PARAMETER', 40002, '缺少必传参数', '张浩', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (125, 'ER_NO_ASIN_SALE_DATA', 40003, '获取ASIN销量数据失败', '张浩', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (126, 'ER_NO_ASIN_INVENTORY_DATA', 40004, '获取ASIN库存数据失败', '张浩', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (127, 'ER_UPLOAD_OSS', 70000, '提交质量反馈,Excel表格上传OSS失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (128, 'ER_EXPORT_EXCEL', 70001, '提交质量反馈,Excel表格导出失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (129, 'ER_EXPORT_IMAGE', 70003, '提交质量反馈, 图片导出出错', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (130, 'ER_CREDIT_CARD_EDITOR', 70004, '信用卡信息编辑失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (131, 'ER_PY_SKU_INBOUND_ERROR', 70005, '组合工厂生产完成-普源入库失败，请联系IT查看', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (132, 'ER_ZH_SKU_KSC_NUM_DEFICIENCY', 70006, '组合商品可生产数量不足', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (133, 'ER_ZH_SKU_INBOUND_OCCUPY', 70007, '组合商品出库占用失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (134, 'ER_ZH_SKU_INBOUND_OCCUPY_RELEASE', 70008, '组合商品出库占用未全部释放', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (135, 'ER_CJFH_INBOUND_OCCUPY_RELEASE', 70009, '创建发货失败, 组合商品出库占用未全部释放', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (136, 'ER_CHECK_DELIVER_GOODS_WEIGHT', 70010, '该批次每票最低重量未大于1千克，需确定是否发货', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (137, 'ER_FC_RELEASE_FAIL', 70011, '亚马逊分仓组合商品库存释放失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (138, 'ER_FC_OCCUPY_FAIL', 70012, '亚马逊分仓组合商品库存占用失败', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (139, 'ER_NO_CONGIGURATION_FOUND', 70013, '未查询到主要物流方式默认配置信息', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (140, 'ER_DELIVER_RISK_CHECK', 70014, '发货流程-风控限制规则', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (141, 'ER_LEXICOGRAPHICAL_VALENCE_CHECK', 70015, '发货流程-词图价审核流程', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (142, 'ER_PLAN_DELIVER_NUM_CHECK', 70016, '发货流程-生成发货任务提交校验', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (143, 'ER_SHEIN_CREATE_CHECK', 70017, 'SHEIN创建发货校验', '郑宏峰', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (144, 'ER_ZHGC_ZC_QA_LC', 100012, '组合工厂自测QA处理-生产单状态错误', '王志平', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (145, 'ER_FUNCTION_NOT_FOUND', 44001, '软件接口找不到对应函数', '倪恒', 1, '2023-04-19 17:00:59', '2023-05-23 11:02:49');
INSERT INTO `t_public_error_code` VALUES (146, 'ER_PARAM_NOT_MATCH', 44002, '软件接口参数匹配失败', '倪恒', 1, '2023-04-19 17:00:59', '2023-05-23 11:02:56');
INSERT INTO `t_public_error_code` VALUES (147, 'ER_RESULT_NOT_MATCH', 44003, '软件接口返回值匹配失败', '倪恒', 1, '2023-04-19 17:00:59', '2023-05-23 11:03:02');
INSERT INTO `t_public_error_code` VALUES (148, 'ER_CODE_NOT_MATCH', 44004, '软件接口返回码匹配失败', '倪恒', 1, '2023-04-19 17:00:59', '2023-05-23 11:03:10');
INSERT INTO `t_public_error_code` VALUES (149, 'ER_TASK_NOT_FOUND', 404005, '未找到功能!', '倪恒', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (150, 'ER_STANDARD_QUERY', 405001, '代码规范查询异常!', '盛荣凯', 1, '2023-04-19 17:00:59', NULL);
INSERT INTO `t_public_error_code` VALUES (151, 'ER_INTERFACE_FUNCTION_ERROR', 44005, '软件接口流程编排调用子函数失败', '倪恒', 1, '2023-05-23 11:01:19', '2023-05-23 13:43:36');
INSERT INTO `t_public_error_code` VALUES (152, 'ER_OSS_UPLOAD_FAIL', 300001, '文件上传OSS失败', '倪恒', 0, '2023-06-05 14:16:09', NULL);

SET FOREIGN_KEY_CHECKS = 1;

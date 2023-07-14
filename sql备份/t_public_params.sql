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

 Date: 12/07/2023 17:18:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_params
-- ----------------------------
DROP TABLE IF EXISTS `t_public_params`;
CREATE TABLE `t_public_params`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `param_code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数编号',
  `param_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '中文名',
  `param_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '英文名',
  `param_detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '注释',
  `create_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `data_type` int(2) NULL DEFAULT NULL COMMENT '参数类型（1.Int,2.Float,3.Boolean,4.String,5.Datetime,11.List,12.Tuple,13.Dictionary,14.Set）',
  `level` int(1) NULL DEFAULT NULL COMMENT '参数级别(1.基础类型，2.复杂类型)',
  `child_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '子级参数id(多个用逗号隔开)',
  `select_info_id` int(11) NULL DEFAULT NULL COMMENT '枚举关联全局下拉框id(枚举类型时，选中的t_online_select_info表id)',
  `status` int(1) NULL DEFAULT NULL COMMENT '发布状态（0.草稿，1.已发布）',
  `release_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '审核人',
  `release_time` datetime NULL DEFAULT NULL COMMENT '审核时间',
  `apply_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '提交人',
  `apply_time` datetime NOT NULL DEFAULT '1900-01-01 00:00:00' COMMENT '提交时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 172 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公共方法参数列表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_params
-- ----------------------------
INSERT INTO `t_public_params` VALUES (27, 'LCBPCS20230314145124', 'shop_name', '店铺名称', '店铺名称', '盛荣凯', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (28, 'LCBPCS20230314145143', 'username', '用户名', '用户名', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 2, '丁俊', '2023-06-16 16:35:11', '严旭', '2023-06-16 16:32:46');
INSERT INTO `t_public_params` VALUES (29, 'LCBPCS20230314145157', 'password', '密码', '密码', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (30, 'LCBPCS20230314145217', 'age', '年龄', '年龄', '盛荣凯', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, '丁俊', '2023-04-27 10:23:19', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (31, 'LCBPCS20230314200111', 'SPU', '商品的属性', '商品的属性', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (32, 'LCBPCS20230314200138', 'SKU', 'SPU下的SKU', 'SPU下的SKU', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (33, 'LCBPCS20230314200156', 'max_size', '最大尺寸', '最大尺寸', '倪恒', '2023-04-19 17:00:59', 2, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (34, 'LCBPCS20230314200210', 'min_size', '最小尺寸', '最小尺寸', '倪恒', '2023-04-19 17:00:59', 2, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (37, 'LCBPCS20230314200356', 'test_param_dict', '测试字典数据', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (38, 'LCBPCS20230314200432', 'test_param_boolean', '测试布尔数据', '测试布尔数据', '倪恒', '2023-04-19 17:00:59', 3, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (39, 'LCBPCS20230314200458', 'return_dict', '字典返回值', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (40, 'LCBPCS20230314200515', 'return_set', '集合返回值', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (41, 'LCBPCS20230314200536', 'return_number', '数字返回值', '数字返回值', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (45, 'LCBPCS20230316111121', 'color', '颜色', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (48, 'LCBPCS20230316192127', 'math_score', '数学分数', '数学分数', '倪恒', '2023-04-19 17:00:59', 2, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (49, 'LCBPCS20230316192149', 'English_score', '英语分数', '英语分数', '倪恒', '2023-04-19 17:00:59', 2, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (50, 'LCBPCS20230316192218', 'sum_score', '总分数', '总分数', '倪恒', '2023-04-19 17:00:59', 2, NULL, NULL, NULL, 2, '严旭', '2023-06-16 13:15:57', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (51, 'LCBPCS20230317095055', 'max_value', '最大值', '最大值', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (52, 'LCBPCS20230320154040', 'number', '数值', '数值', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (53, 'LCBPCS20230320155936', 'test_result_list', '列表类型返回值', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (54, 'LCBPCS20230322135007', 'base_test', '测试参数', 'ss', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 1, '丁俊', '2023-04-27 14:17:51', '倪恒', '2023-06-16 13:31:10');
INSERT INTO `t_public_params` VALUES (55, 'LCBPCS20230323190220', 'order_id', '订单id', '订单id', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (56, 'LCBPCS20230323190316', 'order', '订单', '假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (58, 'LCBPCS20230323190608', 'area', '地区', '市级地区名称', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 2, '丁俊', '2023-05-05 09:10:59', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (59, 'LCBPCS20230323192315', 'number_param', '数字类型参数', '数字类型参数', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (60, 'LCBPCS20230324181515', 'number_list', '数字类型的列表', '数字类型的列表', '倪恒', '2023-04-19 17:00:59', 11, NULL, '52', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (62, 'LCBPCS20230324182038', 'is_odd', '是否为奇数', '是否为奇数', '倪恒', '2023-04-19 17:00:59', 3, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (70, NULL, 'create_time', '创建时间', '创建时间', '倪恒', '2023-04-19 17:00:59', 5, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (74, NULL, 's_school_name', '学校名称', '学校名称', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 2, '丁俊', '2023-05-08 10:40:51', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (75, NULL, 's_location', '地址', '地址', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 2, '丁俊', '2023-05-05 10:00:25', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (76, NULL, 'welcome', '欢迎语句', '欢迎语句', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (80, NULL, 'condition', '查询参数', '列表全字段查询参数', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (81, NULL, 'standard_data_list', '代码规范列表', '代码规范列表返回值，假数据', '倪恒', '2023-04-19 17:00:59', 1, NULL, NULL, NULL, 2, '丁俊', '2023-05-05 09:10:45', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (82, NULL, 'v_in_params', '全局查询参数', '用于列表查询接口，单个输入框的全字段查询参数', '倪恒', '2023-04-19 17:00:59', 4, NULL, NULL, NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (83, NULL, 'a_area_list', '地区列表', '地区列表', '邢鑫', '2023-04-19 17:00:59', 11, NULL, '58', NULL, 0, '常杨', '2023-04-20 16:45:33', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (85, NULL, 'o_test_dict', '测试字典类型', '测试字典类型', '倪恒', '2023-04-19 17:00:59', 12, NULL, '48,49,60,74', NULL, 2, '丁俊', '2023-05-06 16:03:59', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (88, NULL, 'o_one_dict', '一个字段的字典', 'aa', '常杨', '2023-04-19 17:00:59', 12, NULL, '45', NULL, 0, '常杨', '2023-04-26 17:40:53', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (89, NULL, 'a_location_list', '地址列表', '地址列表', '倪恒', '2023-04-19 17:00:59', 11, NULL, '75', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (91, NULL, 'o_dict', '测试参数字典类型', '测试参数字典类型', '倪恒', '2023-04-19 17:00:59', 12, NULL, '30,58', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (92, NULL, 'a_age_list', '测试参数列表类型', '测试参数列表类型', '倪恒', '2023-04-19 17:00:59', 11, NULL, '30', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (93, NULL, 'a_dict_list', '测试列表套字典', '测试列表套字典，易出问题的地方', '倪恒', '2023-04-19 17:00:59', 11, NULL, '85', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (94, NULL, 'o_school', '学校', '测试数据，学校', '倪恒', '2023-04-19 17:00:59', 12, NULL, '74,75', NULL, 0, NULL, NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (95, NULL, 'a_school_list', '学校列表', '测试数据', '倪恒', '2023-04-19 17:00:59', 11, NULL, '94', NULL, 1, '丁俊', '2023-04-27 10:19:43', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (96, NULL, 'o_test_ddd', 'DDD', 'ddd', '倪恒', '2023-04-19 17:00:59', 12, NULL, '85,94', NULL, 1, '', '1900-01-01 00:00:00', '王恒', '2023-06-16 13:56:59');
INSERT INTO `t_public_params` VALUES (99, NULL, 's_pen', '笔', '测试数据', '倪恒', '2023-04-19 17:00:59', 4, NULL, '', NULL, 2, '丁俊', '2023-05-05 09:10:52', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (102, NULL, 's_file_object', 'OSS文件对象', 'OSS文件对象', '常杨', '2023-04-20 20:18:49', 4, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (103, NULL, 'dt2_update_time', '修改时间', '修改时间', '倪恒', '2023-04-23 09:24:30', 6, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:02', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (104, NULL, 'i_a', 'dd', 'dd', '倪恒', '2023-04-25 09:42:26', 1, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (105, NULL, 'a_shlijnnb2', 'svjkjknvb2', 'siumtvb2', '倪恒', '2023-04-25 13:40:17', 11, NULL, '83', NULL, 0, '丁俊', '2023-04-27 10:19:23', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (106, NULL, 'e_aa', '枚举类型', '枚举类型', '倪恒', '2023-04-28 08:48:02', 13, NULL, '', 23, 2, '丁俊', '2023-05-05 10:26:19', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (107, NULL, 'o_after_sales_order', '亚马逊售后订单对象', '发热', '倪恒', '2023-04-28 09:14:08', 12, NULL, '58', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (108, NULL, 'a_after_sales_order', '亚马逊售后订单对象列表亚马逊售后订单对象列表亚马逊售后订单对象列表', '试试试试', '倪恒', '2023-04-28 09:14:35', 11, NULL, '107', NULL, 2, '丁俊', '2023-05-05 10:02:56', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (109, NULL, 'b_is_action_user', '是否提交人', 'true:是提交人，false:不是提交人', '倪恒', '2023-05-04 11:11:10', 3, NULL, '', NULL, 2, '丁俊', '2023-05-15 13:47:18', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (111, NULL, 's_userName', '用户名', '用户名', '丁俊', '2023-05-05 10:55:28', 4, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (112, NULL, 's_funsku', 'funsku', 'funsku', '丁俊', '2023-05-06 09:56:12', 4, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (114, NULL, 's_fnsku', 'fnsku', 'fnsku', '丁俊', '2023-05-06 10:15:23', 4, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (115, NULL, 'a_fnsku', 'fnsku', 'fnsku', '丁俊', '2023-05-06 10:15:40', 11, NULL, '114', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (117, NULL, 'i_function_id', '函数id', '函数id', '丁俊', '2023-05-11 09:11:41', 1, NULL, '', NULL, 2, '丁俊', '2023-05-11 09:16:07', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (118, NULL, 's_function_name', '通用流程函数名', '用在通用流程函数中，表示需执行的函数英文名（通用流程相关函数专用）', '丁俊', '2023-05-11 09:12:48', 4, NULL, '', NULL, 2, '丁俊', '2023-05-11 09:16:11', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (119, NULL, 'o_function_param', '通用流程参数', '用在通用流程函数中，作为其他函数的传参载体（通用流程相关函数专用）', '丁俊', '2023-05-11 09:13:12', 12, NULL, '', NULL, 2, '丁俊', '2023-05-11 09:15:17', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (120, NULL, 'o_function_result', '函数运行结果', '函数运行结果', '丁俊', '2023-05-11 09:13:35', 12, NULL, '', NULL, 2, '丁俊', '2023-05-11 09:16:05', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (121, NULL, 'dt_last_demand_non_end_date', '最后一次备货快速物流截止日期', '针对节日属性配置表，最后一次备货快速物流截止日期', '丁俊', '2023-05-15 13:33:12', 5, NULL, '', NULL, 2, '丁俊', '2023-05-15 13:33:28', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (122, NULL, 'f_fff', 'fff', 'fff', '丁俊', '2023-05-15 18:01:55', 2, NULL, '', NULL, 2, '丁俊', '2023-05-15 18:02:03', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (123, NULL, 'dt2_start_time', '起始时间', '起始时间', '丁俊', '2023-05-15 18:03:35', 6, NULL, '', NULL, 2, '丁俊', '2023-05-15 18:03:43', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (124, NULL, 'dt2_end_time', '结束时间', '结束时间', '倪恒', '2023-05-18 13:42:41', 6, NULL, '', NULL, 2, '丁俊', '2023-05-18 13:47:30', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (125, NULL, 's_principal', '责任人', '责任人', '倪恒', '2023-05-18 13:43:24', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 13:47:20', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (126, NULL, 'i_function_number', '函数数量', '函数数量', '倪恒', '2023-05-18 13:44:21', 1, NULL, '', NULL, 2, '丁俊', '2023-05-18 13:47:28', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (127, NULL, 'i_code_line_number', '代码行数', '代码行数', '倪恒', '2023-05-18 13:44:37', 1, NULL, '', NULL, 2, '丁俊', '2023-05-18 13:47:32', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (128, NULL, 'o_function_statistics', '函数统计信息', '函数统计信息', '倪恒', '2023-05-18 13:45:29', 12, NULL, '125,126,127', NULL, 2, '丁俊', '2023-05-18 13:47:38', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (129, NULL, 'a_function_statistics', '函数统计信息列表', '函数统计信息列表', '倪恒', '2023-05-18 13:46:10', 11, NULL, '128', NULL, 2, '丁俊', '2023-05-18 13:47:42', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (130, NULL, 'i_develop_require_specification_id', '开发规范对象ID', '开发规范对象ID', '盛荣凯', '2023-05-18 14:44:56', 1, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:00', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (131, NULL, 's_desc', '描述', '描述', '盛荣凯', '2023-05-18 14:45:30', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:54:55', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (132, NULL, 's_pic_url', '图片路径', '图片路径', '盛荣凯', '2023-05-18 14:46:09', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:05', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (133, NULL, 's_remarks', '备注信息', '备注信息', '盛荣凯', '2023-05-18 14:46:34', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:07', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (134, NULL, 's_apply_person', '提交人', '提交人', '盛荣凯', '2023-05-18 14:46:58', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:11', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (135, NULL, 'dt2_apply_time', '申请时间', '申请时间', '盛荣凯', '2023-05-18 14:47:15', 6, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:13', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (136, NULL, 'dt2_update_person', '更新人', '更新人', '盛荣凯', '2023-05-18 14:47:34', 6, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:16', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (137, NULL, 'e_develop_require_specification_station', '开发规范考核岗位', '开发规范考核岗位', '盛荣凯', '2023-05-18 14:48:24', 13, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:19', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (138, NULL, 'e_develop_require_specification_type', '规范类别', '规范类别', '盛荣凯', '2023-05-18 14:48:51', 13, NULL, '', NULL, 2, '丁俊', '2023-05-18 14:55:27', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (139, NULL, 'o_develop_require_specification', '开发规范对象', '开发规范对象', '盛荣凯', '2023-05-18 14:50:43', 12, NULL, '130,131,132,133,134,135,136,103,137,138', NULL, 2, '丁俊', '2023-05-18 14:55:21', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (140, NULL, 'a_develop_require_specification', '开发规范对象列表', '开发规范对象列表', '盛荣凯', '2023-05-18 14:51:11', 11, NULL, '139', NULL, 2, '丁俊', '2023-05-18 14:55:29', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (141, NULL, 's_operator', '操作人', '操作人', '盛荣凯', '2023-05-18 14:59:52', 4, NULL, '', NULL, 2, '丁俊', '2023-05-18 15:00:24', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (142, NULL, 'obj_function', '接口函数', '接口函数本身', '倪恒', '2023-05-19 10:19:47', 7, NULL, '', NULL, 2, '丁俊', '2023-05-19 10:00:24', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (143, NULL, 's_function_body_content', '函数体内容', '函数体内容\'1\'\"2\"', '倪恒', '2023-05-19 10:20:26', 4, NULL, '', NULL, 2, '丁俊', '2023-05-19 10:01:24', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (144, NULL, 'o_function_param', '函数参数', '用在通用流程函数中，作为其他函数的传参载体（通用流程相关函数专用）（用于替换原有o_function_param）', '倪恒', '2023-05-29 09:08:51', 12, NULL, '', NULL, 0, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (146, NULL, 'obj_function', '接口函数', '接口函数1', '倪恒', '2023-05-29 13:46:13', 7, NULL, '', NULL, 2, '', NULL, '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (148, NULL, 'page_class_config', '类管理页面', '软件接口定义，类管理页面', '丁俊', '2023-06-12 10:32:59', 21, NULL, '', NULL, 2, '丁俊', '2023-06-12 11:12:05', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (149, NULL, 'page_param_config', '参数管理页面', '软件接口定义，参数管理页面', '丁俊', '2023-06-12 10:34:05', 21, NULL, '', NULL, 2, '丁俊', '2023-06-12 11:12:06', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (150, NULL, 's_param_name_cn', '参数中文名', '参数管理页面中的参数中文名', '丁俊', '2023-06-12 16:34:56', 4, NULL, '', NULL, 2, '丁俊', '2023-06-12 16:37:00', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (151, NULL, 's_param_name_en', '参数英文名', '参数管理页面中的参数英文名', '丁俊', '2023-06-12 16:35:25', 4, NULL, '', NULL, 2, '丁俊', '2023-06-12 16:36:59', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (152, NULL, 'a_param_name_en', '参数英文名列表', '参数英文名列表', '丁俊', '2023-06-12 16:38:36', 11, NULL, '151', NULL, 2, '丁俊', '2023-06-12 16:38:47', '', '2023-06-16 00:00:00');
INSERT INTO `t_public_params` VALUES (153, NULL, 'dt2_test_time', '测试数据：时间', '测试数据：时间，提交人，审核人时间', '倪恒', '2023-06-16 13:52:01', 6, NULL, '', NULL, 1, '', '1900-01-01 00:00:00', '王恒', '2023-06-16 13:53:39');
INSERT INTO `t_public_params` VALUES (154, NULL, 's_page_name', '页面名称', '命名明确，唯一，用于区分不同页面', '丁俊', '2023-06-19 10:55:27', 4, NULL, '', NULL, 2, '丁俊', '2023-06-19 10:55:31', '丁俊', '2023-06-19 10:55:30');
INSERT INTO `t_public_params` VALUES (155, NULL, 's_vue_component_content', 'vue组件文本内容', '组件代码内容，用于生成代码和源码分析', '丁俊', '2023-06-19 11:12:23', 4, NULL, '', NULL, 2, '丁俊', '2023-06-19 11:12:31', '丁俊', '2023-06-19 11:12:30');
INSERT INTO `t_public_params` VALUES (156, NULL, 's_element_name', '组件元素名称', '组件元素名称', '丁俊', '2023-06-25 13:14:19', 4, NULL, '', NULL, 2, '丁俊', '2023-06-25 13:14:22', '丁俊', '2023-06-25 13:14:21');
INSERT INTO `t_public_params` VALUES (157, NULL, 'a_element_name', '组件元素名称列表', '组件元素名称列表', '丁俊', '2023-06-25 13:14:47', 11, NULL, '156', NULL, 2, '丁俊', '2023-06-25 13:14:51', '丁俊', '2023-06-25 13:14:49');
INSERT INTO `t_public_params` VALUES (158, NULL, 's_page_template_config', '页面模板配置', '页面模板配置数据，需要转为json格式渲染', '丁俊', '2023-06-25 14:20:42', 4, NULL, '', NULL, 2, '丁俊', '2023-06-25 14:21:01', '丁俊', '2023-06-25 14:21:00');
INSERT INTO `t_public_params` VALUES (159, NULL, 's_vue_component_file_name', '组件文件名', '组件代码文件名', '丁俊', '2023-06-25 16:29:27', 4, NULL, '', NULL, 2, '丁俊', '2023-06-25 16:29:44', '丁俊', '2023-06-25 16:29:43');
INSERT INTO `t_public_params` VALUES (160, NULL, 'e_after_sales_order_source', '售后订单来源', '售后订单数据来源', '严旭', '2023-04-24 08:51:52', 13, NULL, '', 336, 2, '丁俊', '2023-07-07 10:26:08', '', '1900-01-01 00:00:00');
INSERT INTO `t_public_params` VALUES (161, NULL, 'i_enum_id', '枚举id', '枚举值id，对应t_online_select_info表的id', '倪恒', '2023-07-06 20:14:50', 1, NULL, '', NULL, 2, '丁俊', '2023-07-07 13:22:26', '严旭', '2023-07-06 20:37:53');
INSERT INTO `t_public_params` VALUES (162, NULL, 's_enum_key', '枚举key值', '枚举的key值（用于数据库存储的值，由字母或数字组成，数据类型可以是Int，String）', '倪恒', '2023-07-06 20:16:24', 4, NULL, '', NULL, 2, '丁俊', '2023-07-07 13:22:25', '严旭', '2023-07-06 20:37:51');
INSERT INTO `t_public_params` VALUES (163, NULL, 's_enum_value', '枚举展示值', '枚举展示值（页面显示的枚举值，可以是汉字，字母和数字）', '倪恒', '2023-07-06 20:18:32', 4, NULL, '', NULL, 2, '丁俊', '2023-07-07 13:22:25', '严旭', '2023-07-06 20:37:50');
INSERT INTO `t_public_params` VALUES (164, NULL, 's_enum_variable_name', '枚举程序变量名', '枚举的程序变量名，存在于ConstEnum文件中。\n如:枚举\"FN到货类型\"的选项\"全新品\"所对应程序变量名是\"BRAND_NEW\"', '倪恒', '2023-07-06 20:25:04', 4, NULL, '', NULL, 2, '丁俊', '2023-07-07 13:22:24', '严旭', '2023-07-06 20:37:49');
INSERT INTO `t_public_params` VALUES (165, NULL, 'o_enum', '枚举对象', '直观展示枚举的详细信息', '倪恒', '2023-07-06 20:28:39', 12, NULL, '161,167,169', NULL, 2, '丁俊', '2023-07-07 13:22:22', '倪恒', '2023-07-07 09:57:53');
INSERT INTO `t_public_params` VALUES (167, NULL, 's_enum_name', '枚举参数名', '参数管理中,枚举类型的参数名称', '倪恒', '2023-07-07 09:40:29', 4, NULL, '', NULL, 2, '丁俊', '2023-07-07 13:22:21', '倪恒', '2023-07-07 09:40:43');
INSERT INTO `t_public_params` VALUES (168, NULL, 'o_enum_option', '枚举选项', '枚举的每一个选项', '倪恒', '2023-07-07 09:55:01', 12, NULL, '162,164,163', NULL, 2, '丁俊', '2023-07-07 13:22:20', '倪恒', '2023-07-07 09:56:03');
INSERT INTO `t_public_params` VALUES (169, NULL, 'a_enum_option', '枚举选项列表', '枚举的选项列表', '倪恒', '2023-07-07 09:55:30', 11, NULL, '168', NULL, 2, '丁俊', '2023-07-07 13:22:18', '倪恒', '2023-07-07 09:58:02');
INSERT INTO `t_public_params` VALUES (170, NULL, 'e_product_packaging', '产品外包装', '供应商给合趣发货所使用的产品外包装', '蔡之其', '2023-06-29 14:36:55', 13, NULL, '', 446, 2, '丁俊', '2023-06-29 17:46:52', '王恒', '2023-06-29 14:53:35');
INSERT INTO `t_public_params` VALUES (171, NULL, 'e_sample_image_type', '样品图类型', '产品样品图的类型，包括正面、背面、侧面', '王恒', '2023-06-29 14:42:46', 13, NULL, '', 447, 2, '丁俊', '2023-06-29 17:47:21', '王恒', '2023-06-29 14:58:44');

SET FOREIGN_KEY_CHECKS = 1;

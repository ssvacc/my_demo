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

 Date: 12/07/2023 17:19:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_function
-- ----------------------------
DROP TABLE IF EXISTS `t_public_function`;
CREATE TABLE `t_public_function`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类名',
  `function_code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '函数编号',
  `function_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '函数名',
  `function_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '函数说明',
  `function_detail` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '功能详情（注释）',
  `level` int(2) NULL DEFAULT NULL COMMENT '函数级别（舍弃）',
  `involve_table` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '涉及表',
  `operate_table` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '操作表',
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '函数作者',
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '函数路径',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  `status` int(1) NULL DEFAULT NULL COMMENT '发布状态（0.草稿，1.已提交，2.已审核，3.已发布）',
  `release_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '审核人',
  `release_time` datetime NULL DEFAULT NULL COMMENT '审核时间',
  `s_principal` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '责任人',
  `publish_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '发布人',
  `publish_time` datetime NULL DEFAULT NULL COMMENT '发布时间',
  `is_auto_test` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否加入自动化测试（0.未加入，1.已加入）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 117 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公共方法' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_function
-- ----------------------------
INSERT INTO `t_public_function` VALUES (40, NULL, 'LCBPHS20230324182222', 'show_number_odd_even', '筛选出奇数或者偶数', '输入一个数字集合,传入True,筛选所有奇数，False筛选所有偶数。\n参数示例：1,2,3,4,5,4,3,2\n', NULL, NULL, NULL, '倪恒', 'SVN://app\\custom_function\\math.py', '2023-03-24 18:22:22', '2023-03-29 15:44:58', 1, NULL, NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (41, NULL, 'LCBPHS20230324182448', 'get_max_number', '取列表中最大值', '输入数字列表，取列表中最大值。\n参数示例：1,2,3,4,5,4,3,2', NULL, NULL, NULL, '倪恒', 'SVN://app\\custom_function\\math.py', '2023-03-24 18:24:48', '2023-03-28 08:57:19', 1, NULL, NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (61, 'School', NULL, 'School::show_school_location', '查看学校地址', '类函数,非静态类，需要self参数', NULL, '', '', '倪恒', 'SVN://app\\custom_function\\School.py', '2023-04-04 16:49:01', '2023-05-12 17:26:37', 3, '丁俊', '2023-05-05 10:37:19', '倪恒', '蔡杨林', '2023-05-17 10:26:25', 0);
INSERT INTO `t_public_function` VALUES (63, 'School', NULL, 'School::show_school_location_static', '查看学校地址', '类函数，静态，不需要self参数', NULL, 'a', '', '倪恒', 'SVN://app\\custom_function\\School.py', '2023-04-04 18:05:40', '2023-05-17 10:34:40', 3, '丁俊', '2023-05-05 10:37:17', '倪恒', '蔡杨林', '2023-05-17 10:24:04', 0);
INSERT INTO `t_public_function` VALUES (65, NULL, NULL, 'fun_get_software_standard_info', '获取开发规范信息', '获取开发规范信息', NULL, '', '', '盛荣凯', 'SVN://app\\function\\t_software_develop_standard.py', '2023-04-11 19:43:10', NULL, 0, NULL, NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (66, NULL, NULL, 'f_GetDevelopRequireSpecification', '获取开发规范全量信息', '获取开发规范全量信息', NULL, '', '', '盛荣凯', 'SVN://app\\function\\t_software_develop_standard.py', '2023-04-13 08:54:40', NULL, 1, '丁俊', '2023-07-07 10:36:25', NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (67, NULL, NULL, 'f_CheckErrorCode', '测试数据：校验返回码', 'resetFields', NULL, '', '', '倪恒', 'a4wx', '2023-04-18 11:22:47', '2023-05-12 17:29:48', 1, '丁俊', '2023-07-07 10:36:26', NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (70, NULL, NULL, 'f_ww_aa_f_ww_aaf_ww_aaf_ww_aaf_ww_aa', '测试作者测试作者测试作者测试作者测试作者', '测试作者', NULL, '', '', '倪恒', 'bb/ddaa/ad.py', '2023-04-21 09:04:18', '2023-05-08 20:28:06', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (72, NULL, NULL, 'f_dd', 'aa', '', NULL, '', '', '倪恒', 'wdd', '2023-04-23 10:39:50', '2023-04-25 11:37:51', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (74, '', NULL, 'g_ddwwfregtyuj1', '测试数据：这是新增', '测试数据：这是新增\'1\'\"2\"', NULL, '1', '1', '倪恒', '测试数据：这是新增', '2023-04-25 09:03:45', '2023-06-05 17:39:58', 1, '丁俊', '2023-07-07 10:36:24', '常杨', NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (75, '', NULL, 'g_func111', '测试路径', '测试路径', NULL, '122', '2', '常杨', 'SVN://func_process_app/function/t_software_develop_standard.py', '2023-04-25 16:00:59', '2023-05-06 14:28:07', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (77, 'FNSKU', NULL, 'FNSKU::list', 'FNSKU列表', '12e', NULL, '', '', '倪恒', 'SVN://aaa', '2023-05-04 14:18:02', '2023-05-08 16:07:18', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (78, '', NULL, 'g_awd', '', 'adw', NULL, NULL, NULL, '丁俊', 'SVN://awd', '2023-05-05 14:13:13', NULL, 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (79, 'School', NULL, 'School::dd', '中文名d2', '获取全量的待办配置数据。\n无参数；\n返回待办配置对象列表(a_deal_job_config)\n；列表中是每一个待办配置对象(o_deal_job_config)，每个对象包含页面展示各个字段；\n列表中是每一个待办配置对象(o_deal_job_config)，每个对象包含页面展示各个字段', NULL, NULL, NULL, '丁俊', 'SVN://dd', '2023-05-08 10:41:21', '2023-05-11 18:24:26', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (80, '', NULL, 'g_awdfergrt', 'awd', 'esf', NULL, NULL, NULL, '丁俊', 'SVN://adwgt', '2023-05-08 20:33:20', '2023-05-08 20:35:06', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (81, 'InterfaceFunction', NULL, 'InterfaceFunction::run_interface_function', '通用流程函数', '通用流程函数是用来执行其他函数的，\n没有具体业务，参数和返回值是封装\n被执行函数的参数和返回值', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-05-11 09:18:13', '2023-05-17 10:28:43', 3, '丁俊', '2023-05-12 09:36:52', '倪恒', '徐国锋', '2023-05-18 14:37:26', 0);
INSERT INTO `t_public_function` VALUES (82, '', NULL, 'g_test_debug', '测试数据：测试调试页面', '针对节日属性配置表，最后一次备货快速物流截止日期1111', NULL, NULL, NULL, '丁俊', 'SVN://1', '2023-05-15 13:34:12', '2023-05-15 13:47:40', 0, '', NULL, NULL, NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (83, '', NULL, 'g_all_data_type', '所有数据类型', '测试所有类型的参数', NULL, NULL, NULL, '丁俊', 'SVN://1', '2023-05-15 18:05:37', '2023-05-16 18:11:48', 0, '', NULL, '倪恒', NULL, NULL, 0);
INSERT INTO `t_public_function` VALUES (88, 'InterfaceFunction', NULL, 'InterfaceFunction::function_statistics', '统计各开发责任人的接口函数', '统计各开发责任人的接口函数', NULL, NULL, NULL, '倪恒', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-05-18 14:15:27', '2023-05-18 14:17:49', 1, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (89, 'DevelopRequireSpecification', NULL, 'DevelopRequireSpecification::get_all', '获取开发规范全量条目', '获取开发规范全量条目', NULL, NULL, NULL, '盛荣凯', 'SVN://app\\class_function\\DevelopRequireSpecification.py', '2023-05-18 14:57:08', '2023-06-05 17:43:43', 3, '丁俊', '2023-05-18 15:08:28', '盛荣凯', '徐国锋', '2023-06-12 14:08:53', 1);
INSERT INTO `t_public_function` VALUES (90, 'DevelopRequireSpecification', NULL, 'DevelopRequireSpecification::add', '新增开发规范条目', '新增开发规范条目', NULL, NULL, NULL, '盛荣凯', 'SVN://app\\class_function\\DevelopRequireSpecification.py', '2023-05-18 15:01:45', '2023-05-18 15:02:02', 3, '丁俊', '2023-05-18 15:08:23', '盛荣凯', '徐国锋', '2023-05-18 15:09:03', 1);
INSERT INTO `t_public_function` VALUES (91, 'DevelopRequireSpecification', NULL, 'DevelopRequireSpecification::delete', '删除开发规范条目', '删除开发规范条目', NULL, NULL, NULL, '盛荣凯', 'SVN://app\\class_function\\DevelopRequireSpecification.py', '2023-05-18 15:03:09', '2023-05-18 15:04:45', 3, '丁俊', '2023-05-18 15:08:15', '盛荣凯', '徐国锋', '2023-05-18 15:09:08', 0);
INSERT INTO `t_public_function` VALUES (92, 'DevelopRequireSpecification', NULL, 'DevelopRequireSpecification::edit', '编辑开发规范条目', '编辑开发规范条目', NULL, NULL, NULL, '盛荣凯', 'SVN://app\\class_function\\DevelopRequireSpecification.py', '2023-05-18 15:04:15', NULL, 3, '丁俊', '2023-05-18 15:08:08', '盛荣凯', '徐国锋', '2023-05-18 15:09:16', 0);
INSERT INTO `t_public_function` VALUES (93, 'InterfaceFunction', NULL, 'InterfaceFunction::query_function', '根据函数id查询函数', '根据函数id查询函数', NULL, NULL, NULL, '倪恒', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-05-19 10:26:03', '2023-06-05 20:42:30', 1, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (94, 'InterfaceFunction', NULL, 'InterfaceFunction::query_function_content', '获取函数体内容', '获取函数体文本内容，用于源码的展示和分析', NULL, NULL, NULL, '倪恒', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-05-19 10:47:27', '2023-06-05 20:42:22', 1, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (95, 'InterfaceFunction', NULL, 'InterfaceFunction::get_function_code_line', '获取函数体代码行数', '获取函数体代码行数', NULL, NULL, NULL, '倪恒', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-05-19 10:49:51', NULL, 1, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (96, 'FNSKU', NULL, 'FNSKU::btyh', '新增校验', '1', NULL, NULL, NULL, '倪恒', 'SVN://1', '2023-05-23 08:59:04', NULL, 0, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (97, 'Flow', NULL, 'Flow::add', '新增开发规范条目12', '安稳的', NULL, NULL, NULL, '倪恒', 'SVN://12', '2023-05-23 08:59:31', '2023-05-23 09:16:07', 0, '', NULL, '张创', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (98, 'PageClassConfig', NULL, 'PageClassConfig::get_page_select_area_param_html', '获取页面搜索区参数', '获取页面搜索区对应的字段参数列表', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-12 16:40:38', '2023-06-13 09:59:05', 1, '丁俊', '2023-07-07 10:36:15', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (99, 'PageClassConfig', NULL, 'PageClassConfig::get_page_data_area_param_html', '获取类管理页面数据区参数', '获取类管理页面数据区参数,生成html文件', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-12 16:44:31', '2023-06-13 09:51:09', 1, '丁俊', '2023-06-13 16:52:25', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (100, 'PageClassConfig', NULL, 'PageClassConfig::create_html_by_template', '根据模板创建html', '根据模板创建html,用到了jinja2；循环渲染出列表数据', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-13 14:12:38', '2023-06-13 15:15:41', 1, '丁俊', '2023-07-07 10:36:14', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (101, 'PageClassConfig', NULL, 'PageClassConfig::create_html_and_js', '创建html静态页面和js', '创建html静态页面和js', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-13 17:17:39', NULL, 1, '丁俊', '2023-07-07 10:36:11', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (102, 'PageClassConfig', NULL, 'PageClassConfig::create_vue_file', '创建vue文件', '1', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-14 08:56:46', '2023-06-14 08:57:32', 1, '丁俊', '2023-07-07 10:36:08', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (103, 'PageClassConfig', NULL, 'PageClassConfig::create_vue_Tabs', '生成VUE', '1', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-14 14:28:20', '2023-06-14 14:28:56', 0, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (104, 'PageClassConfig', NULL, 'PageClassConfig::create_vue_page', '生成vue页面', '组件模板形式生成\n吴张洁提供的方案', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\PageClassConfig.py', '2023-06-14 15:44:10', '2023-06-14 15:49:20', 0, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (105, 'InterfaceFunction', NULL, 'InterfaceFunction::aa', '测试函数', '1', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\InterfaceFunction.py', '2023-06-14 16:27:54', '2023-06-14 16:28:11', 0, '', NULL, '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (106, 'CreatePage', NULL, 'CreatePage::create_temp_vue', '生成临时VUE文件', '1', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\CreatePage.py', '2023-06-16 14:40:46', '2023-06-19 09:12:26', 1, '丁俊', '2023-06-19 10:57:50', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (107, 'CreatePage', NULL, 'CreatePage::create_tabs_menu_vue', '创建标签菜单vue文件', '演示函数：根据模板文件创建tabs菜单文件\n说明：这个接口函数是针对某个页面A定制的菜单生成函数', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\CreatePage.py', '2023-06-19 10:41:49', '2023-06-19 17:48:08', 1, '丁俊', '2023-07-07 10:35:52', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (108, 'CreatePage', NULL, 'CreatePage::create_select_area_vue', '创建搜索区vue文件', '演示函数：根据模板文件创建搜索区文件\n说明：这个接口函数是针对某个页面A定制的搜索区生成函数', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\CreatePage.py', '2023-06-19 10:46:05', '2023-06-19 17:48:04', 1, '丁俊', '2023-07-07 10:35:57', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (109, 'CreatePage', NULL, 'CreatePage::create_data_area_vue', '创建数据区vue文件', '演示函数：根据模板文件创建数据区文件\n说明：这个接口函数是针对某个页面A定制的数据区生成函数', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\CreatePage.py', '2023-06-19 10:47:48', '2023-06-19 17:47:59', 1, '丁俊', '2023-07-07 10:35:59', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (110, 'CreatePage', NULL, 'CreatePage::create_global_button_vue', '创建全局按钮区vue文件', '演示函数：根据模板文件创建全局按钮区文件\n说明：这个接口函数是针对某个页面A定制的全局按钮区生成函数', NULL, NULL, NULL, '丁俊', 'SVN://app\\page_function\\CreatePage.py', '2023-06-19 10:50:03', '2023-06-19 17:47:55', 1, '丁俊', '2023-07-07 10:36:01', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (111, 'PageFunction', NULL, 'PageFunction::create_vue_by_page_config', '根据页面配置生成vue页面', '根据页面配置信息，找到相关生成页面的接口函数，并组合后生成需要的vue页面', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageFunction.py', '2023-06-19 10:57:33', '2023-06-19 18:00:54', 1, '丁俊', '2023-07-07 10:35:50', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (112, 'PageFunction', NULL, 'PageFunction::compose_element', '将多个基础组件组合成一个vue组件', '将多个基础组件组合成一个vue组件，这个组件是中间模板，不是最终的输出文件', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageFunction.py', '2023-06-25 13:17:08', '2023-06-25 16:30:08', 1, '丁俊', '2023-07-07 10:35:43', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (113, 'PageDemo2', NULL, 'PageDemo2::create_demo2_page', '生成demo2页面代码', '生成demo2页面代码', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageDemo2.py', '2023-06-25 16:37:21', '2023-06-25 18:09:21', 1, '丁俊', '2023-07-07 10:46:37', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (114, 'PageDemo2', NULL, 'PageDemo2::create_demo2_page2', '生成demo2页面2代码', '生成demo2页面2代码', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageDemo2.py', '2023-06-26 14:58:19', '2023-07-06 16:10:13', 1, '丁俊', '2023-07-07 10:46:34', '倪恒', '', NULL, 0);
INSERT INTO `t_public_function` VALUES (115, 'PageDemo', NULL, 'PageDemo::create_demo_page', '创建页面demo', '生成demo页面代码', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageDemo.py', '2023-07-07 10:42:56', '2023-07-10 13:28:13', 2, '丁俊', '2023-07-07 10:44:01', NULL, '', NULL, 0);
INSERT INTO `t_public_function` VALUES (116, 'PageFunction', NULL, 'PageFunction::get_enum_options_by_name', '根据枚举参数名获取枚举选项列表', '根据枚举参数名获取对应枚举的下拉框选项内容。\n返回值中s_enum_variable_name字段目前数据库没存，先不获取，等后期添加该字段再补充。', NULL, NULL, NULL, '丁俊', 'SVN://app\\class_function\\PageFunction.py', '2023-07-07 13:40:50', '2023-07-10 13:25:57', 2, '丁俊', '2023-07-07 13:41:28', '倪恒', '', NULL, 0);

SET FOREIGN_KEY_CHECKS = 1;

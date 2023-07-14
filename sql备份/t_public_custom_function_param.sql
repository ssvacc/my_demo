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

 Date: 12/07/2023 17:19:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_custom_function_param
-- ----------------------------
DROP TABLE IF EXISTS `t_public_custom_function_param`;
CREATE TABLE `t_public_custom_function_param`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NULL DEFAULT NULL COMMENT '功能id',
  `param_id` int(11) NULL DEFAULT NULL COMMENT '参数id',
  `param_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数名',
  `param_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数说明',
  `data_type` int(2) NULL DEFAULT NULL COMMENT '数据类型',
  `type` int(1) NULL DEFAULT NULL COMMENT '1.参数,2.返回值',
  `example` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数示例',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_custom_function_param
-- ----------------------------
INSERT INTO `t_public_custom_function_param` VALUES (35, 24, 60, 'number_list', '数字类型的列表', 11, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (36, 24, 62, 'is_odd', '是否为奇数', 3, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (37, 24, 51, 'max_value', '最大值', 1, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (42, 28, 60, 'number_list', '数字类型的列表', 11, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (43, 28, 51, 'max_value', '最大值', 1, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (44, 29, 58, 'area', '地区', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (45, 29, 82, 'v_in_params', '全局查询参数', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (46, 29, 95, 'a_school_list', '学校列表', 11, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (49, 31, 30, 'age', '年龄', 1, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (50, 31, 30, 'age', '年龄', 1, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (51, 32, 74, 's_school_name', '学校名称', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (52, 32, 75, 's_location', '地址', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (53, 32, 74, 's_school_name', '学校名称', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (54, 32, 75, 's_location', '地址', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (55, 32, 76, 'welcome', '欢迎语句', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (61, 34, 74, 's_school_name', '学校名称', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (62, 34, 75, 's_location', '地址', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (63, 34, 74, 's_school_name', '学校名称', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (64, 34, 75, 's_location', '地址', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (65, 34, 76, 'welcome', '欢迎语句', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (66, 35, 74, 's_school_name', '学校名称', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (67, 35, 75, 's_location', '地址', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (68, 35, 74, 's_school_name', '学校名称', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (69, 35, 75, 's_location', '地址', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (70, 35, 76, 'welcome', '欢迎语句', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (71, 36, 75, 's_location', '地址', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (72, 36, 74, 's_school_name', '学校名称', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (73, 36, 76, 'welcome', '欢迎语句', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (74, 36, 74, 's_school_name', '学校名称', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (75, 36, 75, 's_location', '地址', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (76, 37, 83, 'a_area_list', '地区列表', 11, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (77, 37, 75, 's_location', '地址', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (78, 37, 74, 's_school_name', '学校名称', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (79, 37, 76, 'welcome', '欢迎语句', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (80, 37, 85, 'o_test_dict', '测试字典类型', 12, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (81, 37, 96, 'o_test_ddd', 'DDD', 12, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (82, 37, 95, 'a_school_list', '学校列表', 11, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (83, 38, 117, 'i_function_id', '函数id', 1, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (84, 38, 127, 'i_code_line_number', '代码行数', 1, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (85, 39, 140, 'a_develop_require_specification', '开发规范对象列表', 11, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (86, 39, 141, 's_operator', '操作人', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (87, 39, 118, 's_interface_function_name', '通用流程函数名', 4, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (88, 39, 142, 'o_interface_function_obj', '接口函数', 12, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (89, 40, 140, 'a_develop_require_specification', '开发规范对象列表', 11, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (90, 40, 130, 'i_develop_require_specification_id', '开发规范对象ID', 1, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (91, 40, 141, 's_operator', '操作人', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (92, 40, 81, 'standard_data_list', '代码规范列表', 1, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (96, 41, 30, 'age', '年龄', 1, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (97, 41, 45, 'color', '颜色', 1, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (98, 41, 54, 'base_test', '测试参数', 4, 1, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (99, 41, 95, 'a_school_list', '学校列表', 11, 2, NULL);
INSERT INTO `t_public_custom_function_param` VALUES (100, 41, 96, 'o_test_ddd', 'DDD', 12, 2, NULL);

SET FOREIGN_KEY_CHECKS = 1;

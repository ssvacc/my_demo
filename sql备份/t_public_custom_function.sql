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

 Date: 12/07/2023 17:19:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_custom_function
-- ----------------------------
DROP TABLE IF EXISTS `t_public_custom_function`;
CREATE TABLE `t_public_custom_function`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '任务名称',
  `task_desc` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '中文名',
  `task_detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '任务详情',
  `task_config_node` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '任务配置(节点)',
  `task_config_link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '任务配置(连线)',
  `task_test_result` int(1) NULL DEFAULT NULL COMMENT '0失败，1成功，2未执行',
  `scheduled_tasks` int(1) NULL DEFAULT NULL COMMENT '0无定时任务，1有定时任务',
  `status` int(1) NULL DEFAULT NULL COMMENT '0未激活，1已激活',
  `create_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_time` datetime NULL DEFAULT NULL,
  `update_time` datetime NULL DEFAULT NULL,
  `release_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '发布人',
  `release_time` datetime NULL DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公共自定义方法' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_custom_function
-- ----------------------------
INSERT INTO `t_public_custom_function` VALUES (24, 'flow_get_max_odd', '测试数据：获取最大奇偶数', '测试数据;\n数据示例number_list: 12,3,4,53,12,13,54', '', '', 2, 0, 1, '倪恒', '2023-04-11 21:08:16', NULL, '常杨', '2023-04-20 16:48:16');
INSERT INTO `t_public_custom_function` VALUES (28, 'p_tets_adda', '测试数据：aaa', '测试数据1', '', '', 2, 0, 2, '倪恒', '2023-04-20 16:35:25', '2023-05-23 10:20:31', '常杨', '2023-04-20 17:02:17');
INSERT INTO `t_public_custom_function` VALUES (29, 'p_derg', '保护眼睛', '黯淡无光突然', '', '', 2, 0, 1, '倪恒', '2023-04-23 14:26:51', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (31, 'p_Test_aDax', '传参', 'w', '', '', 2, 0, 0, '丁俊', '2023-05-05 11:03:05', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (32, 'p_school_show', '测试数据:学校函数，参数的顺序', '函数：location，static,dd\n参数：location,school_name\n返回值：welcome,school_name,location', '', '', 2, 0, 0, '丁俊', '2023-05-08 11:06:09', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (34, 'p_wda', '顺序', '函数：location，static,dd 参数：location,school_name 返回值：welcome,school_name,location', '', '', 2, 0, 0, '丁俊', '2023-05-08 14:29:33', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (35, 'p_sdgrt', '顺序1', '函数：location，dd,static 参数：location,school_name 返回值：welcome,school_name,location', '', '', 2, 0, 0, '丁俊', '2023-05-08 14:32:07', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (36, 'p_sdgrr', '顺序2', '函数：location，dd,static 参数：location,school_name 返回值：welcome,school_name,location', '', '', 2, 0, 0, '丁俊', '2023-05-08 14:49:31', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (37, 'p_f_CheckErrorCode', '复杂参数返回值', '复杂参数返回值', '', '', 2, 0, 0, '丁俊', '2023-05-10 11:02:52', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (38, 'p_get_function_code_line', '根据函数id获取函数体行数', '根据函数id获取函数体行数', '', '', 2, 0, 2, '倪恒', '2023-05-19 14:30:16', '2023-05-23 09:58:51', '丁俊', '2023-05-19 16:37:02');
INSERT INTO `t_public_custom_function` VALUES (39, 'p_awd', 'awd', 'awd', '', '', 2, 0, 0, '倪恒', '2023-05-22 14:39:02', NULL, '', NULL);
INSERT INTO `t_public_custom_function` VALUES (40, 'p_dwa11', 'dwa11', 'dwa11', '', '', 2, 0, 0, '倪恒', '2023-05-23 15:30:19', '2023-05-23 15:33:15', '', NULL);
INSERT INTO `t_public_custom_function` VALUES (41, 'p_awdgrthykui234', 'zb234', 'adwo1234', '', '', 2, 0, 0, '倪恒', '2023-05-23 15:49:12', '2023-05-24 13:09:50', '', NULL);

SET FOREIGN_KEY_CHECKS = 1;

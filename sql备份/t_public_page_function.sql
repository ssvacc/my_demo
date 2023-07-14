/*
 Navicat Premium Data Transfer

 Source Server         : hq-db1
 Source Server Type    : MySQL
 Source Server Version : 50616
 Source Host           : hequpolardb-online-wr.rwlb.rds.aliyuncs.com:3306
 Source Schema         : hq_db

 Target Server Type    : MySQL
 Target Server Version : 50616
 File Encoding         : 65001

 Date: 13/07/2023 11:14:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_page_function
-- ----------------------------
DROP TABLE IF EXISTS `t_public_page_function`;
CREATE TABLE `t_public_page_function`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `page_name_en` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '页面英文名',
  `page_name_cn` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '页面中文名',
  `function_name_en` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '函数英文名',
  `function_name_cn` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '函数中文名',
  `default_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '默认内容',
  `function_type` tinyint(2) NOT NULL DEFAULT 1 COMMENT '函数类型(1.页面配置函数，2.页面样式函数)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 203 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_page_function
-- ----------------------------
INSERT INTO `t_public_page_function` VALUES (193, 'P_demo01', '页面测试01', 'P_demo01::menu', '页面测试01::菜单区', '', 1);
INSERT INTO `t_public_page_function` VALUES (194, 'P_demo01', '页面测试01', 'P_demo01::search', '页面测试01::搜索区', '', 1);
INSERT INTO `t_public_page_function` VALUES (195, 'P_demo01', '页面测试01', 'P_demo01::button', '页面测试01::按钮区', '', 1);
INSERT INTO `t_public_page_function` VALUES (196, 'P_demo01', '页面测试01', 'P_demo01::data', '页面测试01::数据区', '', 1);
INSERT INTO `t_public_page_function` VALUES (197, 'P_demo01', '页面测试01', 'P_demo01::style', '页面测试01::样式区', '', 1);
INSERT INTO `t_public_page_function` VALUES (198, 'P_demo02', '页面测试02', 'P_demo02::menu', '页面测试02::菜单区', '', 1);
INSERT INTO `t_public_page_function` VALUES (199, 'P_demo02', '页面测试02', 'P_demo02::search', '页面测试02::搜索区', '', 1);
INSERT INTO `t_public_page_function` VALUES (200, 'P_demo02', '页面测试02', 'P_demo02::button', '页面测试02::按钮区', '', 1);
INSERT INTO `t_public_page_function` VALUES (201, 'P_demo02', '页面测试02', 'P_demo02::data', '页面测试02::数据区', '', 1);
INSERT INTO `t_public_page_function` VALUES (202, 'P_demo02', '页面测试02', 'P_demo02::style', '页面测试02::样式区', '', 1);

SET FOREIGN_KEY_CHECKS = 1;

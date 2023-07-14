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

 Date: 12/07/2023 17:19:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_class
-- ----------------------------
DROP TABLE IF EXISTS `t_public_class`;
CREATE TABLE `t_public_class`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类名（英文）',
  `class_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类名（中文）',
  `class_detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类描述',
  `create_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_class
-- ----------------------------
INSERT INTO `t_public_class` VALUES (1, 'SKU', 'SKU', 'SKU', '倪恒', '2023-05-04 14:31:25');
INSERT INTO `t_public_class` VALUES (2, 'FNSKU', 'FNSKU', 'FNSKU', '倪恒', '2023-05-04 14:31:25');
INSERT INTO `t_public_class` VALUES (3, 'DevelopRequireSpecification', 'DevelopRequireSpecification', 'DevelopRequireSpecification', '倪恒', '2023-05-04 14:31:25');
INSERT INTO `t_public_class` VALUES (4, 'OrderAmazon', 'OrderAmazon', 'OrderAmazon', '倪恒', '2023-05-04 14:31:25');
INSERT INTO `t_public_class` VALUES (5, 'ShopManage', 'ShopManage', 'ShopManage', '倪恒', '2023-05-04 14:31:25');
INSERT INTO `t_public_class` VALUES (9, 'School', '学校', '测试数据：学校', '丁俊', '2023-05-08 10:39:19');
INSERT INTO `t_public_class` VALUES (10, 'FLOW', '流程', '通用流程相关操作', '丁俊', '2023-05-11 09:10:47');
INSERT INTO `t_public_class` VALUES (11, 'InterfaceFunction', '接口函数', '接口函数相关', '丁俊', '2023-05-16 15:30:57');
INSERT INTO `t_public_class` VALUES (12, 'TestClass', '测试数据：1', '测试数据：1', '倪恒', '2023-05-24 14:23:22');
INSERT INTO `t_public_class` VALUES (13, 'PageClassConfig', '类管理页面', '类管理页面', '倪恒', '2023-06-12 10:30:13');
INSERT INTO `t_public_class` VALUES (14, 'PageDemo2', '测试数据:demo2页面', '测试数据:页面demo2 (勿删)', '倪恒', '2023-06-12 10:30:54');
INSERT INTO `t_public_class` VALUES (15, 'CreatePage', '创建页面', '创建页面', '丁俊', '2023-06-16 14:40:00');
INSERT INTO `t_public_class` VALUES (16, 'PageFunction', '页面函数', '全局的页面配置相关处理', '丁俊', '2023-06-19 10:51:57');
INSERT INTO `t_public_class` VALUES (17, 'PageDemo', 'PageDemo页面', 'PageDemo页面（0707）', '丁俊', '2023-07-07 10:40:59');

SET FOREIGN_KEY_CHECKS = 1;

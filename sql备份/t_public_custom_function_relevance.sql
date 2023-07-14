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

 Date: 12/07/2023 17:19:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_custom_function_relevance
-- ----------------------------
DROP TABLE IF EXISTS `t_public_custom_function_relevance`;
CREATE TABLE `t_public_custom_function_relevance`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NULL DEFAULT NULL COMMENT '功能id',
  `function_id` int(11) NULL DEFAULT NULL COMMENT '函数id',
  `function_order` int(11) NULL DEFAULT NULL COMMENT '函数顺序',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 82 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公共自定义方法关系表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_custom_function_relevance
-- ----------------------------
INSERT INTO `t_public_custom_function_relevance` VALUES (38, 24, 40, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (39, 24, 41, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (44, 28, 41, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (45, 29, 65, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (46, 29, 67, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (49, 31, 77, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (50, 31, 75, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (51, 32, 61, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (52, 32, 63, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (53, 32, 79, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (57, 34, 61, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (58, 34, 63, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (59, 34, 79, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (60, 35, 61, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (61, 35, 79, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (62, 35, 63, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (63, 36, 61, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (64, 36, 79, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (65, 36, 63, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (66, 37, 63, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (67, 37, 67, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (68, 38, 94, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (69, 38, 95, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (70, 39, 92, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (71, 39, 93, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (72, 40, 92, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (73, 40, 66, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (74, 40, 91, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (78, 41, 74, 1);
INSERT INTO `t_public_custom_function_relevance` VALUES (79, 41, 89, 2);
INSERT INTO `t_public_custom_function_relevance` VALUES (80, 41, 67, 3);
INSERT INTO `t_public_custom_function_relevance` VALUES (81, 41, 63, 4);

SET FOREIGN_KEY_CHECKS = 1;

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

 Date: 13/07/2023 11:24:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_params_field
-- ----------------------------
DROP TABLE IF EXISTS `t_public_params_field`;
CREATE TABLE `t_public_params_field`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `param_id` int(11) NOT NULL COMMENT '参数id',
  `param_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参数英文名',
  `param_desc` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参数中文名',
  `field_param_id` int(11) NOT NULL COMMENT '字段参数id',
  `field_param_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '字段参数英文名',
  `field_param_desc` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '字段参数中文名',
  `field_value` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '字段值',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

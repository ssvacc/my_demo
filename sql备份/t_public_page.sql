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

 Date: 13/07/2023 11:22:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_page
-- ----------------------------
DROP TABLE IF EXISTS `t_public_page`;
CREATE TABLE `t_public_page`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `page_name_en` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '页面英文名',
  `page_name_cn` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '页面中文名',
  `page_no` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '页面编号（同页面不同节点页面编号相同）',
  `flow_id` int(11) NOT NULL DEFAULT 0 COMMENT '流程id',
  `flow_name_en` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '流程英文名',
  `flow_name_cn` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '流程中文名',
  `flow_step_no` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '流程节点号',
  `flow_step_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '流程节点名',
  `status` tinyint(2) NOT NULL DEFAULT 0 COMMENT '状态',
  `create_time` datetime NOT NULL DEFAULT '1900-01-01 00:00:00' COMMENT '创建时间',
  `create_person` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `update_time` datetime NOT NULL DEFAULT '1900-01-01 00:00:00' COMMENT '修改时间',
  `update_person` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '修改人',
  `submit_time` datetime NOT NULL DEFAULT '1900-01-01 00:00:00' COMMENT '提交时间',
  `submit_person` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '提交人',
  `examine_time` datetime NOT NULL DEFAULT '1900-01-01 00:00:00' COMMENT '审核时间',
  `examine_person` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '审核人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 97 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

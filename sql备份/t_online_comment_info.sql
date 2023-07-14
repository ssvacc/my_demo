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

 Date: 13/07/2023 10:19:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_online_comment_info
-- ----------------------------
DROP TABLE IF EXISTS `t_online_comment_info`;
CREATE TABLE `t_online_comment_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `model_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `data_id` int(11) NOT NULL DEFAULT 0,
  `comment_time` datetime NULL DEFAULT NULL,
  `comment_person` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `comment_desc` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_cn_name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 78687 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_online_comment_info
-- ----------------------------
INSERT INTO `t_online_comment_info` VALUES (78665, 'func_process_app', 't_public_custom_function', 30, '2023-04-27 09:34:22', '倪恒', '测试数据：这是评论', '参数');
INSERT INTO `t_online_comment_info` VALUES (78666, 'func_process_app', 't_public_custom_function', 30, '2023-04-27 10:04:41', '倪恒', '测试数据：新增评论', '参数');
INSERT INTO `t_online_comment_info` VALUES (78667, 'func_process_app', 't_public_custom_function', 58, '2023-04-27 10:07:43', '倪恒', '新的评论', '参数');
INSERT INTO `t_online_comment_info` VALUES (78668, 'func_process_app', 't_public_custom_function', 83, '2023-04-27 10:08:10', '倪恒', '这个不对', '参数');
INSERT INTO `t_online_comment_info` VALUES (78669, 'func_process_app', 't_public_custom_function', 105, '2023-04-27 10:10:53', '倪恒', '参数名要见名知义', '参数');
INSERT INTO `t_online_comment_info` VALUES (78670, 'func_process_app', 't_public_custom_function', 30, '2023-04-27 10:13:05', '倪恒', '评论后清空数据', '参数');
INSERT INTO `t_online_comment_info` VALUES (78671, 'func_process_app', 't_public_custom_function', 96, '2023-04-27 10:13:39', '倪恒', '复杂类型的参数要怎么样怎么样', '参数');
INSERT INTO `t_online_comment_info` VALUES (78672, 'func_process_app', 't_public_custom_function', 95, '2023-04-27 10:19:59', '丁俊', '不通过', '参数');
INSERT INTO `t_online_comment_info` VALUES (78673, 'func_process_app', 't_public_custom_function', 105, '2023-04-27 10:20:21', '丁俊', '不通过，请修改', '参数');
INSERT INTO `t_online_comment_info` VALUES (78674, 'func_process_app', 't_public_custom_function', 30, '2023-04-27 10:23:36', '丁俊', '不通过，请修改', '参数');
INSERT INTO `t_online_comment_info` VALUES (78675, 'func_process_app', 't_public_custom_function', 75, '2023-04-27 10:41:05', '倪恒', '测试数据，英文名后面不要加数字', '函数');
INSERT INTO `t_online_comment_info` VALUES (78676, 'func_process_app', 't_public_custom_function', 74, '2023-04-27 10:41:35', '倪恒', '这是函数的评论', '函数');
INSERT INTO `t_online_comment_info` VALUES (78677, 'func_process_app', 't_public_custom_function', 28, '2023-04-27 10:41:52', '倪恒', '这是流程的评论', '流程');
INSERT INTO `t_online_comment_info` VALUES (78678, 'func_process_app', 't_public_custom_function', 29, '2023-04-27 10:45:08', '倪恒', '测试数据：流程审核意见', '流程');
INSERT INTO `t_online_comment_info` VALUES (78679, 'func_process_app', 't_public_custom_function', 75, '2023-04-27 11:21:45', '倪恒', 'adf ', '函数');
INSERT INTO `t_online_comment_info` VALUES (78680, 'func_process_app', 't_public_custom_function', 75, '2023-04-27 11:24:19', '倪恒', 'asdfasdsadsdfasd', '函数');
INSERT INTO `t_online_comment_info` VALUES (78681, 'func_process_app', 't_public_custom_function', 58, '2023-04-27 14:18:13', '倪恒', 'dd', '参数');
INSERT INTO `t_online_comment_info` VALUES (78682, 'func_process_app', 't_public_custom_function', 85, '2023-05-05 10:04:27', '倪恒', '呵呵', '参数');
INSERT INTO `t_online_comment_info` VALUES (78683, 'func_process_app', 't_public_custom_function', 85, '2023-05-06 16:03:08', '丁俊', '哈哈哈', '参数');
INSERT INTO `t_online_comment_info` VALUES (78684, 'func_process_app', 't_public_custom_function', 61, '2023-05-15 17:26:40', '丁俊', '测试数据：1', '函数');
INSERT INTO `t_online_comment_info` VALUES (78685, 'func_process_app', 't_public_custom_function', 81, '2023-05-17 18:07:19', '倪恒', '测试数据，平台2', '函数');
INSERT INTO `t_online_comment_info` VALUES (78686, 'func_process_app', 't_public_custom_function', 71, '2023-05-17 18:07:28', '倪恒', '哈哈哈', '函数');

SET FOREIGN_KEY_CHECKS = 1;

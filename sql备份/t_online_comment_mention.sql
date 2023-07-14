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

 Date: 13/07/2023 10:19:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_online_comment_mention
-- ----------------------------
DROP TABLE IF EXISTS `t_online_comment_mention`;
CREATE TABLE `t_online_comment_mention`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) NOT NULL DEFAULT 0,
  `mention_person` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `mention_read` tinyint(4) NOT NULL DEFAULT 0 COMMENT '0未读1已读',
  `read_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7639 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_online_comment_mention
-- ----------------------------
INSERT INTO `t_online_comment_mention` VALUES (1, 2, '倪恒', 1, '2023-04-26 18:24:08');
INSERT INTO `t_online_comment_mention` VALUES (2, 2, '常杨', 1, '2023-04-26 15:07:32');
INSERT INTO `t_online_comment_mention` VALUES (3, 2, '盛荣凯', 0, '2023-04-26 15:07:32');
INSERT INTO `t_online_comment_mention` VALUES (74, 54, '王恒', 1, '2023-02-02 14:38:28');
INSERT INTO `t_online_comment_mention` VALUES (75, 55, '何玲玲', 1, '2023-02-02 18:19:30');
INSERT INTO `t_online_comment_mention` VALUES (7613, 78666, '盛荣凯', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7614, 78666, '常杨', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7615, 78667, '倪恒', 1, '2023-04-27 10:07:45');
INSERT INTO `t_online_comment_mention` VALUES (7616, 78667, '常杨', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7617, 78668, '邢鑫', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7618, 78669, '倪恒', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7619, 78670, '盛荣凯', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7620, 78670, '常杨', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7621, 78670, '倪恒', 1, '2023-04-27 10:13:09');
INSERT INTO `t_online_comment_mention` VALUES (7622, 78671, '倪恒', 1, '2023-05-22 14:11:54');
INSERT INTO `t_online_comment_mention` VALUES (7623, 78672, '倪恒', 1, '2023-04-27 10:21:35');
INSERT INTO `t_online_comment_mention` VALUES (7624, 78673, '倪恒', 1, '2023-05-22 14:11:57');
INSERT INTO `t_online_comment_mention` VALUES (7625, 78674, '盛荣凯', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7626, 78674, '丁俊', 1, '2023-04-27 10:23:37');
INSERT INTO `t_online_comment_mention` VALUES (7627, 78675, '倪恒', 1, '2023-04-27 10:41:10');
INSERT INTO `t_online_comment_mention` VALUES (7628, 78675, '常杨', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7629, 78676, '倪恒', 1, '2023-04-27 10:41:36');
INSERT INTO `t_online_comment_mention` VALUES (7630, 78677, '倪恒', 1, '2023-05-22 14:11:22');
INSERT INTO `t_online_comment_mention` VALUES (7631, 78678, '倪恒', 1, '2023-04-28 11:13:03');
INSERT INTO `t_online_comment_mention` VALUES (7632, 78679, '常杨', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7633, 78681, '倪恒', 1, '2023-04-27 14:18:16');
INSERT INTO `t_online_comment_mention` VALUES (7634, 78682, '倪恒', 1, '2023-05-05 10:04:32');
INSERT INTO `t_online_comment_mention` VALUES (7635, 78683, '倪恒', 1, '2023-05-06 16:03:41');
INSERT INTO `t_online_comment_mention` VALUES (7636, 78684, '倪恒', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7637, 78685, '倪恒', 0, NULL);
INSERT INTO `t_online_comment_mention` VALUES (7638, 78686, '倪恒', 1, '2023-05-18 15:18:08');

SET FOREIGN_KEY_CHECKS = 1;

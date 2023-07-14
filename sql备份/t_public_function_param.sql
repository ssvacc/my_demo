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

 Date: 12/07/2023 17:19:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_public_function_param
-- ----------------------------
DROP TABLE IF EXISTS `t_public_function_param`;
CREATE TABLE `t_public_function_param`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `function_id` int(11) NULL DEFAULT NULL COMMENT '函数id',
  `param_id` int(11) NULL DEFAULT NULL COMMENT '参数id',
  `required` int(1) NULL DEFAULT NULL COMMENT '0.非必传，1.必传',
  `type` int(1) NULL DEFAULT NULL COMMENT '0.返回码，1.参数，2.返回值',
  `code_id` int(11) NULL DEFAULT NULL COMMENT '返回码id',
  `example` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数示例',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 494 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公共方法参数' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_public_function_param
-- ----------------------------
INSERT INTO `t_public_function_param` VALUES (77, 40, 62, 0, 1, NULL, 'True');
INSERT INTO `t_public_function_param` VALUES (78, 40, 60, 0, 1, NULL, '1,2,3,4,5,4,3,2');
INSERT INTO `t_public_function_param` VALUES (79, 40, 60, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (80, 41, 60, 0, 1, NULL, '1,2,3,4,5,4,3,2');
INSERT INTO `t_public_function_param` VALUES (81, 41, 51, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (115, 40, NULL, NULL, 0, 1, NULL);
INSERT INTO `t_public_function_param` VALUES (116, 40, NULL, NULL, 0, 2, NULL);
INSERT INTO `t_public_function_param` VALUES (117, 41, NULL, NULL, 0, 1, NULL);
INSERT INTO `t_public_function_param` VALUES (118, 41, NULL, NULL, 0, 2, NULL);
INSERT INTO `t_public_function_param` VALUES (119, 411, NULL, NULL, 0, 3, NULL);
INSERT INTO `t_public_function_param` VALUES (120, 411, NULL, NULL, 0, 4, NULL);
INSERT INTO `t_public_function_param` VALUES (121, 411, NULL, NULL, 0, 6, NULL);
INSERT INTO `t_public_function_param` VALUES (122, 411, NULL, NULL, 0, 8, NULL);
INSERT INTO `t_public_function_param` VALUES (123, 411, NULL, NULL, 0, 12, NULL);
INSERT INTO `t_public_function_param` VALUES (148, 61, 74, 0, 1, NULL, '安徽大学');
INSERT INTO `t_public_function_param` VALUES (149, 61, 75, 0, 1, NULL, '合肥');
INSERT INTO `t_public_function_param` VALUES (150, 61, 76, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (151, 61, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (152, 61, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (153, 63, 75, 0, 1, NULL, '蚌埠');
INSERT INTO `t_public_function_param` VALUES (154, 63, 74, 0, 1, NULL, '安徽财经大学');
INSERT INTO `t_public_function_param` VALUES (155, 63, 76, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (156, 63, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (157, 63, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (163, 65, 82, 0, 1, NULL, 'a');
INSERT INTO `t_public_function_param` VALUES (164, 65, 81, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (165, 65, NULL, NULL, 0, 377, '');
INSERT INTO `t_public_function_param` VALUES (166, 65, NULL, NULL, 0, 361, '');
INSERT INTO `t_public_function_param` VALUES (167, 65, NULL, NULL, 0, 322, '');
INSERT INTO `t_public_function_param` VALUES (168, 66, 81, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (169, 66, NULL, NULL, 0, 377, '');
INSERT INTO `t_public_function_param` VALUES (170, 66, NULL, NULL, 0, 361, '');
INSERT INTO `t_public_function_param` VALUES (171, 66, NULL, NULL, 0, 436, '');
INSERT INTO `t_public_function_param` VALUES (172, 67, 58, 0, 1, NULL, 'a');
INSERT INTO `t_public_function_param` VALUES (173, 67, 83, 0, 1, NULL, '1,2,3');
INSERT INTO `t_public_function_param` VALUES (174, 67, 95, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (175, 67, 96, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (176, 67, 85, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (177, 67, NULL, NULL, 0, 131, '');
INSERT INTO `t_public_function_param` VALUES (178, 67, NULL, NULL, 0, 39, '');
INSERT INTO `t_public_function_param` VALUES (186, 70, 30, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (187, 70, 58, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (188, 70, 83, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (195, 72, 88, 0, 1, NULL, 'e');
INSERT INTO `t_public_function_param` VALUES (196, 72, 96, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (197, 72, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (198, 72, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (205, 74, 30, 0, 1, NULL, '1');
INSERT INTO `t_public_function_param` VALUES (206, 74, 45, 0, 1, NULL, '2');
INSERT INTO `t_public_function_param` VALUES (207, 74, 58, 0, 1, NULL, '3');
INSERT INTO `t_public_function_param` VALUES (208, 74, 54, 0, 1, NULL, '4');
INSERT INTO `t_public_function_param` VALUES (217, 74, 95, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (218, 74, 30, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (219, 75, 30, 0, 1, NULL, '23');
INSERT INTO `t_public_function_param` VALUES (220, 75, 30, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (228, 77, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (229, 77, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (230, 78, 99, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (231, 78, 106, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (232, 78, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (233, 78, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (236, 79, 75, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (237, 79, 74, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (238, 79, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (239, 79, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (240, 70, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (241, 70, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (242, 70, NULL, NULL, 0, 38, '');
INSERT INTO `t_public_function_param` VALUES (243, 70, NULL, NULL, 0, 90, '');
INSERT INTO `t_public_function_param` VALUES (244, 70, NULL, NULL, 0, 128, '');
INSERT INTO `t_public_function_param` VALUES (245, 70, NULL, NULL, 0, 56, '');
INSERT INTO `t_public_function_param` VALUES (246, 70, NULL, NULL, 0, 136, '');
INSERT INTO `t_public_function_param` VALUES (247, 70, NULL, NULL, 0, 150, '');
INSERT INTO `t_public_function_param` VALUES (252, 80, 108, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (253, 80, 85, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (254, 80, 81, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (255, 80, NULL, NULL, 0, 22, '');
INSERT INTO `t_public_function_param` VALUES (256, 80, NULL, NULL, 0, 17, '');
INSERT INTO `t_public_function_param` VALUES (257, 80, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (258, 80, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (270, 80, 58, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (271, 80, 108, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (272, 80, 106, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (273, 80, 99, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (274, 81, 118, 1, 1, NULL, 'School::show_school_location_static');
INSERT INTO `t_public_function_param` VALUES (275, 81, 119, 0, 1, NULL, '{\n\"s_location\":\"蚌埠\",\n\"s_school_name\":\"安徽财经大学\"\n}');
INSERT INTO `t_public_function_param` VALUES (276, 81, 120, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (277, 81, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (278, 81, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (279, 81, NULL, NULL, 0, 145, '');
INSERT INTO `t_public_function_param` VALUES (325, 79, 75, 0, 1, NULL, 'c');
INSERT INTO `t_public_function_param` VALUES (326, 79, 74, 0, 1, NULL, 'a');
INSERT INTO `t_public_function_param` VALUES (327, 79, 58, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (331, 82, 120, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (332, 82, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (333, 82, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (334, 82, 108, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (335, 82, 121, 1, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (336, 82, 109, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (337, 83, 117, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (338, 83, 122, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (339, 83, 109, 1, 1, NULL, 'True');
INSERT INTO `t_public_function_param` VALUES (340, 83, 75, 1, 1, NULL, '合肥');
INSERT INTO `t_public_function_param` VALUES (341, 83, 121, 0, 1, NULL, '2023-05-16');
INSERT INTO `t_public_function_param` VALUES (342, 83, 123, 0, 1, NULL, '2023-05-17 00:01:00');
INSERT INTO `t_public_function_param` VALUES (343, 83, 108, 0, 1, NULL, '1,2,3,4');
INSERT INTO `t_public_function_param` VALUES (344, 83, 119, 0, 1, NULL, '{\n\"id\":1,\n\"name\":\"哈哈\"\n}');
INSERT INTO `t_public_function_param` VALUES (345, 83, 106, 0, 1, NULL, 'AD');
INSERT INTO `t_public_function_param` VALUES (346, 83, 58, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (347, 83, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (348, 83, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (349, 88, 123, 1, 1, NULL, '2023-05-08 00:00:00');
INSERT INTO `t_public_function_param` VALUES (350, 88, 124, 1, 1, NULL, '2023-05-20 00:00:00');
INSERT INTO `t_public_function_param` VALUES (351, 88, 125, 0, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (352, 88, 129, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (353, 88, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (354, 88, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (355, 88, NULL, NULL, 0, 7, '');
INSERT INTO `t_public_function_param` VALUES (356, 88, NULL, NULL, 0, 124, '');
INSERT INTO `t_public_function_param` VALUES (357, 89, 140, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (361, 90, 139, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (362, 90, 141, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (365, 90, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (366, 90, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (367, 90, NULL, NULL, 0, 6, '');
INSERT INTO `t_public_function_param` VALUES (368, 91, 130, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (371, 92, 140, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (372, 92, 141, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (373, 92, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (374, 92, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (375, 92, NULL, NULL, 0, 4, '');
INSERT INTO `t_public_function_param` VALUES (376, 91, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (377, 91, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (378, 91, NULL, NULL, 0, 4, '');
INSERT INTO `t_public_function_param` VALUES (380, 93, 118, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (381, 93, 142, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (382, 93, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (383, 93, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (384, 93, NULL, NULL, 0, 145, '');
INSERT INTO `t_public_function_param` VALUES (386, 94, 143, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (387, 94, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (388, 94, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (389, 94, NULL, NULL, 0, 145, '');
INSERT INTO `t_public_function_param` VALUES (390, 95, 143, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (391, 95, 127, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (392, 95, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (393, 95, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (394, 96, 108, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (395, 96, 58, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (396, 96, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (397, 96, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (398, 97, 108, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (399, 97, 124, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (400, 97, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (401, 97, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (405, 74, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (406, 74, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (407, 89, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (408, 89, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (409, 94, 118, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (410, 93, 118, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (411, 98, 148, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (412, 98, 152, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (413, 98, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (414, 98, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (415, 98, NULL, NULL, 0, 4, '');
INSERT INTO `t_public_function_param` VALUES (416, 98, NULL, NULL, 0, 3, '');
INSERT INTO `t_public_function_param` VALUES (417, 99, 148, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (418, 99, 152, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (419, 99, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (420, 99, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (421, 99, NULL, NULL, 0, 3, '');
INSERT INTO `t_public_function_param` VALUES (422, 99, NULL, NULL, 0, 4, '');
INSERT INTO `t_public_function_param` VALUES (423, 100, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (424, 100, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (425, 101, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (426, 101, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (427, 102, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (428, 102, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (429, 103, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (430, 103, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (431, 104, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (432, 104, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (433, 105, 129, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (434, 105, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (435, 105, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (436, 106, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (437, 106, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (438, 107, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (439, 107, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (440, 108, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (441, 108, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (442, 109, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (443, 109, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (444, 110, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (445, 110, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (446, 111, 154, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (447, 111, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (448, 111, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (449, 110, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (450, 109, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (451, 108, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (452, 107, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (453, 111, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (460, 112, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (461, 112, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (462, 112, NULL, NULL, 0, 3, '');
INSERT INTO `t_public_function_param` VALUES (463, 112, 157, 1, 1, NULL, '[\"hq-page\",\"hq-table\"]');
INSERT INTO `t_public_function_param` VALUES (464, 112, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (465, 112, 159, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (466, 113, 154, NULL, 1, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (468, 113, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (469, 113, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (470, 113, NULL, NULL, 0, 3, '');
INSERT INTO `t_public_function_param` VALUES (471, 113, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (472, 113, 159, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (473, 114, 154, 0, 1, NULL, 'demo_page');
INSERT INTO `t_public_function_param` VALUES (474, 114, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (475, 114, 159, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (479, 114, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (480, 114, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (481, 114, NULL, NULL, 0, 3, '');
INSERT INTO `t_public_function_param` VALUES (482, 114, NULL, NULL, 0, 51, '');
INSERT INTO `t_public_function_param` VALUES (483, 115, 154, 1, 1, NULL, 'testPage');
INSERT INTO `t_public_function_param` VALUES (484, 115, 159, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (485, 115, 155, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (486, 115, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (487, 115, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (488, 116, 167, 1, 1, NULL, 'e_sample_image_type');
INSERT INTO `t_public_function_param` VALUES (489, 116, 169, NULL, 2, NULL, NULL);
INSERT INTO `t_public_function_param` VALUES (490, 116, NULL, NULL, 0, 1, '');
INSERT INTO `t_public_function_param` VALUES (491, 116, NULL, NULL, 0, 2, '');
INSERT INTO `t_public_function_param` VALUES (492, 116, NULL, NULL, 0, 4, '');
INSERT INTO `t_public_function_param` VALUES (493, 116, NULL, NULL, 0, 7, '');

SET FOREIGN_KEY_CHECKS = 1;

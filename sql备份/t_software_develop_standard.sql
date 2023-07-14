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

 Date: 12/07/2023 17:20:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_software_develop_standard
-- ----------------------------
DROP TABLE IF EXISTS `t_software_develop_standard`;
CREATE TABLE `t_software_develop_standard`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `station` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '对应岗位',
  `standard_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '规范类别',
  `standard_desc` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '规范明细',
  `example_pic` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '示例图片(多张图片之间用,隔开，最多三张图片)',
  `remarks` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '备注信息',
  `apply_person` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '提交人',
  `apply_time` datetime NULL DEFAULT NULL COMMENT '提交时间',
  `update_person` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  `update_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `index_01`(`station`) USING BTREE,
  INDEX `index_02`(`standard_type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 107 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_software_develop_standard
-- ----------------------------
INSERT INTO `t_software_develop_standard` VALUES (21, '开发人员+测试人员', '展示规范', '1、带超链接的标签文字显示蓝色，鼠标放上去要有实线下划线。\n2、带TIPS的标签，文字显示黑色，有虚线下划线，鼠标放上去弹出TIPS。', '', '已评审，描述不完整，已完善', '杨东', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (22, '开发人员', '编码规范', '1.定义函数返回值；必须有返回值的函数必须使用brick.public.ReturnEnum中的ReturnClass类创建返回对象，data属性存储返回数据，msg属性存储文字信息或异常信息。\n2.判断函数返回值；由于ReturnClass类重写了__eq__方法，所以对于调用基于规范1编写的函数所得的返回值，可以直接将返回值与ReturnClass的SUCCESS静态类进行比较，', '', '已评审，采纳', '雷涛', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (23, '开发人员+测试人员', '展示规范', '1.搜索的模板配置应该是页面级别,不是后台表或者model级的\n2.每个页面的核心对象主体应该放到最左边一列\n（top菜单栏是流程节点，左侧菜单栏是对象类型）', '', '已评审，采纳', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (24, '开发人员', 'SQL规范', '1.所有提交的配置库SQL都要在全局配置里面定义,并且定义枚举值。\n', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (25, '开发人员', '编码规范', 'action批量操作的时候增加数量的判定，防止有些运营员一次批量执行几十万条数据，导致系统消耗大，导致卡顿', '', '已评审，采纳', '褚曼瑞', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (26, '开发人员', '数据库操作规范', 'ecs上部署的应用，都要采用私网地址访问 数据库', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (27, '开发人员', '编码规范', 'varchar 字段 字符集为utf8, 排序规则为 utf8_general_ci.', '', '已评审，采纳', '严旭', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (28, '开发人员+测试人员', '展示规范', '按钮点击事件，要做防止重复点击触发的校验', '', '已评审，采纳', '王恒', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (29, '开发人员', '命名规范', '变量不再重复赋值，变量命名以返回赋值类型结尾， 如字典赋值，\'sku_list\', \'sku_dict\'\n模块名写法: module_name ;\n包名写法: package_name ;\n类名: ClsName ;\n方法名: method_name ;\n异常名: ExceptionName ;\n函数名: fun_name ;\n全局常量名: GLOBAL_CONSTANT_NAME ;\n局部常量名: LOCAL_CONSTANT_NAME ;\n全局变量名: global_v_name ;\n实例名: instance_v_name ;\n函数参数名: 入参 v_in_name, 出参 v_out_name;\n局部变量名: v_name .\n函数名,变量名和文件名应该是描述性的,尽量避免缩写,\n特别要避免使用非项目人员不清楚难以理解的缩写,\n不要通过删除单词中的字母来进行缩写. \n始终使用 .py 作为文件后缀名,不要用破折号.\"', '', '已评审，与已有规范合并采纳', '刘杨坡', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (30, '开发人员+测试人员', '展示规范', '标签和内容指向要一致', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (31, '开发人员', '日志规范', '不要把整个函数 try catch，只捕获有意义，能显示处理的异常，不要隐藏问题，要message出来', '', '已评审，采纳', '严旭', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (32, '开发人员', 'SQL规范', '不允许select *. ，  insert 必须指定字段。', '', '已评审，采纳', '严旭', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (33, '开发人员', '数据库操作规范', '测试表要联系严旭 及时删除，测试数据要及时清理', '', '已评审，采纳', '王俊昌', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (34, '开发人员', '上线规范', '测试人员没有测试通过不准上线,这里的测试通过是需求/BUG单流程走完,不是口头', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (35, '开发人员', '大数据操作规范', '程序涉及大数据操作，需提前将sql发给常杨/丁俊,评估后才可上线', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (36, '开发人员', '大数据操作规范', '大数据查询、更新、删除（大数据定义：10000+）操作避开上班时间；普通查询，使用limit；DML/DDL在SQL面板执行', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (37, '开发人员', '编码规范', '代码不允许使用中文作为变量名，判断逻辑', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (38, '开发人员', '编码规范', '代码中避免出现：循环中调用方法/数据库', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (39, '开发人员', '编码规范', '代码中不能出现魔鬼数字，流程类节点枚举值需在实现类中定义；\n各动作需在实现类中定义', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (40, '开发人员', '编码规范', '代码中测试数据要清除，Print输出要删除', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (41, '开发人员', 'SQL规范', '代码中禁止出现数据库建表，表字段的增删改SQL，如有需要 请联系严旭统一维护 提供接口。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (42, '开发人员', '编码规范', '当代码过长时，最后不要用反斜杠连接行，可以用圆括号来包含；例如：a=1+\\2      可以用：a=(1+2)', '', '已评审，采纳', '徐阳', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (43, '开发人员', '数据容错机制', '对待数据准确性一定暴露错误尽量修正，非精确数据类错误才有可能采用容错思路。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (44, '开发人员', '上线规范', '对于某些影响功能模块范围较大的需求，开发工作完成后，在群里通知此功能会影响的模块与页面，防止遗漏', '', '已评审，采纳', '蔡杨林', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (45, '开发人员', '权限设置规范', '对于权限影响范围比较大的(多人的) 要求先发通知 2.要有明确的范围才能执行', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (46, '开发人员', '编码规范', '函数体不能超过50行', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (47, '开发人员', '数据库操作规范', '客户端连接online的mysql数据库请采用只读用户 ： hq_db_read_only；普源数据库只读：fancyqube', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (48, '开发人员', '数据库操作规范', '链接数据库采用django链接', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (49, '开发人员', '上线规范', '每次系统升级时，开发验证无问题后 则发需求单号至钉钉群、bug单无问题则发群里告知无问题   ', '', '已评审，采纳', '徐国锋', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (50, '开发人员', '编码规范', '每个函数都要判断返回码，所有函数必须有返回码', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (51, '开发人员', '编码规范', '每个文件代码不超过5000行', '', '已评审，采纳', '邢鑫', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (52, '开发人员+测试人员', '编码规范', '区间搜索校验，截止数值必须大于起始数值', '', '已评审，采纳', '夏素萍', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (53, '开发人员', '数据库操作规范', '取一条，用fetchone;取多条用fetchmany 循环处理;我们目前mysql性能;size =5000 较好；', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (54, '开发人员', '全局函数规范', '全局函数，任何页面调用，都是统一的入参和统一的出参；请修改全局函数的时候，遵守这个规则：\n确定默认值 0 和无的区别，去除默认值 空或者nul；0：数量统计，没查到表示0；其它值，没有查到默认为 无。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (55, '开发人员+测试人员', '编码规范', '任何页面 点击商品SKU跳转《商品总信息库》，能用hint的绝不用弹窗，能直接展示的绝不弹窗，能用红字提醒的绝不弹窗', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (56, '开发人员', '日志规范', '日志三要素：人、操作时间、事项。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (57, '开发人员+测试人员', '展示规范', '筛选条件的选项<6个必须平铺，否则用下拉框', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (58, '开发人员', '定时任务规范', '上班时间不要跑耗时的定时任务', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (59, '开发人员+测试人员', '展示规范', '少用NULL，数字含义要唯一，最大值用999,999,\n最小值用-999,999,', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (60, '开发人员', '数据库操作规范', '使用阿里云设备访问数据库，使用数据内网链接', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (61, '开发人员+测试人员', '展示规范', '数量要格式化，页面数量千分位逗号', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (62, '开发人员', '展示规范', '所有的输入条件和查询条件都要前后trim和去TAB符', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (63, '开发人员', '编码规范', '所有函数都要按照规范定义错误码并在brick.public.ReturnEnum文件中定义。\n', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (64, '开发人员+测试人员', '编码规范', '所有软件功能的名称严谨规范，菜单名称、页面名称和URL的英文说明保持一致，URL命名也必须跟中文密切相关。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (65, '开发人员+测试人员', '展示规范', '所有涉及平台的订单时间，必须使用UTC时间作为核心时间，不允许用中国时间或平台默认美西时间（美东时间）', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (66, '开发人员+测试人员', '审核跳转规范', '所有审核或者提交数据环节，处理后都要提示结果成功或失败', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (67, '开发人员', '数据库操作规范', '所有新建表和新增字段，需增加注释，若是枚举值，需一一注释', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (68, '开发人员+测试人员', '权限设置规范', '所有新页面，要配置并验证相关人员的页面权限', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (69, '开发人员+测试人员', '展示规范', '所有新页面关于员工的下拉框不能出现离职员工', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (70, '开发人员/测试人员', '展示规范', '所有新页面要增加页面功能说明，维护人 且支持修改，并且要展示历史需求单，功能更新日期。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (71, '开发人员', '编码规范', '所有新增代码不允许直接使用 \"import *\"，必须规范使用\"import 模块名\"，以防覆盖他人，且不便于排查问题。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (72, '开发人员+测试人员', '数字校验', '所有新增页面 数值输入超过阈值或者低于阈值需要提示时，除了页面红字提示，还必须要有弹出确认环节。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (73, '开发人员+测试人员', '上传下载规范', '所有页面涉及到导入导出下载文件的请用离线方式，\n前台触发消息后台处理，最后给OSS URL 下载，\n如果是上传请先上传到OSS然后后台处理 OSS URL再处理', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (74, '开发人员+测试人员', '展示规范', '所有页面下拉框选项都需要进行正向排序，并且支持搜索。并保持选项为最新的有效选项 (特殊情况除外)。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (75, '开发人员', '编码规范', '索引名， 普源索引， idx_表名_字段名，唯一索引，un_表名_字段名, 一律使用小写格式。\n注意冗余索引：冗余索引示例：index(a,b,c)、index(a,b)、index(a)。', '', '已评审，采纳', '严旭', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (76, '开发人员', '编码规范', '提供的接口方法  传递接收的参数  须做校验 ', '', '已评审，采纳', '王志平', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (77, '开发人员+测试人员', '上线规范', '提交SVN代码必须有单号和描述，提交时有备注。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (78, '开发人员', '上线规范', '提交代码时不要有代码遗漏，不要覆盖别人的代码。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (79, '开发人员+测试人员', '设计规范', '通用处理流程所有新的流程配置都要在页面上方展示简单的节点间流转的状态图', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (80, '开发人员', '编码规范', '写函数(Python和Mysql脚本)，存储过程时:\n1.功能描述简要概括\n2.作者\n3.开发时间\n4.更新内容(时间，人，更新说明)', '', '.', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (81, '开发人员', 'SQL规范', '新建表时必须要有数据创建时间和数据更新时间，创建时间默认是当前时间，数据更新时间默认是当前时间可随数据更新而自动更新', '', '已评审，采纳', '王恒', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (82, '开发人员+测试人员', '设计规范', '新需求首次上线要在Processon上面有页面设计图', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (83, '开发人员+测试人员', '上传下载规范', '新增界面文件上传需要校验字段的必填性、字符类型、同一文件内重复数据、单条/多条，数据行数上限，文件大小上限，文件重复上传、文件格式、空文件', '', '已评审，采纳', '李萌萌', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (84, '开发人员+测试人员', '展示规范', '新增页面 所有必填项需要有必填标志以及必填校验，输入框要有灰色的提示', '', '已评审，与已有规范合并采纳', '李萌萌', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (85, '开发人员+测试人员', '展示规范', '新增页面不需要新增数据和删除时，需隐藏新增按钮和删除，防止误点', '', '已评审，采纳', '李明阳', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (86, '开发人员', '大数据操作规范', '修改表索引、主键、字段类型、id是否自增、增加字段等操作，交由专人处理，不能私自更改。', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (87, '开发人员+测试人员', '展示规范', '需要展示百分比的要用百分比显示，如 0.1234应该写成12.34%\n如果一整栏都是数字，标题加上(%),表格里面写成12.34', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (88, '开发人员+测试人员', 'SQL规范', '严禁取值普源“库存金额”=“库存数量”*“平均单价”，只允许取值普源”商品成本价”“商品成本金额”字段。在online系统中只允许出现“商品成本价库存金额”和“商品采购价库存金额”，默认online系统库存金额是“商品成本价库存金额”.', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (89, '开发人员', '展示规范', '页面排版不要左右拖动', '', '已评审，采纳', '何玲玲', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (90, '开发人员+测试人员', '展示规范', '页面筛选条件不能超出详情页面字段,要全字匹配', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (91, '开发人员+测试人员', '展示规范', '一、默认规则：\n1.搜索值不区分大小写 2.后通配符搜索；\n二、标题类、名称类：\n采用前后通配符模糊搜索；\n三、店铺账号、人员名称、类型类：\n采用下拉输入自动匹配选择项', '', ' ', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (92, '开发人员+测试人员', '展示规范', '引用现有名词解释,不得自己编造和已经存在的名词解释一样含义的字段,名词或者标签', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (93, '开发人员+测试人员', '编码规范', '有全局函数的必须要用全局函数(包括全局下拉框,全局SQL),不允许另起炉灶', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (94, '开发人员', '上线规范', '原计划升级上线的功能,由于人为疏忽导致未按时上线', 'https://fancyqube-download.oss-cn-shanghai.aliyuncs.com/software_develop_standard/standard_209.png', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (95, '开发人员', '编码规范', '在开发过程中，数据涉及换表，删除，应当在对应的action添加二次确认，避免业务同事因误操作导致数据被删除及流转', '', '已评审，采纳', '蔡之其', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (96, '开发人员', '数据库操作规范', '正式数据库电脑客户端连接使用只读用户', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (97, '开发人员', '数据库操作规范', '字段类型int型用小不用大，能用int型，不用varchar，减少使用text', '', '', '', '2023-04-06 16:11:32', '李萌萌', '2023-04-06 16:11:32');
INSERT INTO `t_software_develop_standard` VALUES (106, '2', '编码规范', 'addafaf', 'https://fancyqube-download.oss-cn-shanghai.aliyuncs.com/software_develop_standard/standard_209.png', '', '盛荣凯', '2023-04-10 11:14:30', '盛荣凯', '2023-04-10 11:14:30');

SET FOREIGN_KEY_CHECKS = 1;

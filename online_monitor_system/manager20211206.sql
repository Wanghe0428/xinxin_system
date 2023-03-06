/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : 1231

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 10/02/2022 10:08:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 109 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add sys log', 7, 'add_syslog');
INSERT INTO `auth_permission` VALUES (26, 'Can change sys log', 7, 'change_syslog');
INSERT INTO `auth_permission` VALUES (27, 'Can delete sys log', 7, 'delete_syslog');
INSERT INTO `auth_permission` VALUES (28, 'Can view sys log', 7, 'view_syslog');
INSERT INTO `auth_permission` VALUES (29, 'Can add sys menu', 8, 'add_sysmenu');
INSERT INTO `auth_permission` VALUES (30, 'Can change sys menu', 8, 'change_sysmenu');
INSERT INTO `auth_permission` VALUES (31, 'Can delete sys menu', 8, 'delete_sysmenu');
INSERT INTO `auth_permission` VALUES (32, 'Can view sys menu', 8, 'view_sysmenu');
INSERT INTO `auth_permission` VALUES (33, 'Can add sys org', 9, 'add_sysorg');
INSERT INTO `auth_permission` VALUES (34, 'Can change sys org', 9, 'change_sysorg');
INSERT INTO `auth_permission` VALUES (35, 'Can delete sys org', 9, 'delete_sysorg');
INSERT INTO `auth_permission` VALUES (36, 'Can view sys org', 9, 'view_sysorg');
INSERT INTO `auth_permission` VALUES (37, 'Can add sys role', 10, 'add_sysrole');
INSERT INTO `auth_permission` VALUES (38, 'Can change sys role', 10, 'change_sysrole');
INSERT INTO `auth_permission` VALUES (39, 'Can delete sys role', 10, 'delete_sysrole');
INSERT INTO `auth_permission` VALUES (40, 'Can view sys role', 10, 'view_sysrole');
INSERT INTO `auth_permission` VALUES (41, 'Can add sys role menu', 11, 'add_sysrolemenu');
INSERT INTO `auth_permission` VALUES (42, 'Can change sys role menu', 11, 'change_sysrolemenu');
INSERT INTO `auth_permission` VALUES (43, 'Can delete sys role menu', 11, 'delete_sysrolemenu');
INSERT INTO `auth_permission` VALUES (44, 'Can view sys role menu', 11, 'view_sysrolemenu');
INSERT INTO `auth_permission` VALUES (45, 'Can add sys user', 12, 'add_sysuser');
INSERT INTO `auth_permission` VALUES (46, 'Can change sys user', 12, 'change_sysuser');
INSERT INTO `auth_permission` VALUES (47, 'Can delete sys user', 12, 'delete_sysuser');
INSERT INTO `auth_permission` VALUES (48, 'Can view sys user', 12, 'view_sysuser');
INSERT INTO `auth_permission` VALUES (49, 'Can add sys user org', 13, 'add_sysuserorg');
INSERT INTO `auth_permission` VALUES (50, 'Can change sys user org', 13, 'change_sysuserorg');
INSERT INTO `auth_permission` VALUES (51, 'Can delete sys user org', 13, 'delete_sysuserorg');
INSERT INTO `auth_permission` VALUES (52, 'Can view sys user org', 13, 'view_sysuserorg');
INSERT INTO `auth_permission` VALUES (53, 'Can add sys user role', 14, 'add_sysuserrole');
INSERT INTO `auth_permission` VALUES (54, 'Can change sys user role', 14, 'change_sysuserrole');
INSERT INTO `auth_permission` VALUES (55, 'Can delete sys user role', 14, 'delete_sysuserrole');
INSERT INTO `auth_permission` VALUES (56, 'Can view sys user role', 14, 'view_sysuserrole');
INSERT INTO `auth_permission` VALUES (57, 'Can add auth group', 15, 'add_authgroup');
INSERT INTO `auth_permission` VALUES (58, 'Can change auth group', 15, 'change_authgroup');
INSERT INTO `auth_permission` VALUES (59, 'Can delete auth group', 15, 'delete_authgroup');
INSERT INTO `auth_permission` VALUES (60, 'Can view auth group', 15, 'view_authgroup');
INSERT INTO `auth_permission` VALUES (61, 'Can add auth group permissions', 16, 'add_authgrouppermissions');
INSERT INTO `auth_permission` VALUES (62, 'Can change auth group permissions', 16, 'change_authgrouppermissions');
INSERT INTO `auth_permission` VALUES (63, 'Can delete auth group permissions', 16, 'delete_authgrouppermissions');
INSERT INTO `auth_permission` VALUES (64, 'Can view auth group permissions', 16, 'view_authgrouppermissions');
INSERT INTO `auth_permission` VALUES (65, 'Can add auth permission', 17, 'add_authpermission');
INSERT INTO `auth_permission` VALUES (66, 'Can change auth permission', 17, 'change_authpermission');
INSERT INTO `auth_permission` VALUES (67, 'Can delete auth permission', 17, 'delete_authpermission');
INSERT INTO `auth_permission` VALUES (68, 'Can view auth permission', 17, 'view_authpermission');
INSERT INTO `auth_permission` VALUES (69, 'Can add auth user', 18, 'add_authuser');
INSERT INTO `auth_permission` VALUES (70, 'Can change auth user', 18, 'change_authuser');
INSERT INTO `auth_permission` VALUES (71, 'Can delete auth user', 18, 'delete_authuser');
INSERT INTO `auth_permission` VALUES (72, 'Can view auth user', 18, 'view_authuser');
INSERT INTO `auth_permission` VALUES (73, 'Can add auth user groups', 19, 'add_authusergroups');
INSERT INTO `auth_permission` VALUES (74, 'Can change auth user groups', 19, 'change_authusergroups');
INSERT INTO `auth_permission` VALUES (75, 'Can delete auth user groups', 19, 'delete_authusergroups');
INSERT INTO `auth_permission` VALUES (76, 'Can view auth user groups', 19, 'view_authusergroups');
INSERT INTO `auth_permission` VALUES (77, 'Can add auth user user permissions', 20, 'add_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES (78, 'Can change auth user user permissions', 20, 'change_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES (79, 'Can delete auth user user permissions', 20, 'delete_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES (80, 'Can view auth user user permissions', 20, 'view_authuseruserpermissions');
INSERT INTO `auth_permission` VALUES (81, 'Can add django admin log', 21, 'add_djangoadminlog');
INSERT INTO `auth_permission` VALUES (82, 'Can change django admin log', 21, 'change_djangoadminlog');
INSERT INTO `auth_permission` VALUES (83, 'Can delete django admin log', 21, 'delete_djangoadminlog');
INSERT INTO `auth_permission` VALUES (84, 'Can view django admin log', 21, 'view_djangoadminlog');
INSERT INTO `auth_permission` VALUES (85, 'Can add django content type', 22, 'add_djangocontenttype');
INSERT INTO `auth_permission` VALUES (86, 'Can change django content type', 22, 'change_djangocontenttype');
INSERT INTO `auth_permission` VALUES (87, 'Can delete django content type', 22, 'delete_djangocontenttype');
INSERT INTO `auth_permission` VALUES (88, 'Can view django content type', 22, 'view_djangocontenttype');
INSERT INTO `auth_permission` VALUES (89, 'Can add django migrations', 23, 'add_djangomigrations');
INSERT INTO `auth_permission` VALUES (90, 'Can change django migrations', 23, 'change_djangomigrations');
INSERT INTO `auth_permission` VALUES (91, 'Can delete django migrations', 23, 'delete_djangomigrations');
INSERT INTO `auth_permission` VALUES (92, 'Can view django migrations', 23, 'view_djangomigrations');
INSERT INTO `auth_permission` VALUES (93, 'Can add django session', 24, 'add_djangosession');
INSERT INTO `auth_permission` VALUES (94, 'Can change django session', 24, 'change_djangosession');
INSERT INTO `auth_permission` VALUES (95, 'Can delete django session', 24, 'delete_djangosession');
INSERT INTO `auth_permission` VALUES (96, 'Can view django session', 24, 'view_djangosession');
INSERT INTO `auth_permission` VALUES (97, 'Can add sys image setting', 25, 'add_sysimagesetting');
INSERT INTO `auth_permission` VALUES (98, 'Can change sys image setting', 25, 'change_sysimagesetting');
INSERT INTO `auth_permission` VALUES (99, 'Can delete sys image setting', 25, 'delete_sysimagesetting');
INSERT INTO `auth_permission` VALUES (100, 'Can view sys image setting', 25, 'view_sysimagesetting');
INSERT INTO `auth_permission` VALUES (101, 'Can add sys grant', 26, 'add_sysgrant');
INSERT INTO `auth_permission` VALUES (102, 'Can change sys grant', 26, 'change_sysgrant');
INSERT INTO `auth_permission` VALUES (103, 'Can delete sys grant', 26, 'delete_sysgrant');
INSERT INTO `auth_permission` VALUES (104, 'Can view sys grant', 26, 'view_sysgrant');
INSERT INTO `auth_permission` VALUES (105, 'Can add sys user grant', 27, 'add_sysusergrant');
INSERT INTO `auth_permission` VALUES (106, 'Can change sys user grant', 27, 'change_sysusergrant');
INSERT INTO `auth_permission` VALUES (107, 'Can delete sys user grant', 27, 'delete_sysusergrant');
INSERT INTO `auth_permission` VALUES (108, 'Can view sys user grant', 27, 'view_sysusergrant');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (15, 'app', 'authgroup');
INSERT INTO `django_content_type` VALUES (16, 'app', 'authgrouppermissions');
INSERT INTO `django_content_type` VALUES (17, 'app', 'authpermission');
INSERT INTO `django_content_type` VALUES (18, 'app', 'authuser');
INSERT INTO `django_content_type` VALUES (19, 'app', 'authusergroups');
INSERT INTO `django_content_type` VALUES (20, 'app', 'authuseruserpermissions');
INSERT INTO `django_content_type` VALUES (21, 'app', 'djangoadminlog');
INSERT INTO `django_content_type` VALUES (22, 'app', 'djangocontenttype');
INSERT INTO `django_content_type` VALUES (23, 'app', 'djangomigrations');
INSERT INTO `django_content_type` VALUES (24, 'app', 'djangosession');
INSERT INTO `django_content_type` VALUES (26, 'app', 'sysgrant');
INSERT INTO `django_content_type` VALUES (25, 'app', 'sysimagesetting');
INSERT INTO `django_content_type` VALUES (7, 'app', 'syslog');
INSERT INTO `django_content_type` VALUES (8, 'app', 'sysmenu');
INSERT INTO `django_content_type` VALUES (9, 'app', 'sysorg');
INSERT INTO `django_content_type` VALUES (10, 'app', 'sysrole');
INSERT INTO `django_content_type` VALUES (11, 'app', 'sysrolemenu');
INSERT INTO `django_content_type` VALUES (12, 'app', 'sysuser');
INSERT INTO `django_content_type` VALUES (27, 'app', 'sysusergrant');
INSERT INTO `django_content_type` VALUES (13, 'app', 'sysuserorg');
INSERT INTO `django_content_type` VALUES (14, 'app', 'sysuserrole');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-01-10 10:26:03.254654');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2020-01-10 10:26:04.775741');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2020-01-10 10:26:10.862089');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-01-10 10:26:12.638191');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-01-10 10:26:12.678193');
INSERT INTO `django_migrations` VALUES (6, 'app', '0001_initial', '2020-01-10 10:26:12.733196');
INSERT INTO `django_migrations` VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2020-01-10 10:26:13.890262');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2020-01-10 10:26:15.008326');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2020-01-10 10:26:15.853375');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2020-01-10 10:26:15.910378');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2020-01-10 10:26:16.822430');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2020-01-10 10:26:16.880433');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2020-01-10 10:26:16.938437');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2020-01-10 10:26:17.971496');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2020-01-10 10:26:18.666535');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2020-01-10 10:26:19.469581');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2020-01-10 10:26:19.522584');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2020-01-10 10:26:19.785599');
INSERT INTO `django_migrations` VALUES (19, 'app', '0002_sysimagesetting', '2020-07-21 11:30:13.190826');
INSERT INTO `django_migrations` VALUES (20, 'app', '0003_sysgrant_sysusergrant', '2021-01-05 10:44:23.230886');
INSERT INTO `django_migrations` VALUES (21, 'auth', '0012_alter_user_first_name_max_length', '2021-05-29 15:48:01.372937');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('fa1ilx1jx6itu69kkx20ncc9f58vjb1u', '.eJyFj9sKwjAMht-l1-LadV3cnmUwujYbkZ3oQRTx3c300gsJhCT_l5_kKWgXrVAlnCWHEidhvQ8YI0-7XEPpumxAyy5DDQPXozEH5BwD1i-0cpc_MLiRAUA_ch6s4lzJmlcqc2FoxhvOX_BXzBFDT57lQWHTOFlqDaAU2kGbSrsGJHowqnEHHA6fIiabyBW02AljsW8hBUup-Gdwvu4Tm1Ds523i89sUMp5EH_lp2tYe7zuFh2h1LeXrDcoYVcY:1nBSPc:BjELKCukpTk4A0PoektIHndohR3_8IrnBY6VheOTVi4', '2022-01-23 11:15:24.330664');
INSERT INTO `django_session` VALUES ('p6u0hgvmfqfkhfv1f3zw9jl3rwul0pjr', '.eJyFj9sKwjAMht-l1-LadV3cnmUwujYbkZ3oQRTx3c300gsJhCT_l5_kKWgXrVAlnCWHEidhvQ8YI0-7XEPpumxAyy5DDQPXozEH5BwD1i-0cpc_MLiRAUA_ch6s4lzJmlcqc2FoxhvOX_BXzBFDT57lQWHTOFlqDaAU2kGbSrsGJHowqnEHHA6fIiabyBW02AljsW8hBUup-Gdwvu4Tm1Ds523i89sUMp5EH_lp2tYe7zuFh2h1LeXrDcoYVcY:1mu4Tx:_AZa29IDTA6Pvcaqtj9ztOjyxKuLs47uzoVdxT0eyoY', '2021-12-06 12:16:01.575857');

-- ----------------------------
-- Table structure for sys_dic_from
-- ----------------------------
DROP TABLE IF EXISTS `sys_dic_from`;
CREATE TABLE `sys_dic_from`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dic_key` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `p_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dic_values` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `dic_key`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_dic_from
-- ----------------------------
INSERT INTO `sys_dic_from` VALUES ('02418196107611ec8ff21cbfc0546006', 'in', 'b88d58bf107511ecbe641cbfc0546006', '中', '2021-09-08 15:25:57.000000');
INSERT INTO `sys_dic_from` VALUES ('08741edf107611ec8c141cbfc0546006', 'low', 'b88d58bf107511ecbe641cbfc0546006', '低', '2021-09-08 15:26:07.000000');
INSERT INTO `sys_dic_from` VALUES ('1b845f094dcc11ec925f1cbfc0546006', 'ip_query', '0fbbe766eb9711eb89191cbfc0546006', 'https://www.ip.cn/ip/', '2021-11-25 16:45:57.000000');
INSERT INTO `sys_dic_from` VALUES ('23390e18f3f411eb81d51cbfc0546006', 'System', 'ff66ea03f3f311eb86e51cbfc0546006', '系统消息', '2021-08-03 08:45:45.000000');
INSERT INTO `sys_dic_from` VALUES ('2a42bf79f3f411ebab3c1cbfc0546006', 'ordinary', 'ff66ea03f3f311eb86e51cbfc0546006', '普通消息', '2021-08-03 08:45:57.000000');
INSERT INTO `sys_dic_from` VALUES ('4a8e665c4a8011ec85812cf05d231dfa', 'default_image', '0fbbe766eb9711eb89191cbfc0546006', 'avatar.jpg', '2021-11-21 12:05:40.000000');
INSERT INTO `sys_dic_from` VALUES ('5bb09bc0eb9711eb94e01cbfc0546006', 'system_name', '0fbbe766eb9711eb89191cbfc0546006', '后台管理系统', '2021-07-25 09:54:51.000000');
INSERT INTO `sys_dic_from` VALUES ('923c837903da11ecbd061cbfc0546006', 'version', '0fbbe766eb9711eb89191cbfc0546006', '1.0', '2021-08-23 14:23:03.000000');
INSERT INTO `sys_dic_from` VALUES ('af5ce913564011ecae411cbfc0546006', 'staff', '9cd04574564011ecb6f11cbfc0546006', '内部员工', '2021-12-06 11:00:36.000000');
INSERT INTO `sys_dic_from` VALUES ('bae1ba0f564011ec8b9d1cbfc0546006', 'member', '9cd04574564011ecb6f11cbfc0546006', '会员用户', '2021-12-06 11:00:55.000000');
INSERT INTO `sys_dic_from` VALUES ('e70553ed107511ecbe7f1cbfc0546006', 'high', 'b88d58bf107511ecbe641cbfc0546006', '高', '2021-09-08 15:25:11.000000');

-- ----------------------------
-- Table structure for sys_dic_main
-- ----------------------------
DROP TABLE IF EXISTS `sys_dic_main`;
CREATE TABLE `sys_dic_main`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `key` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_dic_main
-- ----------------------------
INSERT INTO `sys_dic_main` VALUES ('0fbbe766eb9711eb89191cbfc0546006', 'system', '系统配置');
INSERT INTO `sys_dic_main` VALUES ('9cd04574564011ecb6f11cbfc0546006', 'user_type', '账户类型');
INSERT INTO `sys_dic_main` VALUES ('b88d58bf107511ecbe641cbfc0546006', 'urgent', '紧急程度');
INSERT INTO `sys_dic_main` VALUES ('ff66ea03f3f311eb86e51cbfc0546006', 'message', '消息类型');

-- ----------------------------
-- Table structure for sys_feedback
-- ----------------------------
DROP TABLE IF EXISTS `sys_feedback`;
CREATE TABLE `sys_feedback`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `creat_time` datetime(0) NULL DEFAULT NULL,
  `urgent` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creat_account` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creat_username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_feedback
-- ----------------------------
INSERT INTO `sys_feedback` VALUES ('3a805eb4107d11eca3b81cbfc0546006', '2021-09-08 16:17:38', 'high', 'admin', '系统管理员', '12312', 2);
INSERT INTO `sys_feedback` VALUES ('7c66c598113b11ec94dd1cbfc0546006', '2021-09-09 14:59:32', 'centre', 'admin', '系统管理员', '系统无法提交任务', 2);
INSERT INTO `sys_feedback` VALUES ('8c3367d2113b11ec853b1cbfc0546006', '2021-09-09 14:59:59', 'low', 'admin', '系统管理员', '测试问题1', 2);
INSERT INTO `sys_feedback` VALUES ('95710318113b11ecb1951cbfc0546006', '2021-09-09 15:00:14', 'low', 'admin', '系统管理员', '测试问题2', 2);
INSERT INTO `sys_feedback` VALUES ('c93db42711e111ec9f1f1cbfc0546006', '2021-09-10 10:49:58', 'low', 'admin', '系统管理员', '1231231', 2);
INSERT INTO `sys_feedback` VALUES ('cf0192aa146511ec923e1cbfc0546006', '2021-09-13 15:40:03', 'low', 'admin', '系统管理员', '12312', 2);
INSERT INTO `sys_feedback` VALUES ('d620cc4711e211eca39c1cbfc0546006', '2021-09-10 10:57:29', 'low', 'admin', '系统管理员', 'a\'asdad', 2);
INSERT INTO `sys_feedback` VALUES ('eab6e5fe1f6811ec8d871cbfc0546006', '2021-09-27 16:00:01', 'low', 'admin', '系统管理员', '1231', 1);
INSERT INTO `sys_feedback` VALUES ('fd6a5814145911eca3c11cbfc0546006', '2021-09-13 14:15:27', 'low', 'admin', '系统管理员', '测试', 2);

-- ----------------------------
-- Table structure for sys_feedback_info
-- ----------------------------
DROP TABLE IF EXISTS `sys_feedback_info`;
CREATE TABLE `sys_feedback_info`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  `op_username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `op_account` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `content` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_feedback_info
-- ----------------------------
INSERT INTO `sys_feedback_info` VALUES ('09910a19113b11ec9efc1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:56:20', '系统管理员', 'admin', '123123');
INSERT INTO `sys_feedback_info` VALUES ('0da6290c218b11ec84801cbfc0546006', 'eab6e5fe1f6811ec8d871cbfc0546006', '2021-09-30 09:09:25', '系统管理员', 'admin', '阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大阿萨大大大');
INSERT INTO `sys_feedback_info` VALUES ('1ce163a7113911ec97881cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:42:33', '系统管理员', 'admin', '123123');
INSERT INTO `sys_feedback_info` VALUES ('1ec31ae8113911ecb0c61cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:42:36', '系统管理员', 'admin', '1231231');
INSERT INTO `sys_feedback_info` VALUES ('2111aea9113911ecbe9a1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:42:40', '系统管理员', 'admin', '1231231');
INSERT INTO `sys_feedback_info` VALUES ('23744180113911ecb9eb1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:42:44', '系统管理员', 'admin', 'aaa');
INSERT INTO `sys_feedback_info` VALUES ('25c53c14113911ec9b6e1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:42:48', '系统管理员', 'admin', 'vsdsd');
INSERT INTO `sys_feedback_info` VALUES ('2e890c1c113911ec879b1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:43:03', '系统管理员', 'admin', 'wesda');
INSERT INTO `sys_feedback_info` VALUES ('3a81c567107d11ec8ac01cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-08 16:17:38', '系统管理员', 'admin', '3131');
INSERT INTO `sys_feedback_info` VALUES ('690ca07711e111ec86c51cbfc0546006', '8c3367d2113b11ec853b1cbfc0546006', '2021-09-10 10:47:16', '系统管理员', 'admin', '1231');
INSERT INTO `sys_feedback_info` VALUES ('70a70f3e113a11ec80c01cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:52:03', '系统管理员', 'admin', '1231');
INSERT INTO `sys_feedback_info` VALUES ('73303e8f113911ec96b61cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:44:58', '系统管理员', 'admin', '1asd');
INSERT INTO `sys_feedback_info` VALUES ('7c689915113b11ec93801cbfc0546006', '7c66c598113b11ec94dd1cbfc0546006', '2021-09-09 14:59:32', '系统管理员', 'admin', '系统无法提交任务');
INSERT INTO `sys_feedback_info` VALUES ('80ea2f0d11dc11ec98b51cbfc0546006', '7c66c598113b11ec94dd1cbfc0546006', '2021-09-10 10:12:09', '钢铁侠', 'aaaa', '11');
INSERT INTO `sys_feedback_info` VALUES ('8c33b675113b11ec899c1cbfc0546006', '8c3367d2113b11ec853b1cbfc0546006', '2021-09-09 14:59:59', '系统管理员', 'admin', '测试问题1');
INSERT INTO `sys_feedback_info` VALUES ('957288a7113b11ec8a3a1cbfc0546006', '95710318113b11ecb1951cbfc0546006', '2021-09-09 15:00:14', '系统管理员', 'admin', '测试问题2');
INSERT INTO `sys_feedback_info` VALUES ('a05d2aa1113811ec914a1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:39:04', '系统管理员', 'admin', '123123');
INSERT INTO `sys_feedback_info` VALUES ('a0b27eda145d11ecbb041cbfc0546006', 'fd6a5814145911eca3c11cbfc0546006', '2021-09-13 14:41:30', '系统管理员', 'admin', '11');
INSERT INTO `sys_feedback_info` VALUES ('acaa7ab7114511ec96a11cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 16:12:28', '系统管理员', 'admin', '111');
INSERT INTO `sys_feedback_info` VALUES ('b073b36d200211ecac9b1cbfc0546006', 'eab6e5fe1f6811ec8d871cbfc0546006', '2021-09-28 10:20:46', '系统管理员', 'admin', '1231231');
INSERT INTO `sys_feedback_info` VALUES ('ba33d87a113811ec96921cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:39:48', '系统管理员', 'admin', '东西还没有修改');
INSERT INTO `sys_feedback_info` VALUES ('bd3ecbdc113a11ec8aa21cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:54:12', '系统管理员', 'admin', '123123');
INSERT INTO `sys_feedback_info` VALUES ('c54cd6d6113911ec937d1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:47:16', '系统管理员', 'admin', '手打');
INSERT INTO `sys_feedback_info` VALUES ('c93f7a5611e111ec84521cbfc0546006', 'c93db42711e111ec9f1f1cbfc0546006', '2021-09-10 10:49:58', '系统管理员', 'admin', '3132131');
INSERT INTO `sys_feedback_info` VALUES ('cdcf37fc11e111ecbd981cbfc0546006', 'c93db42711e111ec9f1f1cbfc0546006', '2021-09-10 10:50:05', '系统管理员', 'admin', '1231231');
INSERT INTO `sys_feedback_info` VALUES ('cf0192ab146511eca1bc1cbfc0546006', 'cf0192aa146511ec923e1cbfc0546006', '2021-09-13 15:40:03', '系统管理员', 'admin', '3123');
INSERT INTO `sys_feedback_info` VALUES ('d621999f11e211eca84e1cbfc0546006', 'd620cc4711e211eca39c1cbfc0546006', '2021-09-10 10:57:29', '系统管理员', 'admin', 'a大');
INSERT INTO `sys_feedback_info` VALUES ('da1d6ba611e211ec88351cbfc0546006', 'd620cc4711e211eca39c1cbfc0546006', '2021-09-10 10:57:36', '系统管理员', 'admin', '阿萨大大');
INSERT INTO `sys_feedback_info` VALUES ('e0a14df9113a11ec9daf1cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:55:11', '系统管理员', 'admin', '1231');
INSERT INTO `sys_feedback_info` VALUES ('eab873881f6811ecb6ba1cbfc0546006', 'eab6e5fe1f6811ec8d871cbfc0546006', '2021-09-27 16:00:01', '系统管理员', 'admin', '3131');
INSERT INTO `sys_feedback_info` VALUES ('f5ffa7fd11db11ecb9671cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-10 10:08:16', '钢铁侠', 'aaaa', '啊啊啊啊');
INSERT INTO `sys_feedback_info` VALUES ('f926df7d113a11ecbc231cbfc0546006', '3a805eb4107d11eca3b81cbfc0546006', '2021-09-09 14:55:52', '系统管理员', 'admin', '123123');
INSERT INTO `sys_feedback_info` VALUES ('fd6c2bb5145911ec9de31cbfc0546006', 'fd6a5814145911eca3c11cbfc0546006', '2021-09-13 14:15:27', '系统管理员', 'admin', '测试');
INSERT INTO `sys_feedback_info` VALUES ('fe69c8ae11e111eca1ba1cbfc0546006', 'c93db42711e111ec9f1f1cbfc0546006', '2021-09-10 10:51:27', '系统管理员', 'admin', '1231231');

-- ----------------------------
-- Table structure for sys_grant
-- ----------------------------
DROP TABLE IF EXISTS `sys_grant`;
CREATE TABLE `sys_grant`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `menu_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grant_code` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_grant` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_grant
-- ----------------------------
INSERT INTO `sys_grant` VALUES ('4d6651c641d111ec94891cbfc0546006', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('4d66ed1841d111ec85101cbfc0546006', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('4d67980841d111ec86921cbfc0546006', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('4e2362074dcd11ecbaaf1cbfc0546006', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('4e2424f44dcd11eca4fb1cbfc0546006', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('4e250ee74dcd11eca9951cbfc0546006', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('4e25ac814dcd11ecad521cbfc0546006', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('541c33bd51ac11ec9e541cbfc0546006', '34a98e1051ac11eca0871cbfc0546006', '角色管理', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('541d1d7251ac11ecb5c91cbfc0546006', '34a98e1051ac11eca0871cbfc0546006', '角色管理', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('541d92b751ac11ec92b31cbfc0546006', '34a98e1051ac11eca0871cbfc0546006', '角色管理', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('541e2e3851ac11ecbe8d1cbfc0546006', '34a98e1051ac11eca0871cbfc0546006', '角色管理', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('7f5b15c050bd11ebba0b3c970ed7519c', '6f396f634be011ebbdf63c970ed7519c', '采集设置', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('7f6239e250bd11ebbc863c970ed7519c', '6f396f634be011ebbdf63c970ed7519c', '采集设置', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('7f72e38650bd11eb89f63c970ed7519c', '6f396f634be011ebbdf63c970ed7519c', '采集设置', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('7f91d56850bd11eb81723c970ed7519c', '6f3e32254be011ebaa0d3c970ed7519c', '数据权限', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('7f98f98850bd11eb94a53c970ed7519c', '6f3e32254be011ebaa0d3c970ed7519c', '数据权限', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('7fa4e06850bd11ebb3c73c970ed7519c', '6f4093824be011eba0d63c970ed7519c', '菜单管理', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('7fa9a32850bd11ebabcc3c970ed7519c', '6f4093824be011eba0d63c970ed7519c', '菜单管理', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('7fac048a50bd11eb8ef63c970ed7519c', '6f4093824be011eba0d63c970ed7519c', '菜单管理', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('7fb328ac50bd11eb8d863c970ed7519c', '6f4093824be011eba0d63c970ed7519c', '菜单管理', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('7fb58a0c50bd11ebafcb3c970ed7519c', '6f4093834be011eba2493c970ed7519c', '部门管理', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('7fbf0f8c50bd11eb88213c970ed7519c', '6f4093834be011eba2493c970ed7519c', '部门管理', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('7fc3d24c50bd11eb98673c970ed7519c', '6f4093834be011eba2493c970ed7519c', '部门管理', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('7fc633ae50bd11eb93913c970ed7519c', '6f4093844be011eb80b63c970ed7519c', '用户管理', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('7fcd57cc50bd11eba3123c970ed7519c', '6f4093844be011eb80b63c970ed7519c', '用户管理', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('7fcfb92e50bd11ebb5853c970ed7519c', '6f4093844be011eb80b63c970ed7519c', '用户管理', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('7fd47bee50bd11eb8b983c970ed7519c', '6f4093844be011eb80b63c970ed7519c', '用户管理', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('8d2706f6fe5911ebbc591cbfc0546006', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('8d2754e7fe5911eba39c1cbfc0546006', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('8d277bd7fe5911eba6841cbfc0546006', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('8d27a2cbfe5911ebaaf51cbfc0546006', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', 'del', '删除数据');
INSERT INTO `sys_grant` VALUES ('dd312184eac811ebb5491cbfc0546006', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'show', '数据展示');
INSERT INTO `sys_grant` VALUES ('dd312185eac811eb924d1cbfc0546006', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'see', '查看详情');
INSERT INTO `sys_grant` VALUES ('dd312186eac811ebb6141cbfc0546006', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'edit', '编辑数据');
INSERT INTO `sys_grant` VALUES ('dd312187eac811ebab5b1cbfc0546006', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'del', '删除数据');

-- ----------------------------
-- Table structure for sys_image_setting
-- ----------------------------
DROP TABLE IF EXISTS `sys_image_setting`;
CREATE TABLE `sys_image_setting`  (
  `edition` int(1) NOT NULL COMMENT '0为临时目录，1为图片存放目录',
  `path` varchar(126) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '图片存放路径(必须以\'/\'结尾)',
  `temp_path` varchar(126) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cjcs` int(1) NULL DEFAULT NULL COMMENT '图片采集次数',
  `jgsj` int(1) NULL DEFAULT NULL COMMENT '采集多张照片时，每两张照片的间隔时间(edition为0时无效)',
  `dqsj` int(1) NULL DEFAULT NULL COMMENT '登录读取人脸数据时间',
  `sfqy` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`edition`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_image_setting
-- ----------------------------
INSERT INTO `sys_image_setting` VALUES (1, 'F:\\py_object\\manager\\face\\', 'F:\\py_object\\manager\\temp\\', 3, 3, 3, 1);

-- ----------------------------
-- Table structure for sys_information
-- ----------------------------
DROP TABLE IF EXISTS `sys_information`;
CREATE TABLE `sys_information`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `content` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` int(1) NULL DEFAULT NULL COMMENT '0:未读，1:已读',
  `type` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_information
-- ----------------------------
INSERT INTO `sys_information` VALUES ('04085b7b4a8711eca6912cf05d231dfa', 'b1e99c10337711eaa9833c970ed7519c', '2021-11-21 12:53:49《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:53:49');
INSERT INTO `sys_information` VALUES ('0c312b8a4a8711ec9a532cf05d231dfa', 'd603ef76334c11eab0e23c970ed7519c', '2021-11-21 12:54:02《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:54:02');
INSERT INTO `sys_information` VALUES ('0f013911f98511ebad401cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', '2021-08-10 10:45:44《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-08-10 10:45:44');
INSERT INTO `sys_information` VALUES ('4330dbc6063c11ecb9871cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', '2021-08-26 15:07:23《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-08-26 15:07:23');
INSERT INTO `sys_information` VALUES ('52374e8a4a8411ecaf972cf05d231dfa', 'b1e99c06337711ea9ecd3c970ed7519c', '2021-11-21 12:34:31《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:34:31');
INSERT INTO `sys_information` VALUES ('60b226af4a0e11ec89f12cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', '2021-11-20 22:30:15《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-20 22:30:15');
INSERT INTO `sys_information` VALUES ('670e07194a0e11ec8d8e2cf05d231dfa', 'b1e99c04337711eab8233c970ed7519c', '2021-11-20 22:30:26《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-20 22:30:26');
INSERT INTO `sys_information` VALUES ('6b9a835c4a7e11ecb60d2cf05d231dfa', 'b1e99c07337711ea9ad93c970ed7519c', '2021-11-21 11:52:17《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 11:52:17');
INSERT INTO `sys_information` VALUES ('70a25d8c4a7111ec8da62cf05d231dfa', 'b1e99c05337711eab6993c970ed7519c', '2021-11-21 10:19:22《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:19:22');
INSERT INTO `sys_information` VALUES ('769df7414a7e11ec9ba52cf05d231dfa', 'b1e99c08337711eaa8e03c970ed7519c', '2021-11-21 11:52:35《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 11:52:35');
INSERT INTO `sys_information` VALUES ('786cb6ebf8e411eb9d601cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', '2021-08-09 15:36:12《系统管理员》 修改了你的信息！', 1, '普通消息', '2021-08-09 15:36:12');
INSERT INTO `sys_information` VALUES ('7b42f6764a7111ec85e92cf05d231dfa', 'b1e99c06337711ea9ecd3c970ed7519c', '2021-11-21 10:19:40《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:19:40');
INSERT INTO `sys_information` VALUES ('8025205bf8d411eb93981cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', '2021-08-09 13:41:53《系统管理员》 修改了你的信息！', 1, '普通消息', '2021-08-09 13:41:53');
INSERT INTO `sys_information` VALUES ('87021b304a8411ecacc02cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', '2021-11-21 12:36:00《系统管理员》 修改了你的信息！', 1, '普通消息', '2021-11-21 12:36:00');
INSERT INTO `sys_information` VALUES ('8804fbb44a7111ec85812cf05d231dfa', 'b1e99c09337711eabfa63c970ed7519c', '2021-11-21 10:20:01《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:20:01');
INSERT INTO `sys_information` VALUES ('9090467b4a7111ec8aba2cf05d231dfa', 'b1e99c0a337711eaba783c970ed7519c', '2021-11-21 10:20:15《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:20:15');
INSERT INTO `sys_information` VALUES ('97d26a074a7111ecae0d2cf05d231dfa', 'b1e99c0b337711ea9e293c970ed7519c', '2021-11-21 10:20:28《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:20:28');
INSERT INTO `sys_information` VALUES ('a2944d494a7111eca4f82cf05d231dfa', 'b1e99c0c337711ea9b2e3c970ed7519c', '2021-11-21 10:20:46《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 10:20:46');
INSERT INTO `sys_information` VALUES ('d1c8b8c74a0111eca1ac2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', '2021-11-20 21:00:21《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-20 21:00:21');
INSERT INTO `sys_information` VALUES ('d77723594a0d11ec84892cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', '2021-11-20 22:26:25《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-20 22:26:25');
INSERT INTO `sys_information` VALUES ('e09b45724a8611eca5242cf05d231dfa', 'b1e99c0d337711eaa77e3c970ed7519c', '2021-11-21 12:52:49《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:52:49');
INSERT INTO `sys_information` VALUES ('ed4454be4a8611ecb4762cf05d231dfa', 'b1e99c0e337711ea9daf3c970ed7519c', '2021-11-21 12:53:10《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:53:10');
INSERT INTO `sys_information` VALUES ('f429f5004a8611ec9a282cf05d231dfa', 'b1e99c0e337711ea9daf3c970ed7519c', '2021-11-21 12:53:22《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:53:22');
INSERT INTO `sys_information` VALUES ('fc2accc04a8611ecaff92cf05d231dfa', 'b1e99c0f337711eab42c3c970ed7519c', '2021-11-21 12:53:35《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-21 12:53:35');
INSERT INTO `sys_information` VALUES ('fcc03d504a0d11ec961a2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', '2021-11-20 22:27:27《系统管理员》 修改了你的信息！', 0, '普通消息', '2021-11-20 22:27:27');

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `accout` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作账号',
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人姓名',
  `type` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '类型',
  `time` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '时间',
  `content` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '内容',
  `ip` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录ip',
  `address` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录地点',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_log
-- ----------------------------
INSERT INTO `sys_log` VALUES ('027bb39d51ab11ec806a1cbfc0546006', 'admin', '系统管理员', 'create', '2021-11-30 14:59:06', '系统管理员创建菜单：《日志管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('02bf037751a911ecad691cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:44:47', '系统管理员编辑菜单：《2222》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('03b9918951aa11eca6ef1cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:51:59', '系统管理员删除菜单：《4》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('0540e4db51af11ec86611cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:27:49', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('072bf2d951a711ecb5b11cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:30:36', '系统管理员编辑菜单：《12313》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('09c08e4351ae11eca3c51cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:20:47', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('0b3e6d1e51af11ec90fb1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:27:59', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('11d414b251a611ecbfa11cbfc0546006', 'admin', '系统管理员', 'create', '2021-11-30 14:23:44', '系统管理员创建菜单：《2222》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('120eb3cc51ab11ecb5bf1cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:59:32', '系统管理员编辑菜单：《日志管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('189b79e351ac11ecb0a51cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 15:06:53', '系统管理员删除菜单：《角色管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('22d21a2951ae11ecabad1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:21:29', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('2a26db824e8411ecb9901cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-26 14:43:29', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('31aff62351a211ecab8d1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 13:56:00', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('34afcb6951ac11ec99701cbfc0546006', 'admin', '系统管理员', 'create', '2021-11-30 15:07:40', '系统管理员创建菜单：《角色管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('50db1a8651aa11ec89a21cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:54:08', '系统管理员删除菜单：《日志管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('52cf0f667bf211ec8ef12cf05d231dfa', 'admin', '系统管理员', 'login', '2022-01-23 10:15:24', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('541f3ece51ac11ecba6d1cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 15:08:32', '系统管理员编辑菜单：《角色管理》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('57c7899a51ad11ecb9121cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:15:48', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('57e2d4f651a911ec97881cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:47:10', '系统管理员编辑菜单：《7》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('6c0fedcc51a211ecac1e1cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 13:57:38', '系统管理员更新角色用户：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('74956d2451a811eca4181cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:40:49', '系统管理员删除菜单：《3》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('790fbcad50b211ec9a061cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-29 09:20:00', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('84431d0350b211ec9da01cbfc0546006', 'user1', '钢铁侠', 'login', '2021-11-29 09:20:19', '钢铁侠登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('889b5d4a51ae11ec88a21cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:24:19', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('93ab0fb851af11ec8ee91cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:31:48', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('944f1dcf51ad11ec99e91cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:17:30', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('9813171851a311ec9f7e1cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:06:01', '系统管理员更新角色菜单：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('a1c6077651b011ec8f351cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:39:21', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('a3bbb26451ae11eca5cd1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:25:05', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('a8d79d1251a911eca3e71cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:49:26', '系统管理员删除菜单：《2222》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('aa938ba751b011ec90251cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:39:35', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('afb57a0b51ae11ec9cc91cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:25:25', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('b557dfda51a911ec91b81cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:49:47', '系统管理员删除菜单：《7》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('b68314ba51b011ec88ac1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:39:55', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('c8d38af551aa11ecad771cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 14:57:29', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('d14417a351ad11ec8bef1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:19:12', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('d171271c51b011ec9b5e1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:40:41', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('d1a2246b51ae11eca5891cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-30 15:26:22', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('d6ef9387564211ecb0d61cbfc0546006', 'admin', '系统管理员', 'login', '2021-12-06 11:16:01', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('dbb916f1564211ecb1ce1cbfc0546006', 'admin', '系统管理员', 'update', '2021-12-06 11:16:09', '系统管理员更新角色用户：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('e026b00b51a311eca7801cbfc0546006', 'admin', '系统管理员', 'update', '2021-11-30 14:08:02', '系统管理员更新角色用户：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('e293dc45564211ec94a01cbfc0546006', 'admin', '系统管理员', 'update', '2021-12-06 11:16:21', '系统管理员更新角色菜单：《普通用户》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('e50e112b51a511ecb9301cbfc0546006', 'admin', '系统管理员', 'create', '2021-11-30 14:22:29', '系统管理员创建菜单：《12313》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('e5671a19564211ec8ff41cbfc0546006', 'admin', '系统管理员', 'update', '2021-12-06 11:16:25', '系统管理员更新角色用户：《普通用户》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('e7f83efa564211ec9ac81cbfc0546006', 'admin', '系统管理员', 'update', '2021-12-06 11:16:30', '系统管理员更新角色菜单：《临时用户》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('ea10054350ba11ecb59d1cbfc0546006', 'admin', '系统管理员', 'login', '2021-11-29 10:20:26', '系统管理员登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('eabb9bf8564211ec8f581cbfc0546006', 'admin', '系统管理员', 'update', '2021-12-06 11:16:34', '系统管理员更新角色用户：《临时用户》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('ed413ed451ab11ec805a1cbfc0546006', 'admin', '系统管理员', 'select', '2021-11-30 15:05:40', '系统管理员查看角色：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('f4a967bd51a611ec9a4e1cbfc0546006', 'admin', '系统管理员', 'create', '2021-11-30 14:30:05', '系统管理员创建菜单：《7》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('f6bfdf5650ba11ec9e491cbfc0546006', 'user1', '钢铁侠', 'login', '2021-11-29 10:20:47', '钢铁侠登录系统', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('f707e23951ab11ecb75f1cbfc0546006', 'admin', '系统管理员', 'select', '2021-11-30 15:05:56', '系统管理员查看角色：《管理员》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('fafe2e3151a911ec964f1cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:51:44', '系统管理员删除菜单：《12313》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('fe859b1151a911ec86b91cbfc0546006', 'admin', '系统管理员', 'delete', '2021-11-30 14:51:50', '系统管理员删除菜单：《5》', '127.0.0.1', '本地登录');
INSERT INTO `sys_log` VALUES ('ff9c197251ab11ec94061cbfc0546006', 'admin', '系统管理员', 'select', '2021-11-30 15:06:11', '系统管理员查看角色：《管理员》', '127.0.0.1', '本地登录');

-- ----------------------------
-- Table structure for sys_login_setting
-- ----------------------------
DROP TABLE IF EXISTS `sys_login_setting`;
CREATE TABLE `sys_login_setting`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户ID',
  `font_size` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '字体大小',
  `font_color` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '字体颜色',
  `background_color` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '背景色',
  `login_width` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '窗口宽度',
  `longin_height` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '窗口高度',
  `move_window_right` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '窗口右移',
  `move_window_down` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '窗口下移',
  `but_color` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '按钮颜色',
  `inner_frame_width` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `move_inner_frame_right` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `move_inner_frame_down` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `last_time` datetime(0) NULL DEFAULT NULL COMMENT '操作日期',
  `state` int(1) NULL DEFAULT 0 COMMENT '是否能修改(0:否，1:是)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_login_setting
-- ----------------------------
INSERT INTO `sys_login_setting` VALUES ('326d27b0438411ec83d91cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', '16', '#1aa094', '#30a59129', '480', '400', '50', '50', '#081e2f', '220', '20', '20', '2021-11-21 12:39:49', 0);
INSERT INTO `sys_login_setting` VALUES ('c10930d3429511ecb58e1cbfc0546006', '', '16', '#02e1f4', '#30a59129', '480', '400', '50', '50', '#081e2f', '220', '20', '20', '2021-11-11 11:14:56', 1);

-- ----------------------------
-- Table structure for sys_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE `sys_menu`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order` int(32) NULL DEFAULT NULL,
  `caption` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lcon` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remark` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `display` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_menu
-- ----------------------------
INSERT INTO `sys_menu` VALUES ('027722e651ab11ec97db1cbfc0546006', 3, '日志管理', 'layui-icon-fa-book', 'log.html', '0', '系统操作日志记录', 1);
INSERT INTO `sys_menu` VALUES ('2ecc21bfe9fc11eb976f1cbfc0546006', 8, '数据字典', 'layui-icon-fa-list-alt', 'dictionary.html', '6f396f624be011ebbf3f3c970ed7519c', '系统数据字典', 1);
INSERT INTO `sys_menu` VALUES ('34a98e1051ac11eca0871cbfc0546006', 2, '角色管理', 'layui-icon-fa-eercast', 'role.html', '6f396f624be011ebbf3f3c970ed7519c', '系统角色管理', 1);
INSERT INTO `sys_menu` VALUES ('5a19ada83dfe11ec820f1cbfc0546006', 11, '窗口设置', 'layui-icon-fa-window-maximize', 'design.html', '6f396f624be011ebbf3f3c970ed7519c', '用户自定义登录窗口样式', 1);
INSERT INTO `sys_menu` VALUES ('6f396f624be011ebbf3f3c970ed7519c', 1, '系统设置', 'layui-icon-fa-cog', '', '0', 'None', 1);
INSERT INTO `sys_menu` VALUES ('6f396f634be011ebbdf63c970ed7519c', 6, '采集设置', 'layui-icon-fa-camera', 'face_gather.html', '6f396f624be011ebbf3f3c970ed7519c', '用于用户的人脸信息采集登记的各项设置', 1);
INSERT INTO `sys_menu` VALUES ('6f3bd0c24be011eb829c3c970ed7519c', 2, '其他功能', 'layui-icon-fa-briefcase', '', '0', 'b', 1);
INSERT INTO `sys_menu` VALUES ('6f3e32254be011ebaa0d3c970ed7519c', 7, '数据权限', 'layui-icon-fa-superpowers', 'data_rights.html', '6f396f624be011ebbf3f3c970ed7519c', '系统数据权限管理', 1);
INSERT INTO `sys_menu` VALUES ('6f4093824be011eba0d63c970ed7519c', 3, '菜单管理', 'layui-icon-fa-server', 'menu.html', '6f396f624be011ebbf3f3c970ed7519c', 'None', 1);
INSERT INTO `sys_menu` VALUES ('6f4093834be011eba2493c970ed7519c', 5, '部门管理', 'layui-icon-fa-gears', 'position.html', '6f396f624be011ebbf3f3c970ed7519c', 'None', 1);
INSERT INTO `sys_menu` VALUES ('6f4093844be011eb80b63c970ed7519c', 4, '用户管理', 'layui-icon-fa-user-md', 'user.html', '6f396f624be011ebbf3f3c970ed7519c', 'None', 1);
INSERT INTO `sys_menu` VALUES ('76256da40f7f11ec892c1cbfc0546006', 1, '问题反馈', 'layui-icon-fa-product-hunt', 'feedback.html', '6f3bd0c24be011eb829c3c970ed7519c', '问题反馈', 1);
INSERT INTO `sys_menu` VALUES ('a02f099ffb3711eb97241cbfc0546006', 9, '桌面背景', 'layui-icon-fa-themeisle', 'theme.html', '6f396f624be011ebbf3f3c970ed7519c', '自定义桌面背景', 1);

-- ----------------------------
-- Table structure for sys_org
-- ----------------------------
DROP TABLE IF EXISTS `sys_org`;
CREATE TABLE `sys_org`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `org_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `org_code` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remark` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `great_date` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_org
-- ----------------------------
INSERT INTO `sys_org` VALUES ('04fa3bf644d111eb969f3c970ed7519c', '功能测试', 'gncs', '9dd9f37644d011eb94453c970ed7519c', '功能测试', '2020-12-23 11:43:28.000000');
INSERT INTO `sys_org` VALUES ('0e66f07a44d111eb9fbe3c970ed7519c', 'KH1B', 'KH1B', 'b0cf224644d011eba3c63c970ed7519c', 'KH1B', '2020-12-23 11:43:44.000000');
INSERT INTO `sys_org` VALUES ('16e2158644d111eb8f7d3c970ed7519c', 'KH2B', 'KH2B', 'b0cf224644d011eba3c63c970ed7519c', 'KH2B', '2020-12-23 11:43:58.000000');
INSERT INTO `sys_org` VALUES ('709b1acc44d011eb992c3c970ed7519c', '软件部', 'rjb', 'a253148a337611eaa3373c970ed7519c', '软件部', '2020-12-23 11:39:19.000000');
INSERT INTO `sys_org` VALUES ('7b309c3844d011ebbb4b3c970ed7519c', '商务部', 'swb', 'a253148a337611eaa3373c970ed7519c', '商务部', '2020-12-23 11:39:37.000000');
INSERT INTO `sys_org` VALUES ('853ec33a44d011eb88743c970ed7519c', '销售部', 'xsb', 'a253148a337611eaa3373c970ed7519c', '销售部', '2020-12-23 11:39:54.000000');
INSERT INTO `sys_org` VALUES ('8fca597044d011ebb1113c970ed7519c', '开发部', 'KFB', '709b1acc44d011eb992c3c970ed7519c', '开发部', '2020-12-23 11:40:12.000000');
INSERT INTO `sys_org` VALUES ('9dd9f37644d011eb94453c970ed7519c', '测试部', 'csb', '709b1acc44d011eb992c3c970ed7519c', '测试部', '2020-12-23 11:40:35.000000');
INSERT INTO `sys_org` VALUES ('a253148a337611eaa3373c970ed7519c', '根目录', 'ROOT', '0', '根目录', '2020-11-13 11:51:19.000000');
INSERT INTO `sys_org` VALUES ('a754d9d2650911eb8d372cf05d231dfa', '销售3部', 'xs3b', '853ec33a44d011eb88743c970ed7519c', '销售3部', '2021-02-02 11:49:30.000000');
INSERT INTO `sys_org` VALUES ('b0cf224644d011eba3c63c970ed7519c', '客户部', 'khb', '7b309c3844d011ebbb4b3c970ed7519c', '客户部', '2020-12-23 11:41:07.000000');
INSERT INTO `sys_org` VALUES ('b3ab255a650611eb82f72cf05d231dfa', '销售2部', 'xs2b', '853ec33a44d011eb88743c970ed7519c', '销售2部', '2021-02-02 11:28:22.000000');
INSERT INTO `sys_org` VALUES ('b993fb9444d011eba21c3c970ed7519c', '售后部', 'shb', '7b309c3844d011ebbb4b3c970ed7519c', '售后部', '2020-12-23 11:41:22.000000');
INSERT INTO `sys_org` VALUES ('c910e69244d011eba2743c970ed7519c', '销售1部', '1b', '853ec33a44d011eb88743c970ed7519c', '销售1部', '2020-12-23 11:41:48.000000');
INSERT INTO `sys_org` VALUES ('d2b735e3f10011eb85611cbfc0546006', 'g1', 'g1', 'e13e5f4644d011eb822a3c970ed7519c', 'g1', '2021-07-30 14:39:00.000000');
INSERT INTO `sys_org` VALUES ('e13e5f4644d011eb822a3c970ed7519c', 'GUI', 'GUI', '8fca597044d011ebb1113c970ed7519c', 'GUI', '2020-12-23 11:42:28.000000');
INSERT INTO `sys_org` VALUES ('ed8d7e0844d011eb8f813c970ed7519c', '后端', 'HD', '8fca597044d011ebb1113c970ed7519c', '后端', '2020-12-23 11:42:49.000000');
INSERT INTO `sys_org` VALUES ('f9fc815244d011eba64c3c970ed7519c', '性能测试', 'xncs', '9dd9f37644d011eb94453c970ed7519c', '性能测试', '2020-12-23 11:43:10.000000');

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `caption` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `abbreviation` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remark` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pxh` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES ('66cc73a2337711eabdbc3c970ed7519c', '临时用户', '临时用户', '临时用户', 3);
INSERT INTO `sys_role` VALUES ('a2533b9f337611ea84c03c970ed7519c', '管理员', 'administrator', '系统管理员', 1);
INSERT INTO `sys_role` VALUES ('bf738462638411ebb6d82cf05d231dfa', '普通用户', '普通用户', '普通用户', 2);

-- ----------------------------
-- Table structure for sys_role_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_menu`;
CREATE TABLE `sys_role_menu`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `role_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role_menu
-- ----------------------------
INSERT INTO `sys_role_menu` VALUES ('027b3ec751ab11ec93591cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '027722e651ab11ec97db1cbfc0546006', '日志管理');
INSERT INTO `sys_role_menu` VALUES ('06299f0c4be111eb97273c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f3bd0c24be011eb829c3c970ed7519c', '其他功能');
INSERT INTO `sys_role_menu` VALUES ('1e8f47b1fc0711eb83371cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景');
INSERT INTO `sys_role_menu` VALUES ('34af2f7951ac11ec95f51cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '34a98e1051ac11eca0871cbfc0546006', '角色管理');
INSERT INTO `sys_role_menu` VALUES ('3af5f672e9fc11eba86d1cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典');
INSERT INTO `sys_role_menu` VALUES ('526223d411db11eca8681cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '76256da40f7f11ec892c1cbfc0546006', '问题反馈');
INSERT INTO `sys_role_menu` VALUES ('63fefd4a3dfe11ec8dc41cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置');
INSERT INTO `sys_role_menu` VALUES ('7dfcd3aa0f7f11ec9bad1cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '76256da40f7f11ec892c1cbfc0546006', '问题反馈');
INSERT INTO `sys_role_menu` VALUES ('a81e3c66fb3711ebbd7a1cbfc0546006', 'a2533b9f337611ea84c03c970ed7519c', '管理员', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景');
INSERT INTO `sys_role_menu` VALUES ('aa615f8bf0fa11eb8efe1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f4093844be011eb80b63c970ed7519c', '用户管理');
INSERT INTO `sys_role_menu` VALUES ('aa6328d7f0fa11ebbae91cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f4093834be011eba2493c970ed7519c', '部门管理');
INSERT INTO `sys_role_menu` VALUES ('aa63c4c2f0fa11eb82161cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f396f634be011ebbdf63c970ed7519c', '采集设置');
INSERT INTO `sys_role_menu` VALUES ('aa6410bdf0fa11eb89791cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典');
INSERT INTO `sys_role_menu` VALUES ('b3b6a10541d111ec92811cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置');
INSERT INTO `sys_role_menu` VALUES ('caf186704be011ebb9053c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f396f624be011ebbf3f3c970ed7519c', '系统设置');
INSERT INTO `sys_role_menu` VALUES ('cafcf84c4be011ebbe8d3c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f4093824be011eba0d63c970ed7519c', '菜单管理');
INSERT INTO `sys_role_menu` VALUES ('cb0361064be011ebb1923c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f4093844be011eb80b63c970ed7519c', '用户管理');
INSERT INTO `sys_role_menu` VALUES ('cb0e5dae4be011eb854c3c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f4093834be011eba2493c970ed7519c', '部门管理');
INSERT INTO `sys_role_menu` VALUES ('cb16c23e4be011eb809a3c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f396f634be011ebbdf63c970ed7519c', '采集设置');
INSERT INTO `sys_role_menu` VALUES ('cb1ba4504be011eb8c493c970ed7519c', 'a2533b9f337611ea84c03c970ed7519c', '管理员', '6f3e32254be011ebaa0d3c970ed7519c', '数据权限');
INSERT INTO `sys_role_menu` VALUES ('e2925125564211ecbc931cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '34a98e1051ac11eca0871cbfc0546006', '角色管理');
INSERT INTO `sys_role_menu` VALUES ('e292ecf7564211ec9f351cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f3bd0c24be011eb829c3c970ed7519c', '其他功能');
INSERT INTO `sys_role_menu` VALUES ('e29365ef564211ec99ea1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '027722e651ab11ec97db1cbfc0546006', '日志管理');
INSERT INTO `sys_role_menu` VALUES ('eeccf827e9f911eb89bd1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f396f624be011ebbf3f3c970ed7519c', '系统设置');
INSERT INTO `sys_role_menu` VALUES ('eecfb788e9f911eb95bf1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f4093824be011eba0d63c970ed7519c', '菜单管理');
INSERT INTO `sys_role_menu` VALUES ('eed16418e9f911eb82dc1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f3e32254be011ebaa0d3c970ed7519c', '数据权限');
INSERT INTO `sys_role_menu` VALUES ('eed16418e9f911eb82dc1cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', '6f3e32254be011ebaa0d3c970ed7519c', '数据分析');
-- ----------------------------
-- Table structure for sys_theme
-- ----------------------------
DROP TABLE IF EXISTS `sys_theme`;
CREATE TABLE `sys_theme`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `path` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `full_path` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` int(11) NULL DEFAULT NULL COMMENT '是否动态',
  `state` int(1) NULL DEFAULT NULL,
  `creat_data` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_theme
-- ----------------------------
INSERT INTO `sys_theme` VALUES ('1', 'image3.jpg', '/static/images/image3.jpg', NULL, 0, 0, '2021-08-13 17:00:41');
INSERT INTO `sys_theme` VALUES ('85ada03445dc11ec99aa1cbfc0546006', '85ad793f45dc11ec8aff1cbfc0546006.jpg', '/static/images/85ad793f45dc11ec8aff1cbfc0546006.jpg', 'E:/py_object/manager/static/images/85ad793f45dc11ec8aff1cbfc0546006.jpg', 1, 1, '2021-11-15 14:23:17');
INSERT INTO `sys_theme` VALUES ('af5efd92fe3711ebb0f31cbfc0546006', 'af5d1592fe3711ebb2791cbfc0546006.jpg', '/static/images/af5d1592fe3711ebb2791cbfc0546006.jpg', 'E:/py_object/manager/static/images/af5d1592fe3711ebb2791cbfc0546006.jpg', 0, 0, '2021-08-16 10:14:28');
INSERT INTO `sys_theme` VALUES ('b2678dfdfe3711eba9de1cbfc0546006', 'b2665658fe3711ebb7e11cbfc0546006.jpg', '/static/images/b2665658fe3711ebb7e11cbfc0546006.jpg', 'E:/py_object/manager/static/images/b2665658fe3711ebb7e11cbfc0546006.jpg', 0, 0, '2021-08-16 10:14:33');
INSERT INTO `sys_theme` VALUES ('c232186afc1711eba4df1cbfc0546006', 'c231f2bafc1711ebb4381cbfc0546006.jpg', '/static/images/c231f2bafc1711ebb4381cbfc0546006.jpg', 'E:/py_object/manager/static/images/c231f2bafc1711ebb4381cbfc0546006.jpg', 0, 0, '2021-08-13 17:20:53');

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `account` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tell` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `gender` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sfcj` int(1) UNSIGNED ZEROFILL NOT NULL DEFAULT 0,
  `sfqy` int(1) UNSIGNED ZEROFILL NOT NULL DEFAULT 1,
  `url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `account`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES ('b1e99c02337711eab3543c970ed7519c', '系统管理员', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'admin', '13256468596', '成都市成华区', '管理员', '男', 1, 1, '/static/images/portrait/b1e99c02337711eab3543c970ed7519c.jpg');
INSERT INTO `sys_user` VALUES ('b1e99c03337711ea9f373c970ed7519c', '钢铁侠', '4297f44b13955235245b2497399d7a93', '123123@qq.com', 'user1', '13256565651', '四川省成都市', '普通用户', '女', 1, 1, '/static/images/portrait/b1e99c03337711ea9f373c970ed7519c.jpg');
INSERT INTO `sys_user` VALUES ('b1e99c04337711eab8233c970ed7519c', '测试用户2', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user2', '13256565656', '阿达的撒大多撒', '普通用户', '女', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c05337711eab6993c970ed7519c', '测试用户3', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user3', '13256565654', '啊是大大阿达', '普通用户', '男', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c06337711ea9ecd3c970ed7519c', '测试用户4', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user4', '13256565654', '啊双打哒哒哒', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c07337711ea9ad93c970ed7519c', '测试用户5', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user5', '13256565656', '阿达啊大大', '普通用户', '男', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c08337711eaa8e03c970ed7519c', '测试用户6', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user6', '13256565656', '啊大大大啊', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c09337711eabfa63c970ed7519c', '测试用户7', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user7', '13256565656', '啊大大大啊', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0a337711eaba783c970ed7519c', '测试用户8', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user8', '13256565656', '啊大大大啊', '普通用户', '男', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0b337711ea9e293c970ed7519c', '测试用户9', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user9', '13256565656', '啊大大大啊', '普通用户', '男', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0c337711ea9b2e3c970ed7519c', '测试用户10', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user10', '13256468596', '成都市123', '普通用户', '男', 1, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0d337711eaa77e3c970ed7519c', '测试用户11', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user11', '13256565656', '啊大大大啊', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0e337711ea9daf3c970ed7519c', '测试用户12', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user12', '13256565656', 'asdsadadadad', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c0f337711eab42c3c970ed7519c', '测试用户13', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user13', '13232323232', 'asdadsadad', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('b1e99c10337711eaa9833c970ed7519c', '测试用户14', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user14', '13256565656', 'asdadadad', '普通用户', '男', 0, 1, NULL);
INSERT INTO `sys_user` VALUES ('d603ef76334c11eab0e23c970ed7519c', '测试用户15', '4297f44b13955235245b2497399d7a93', '123@qq.com', 'user15', '13256565656', '是胜多负少的事实上', '普通用户', '男', 0, 1, NULL);

-- ----------------------------
-- Table structure for sys_user_grant
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_grant`;
CREATE TABLE `sys_user_grant`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_account` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grant_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grant_code` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grant_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_grant
-- ----------------------------
INSERT INTO `sys_user_grant` VALUES ('058d06554a8511ecbb272cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', '4d6651c641d111ec94891cbfc0546006', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('0645b49d4a8511ec90792cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', '86a99f3a0f7f11ec8fad1cbfc0546006', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('072caf2f4a8511eca8e62cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', '86aa15ca0f7f11ec98c51cbfc0546006', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('0802bc0e4a8511eca3d22cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '76256da40f7f11ec892c1cbfc0546006', '问题反馈', '86aa4de00f7f11ec9a931cbfc0546006', 'edit', '编辑数据');
INSERT INTO `sys_user_grant` VALUES ('0a671b9b4a8511ecaffb2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', '4d66ed1841d111ec85101cbfc0546006', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('0beae04f4a8511ec86cf2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '5a19ada83dfe11ec820f1cbfc0546006', '窗口设置', '4d67980841d111ec86921cbfc0546006', 'edit', '编辑数据');
INSERT INTO `sys_user_grant` VALUES ('18cb76454a8511ec9e9d2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', '8d2706f6fe5911ebbc591cbfc0546006', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('1b9734da4a8511ecbb4d2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', '8d2754e7fe5911eba39c1cbfc0546006', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('1c4bda774a8511ec8a622cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', '8d277bd7fe5911eba6841cbfc0546006', 'edit', '编辑数据');
INSERT INTO `sys_user_grant` VALUES ('1da6419e4a8511ecacb82cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', 'a02f099ffb3711eb97241cbfc0546006', '桌面背景', '8d27a2cbfe5911ebaaf51cbfc0546006', 'del', '删除数据');
INSERT INTO `sys_user_grant` VALUES ('56dca9874a8511ec88e22cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f396f634be011ebbdf63c970ed7519c', '采集设置', '7f6239e250bd11ebbc863c970ed7519c', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('7869ad0a4a8511ec910a2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093824be011eba0d63c970ed7519c', '菜单管理', '7fa9a32850bd11ebabcc3c970ed7519c', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('a6aa072b4a8411ec88352cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093824be011eba0d63c970ed7519c', '菜单管理', '7fa4e06850bd11ebb3c73c970ed7519c', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('a967984251ac11ecbc461cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '34a98e1051ac11eca0871cbfc0546006', '角色管理', '541c33bd51ac11ec9e541cbfc0546006', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('a98883c04a8411ec9c502cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093844be011eb80b63c970ed7519c', '用户管理', '7fc633ae50bd11eb93913c970ed7519c', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('aa1d2ccc51ac11ecb5e11cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '34a98e1051ac11eca0871cbfc0546006', '角色管理', '541d1d7251ac11ecb5c91cbfc0546006', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('aadff63051ac11ec81d51cbfc0546006', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '34a98e1051ac11eca0871cbfc0546006', '角色管理', '541d92b751ac11ec92b31cbfc0546006', 'edit', '编辑数据');
INSERT INTO `sys_user_grant` VALUES ('ac7d01934a8411ecab402cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093834be011eba2493c970ed7519c', '部门管理', '7fb58a0c50bd11ebafcb3c970ed7519c', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('adf680914a8411ec91e12cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f396f634be011ebbdf63c970ed7519c', '采集设置', '7f5b15c050bd11ebba0b3c970ed7519c', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('af5249ef4a8411eca0422cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f3e32254be011ebaa0d3c970ed7519c', '数据权限', '7f91d56850bd11eb81723c970ed7519c', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('b0c5a5924a8411ecb3ce2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'dd312184eac811ebb5491cbfc0546006', 'show', '数据展示');
INSERT INTO `sys_user_grant` VALUES ('b54702cb4a8411ec85772cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '2ecc21bfe9fc11eb976f1cbfc0546006', '数据字典', 'dd312185eac811eb924d1cbfc0546006', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('b6da5cb24a8411ec86ab2cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093844be011eb80b63c970ed7519c', '用户管理', '7fcd57cc50bd11eba3123c970ed7519c', 'see', '查看详情');
INSERT INTO `sys_user_grant` VALUES ('bd1b84044a8411ecb6562cf05d231dfa', 'b1e99c03337711ea9f373c970ed7519c', 'user1', '钢铁侠', '6f4093824be011eba0d63c970ed7519c', '菜单管理', '7fac048a50bd11eb8ef63c970ed7519c', 'edit', '编辑数据');

-- ----------------------------
-- Table structure for sys_user_org
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_org`;
CREATE TABLE `sys_user_org`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `org_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `org_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `used` int(1) UNSIGNED ZEROFILL NULL DEFAULT NULL COMMENT '当前登录机构',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_org
-- ----------------------------
INSERT INTO `sys_user_org` VALUES ('0407be794a8711ecb6da2cf05d231dfa', '0e66f07a44d111eb9fbe3c970ed7519c', 'KH1B', 'b1e99c10337711eaa9833c970ed7519c', '测试用户14', 1);
INSERT INTO `sys_user_org` VALUES ('0c2ff2a24a8711ec853b2cf05d231dfa', '16e2158644d111eb8f7d3c970ed7519c', 'KH2B', 'd603ef76334c11eab0e23c970ed7519c', '测试用户15', 1);
INSERT INTO `sys_user_org` VALUES ('2cabd0b1645f11eb834d2cf05d231dfa', 'a253148a337611eaa3373c970ed7519c', '根目录', 'b1e99c02337711eab3543c970ed7519c', '系统管理员', 1);
INSERT INTO `sys_user_org` VALUES ('4f0ab509f01811ebb10c1cbfc0546006', 'b3ab255a650611eb82f72cf05d231dfa', '销售2部', 'b1e99c04337711eab8233c970ed7519c', 'wang', 1);
INSERT INTO `sys_user_org` VALUES ('4f0b02e1f01811eba4d41cbfc0546006', 'c910e69244d011eba2743c970ed7519c', '销售1部', 'b1e99c04337711eab8233c970ed7519c', 'wang', 0);
INSERT INTO `sys_user_org` VALUES ('5236b2ab4a8411ec871b2cf05d231dfa', '709b1acc44d011eb992c3c970ed7519c', '软件部', 'b1e99c06337711ea9ecd3c970ed7519c', '测试用户4', 1);
INSERT INTO `sys_user_org` VALUES ('6b98fed74a7e11eca9312cf05d231dfa', '7b309c3844d011ebbb4b3c970ed7519c', '商务部', 'b1e99c07337711ea9ad93c970ed7519c', 'user4', 1);
INSERT INTO `sys_user_org` VALUES ('6b994f654a7e11ec8e932cf05d231dfa', '853ec33a44d011eb88743c970ed7519c', '销售部', 'b1e99c07337711ea9ad93c970ed7519c', 'user4', 0);
INSERT INTO `sys_user_org` VALUES ('70a0d8154a7111ec9ac42cf05d231dfa', '8fca597044d011ebb1113c970ed7519c', '开发部', 'b1e99c05337711eab6993c970ed7519c', 'user2', 0);
INSERT INTO `sys_user_org` VALUES ('769cbf7d4a7e11ecac862cf05d231dfa', '709b1acc44d011eb992c3c970ed7519c', '软件部', 'b1e99c08337711eaa8e03c970ed7519c', 'user5', 1);
INSERT INTO `sys_user_org` VALUES ('769d0d714a7e11ec9c482cf05d231dfa', '7b309c3844d011ebbb4b3c970ed7519c', '商务部', 'b1e99c08337711eaa8e03c970ed7519c', 'user5', 0);
INSERT INTO `sys_user_org` VALUES ('769d82484a7e11ec9f922cf05d231dfa', '853ec33a44d011eb88743c970ed7519c', '销售部', 'b1e99c08337711eaa8e03c970ed7519c', 'user5', 0);
INSERT INTO `sys_user_org` VALUES ('7f34ba784b4411eb9ecf3c970ed7519c', 'a253148a337611eaa3373c970ed7519c', '根目录', 'b1e99c03337711ea9f373c970ed7519c', '钢铁侠', 1);
INSERT INTO `sys_user_org` VALUES ('8e73275e337811ea8b983c970ed7519c', 'a253148b337611ea8d653c970ed7519c', '软件部', 'b1e99c02337711eab3543c970ed7519c', '系统管理员', 0);
INSERT INTO `sys_user_org` VALUES ('8e796906337811eaacb53c970ed7519c', 'a2533b9d337611ea89f03c970ed7519c', '技术部', 'b1e99c02337711eab3543c970ed7519c', '系统管理员', 0);
INSERT INTO `sys_user_org` VALUES ('908e45cd4a7111ecace42cf05d231dfa', '853ec33a44d011eb88743c970ed7519c', '销售部', 'b1e99c0a337711eaba783c970ed7519c', 'user7', 1);
INSERT INTO `sys_user_org` VALUES ('908e9fd94a7111eca1252cf05d231dfa', '7b309c3844d011ebbb4b3c970ed7519c', '商务部', 'b1e99c0a337711eaba783c970ed7519c', 'user7', 0);
INSERT INTO `sys_user_org` VALUES ('97d0d81b4a7111ec81352cf05d231dfa', '7b309c3844d011ebbb4b3c970ed7519c', '商务部', 'b1e99c0b337711ea9e293c970ed7519c', 'user8', 1);
INSERT INTO `sys_user_org` VALUES ('97d144e54a7111eca3e52cf05d231dfa', '853ec33a44d011eb88743c970ed7519c', '销售部', 'b1e99c0b337711ea9e293c970ed7519c', 'user8', 0);
INSERT INTO `sys_user_org` VALUES ('97e6e2d8f0fd11ebb4a81cbfc0546006', '04fa3bf644d111eb969f3c970ed7519c', '功能测试', 'b1e99c05337711eab6993c970ed7519c', 'user2', 1);
INSERT INTO `sys_user_org` VALUES ('a292a0bd4a7111ec907a2cf05d231dfa', 'b0cf224644d011eba3c63c970ed7519c', '客户部', 'b1e99c0c337711ea9b2e3c970ed7519c', '测试用户', 1);
INSERT INTO `sys_user_org` VALUES ('a293159b4a7111ec93292cf05d231dfa', '8fca597044d011ebb1113c970ed7519c', '开发部', 'b1e99c0c337711ea9b2e3c970ed7519c', '测试用户', 0);
INSERT INTO `sys_user_org` VALUES ('e09aa8c54a8611ec84842cf05d231dfa', 'b0cf224644d011eba3c63c970ed7519c', '客户部', 'b1e99c0d337711eaa77e3c970ed7519c', '测试用户11', 1);
INSERT INTO `sys_user_org` VALUES ('e15e6955646511ebb2a12cf05d231dfa', '709b1acc44d011eb992c3c970ed7519c', '软件部', 'b1e99c09337711eabfa63c970ed7519c', 'user6', 1);
INSERT INTO `sys_user_org` VALUES ('ed4390b94a8611ecaefc2cf05d231dfa', 'a754d9d2650911eb8d372cf05d231dfa', '销售3部', 'b1e99c0e337711ea9daf3c970ed7519c', '测试用户12', 1);
INSERT INTO `sys_user_org` VALUES ('f22700a64b4411ebaddd3c970ed7519c', 'a754d9d2650911eb8d372cf05d231dfa', '销售3部', 'b1e99c04337711eab8233c970ed7519c', 'wang', 0);
INSERT INTO `sys_user_org` VALUES ('fc2a31fa4a8611ec843f2cf05d231dfa', 'b993fb9444d011eba21c3c970ed7519c', '售后部', 'b1e99c0f337711eab42c3c970ed7519c', '测试用户13', 1);

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rle_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `rle_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_role
-- ----------------------------
INSERT INTO `sys_user_role` VALUES ('742b18d665bf11eba2462cf05d231dfa', 'a2533b9f337611ea84c03c970ed7519c', '管理员', 'b1e99c02337711eab3543c970ed7519c', '系统管理员');
INSERT INTO `sys_user_role` VALUES ('e566305f564211ecb1671cbfc0546006', 'bf738462638411ebb6d82cf05d231dfa', '普通用户', 'b1e99c03337711ea9f373c970ed7519c', '钢铁侠');

SET FOREIGN_KEY_CHECKS = 1;

# 后台管理

#### 介绍
	基于python3编写的web后台管理系统

#### 软件架构
	本项目基于python3语言开发，后台框架使用layui，并使用了一些基于layui的第三方插件进行开发。


#### 安装教程
	1.  安装mysql数据库，版本5.7以上
	2.  在数据库导入文件中的sql文件
	3.  安装pycharm，并搭建django环境
	4.  导入项目
	5.  修改项目中settings.py中的数据库配置
	6.  启动项目

#### 插件版本
	1.  python 3.8.5
	2.  django 3.2.3
	3.  opencv-python 4.5.2.52
	4.  requests 2.25.1
	5.  bs4 0.0.1
	6.  face_recognition 1.3.0
	7.  treelib 1.6.1
	8.  fake_useragent 0.1.11

#### 使用说明
	1.  本项目基于python3语言开发，后台框架使用layui，并使用了一些基于layui的第三方插件。
	2.  本项目属于私有项目，未经允许，严谨售卖，否则后果自负。
	3.  欢迎大家提出自己的优化建议、系统的BUG，我会及时进行修复。
	4.  由于服务器是远程服务器，因此没有可用的摄像头，无法使用人脸识别登录。

#### 系统介绍
	1.  系统包含账号登录和人脸识别登录。
	2.  系统可自定义登录页背景图片。
	3.  系统包含了机构权限、数据权限、菜单权限三大模块。
	4.  系统包含用户问题反馈功能，便于运维人员进行线上问题处理。
	5.  系统包含消息推送以及个人资料修改、头像上传功能。
	6.  系统包含审批流程功能，可视化的流程配置。
	7.  系统包含线上问题反馈功能，可实时进行沟通。
	8.  系统用于强大的日志记录，可记录登录人员IP和地址。

#### 开发周期
	1. 2021.06.10 更新了机构数的数据组装，使用treelib解决了机构数层级限制问题。
	2. 2021.06.18 解决layui表格筛选勾选隐藏列后导致隐藏列在表格中展示
	3. 2021.06.24 调整了部门管理页面有滚动条的问题
	4. 2021.07.08 优化了页面数据展示权限，无权限是跳转指定页面
	5. 2021.07.14 给登录页面账户名称前添加了头像和子菜单
	6. 2021.07.16 添加了个人资料与密码修改，同时增加了表字段
	7. 2021.07.20 优化了角色管理部分页面
	8. 2021.07.27 添加了数据字典功能
	9. 2021.07.26 优化菜单管理在添加菜单时通过页面按钮初始化菜单权限
	10. 2021.07.30 添加了管辖范围限制，当前机构的人员只能查询当前机构以及下属机构的数据
	11. 2021.08.02 给角色管理添加了数据过滤，仅展示当前用户权限范围内的数据
	12. 2021.08.05 完善了左上角了个人消息功能
	13. 2021.08.09 完善左上角消息图标添加数量提示
	14. 2021.08.16 新增了自定义桌面壁纸功能
	15. 2021.08.21 新增了桌面背景菜单中图片点击预览功能，同时新增了系统版本字典项
	16. 2021.09.14 新增了问题反馈功能
	17. 2021.11.8 首页添加了echarts图表
	17. 2021.11.11 新增登录窗口自定义功能
	18. 2021.11.11 新添加了一个动态背景
	19. 2021-11-21 在人物头像下添加了机构切换功能
	20. 2021-11-25 日志记录添增加IP记录和登录地点记录
	20. 2021-11-29 个人消息添加了批量阅读和删除功能
	21. 2021-12-20 OA审批工作流开发
	22. 2022-02-18 系统公告功能开发

#### 更新记录
	1. 2021-11-02 上传了源代码
	2. 2021-11-05 上传了桌面背景菜单自定义设置功能相关源代码
	3. 2021-11-08 上传了问题反馈功能功能相关源代码
	4. 2021-11-11 上传了登录窗口自定义功能相关源代码
	5. 2021-11-11 处理了linux系统下菜单图标展示异常的问题
	6. 2021-11-12 对窗口设置进行了优化
	7. 2021-11-15 添加了动态背景
	8. 2021-11-15 对系统进行了优化，修复已知BUG
	9. 2021-11-22 在人物头像下新增机构切换功能
	10. 2021-11-26 日志记录添增加IP记录和登录地点记录
	11. 2021-11-29 个人消息添加了批量阅读和删除功能
	12. 2021-12-21 OA审批流程更新
	13. 2021-12-21 O系统公告功能更新

#### python3技术交流群
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/20211203154745.png)


#### 作者留言
	1.  最新需要源代码的请加群。
	2.  欢迎大家对系统中存在的BUG积极提出。
	3.  欢迎大家提出新的需求。
	4.  为了防止有些朋友在系统中胡乱操作，演示系统已禁用部分编辑权限。
	5.  源码中只包含基本的后台管理功能菜单，和演示系统功能菜单可能对不上。
	6.  该系统将持续进行更新，对大家提出的问题也会及时进行答复。
	7.  有任何问题可扫描二维码加群私聊。
	8.  有任何个性化需求请加群联系作者。

#### 《 后台管理》演示地址：http://47.100.44.142:8081/
	登录账号：user1 密码：123123
	
#### 《 资源监控系统》源码下载地址：
https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/monitor

#### 《 资源监控系统》演示地址：http://47.100.44.142:8082/


#### 系统截图
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/login.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E7%B3%BB%E7%BB%9F%E8%AE%BE%E7%BD%AE.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E8%8F%9C%E5%8D%95.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E9%83%A8%E9%97%A8.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E4%B8%AA%E4%BA%BA%E8%AE%BE%E7%BD%AE.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E5%85%B6%E4%BB%96%E5%8A%9F%E8%83%BD.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E6%9D%83%E9%99%90.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E6%A1%8C%E9%9D%A2.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E6%B5%81%E7%A8%8B%E7%AE%A1%E7%90%86.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E6%B5%81%E7%A8%8B.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E7%94%A8%E6%88%B7.png)
![Image text](https://gitee.com/XueHuaPiaoPiaoYiZhenFeng/back-stage-management/raw/master/qr_code/%E7%AA%97%E5%8F%A3.png)

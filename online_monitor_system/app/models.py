# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SysDicFrom(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    dic_key = models.CharField(max_length=32)
    p_id = models.CharField(max_length=32, blank=True, null=True)
    dic_values = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dic_from'
        unique_together = (('id', 'dic_key'),)


class SysDicMain(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dic_main'


class SysFeedback(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    creat_time = models.DateTimeField(blank=True, null=True)
    urgent = models.CharField(max_length=32, blank=True, null=True)
    creat_account = models.CharField(max_length=32, blank=True, null=True)
    creat_username = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_feedback'


class SysFeedbackInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    pid = models.CharField(max_length=32, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    op_username = models.CharField(max_length=32, blank=True, null=True)
    op_account = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_feedback_info'


class SysGrant(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    menu_id = models.CharField(max_length=32, blank=True, null=True)
    menu_name = models.CharField(max_length=32, blank=True, null=True)
    grant_code = models.CharField(max_length=32, blank=True, null=True)
    menu_grant = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_grant'


class SysImageSetting(models.Model):
    edition = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=126)
    temp_path = models.CharField(max_length=126, blank=True, null=True)
    cjcs = models.IntegerField(blank=True, null=True)
    jgsj = models.IntegerField(blank=True, null=True)
    dqsj = models.IntegerField(blank=True, null=True)
    sfqy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_image_setting'


class SysInformation(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=128, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_information'


class SysLog(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    accout = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    time = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=128, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_log'


class SysLoginSetting(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    font_size = models.CharField(max_length=32, blank=True, null=True)
    font_color = models.CharField(max_length=64, blank=True, null=True)
    background_color = models.CharField(max_length=64, blank=True, null=True)
    login_width = models.CharField(max_length=32, blank=True, null=True)
    longin_height = models.CharField(max_length=32, blank=True, null=True)
    move_window_right = models.CharField(max_length=32, blank=True, null=True)
    move_window_down = models.CharField(max_length=32, blank=True, null=True)
    but_color = models.CharField(max_length=64, blank=True, null=True)
    inner_frame_width = models.CharField(max_length=32, blank=True, null=True)
    move_inner_frame_right = models.CharField(max_length=32, blank=True, null=True)
    move_inner_frame_down = models.CharField(max_length=32, blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_login_setting'


class SysMenu(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    order = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=32, blank=True, null=True)
    lcon = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    pid = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=128, blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysOrg(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    org_name = models.CharField(max_length=32, blank=True, null=True)
    org_code = models.CharField(max_length=128, blank=True, null=True)
    pid = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=128, blank=True, null=True)
    great_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_org'


class SysRole(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    caption = models.CharField(max_length=32, blank=True, null=True)
    abbreviation = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=128, blank=True, null=True)
    pxh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleMenu(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    role_id = models.CharField(max_length=32, blank=True, null=True)
    role_name = models.CharField(max_length=32, blank=True, null=True)
    menu_id = models.CharField(max_length=32, blank=True, null=True)
    menu_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role_menu'


class SysTheme(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    image_name = models.CharField(max_length=64, blank=True, null=True)
    path = models.CharField(max_length=128, blank=True, null=True)
    full_path = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    creat_data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_theme'


class SysUser(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    pwd = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    account = models.CharField(max_length=32)
    tell = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=32, blank=True, null=True)
    level = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    sfcj = models.IntegerField()
    sfqy = models.IntegerField()
    url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'
        unique_together = (('id', 'account'),)


class SysUserGrant(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_account = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    menu_id = models.CharField(max_length=32, blank=True, null=True)
    menu_name = models.CharField(max_length=32, blank=True, null=True)
    grant_id = models.CharField(max_length=32, blank=True, null=True)
    grant_code = models.CharField(max_length=32, blank=True, null=True)
    grant_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_grant'


class SysUserOrg(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    org_id = models.CharField(max_length=32, blank=True, null=True)
    org_name = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_org'


class SysUserRole(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    rle_id = models.CharField(max_length=32, blank=True, null=True)
    rle_name = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'

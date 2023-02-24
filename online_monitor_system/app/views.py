from django.shortcuts import render, redirect, HttpResponse
from app import models
import json, datetime, hashlib, uuid
# Create your views here.
from utils import call
from utils import query
from utils import user_page
from django.db import connection
import os
from django.db.models import Q

# '''初始化照片存放目录'''
query.creat_path()


def now_time():
    n_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return n_time


def uid():
    uid = str(uuid.uuid1())
    suid = ''.join(uid.split('-'))
    return suid


def login(request):
    '''动态窗口'''
    if request.method == 'POST':
        dlfs = request.POST.get('key', None)
        if dlfs == 'login':
            data = call.dlfs_login(request)
            return HttpResponse(json.dumps(data))
        elif dlfs == 'face':
            qyzt = models.SysImageSetting.objects.filter(edition=1)
            for zt in qyzt.values('sfqy'):
                if zt['sfqy'] == 1:
                    data = query.face_login(request)
                    return HttpResponse(json.dumps(data))
                else:
                    return HttpResponse(json.dumps('server_stop'))
        else:
            return redirect('/login.html')
    session_key = request.session.session_key
    request.session.delete(session_key)
    date = call.login_select()
    return render(request, 'system/login.html', date)


def live(request):
    if call.is_login(request):
        return render(request, 'system/live.html')
    else:
        return redirect('/login.html')


def rtmp(request):
    if call.is_login(request):
        return render(request, 'system/rtmp.html')
    else:
        return redirect('/login.html')


def index(request):
    if call.is_login(request):
        user_id = request.session['user_id']
        data = query.index_data(user_id)
        count = user_page.dic_msg_num(user_id)
        data['count'] = count
        return render(request, 'system/index.html', data)
    else:
        return redirect('/login.html')


def home(request):
    if call.is_login(request):
        return render(request, 'system/home.html')
    else:
        return redirect('/login.html')


def design(request):
    '''登陆窗口页面'''
    if call.is_login(request):
        re_url = request.path_info
        user_id = request.session['user_id']
        if call.is_see_grant(request, re_url):
            date = call.design_login(re_url, user_id)
            return render(request, 'system/design.html', date)
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def design_submit(request):
    '''登陆窗口设置'''
    if call.is_login(request):
        re_url = request.POST.get('type', None)
        re_date = request.POST
        if call.is_see_grant(request, re_url):
            if request.method == 'POST':
                result = call.login_setting(request, re_date)
                return HttpResponse(json.dumps(result))
            else:
                return HttpResponse(json.dumps(None))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def theme(request):
    '''桌面壁纸'''
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            str_data = query.creat_theme(request, re_url)
            menu_str = query.menu_theme(request, re_url)
            return render(request, 'system/theme.html', {'url_data': re_url, 'data': str_data, 'menu_str': menu_str})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def theme_use(request):
    '''桌面壁纸生效'''
    if call.is_login(request) and request.method == 'POST':
        re_url = request.POST.get('type', None)
        if call.is_edit_grant(request, re_url):
            theme_id = request.POST
            models.SysTheme.objects.filter(id=theme_id['base']).update(state=1)
            models.SysTheme.objects.exclude(id=theme_id['base']).update(state=0)
            call.create_log(request, 'update', '修改了', '桌面壁纸')
            return HttpResponse(json.dumps(True))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def theme_detail(request):
    '''桌面背景预览'''
    if call.is_login(request):
        re_url = request.GET.get('type', None)
        user_id = request.session['user_id']
        if call.is_see_grant(request, re_url):
            date = call.theme_setting(request, re_url, user_id)
            return render(request, 'system/theme_detail.html', date)
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def theme_upload(request):
    '''桌面壁纸上传接口'''
    if call.is_login(request):
        re_url = request.POST.get('type', None)
        if call.is_edit_grant(request, re_url):
            if call.upload_theme(request):
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def theme_delete(request):
    '''删除背景图片'''
    if call.is_login(request) and request.method == 'POST':
        re_url = request.POST.get('type', None)
        if call.is_delete_grant(request, re_url):
            theme_id = request.POST
            image_path = models.SysTheme.objects.filter(id=theme_id['base'])
            for path in image_path.values('full_path'):
                if os.path.exists(path['full_path']):
                    os.remove(path['full_path'])
            models.SysTheme.objects.filter(id=theme_id['base']).delete()
            call.create_log(request, 'delete', '删除了', '一张桌面壁纸')
            return HttpResponse(json.dumps(True))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def information(request):
    '''个人资料页面'''
    if call.is_login(request):
        return render(request, 'system/information.html')
    else:
        return redirect('/login.html')


def information_data(request):
    if call.is_login(request):
        base = []
        user_id = request.session['user_id']
        info_data = user_page.dic_msg(user_id)
        for info in info_data.values('id', 'content', 'user_id', 'state', 'type'):
            if info['state'] == 1:
                info['state'] = '已读'
            else:
                info['state'] = '未读'
            base.append(info)
        data = {'code': 0, 'page_num': 1, 'bg_hs': 10, 'count': 0, 'data': base}
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/login.html')


def information_del(request):
    if call.is_login(request):
        data = request.POST
        try:
            models.SysInformation.objects.filter(id=data['ID']).delete()
            return HttpResponse(json.dumps(True))
        except:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def information_update(request):
    if call.is_login(request):
        up_id = request.POST
        if up_id['state'] == '未读':
            models.SysInformation.objects.filter(id=up_id['ID']).update(state=1)
            return HttpResponse(json.dumps(True))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def role(request):
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            sfkbj = call.see_grant(request, re_url)
            return render(request, 'system/role.html', {'url_data': re_url, 'anzs': sfkbj})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def role_insert(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                temp = request.POST
                models.SysRole.objects.create(id=call.uid(), caption=temp['base[name]'],
                                              abbreviation=temp['base[level]'], remark=temp['base[remark]'],
                                              pxh=temp['base[pxh]'])
                call.create_log(request, 'create', '创建角色', temp['base[name]'])
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                return render(request, 'system/role_insert.html', {'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def role_edit(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                temp = request.POST
                models.SysRole.objects.filter(id=temp['base[id]']).update(caption=temp['base[name]'],
                                                                          abbreviation=temp['base[level]'],
                                                                          remark=temp['base[remark]'],
                                                                          pxh=temp['base[pxh]'])
                call.create_log(request, 'update', '修改角色', temp['base[name]'])
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                role_id = request.GET.get('role_id', None)
                role_obj = models.SysRole.objects.filter(id=role_id)
                call.create_log(request, 'select', '查看角色', role_obj.values()[0]['caption'])
                role_base = list(role_obj.values_list()[0])
                return render(request, 'system/role_edit.html', {'role_base': role_base, 'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def role_del(request):
    if call.is_login(request):
        cur = connection.cursor()
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_delete_grant(request, re_url):
                re_id = request.POST
                cur.execute("delete from sys_role_menu where role_id = %s", [re_id['base']])
                cur.execute("delete from sys_user_role where rle_id = %s", [re_id['base']])
                cur.execute("delete from sys_role where id = %s", [re_id['base']])
                call.create_log(request, 'delete', '删除角色', re_id['ro_name'])
                cur.close()
                return HttpResponse(json.dumps(True))
            else:
                cur.close()
                return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def role_menu(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                query.P_role(request)
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            # 查询当前角色拥有的菜单权限
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                ro_id = request.GET.get('role_id', None)
                ro_name = request.GET.get('role_name', None)
                ro_base = [ro_id, ro_name]
                re_list = query.G_role(request, ro_id)
                role_id = query.G_roleid(request)
                return render(request, 'system/role_menu.html',
                              {'data': re_list, 'ro_base': ro_base, 'role_id': role_id, 'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def role_user(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                user_page.role_user(request)
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                role_id = request.GET.get('role_id', None)
                role_name = request.GET.get('role_name', None)
                role_base = [role_id, role_name]
                return render(request, 'system/role_user.html', {'role_base': role_base, 'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def role_data(request):
    '''角色页面数据接口'''
    if call.is_login(request):
        data = user_page.role_data(request)
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/login.html')


def user_detail(request):
    if call.is_login(request):
        re_url = request.GET.get('type', None)
        if call.is_see_grant(request, re_url):
            u_id = request.GET.get('role_id', None)
            data = query.detail_user(request, u_id)
            ex_data = call.ex_btn(u_id)
            return render(request, 'system/user_detail.html', {'data': list(data), 'ex_data': ex_data})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def user(request):
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            sfkbj = call.edit_grant(request, re_url)
            return render(request, 'system/user.html', {'url_data': re_url, 'anzs': sfkbj})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def user_insert(request):
    if call.is_login(request):
        if request.method == 'POST':
            u_data = call.inser_user(request)
            return HttpResponse(json.dumps(u_data))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                base = call.create_tree(request)
                user_type = call.select_user_type(request)
                return render(request, 'system/user_insert.html', {'data': base, 'user_type': user_type})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def user_data(request):
    # 用户管理数据接口
    if call.is_login(request):
        value = request.GET.get('id', None)
        search = request.GET.get('keyword', None)
        result = user_page.user_page(request, value, search)
        return HttpResponse(json.dumps(result))
    else:
        return redirect('/login.html')


def user_edit(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_data = request.POST
            data = call.edit_user(request, re_data['base[id]'])
            return HttpResponse(json.dumps(data))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                user_id = request.GET.get('user_id', None)
                cid = models.SysUser.objects.get(id=user_id)
                data = call.create_tree(request)
                ex_data = call.ex_data(user_id)
                return render(request, 'system/user_edit.html',
                              {'acc': cid.account, 'id': user_id, 'name': cid.name, 'gender': cid.gender,
                               'address': cid.address, 'email': cid.email, 'tell': cid.tell, 'sfqy': cid.sfqy,
                               'data': data, 'ex_data': ex_data})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def user_del(request):
    if call.is_login(request):
        cur = connection.cursor()
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_delete_grant(request, re_url):
                key = request.POST.get('key', None)
                if key == 'delete':
                    user_id = request.POST.get('ID', None)
                    user_name = request.POST.get('name', None)
                    cur.execute("delete from sys_user_role where user_id = %s", [user_id])
                    cur.execute("delete from sys_user where id = %s", [user_id])
                    call.create_log(request, 'delete', '删除用户', user_name)
                    cur.close()
                    return HttpResponse(json.dumps(True))
            else:
                cur.close()
                return HttpResponse(json.dumps(False))
        else:
            cur.close()
            return HttpResponse(json.dumps(None))
    else:
        return redirect('/login.html')


def menu(request):
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            sfkbj = call.edit_grant(request, re_url)
            return render(request, 'system/menu.html', {'url_data': re_url, 'anzs': sfkbj})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def menu_insert(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                role_id = request.POST
                if 'base[display]' in role_id:
                    sfxs = 1
                else:
                    sfxs = 0
                menu_id = uid()
                models.SysMenu.objects.create(id=menu_id, caption=role_id['base[p_name]'], order=role_id['base[order]'],
                                              lcon=role_id['base[font]'], url=role_id['base[link]'], pid=role_id['key'],
                                              remark=role_id['base[remark]'], display=sfxs)
                call.grant_creat(menu_id, role_id)
                call.create_log(request, 'create', '创建菜单', role_id['base[p_name]'])
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            get_url = request.GET.get('type', None)
            if call.is_edit_grant(request, get_url):
                menu_dic = {}
                menu_obj = models.SysMenu.objects.filter(pid=0)
                for m in menu_obj.values('id', 'caption'):
                    menu_dic[m['id']] = m['caption']
                menu_dic['0'] = 'ROOT'
                return render(request, 'system/menu_insert.html', {'menu_dic': menu_dic})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def menu_detail(request):
    if call.is_login(request):
        re_url = request.GET.get('type', None)
        if call.is_see_grant(request, re_url):
            menu_id = request.GET.get('menu_id', None)
            m_base = models.SysMenu.objects.filter(id=menu_id)
            base = m_base.values()
            data = base[0]
            grant_val = models.SysGrant.objects.filter(menu_id=data['id'])
            for gv in grant_val.values():
                data[gv['grant_code']] = 1
            call.create_log(request, 'select', '查看菜单', data['caption'])
            if data['pid'] != '0':
                p_sql = models.SysMenu.objects.filter(id=data['pid'])
                p_base = p_sql.values()
                p_name = p_base[0]['caption']
            else:
                p_name = 'ROOT'
            return render(request, 'system/menu_detail.html', {'p_name': p_name, 'data': data})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def menu_edit(request):
    if call.is_login(request):
        if request.method == 'POST':
            menu_base = request.POST
            if 'base[display]' in menu_base:
                sfxs = 1
            else:
                sfxs = 0
                models.SysMenu.objects.filter(pid=menu_base['base[menu_id]']).update(display=sfxs)
            call.grant_update(menu_base)
            models.SysMenu.objects.filter(id=menu_base['base[menu_id]']).update(caption=menu_base['base[p_name]'],
                                                                                order=menu_base['base[order]'],
                                                                                lcon=menu_base['base[font]'],
                                                                                url=menu_base['base[link]'],
                                                                                pid=menu_base['key'],
                                                                                remark=menu_base['base[remark]'],
                                                                                display=sfxs)
            call.create_log(request, 'update', '编辑菜单', menu_base['base[p_name]'])
            return HttpResponse(json.dumps(True))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                data = user_page.menu(request)
                return render(request, 'system/menu_edit.html', data)
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def menu_del(request):
    if call.is_login(request):
        cur = connection.cursor()
        menu_base = request.POST
        re_url = request.POST.get('type', None)
        if call.is_delete_grant(request, re_url):
            count = cur.execute("select id from sys_menu where pid = %s", [menu_base['base']])
            if count > 0:  # 有子菜单
                return HttpResponse(json.dumps(False))
            else:  # 没有子菜单
                cur.execute("delete from sys_role_menu where menu_id = %s", [menu_base['base']])
                models.SysGrant.objects.filter(menu_id=menu_base['base']).delete()
                cur.execute("delete from sys_menu where id = %s", [menu_base['base']])
                models.SysUserGrant.objects.filter(menu_id=menu_base['base']).delete()
                models.SysGrant.objects.filter(menu_id=menu_base['base']).delete()
                call.create_log(request, 'delete', '删除菜单', menu_base['m_name'])
            cur.close()
            return HttpResponse(json.dumps(True))
        else:
            cur.close()
            return HttpResponse(json.dumps(None))
    else:
        return redirect('/login.html')


def menu_data(request):
    '''菜单数据接口'''
    if call.is_login(request):
        data = query.tree(request)
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/login.html')


def log(request):
    '''日志管理'''
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            log_obj = models.SysLog.objects.values('type').distinct()
            ty_li = []
            for l in log_obj.values('type'):
                ty_li.append(l['type'])
            return render(request, 'system/log.html', {'log_base': ty_li, 'url_data': re_url})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def log_data(request):
    '''日志数据接口'''
    if call.is_login(request):
        re_url = request.GET.get('type', None)
        if call.is_grant(request, re_url):
            data = user_page.log_page(request)
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(json.dumps({'code': 0, 'data': []}))
    else:
        return redirect('/login.html')


def position(request):
    '''部门管理'''
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            bjqx = call.edit_grant(request, re_url)
            scqx = call.delete_grant(request, re_url)
            data = call.create_tree(request)
            return render(request, 'system/position.html',
                          {'data': data, 'url_data': re_url, 'bjqx': bjqx, 'scqx': scqx})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def org_add(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                n_base = request.POST
                ex_val = models.SysOrg.objects.filter(org_code=n_base['base[Code]'])
                if len(ex_val) == 0:
                    models.SysOrg.objects.create(id=uid(), org_code=n_base['base[Code]'], org_name=n_base['base[name]'],
                                                 pid=n_base['base[PID]'], remark=n_base['base[remark]'],
                                                 great_date=now_time())
                    call.create_log(request, 'create', '新增部门', n_base['base[name]'])
                    return HttpResponse(json.dumps(True))
                else:
                    return HttpResponse(json.dumps(False))
            else:
                return HttpResponse(json.dumps(None))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                org_id = request.GET.get('org_id', None)
                org_val = models.SysOrg.objects.filter(id=org_id)
                for org in org_val.values():
                    return render(request, 'system/org_add.html',
                                  {'org_name': org['org_name'], 'org_id': org['id'], 'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def org_edit(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                n_base = request.POST
                models.SysOrg.objects.filter(org_code=n_base['base[Code]']).update(org_name=n_base['base[name]'],
                                                                                   remark=n_base['base[remark]'])
                call.create_log(request, 'update', '编辑部门', n_base['base[name]'])
                return HttpResponse(json.dumps(True))
            else:
                return HttpResponse(json.dumps(False))
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                org_id = request.GET.get('org_id', None)
                org_val = models.SysOrg.objects.filter(id=org_id)
                for org in org_val.values():
                    if org['pid'] != '0':
                        p_val = models.SysOrg.objects.filter(id=org['pid'])
                        for p in p_val.values():
                            pass
                    else:
                        p = org
                return render(request, 'system/org_edit.html',
                              {'pid': org['pid'], 'p_name': p['org_name'], 'org_name': org['org_name'],
                               'org_code': org['org_code'], 'remark': org['remark'], 'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def org_del(request):
    if call.is_login(request):
        re_url = request.POST.get('type', None)
        if call.is_delete_grant(request, re_url):
            del_base = request.POST
            del_obj = models.SysOrg.objects.filter(pid=del_base['base'])
            if len(del_obj) > 0:
                return HttpResponse(json.dumps(False))
            else:
                models.SysOrg.objects.filter(id=del_base['base']).delete()
                models.SysUserOrg.objects.filter(org_id=del_base['base']).delete()
                return HttpResponse(json.dumps(True))
        else:
            return HttpResponse(json.dumps(None))
    else:
        return redirect('/login.html')


def org_data(request):
    if call.is_login(request):
        result = user_page.org_data(request)
        return HttpResponse(json.dumps(result))
    else:
        return redirect('/login.html')


def face_gather(request):
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                fhjg = call.face_cj(request)
                return HttpResponse(json.dumps(fhjg))
            else:
                return HttpResponse(json.dumps(False))
        else:
            re_url = request.path_info
            if call.is_grant(request, re_url):
                text_dic = {}
                set_text = models.SysImageSetting.objects.filter(edition=1)
                for set in set_text.values():
                    for s, k in set.items():
                        text_dic[s] = k
                text_dic['url_data'] = re_url
                if call.is_edit_grant(request, re_url):
                    text_dic['anzs'] = 1
                    dis = ''' '''
                else:
                    text_dic['anzs'] = 0
                    dis = '''disabled = '' '''
                if text_dic['sfqy'] == 1:
                    text_dic[
                        'sfqy'] = '''<input type="checkbox" checked="" ''' + dis + ''' name="open" lay-skin="switch" lay-filter="switchTest" lay-text="ON|OFF">'''
                else:
                    text_dic[
                        'sfqy'] = '''<input type="checkbox" ''' + dis + ''' name="close" lay-skin="switch" lay-filter="switchTest" lay-text="ON|OFF">'''
                return render(request, 'system/face_gather.html', text_dic)
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def data_rights(request):
    '''数据权限'''
    if call.is_login(request):
        if request.method == 'POST':
            data = query.change_grant(request)
            return HttpResponse(json.dumps(data))
        else:
            re_url = request.path_info
            if call.is_grant(request, re_url):
                return render(request, 'system/data_rights.html', {'url_data': re_url})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def menu_grant(request):
    if call.is_login(request):
        account = request.session['acc']
        data = query.menu_tree(request, account)
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/login.html')


def no_permission(request):
    '''403页面'''
    return render(request, 'system/403.html')


def single(request):
    '''个人资料修改'''
    if call.is_login(request):
        if request.method == 'POST':
            re_data = request.POST
            models.SysUser.objects.filter(id=re_data['base[id]']).update(account=re_data['base[username]'],
                                                                         name=re_data['base[name]'],
                                                                         gender=re_data['base[sex]'],
                                                                         address=re_data['base[address]'],
                                                                         tell=re_data['base[tell]'],
                                                                         email=re_data['base[email]'])
            call.create_log(request, 'update', '修改了个人资料', '********')
            return HttpResponse(json.dumps(True))
        else:
            user_id = request.GET.get('user_id', None)
            user_information = models.SysUser.objects.filter(id=user_id)
            for information in user_information.values('id', 'account', 'name', 'gender', 'address', 'tell', 'email',
                                                       'url'):
                information_data = information
            return render(request, "system/single.html", information_data)
    else:
        return redirect('/login.html')


def pwd_edit(request):
    '''个人密码修改'''
    if call.is_login(request):
        if request.method == 'POST':
            result = call.ex_pwd_edit(request)
            return HttpResponse(json.dumps(result))
        else:
            user_id = request.GET.get('user_id', None)
            return render(request, 'system/pwd_edit.html', {'user_id': user_id})
    else:
        return redirect('/login.html')


def image_upload(request):
    '''图片上传接口'''
    if call.is_login(request):
        if call.upload_image(request):
            return HttpResponse(json.dumps(True))
        else:
            return HttpResponse(json.dumps(False))
    else:
        return redirect('/login.html')


def dictionary(request):
    '''数据字典'''
    if call.is_login(request):
        re_url = request.path_info
        if call.is_grant(request, re_url):
            sfkbj = call.edit_grant(request, re_url)
            return render(request, 'system/dictionary.html', {'url_data': re_url, 'anzs': sfkbj})
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dictkey_data(request):
    '''数据字典属性值接口'''
    re_url = request.GET.get('type', None)
    if call.is_login(request) and call.is_grant(request, re_url):
        data = user_page.dickey_data(request, re_url)
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/login.html')


def dict_main_insert(request):
    '''新增数据字典属性值'''
    if call.is_login(request):
        if request.method == 'POST':
            data = user_page.main_insert(request, uid())
            return HttpResponse(json.dumps(data))
        else:
            re_url = request.GET.get('type', None)
            if call.is_see_grant(request, re_url):
                return render(request, 'system/dict_main_insert.html')
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dict_main_edit(request):
    '''编辑数据字典属性'''
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                data = request.POST
                models.SysDicMain.objects.filter(id=data['base[id]']).update(name=data['base[csms]'])
                call.create_log(request, 'edit', '编辑了字典属性', data['base[csms]'])
                return HttpResponse(json.dumps(True))
            else:
                return render(request, 'system/403.html')
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                main_id = request.GET.get('main_id', None)
                main_value = models.SysDicMain.objects.filter(id=main_id)
                for value in main_value.values('id', 'key', 'name'):
                    value['url_data'] = re_url
                return render(request, 'system/dict_main_edit.html', value)
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dict_main_detail(request):
    '''查看数据字典属性'''
    re_url = request.GET.get('type', None)
    if call.is_login(request):
        if call.is_see_grant(request, re_url):
            main_id = request.GET.get('main_id', None)
            main_value = models.SysDicMain.objects.filter(id=main_id)
            for value in main_value.values('id', 'key', 'name'):
                pass
            call.create_log(request, 'select', '查看了字典属性', value['name'])
            return render(request, 'system/dict_main_detail.html', value)
        else:
            return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dict_main_delete(request):
    '''删除字典属性'''
    if call.is_login(request):
        re_url = request.POST.get('type', None)
        if call.is_delete_grant(request, re_url):
            try:
                data = request.POST
                if data['dic_key'] != 'system':
                    count = models.SysDicFrom.objects.filter(p_id=data['ID']).count()
                    if count == 0:
                        models.SysDicFrom.objects.filter(p_id=data['ID']).delete()
                        models.SysDicMain.objects.filter(id=data['ID']).delete()
                        call.create_log(request, 'delete', '删除了字典属性', data['name'])
                        return HttpResponse(json.dumps(True))
                    else:
                        return HttpResponse(json.dumps('exist'))
                else:
                    return HttpResponse(json.dumps(None))
            except:
                return HttpResponse(json.dumps(False))
        else:
            return HttpResponse(json.dumps('Illegal'))
    else:
        return redirect('/login.html')


def dictvalues_data(request):
    '''数据字典参数接口'''
    re_url = request.GET.get('type', None)
    if call.is_login(request) and call.is_grant(request, re_url):
        data_values = user_page.dict_values(request, re_url)
        return HttpResponse(json.dumps(data_values))
    else:
        return redirect('/login.html')


def dic_child_insert(request):
    '''新增数据字典参数'''
    if call.is_login(request):
        if request.method == 'POST':
            data = user_page.child_insert(request, uid(), now_time())
            return HttpResponse(json.dumps(data))
        else:
            re_url = request.GET.get('type', None)
            P_id = request.GET.get('main_id', None)
            if call.is_see_grant(request, re_url):
                return render(request, 'system/dic_child_insert.html', {'P_id': P_id})
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dic_child_edit(request):
    '''编辑数据字典参数'''
    if call.is_login(request):
        if request.method == 'POST':
            re_url = request.POST.get('type', None)
            if call.is_edit_grant(request, re_url):
                data = request.POST
                models.SysDicFrom.objects.filter(id=data['base[id]']).update(dic_key=data['base[zdbm]'],
                                                                             dic_values=data['base[zdmc]'])
                call.create_log(request, 'update', '编辑了字典参数', data['base[zdmc]'])
                return HttpResponse(json.dumps(True))
            else:
                return render(request, 'system/403.html')
        else:
            re_url = request.GET.get('type', None)
            if call.is_edit_grant(request, re_url):
                main_id = request.GET.get('main_id', None)
                main_value = models.SysDicFrom.objects.filter(id=main_id)
                for value in main_value.values('id', 'dic_key', 'dic_values'):
                    value['url_data'] = re_url
                return render(request, 'system/dic_child_edit.html', value)
            else:
                return render(request, 'system/403.html')
    else:
        return redirect('/login.html')


def dic_child_detail(request):
    '''查看数据字典参数'''
    re_url = request.GET.get('type', None)
    if call.is_see_grant(request, re_url):
        main_id = request.GET.get('main_id', None)
        main_value = models.SysDicFrom.objects.filter(id=main_id)
        for value in main_value.values('id', 'dic_key', 'dic_values'):
            value['url_data'] = re_url
        call.create_log(request, 'select', '查看了字典参数', value['dic_values'])
        return render(request, 'system/dic_child_detail.html', value)
    else:
        return render(request, 'system/403.html')


def dic_child_delete(request):
    '''删除数据字典参数'''
    if call.is_login(request):
        re_url = request.POST.get('type', None)
        if call.is_delete_grant(request, re_url):
            try:
                data = request.POST
                '''判断是否为系统参数子项'''
                sys_date = models.SysDicMain.objects.filter(key='system')
                for sys in sys_date.values('id'):
                    Parent_id = sys['id']
                if models.SysDicFrom.objects.filter(Q(id=data['ID']) & ~Q(p_id=Parent_id)).count() > 0:
                    models.SysDicFrom.objects.filter(Q(id=data['ID']) & ~Q(p_id=Parent_id)).delete()
                    call.create_log(request, 'delete', '删除了字典参数', data['name'])
                    return HttpResponse(json.dumps(True))
                else:
                    return HttpResponse(json.dumps('system'))
            except:
                return HttpResponse(json.dumps(False))
        else:
            return HttpResponse(json.dumps('Illegal'))
    else:
        return redirect('/login.html')


def feedback(request):
    if call.is_login(request):
        date = user_page.theme_detail(request)
        return render(request, 'system/feedback.html', date)
    else:
        return redirect('/login.html')


def creat_feedback(request):
    if call.is_login(request):
        if request.method == 'POST':
            base = query.creat_feed(request)
            return HttpResponse(json.dumps(base))
        else:
            return render(request, 'system/creat_feedback.html')
    else:
        return redirect('/login.html')


def feedback_detail(request):
    if call.is_login(request):
        data = user_page.feed_detail(request)
        return render(request, 'system/feedback_detail.html', data)
    else:
        return redirect('/login.html')


def insert_feedback_detail(request):
    if call.is_login(request):
        data = request.POST
        result = query.feed_detail_insert(request, data)
        return HttpResponse(json.dumps(result))
    else:
        return redirect('/login.html')


def change_org(request):
    if call.is_login(request):
        user_id = request.session['user_id']
        if request.method == 'POST':
            data = call.chang_used_org(request, user_id)
            return HttpResponse(json.dumps(data))
        else:
            data = call.user_uesd_org(request, user_id)
            return render(request, "system/change_org.html", data)
    else:
        return redirect('/login.html')


def information_batch_del(request):
    if call.is_login(request):
        user_id = request.session['user_id']
        not_dalete = models.SysInformation.objects.filter(Q(user_id=user_id) & Q(state=1))
        if len(not_dalete) == 0:
            return HttpResponse(json.dumps(False))
        else:
            models.SysInformation.objects.filter(Q(user_id=user_id) & Q(state=1)).delete()
            return HttpResponse(json.dumps(True))
    else:
        return redirect('/login.html')


def information_batch_read(request):
    if call.is_login(request):
        user_id = request.session['user_id']
        not_reda = models.SysInformation.objects.filter(Q(user_id=user_id) & Q(state=0)).update(state=1)
        if not_reda == 0:
            return HttpResponse(json.dumps(False))
        else:
            return HttpResponse(json.dumps(True))
    else:
        return redirect('/login.html')

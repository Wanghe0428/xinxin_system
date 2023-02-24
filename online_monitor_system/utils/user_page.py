#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time      :2019-7-29 9:54
# Author    :"wangjunlin"

from app import models
from utils import call
from django.db import connection
from django.db.models import Q


def org_user_filter(request):
    if request.session['acc'] != 'admin':
        '''通过call.user_org过滤机构,再通过机构获取用户 '''
        org_list = []
        org_data = call.user_org(request)
        for d in org_data.paths_to_leaves():
            org_list += d
        org_list = list(set(org_list))
        u_id = models.SysUserOrg.objects.filter(org_id__in=org_list)
        use_id = []
        for u in u_id.values('user_id'):
            use_id.append(u['user_id'])
        return use_id
    else:
        return False


def user_page(request, value, search):
    u_number = 0
    # 角色ID：value 查询内容：search
    page_num = int(request.GET.get('page', 1))
    bg_hs = int(request.GET.get('limit', 10))
    re_url = request.GET.get('type', None)
    bjqx = call.edit_grant(request, re_url)
    scqx = call.delete_grant(request, re_url)
    ckqx = call.see_grant(request, re_url)
    if search != None and search != '':
        sear = []
        if org_user_filter(request) != False:
            u_id = org_user_filter(request)
            user_all = models.SysUser.objects.filter(
                Q(id__in=u_id) & Q(Q(account__icontains=search) | Q(name__contains=search)) & ~Q(
                    account='admin')).order_by('id')
        else:
            user_all = models.SysUser.objects.filter(
                Q(Q(account__contains=search) | Q(name__contains=search)) & ~Q(account='admin')).order_by('id')
        sear_base = user_all[(page_num - 1) * bg_hs:page_num * bg_hs]
        for se in sear_base.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level', 'sfcj',
                                   'sfqy'):
            if se['sfqy'] == 1:
                se['sfqy'] = '启用'
            else:
                se['sfqy'] = '停用'
            se['sfkbj'] = bjqx
            se['sfksc'] = scqx
            se['sfkck'] = ckqx
            u_number += 1
            se['order'] = u_number + (page_num - 1) * bg_hs
            user_org = models.SysUserOrg.objects.filter(user_id=se['id']).order_by('id')
            for uorg in user_org.values('org_name'):
                se['org_name'] = uorg['org_name']
            sear.append(se)
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(user_all), 'data': sear}
    else:
        li = []
        if org_user_filter(request) != False:
            u_id = org_user_filter(request)
            all = models.SysUser.objects.filter(Q(id__in=u_id) & ~Q(account='admin')).order_by('id')
        else:
            all = models.SysUser.objects.filter(~Q(account='admin')).order_by('id')
        aggregate = all[(page_num - 1) * bg_hs:page_num * bg_hs]
        for n in aggregate.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level', 'sfcj',
                                  'sfqy'):
            if value != None:
                ex_obj = models.SysUserRole.objects.filter(rle_id=value, user_id=str(n['id']))
                if len(ex_obj.values()):
                    n["LAY_CHECKED"] = True
            u_number += 1
            n['order'] = u_number + (page_num - 1) * bg_hs
            if n['sfqy'] == 1:
                n['sfqy'] = '启用'
            else:
                n['sfqy'] = '停用'
            if n['sfcj'] == 1:
                n['pdcj'] = '是'
            else:
                n['pdcj'] = '否'
            n['sfkbj'] = bjqx
            n['sfksc'] = scqx
            n['sfkck'] = ckqx
            u_org = models.SysUserOrg.objects.filter(Q(user_id=n['id']) & Q(used=1)).order_by('id')
            for user_org in u_org.values('org_name'):
                n['org_name'] = user_org['org_name']
            li.append(n)
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(all), 'data': li}


def role_user(request):
    cur = connection.cursor()
    role_base = request.POST.get('key', None)
    user_base = request.POST.get('user_base', None)
    ro_base = eval(role_base)
    exist = []
    # 查询当前角色已有的所有用户ID
    cur.execute("select id from sys_user where account = 'admin'")
    admin_id = cur.fetchall()
    cur.execute("select distinct(user_id),rle_name from sys_user_role where rle_id=%s and user_id != %s",
                [ro_base[0], admin_id[0][0]])
    user_id = cur.fetchall()
    for u in user_id:
        exist.append(u[0])
    for user in eval(user_base):
        if user['id'] in exist:
            exist.remove(user['id'])
        else:
            # 如果当前角色下没有该用户ID,就给当前用户ID添加权限
            cur.execute("INSERT INTO sys_user_role(id,rle_id,rle_name,user_id,user_name) VALUES (%s,%s,%s,%s,%s)",
                        [call.uid(), ro_base[0], ro_base[1], user['id'], user['name']])
    # exist是这次没传过来，但是之前有的用户ID，执行删除操作
    for eu in exist:
        cur.execute("delete from sys_user_role where rle_id=%s and user_id = %s", [ro_base[0], eu])
    cur.execute("select caption from sys_role where id = %s", [ro_base[0]])
    role_name = cur.fetchall()
    call.create_log(request, 'update', '更新角色用户', role_name[0][0])
    cur.close()
    return True


def role_data(request):
    cur = connection.cursor()
    all_list = []
    user_id = request.session['user_id']
    user_acc = request.session['acc']
    if user_acc != 'admin':
        cur.execute(
            "select DISTINCT(c.id) from (sys_user_role a INNER JOIN sys_role_menu b on a.rle_id = b.role_id) INNER JOIN sys_role c on b.role_id=c.id where a.user_id = %s",
            user_id)
        all_role = cur.fetchall()
        for all in all_role:
            all_list.append(all[0])
    re_url = request.GET.get('type', None)
    bjqx = call.edit_grant(request, re_url)
    scqx = call.delete_grant(request, re_url)
    r_number = 0
    page_num = int(request.GET.get('page', 1))
    bg_hs = int(request.GET.get('limit', 10))
    search = request.GET.get('role_key', None)
    if search != '' and search != None:
        sear_list = []
        Role_all = models.SysRole.objects.filter(Q(caption__contains=search) & Q(id__in=all_list)).order_by('pxh')
        role_obj = Role_all[(page_num - 1) * bg_hs:page_num * bg_hs]
        for ro in role_obj.values('id', 'caption', 'abbreviation', 'remark', 'pxh'):
            r_number += 1
            ro['orderid'] = r_number + (page_num - 1) * bg_hs
            ro['bjqx'] = bjqx
            ro['scqx'] = scqx
            sear_list.append(ro)
        cur.close()
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(Role_all), 'data': sear_list}
    else:
        ro_list = []
        if user_acc != 'admin':
            all = models.SysRole.objects.filter(id__in=all_list).order_by('pxh')
        else:
            all = models.SysRole.objects.all().order_by('pxh')
        ro_obj = all[(page_num - 1) * bg_hs:page_num * bg_hs]
        for r in ro_obj.values('id', 'caption', 'abbreviation', 'remark', 'pxh'):
            r_number += 1
            r['orderid'] = r_number + (page_num - 1) * bg_hs
            r['bjqx'] = bjqx
            r['scqx'] = scqx
            ro_list.append(r)
        cur.close()
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(all), 'data': ro_list}


def menu(request):
    menu_id = request.GET.get('menu_id', None)
    m_base = models.SysMenu.objects.filter(id=menu_id)
    base = m_base.values()
    n_base = base[0]
    grant_list = []
    if n_base['display'] == 1:
        n_base[
            'display'] = '''<input id="orgProblemStatus" type="checkbox" name="display" lay-skin="switch" lay-filter="switchTest" lay-text="是|否" checked="">'''
    else:
        n_base[
            'display'] = '''<input id="orgProblemStatus" type="checkbox" name="display" lay-skin="switch" lay-filter="switchTest" lay-text="是|否">'''
    menu_dic = {}
    if base[0]['pid'] != '0':
        p_sql = models.SysMenu.objects.filter(id=base[0]['pid'])
        p_base = p_sql.values()
        menu_dic[p_base[0]['id']] = p_base[0]['caption']
        menu_grant = models.SysGrant.objects.filter(menu_id=base[0]['id'])
        for mg in menu_grant.values('grant_code'):
            grant_list.append(mg['grant_code'])
        if 'show' in grant_list:
            n_base[
                'grantshow'] = '''<input id="grantshow" type="checkbox" name="grantshow" lay-filter="grantStatus" lay-skin="primary" title="数据展示" checked="">'''
        else:
            n_base[
                'grantshow'] = '''<input id="grantshow" type="checkbox" name="grantshow" lay-filter="grantStatus" lay-skin="primary" title="数据展示">'''
        if 'see' in grant_list:
            n_base[
                'grantsee'] = '''<input id="grantsee" type="checkbox" name="grantsee" lay-filter="grantStatus" lay-skin="primary" title="查看详情" checked="">'''
        else:
            n_base[
                'grantsee'] = '''<input id="grantsee" type="checkbox" name="grantsee" lay-filter="grantStatus" lay-skin="primary" title="查看详情">'''
        if 'edit' in grant_list:
            n_base[
                'grantedit'] = '''<input id="grantedit" type="checkbox" name="grantedit" lay-filter="grantStatus" lay-skin="primary" title="编辑数据" checked="">'''
        else:
            n_base[
                'grantedit'] = '''<input id="grantedit" type="checkbox" name="grantedit" lay-filter="grantStatus" lay-skin="primary" title="编辑数据">'''
        if 'del' in grant_list:
            n_base[
                'grantdel'] = '''<input id="grantdel" type="checkbox" name="grantdel" lay-filter="grantStatus" lay-skin="primary" title="删除数据" checked="">'''
        else:
            n_base[
                'grantdel'] = '''<input id="grantdel" type="checkbox" name="grantdel" lay-filter="grantStatus" lay-skin="primary" title="删除数据">'''
        menu_obj = models.SysMenu.objects.filter(pid=0)
        for m in menu_obj.values('id', 'caption'):
            menu_dic[m['id']] = m['caption']
        menu_dic[0] = 'ROOT'
    else:
        ch_base = models.SysMenu.objects.filter(pid=menu_id)
        n_base['grantshow'] = '''<input type="checkbox" disabled lay-skin="primary" title="数据展示">'''
        n_base['grantsee'] = '''<input type="checkbox" disabled lay-skin="primary" title="查看详情">'''
        n_base['grantedit'] = '''<input type="checkbox" disabled lay-skin="primary" title="编辑数据">'''
        n_base['grantdel'] = '''<input type="checkbox" disabled lay-skin="primary" title="删除数据">'''
        menu_dic[0] = 'ROOT'
        if len(ch_base.values()) == 0:
            p_base1 = models.SysMenu.objects.filter(pid=base[0]['pid'])
            for p_id in p_base1.values('id', 'caption'):
                if p_id['caption'] != base[0]['caption']:
                    menu_dic[p_id['id']] = p_id['caption']
    return {'menu': menu_dic, 'data': n_base}


def log_page(request):
    page_num = int(request.GET.get('page', 1))
    bg_hs = int(request.GET.get('limit', 10))
    log_type = request.GET.get('log_key', None)
    if log_type != None and log_type != '':
        log_list = []
        all = models.SysLog.objects.filter(type=log_type).order_by('-time')
        ro_obj = all[(page_num - 1) * bg_hs:page_num * bg_hs]
        number = len(all.values()) - (page_num - 1) * bg_hs
        for r in ro_obj.values('accout', 'name', 'type', 'time', 'content', 'ip', 'address'):
            r['order'] = number
            number -= 1
            log_list.append(r)
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(all), 'data': log_list}
    else:
        ro_list = []
        all = models.SysLog.objects.all().order_by('-time')
        ro_obj = all[(page_num - 1) * bg_hs:page_num * bg_hs]
        num = len(all.values()) - (page_num - 1) * bg_hs
        for r in ro_obj.values('accout', 'name', 'type', 'time', 'content', 'ip', 'address'):
            r['order'] = num
            num -= 1
            ro_list.append(r)
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(all), 'data': ro_list}


def org_data(request):
    num = 0
    page_num = int(request.GET.get('page', 1))
    bg_hs = int(request.GET.get('limit', 10))
    org_id = request.GET.get('org_id', None)
    search = request.GET.get('serch_key', None)
    if org_id != None and search != None and search != '' and org_id != '':
        org_list = []
        u_id = models.SysUserOrg.objects.filter(org_id=org_id)
        for u in u_id.values():
            user_data = models.SysUser.objects.filter((Q(id=u['user_id']) | Q(name=search)) & ~Q(account='admin'))
            for ud in user_data.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level'):
                num += 1
                ud['order'] = num + (page_num - 1) * bg_hs
                user_org = models.SysUserOrg.objects.filter(user_id=ud['id']).order_by('id')
                for uorg in user_org.values('org_name'):
                    ud['org_name'] = uorg['org_name']
                org_list.append(ud)
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(org_list), 'data': org_list}
    else:
        if org_id != None and org_id != '':
            org_list1 = []
            u_id = models.SysUserOrg.objects.filter(org_id=org_id)
            for u1 in u_id.values():
                user_data = models.SysUser.objects.filter(Q(id=u1['user_id']) & ~Q(account='admin'))
                for ud1 in user_data.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level'):
                    num += 1
                    ud1['order'] = num + (page_num - 1) * bg_hs
                    user_org = models.SysUserOrg.objects.filter(Q(user_id=ud1['id']) & Q(org_id=org_id)).order_by('id')
                    for uorg in user_org.values('org_name'):
                        ud1['org_name'] = uorg['org_name']
                    org_list1.append(ud1)
            u_base1 = org_list1[(page_num - 1) * bg_hs:page_num * bg_hs]
            return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(org_list1), 'data': u_base1}
        elif search != None and search != '':
            sear = []
            if org_user_filter(request) != False:
                in_userid = org_user_filter(request)
                user_all = models.SysUser.objects.filter(
                    (Q(account__contains=search) | Q(name__contains=search)) & ~Q(account='admin') & Q(
                        id__in=in_userid)).order_by('id')
            else:
                user_all = models.SysUser.objects.filter(
                    (Q(account__contains=search) | Q(name__contains=search)) & ~Q(account='admin')).order_by('id')
            sear_base = user_all[(page_num - 1) * bg_hs:page_num * bg_hs]
            for se in sear_base.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level'):
                num += 1
                se['order'] = num + (page_num - 1) * bg_hs
                user_org = models.SysUserOrg.objects.filter(user_id=se['id']).order_by('id')
                for uorg in user_org.values('org_name'):
                    se['org_name'] = uorg['org_name']
                sear.append(se)
            return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(user_all), 'data': sear}
        else:
            li = []
            value = request.GET.get('0', None)
            if org_user_filter(request) != False:
                in_userid = org_user_filter(request)
                all = models.SysUser.objects.filter(~Q(account='admin') & Q(id__in=in_userid)).order_by('id')
            else:
                all = models.SysUser.objects.filter(~Q(account='admin')).order_by('id')
            aggregate = all[(page_num - 1) * bg_hs:page_num * bg_hs]
            for n in aggregate.values('account', 'name', 'gender', 'tell', 'email', 'address', 'id', 'level'):
                num += 1
                n['order'] = num + (page_num - 1) * bg_hs
                user_org = models.SysUserOrg.objects.filter(user_id=n['id']).order_by('id')
                for uorg in user_org.values('org_name'):
                    n['org_name'] = uorg['org_name']
                if value != None:
                    ex_obj = models.SysUserRole.objects.filter(rle_id=value, user_id=str(n['id']))
                    if len(ex_obj.values()):
                        n["LAY_CHECKED"] = True
                li.append(n)
            return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len(all), 'data': li}


def dickey_data(request, re_url):
    dic_list = []
    dic = {'code': 0, 'page_num': 1, 'bg_hs': 10, 'count': 0, 'data': []}
    serch_key = request.GET.get('serch_key', None)
    number = 0
    ckqx = call.see_grant(request, re_url)
    bjqx = call.edit_grant(request, re_url)
    scqx = call.delete_grant(request, re_url)
    if serch_key != None and serch_key != '':
        search_data = models.SysDicMain.objects.filter(Q(key__contains=serch_key) | Q(name__contains=serch_key))
        for sd in search_data.values('id', 'key', 'name'):
            number += 1
            dic_list.append({'id': sd['id'], 'order': number, 'key': sd['key'], 'name': sd['name'],
                             'sfkck': ckqx, 'sfkbj': bjqx, 'sfksc': scqx})
        dic['data'] = dic_list
        dic['count'] = len(search_data)
        return dic
    else:
        main_base = models.SysDicMain.objects.all()
        if len(main_base) > 0:
            for main in main_base.values('id', 'key', 'name'):
                number += 1
                dic_list.append(
                    {'id': main['id'], 'order': number, 'key': main['key'], 'name': main['name'], 'sfkck': ckqx,
                     'sfkbj': bjqx, 'sfksc': scqx})
            dic['data'] = dic_list
            dic['count'] = len(main_base)
        return dic


def dict_values(request, re_url):
    child_list = []
    number = 0
    re_key = request.GET.get('keyword', None)
    ckqx = call.see_grant(request, re_url)
    bjqx = call.edit_grant(request, re_url)
    scqx = call.delete_grant(request, re_url)
    child_data = {'code': 0, 'page_num': 1, 'bg_hs': 10, 'count': 0, 'data': []}
    if re_key == 'obtain':
        p_id = request.GET.get('base', None)
        all_data = models.SysDicFrom.objects.filter(p_id=eval(p_id)['id'])
        if len(all_data) > 0:
            for child in all_data.values('id', 'dic_key', 'dic_values').order_by('-create_time'):
                number += 1
                child['order'] = number
                child['sfkck'] = ckqx
                child['sfkbj'] = bjqx
                child['sfksc'] = scqx
                child_list.append(child)
            child_data['data'] = child_list
            child_data['count'] = len(all_data)
        return child_data
    else:
        all_data = models.SysDicFrom.objects.all()
        if len(all_data) > 0:
            for data in all_data.values('id', 'dic_key', 'dic_values').order_by('-create_time'):
                number += 1
                data['order'] = number
                data['sfkck'] = ckqx
                data['sfkbj'] = bjqx
                data['sfksc'] = scqx
                child_list.append(data)
            child_data['data'] = child_list
            child_data['count'] = len(all_data)
        return child_data


def child_insert(request, uid, now_time):
    re_url = request.POST.get('type', None)
    if call.is_edit_grant(request, re_url):
        dic_child_data = request.POST
        length = models.SysDicFrom.objects.filter(dic_key=dic_child_data['base[zdbm]'])
        if len(length) > 0:
            return False
        else:
            models.SysDicFrom.objects.create(id=uid, dic_key=dic_child_data['base[zdbm]'],
                                             p_id=dic_child_data['base[id]'], dic_values=dic_child_data['base[zdmc]'],
                                             create_time=now_time)
            call.create_log(request, 'create', '添加了字典参数', dic_child_data['base[zdmc]'])
            return True
    else:
        return 'no_right'


def main_insert(request, uid):
    re_url = request.POST.get('type', None)
    if call.is_edit_grant(request, re_url):
        dic_main_data = request.POST
        lang = models.SysDicMain.objects.filter(key=dic_main_data['base[csmc]'])
        if len(lang) > 0:
            return False
        else:
            models.SysDicMain.objects.create(id=uid, key=dic_main_data['base[csmc]'], name=dic_main_data['base[csms]'])
            call.create_log(request, 'create', '添加字典属性', dic_main_data['base[csms]'])
            return True
    else:
        return 'no_right'


def dic_msg(user_id):
    cur = connection.cursor()
    msg_dic = {}
    cur.execute(
        "select b.dic_key,b.dic_values from sys_dic_main a INNER JOIN sys_dic_from b on a.id = b.p_id where a.key='message'")
    msg_data = cur.fetchall()
    for msg in msg_data:
        msg_dic[msg[0]] = msg[1]
    info_data = models.SysInformation.objects.filter(Q(user_id=user_id) | Q(type=msg_dic['System'])).order_by('state',
                                                                                                              '-time')
    cur.close()
    return info_data


def dic_msg_num(user_id):
    cur = connection.cursor()
    msg_dic = {}
    cur.execute(
        "select b.dic_key,b.dic_values from sys_dic_main a INNER JOIN sys_dic_from b on a.id = b.p_id where a.key='message'")
    msg_data = cur.fetchall()
    for msg in msg_data:
        msg_dic[msg[0]] = msg[1]
    count = models.SysInformation.objects.filter((Q(user_id=user_id) | Q(type=msg_dic['System'])) & ~Q(state=1)).count()
    cur.close()
    return count


def feed_detail(request):
    re_id = request.GET.get('id', None)
    active_user = ''
    active_list = []
    data1 = models.SysFeedbackInfo.objects.filter(pid=re_id).order_by('-update_time')
    data_result = ''
    for da1 in data1.values('update_time', 'op_username', 'content', 'op_account'):
        image_data = models.SysUser.objects.filter(account=da1['op_account'])
        for image in image_data.values('url', 'name'):
            data_result += '''<dd><div class="layui-status-img"><a href="javascript:;"><img style="width: 32px;height: 32px;border-radius: 50px;"src=''' + \
                           image['url'] + '''></a></div><div style="margin-left: 10px;">''' + str(
                da1['update_time']) + ''' <<''' + da1['op_username'] + '''>>提交内容：''' + da1[
                               'content'] + '''</div></dd>'''
            if image['name'] not in active_list:
                active_user += '''<li class="list-item"><span class="title"><img style="width: 32px;height: 32px;border: 1px solid #c21515;border-radius: 50px;"src=''' + \
                               image[
                                   'url'] + '''></span><span class="footer" style ="margin-left: 15px;color: black;">''' + \
                               image['name'] + '''</span></li>'''
                active_list.append(image['name'])
    return {'data_result': data_result, 're_id': re_id, 'active_user': active_user}


def theme_detail(request):
    re_url = request.path_info
    acc = request.session['acc']
    class_dic = {'high': ':高', 'centre': '中', 'low': '低'}
    result0 = ''
    result1 = ''
    result2 = ''
    result3 = ''
    result4 = ''
    but = ''
    but1 = ''
    data0 = models.SysFeedback.objects.filter(state=0)
    # for D0 in data0.values('id', 'creat_account', 'creat_time', 'urgent', 'creat_username', 'title'):
    for D0 in data0.values('id', 'creat_account', 'creat_time', 'title'):
        but = '''<div style="width: 55px;"><button id="''' + D0[
            'id'] + '''" type="submit" class="layui-btn layui-btn-sm btu" lay-submit="" lay-filter="delete">删除</button></div>'''

        result0 += '''<dd><div class="layui-status-img"><a href="javascript:;"><img style="width: 32px;height: 32px;border-radius: 50px;"src=/static/images/new.png;''' + \
                   '''></a></div><div style="width: calc(100% - 85px);"><a id='0' style="color: #1e9fff;margin-left: 10px;" href="javascript:;">''' + \
                   str(D0['creat_time']) + '''【系统提示】：''' + \
                   D0['title'] + '''</a></div>''' + but + '''</dd>'''
    data1 = models.SysFeedback.objects.filter(state=1)
    # for D1 in data1.values('id', 'creat_account', 'creat_time', 'urgent', 'creat_username', 'title'):
    for D1 in data1.values('id', 'creat_account', 'creat_time', 'title'):
        if acc == D1['creat_account']:
            but1 = '''<div style="width: 110px;">
                                            <button id="''' + D1['id'] + '''" type="submit" class="layui-btn layui-btn-sm btu" lay-submit="" lay-filter="close">关闭</button>
                                            <button id="''' + D1['id'] + '''" type="submit" class="layui-btn layui-btn-sm btu" lay-submit="" lay-filter="delete">删除</button>
                                        </div>'''
        result1 += '''<dd><div class="layui-status-img"><a href="javascript:;"><img style="width: 32px;height: 32px;border-radius: 50px;"src=/static/images/new.png>''' + \
                   '''</a></div><div style="width: calc(100% - 145px);"><a style="color: #1e9fff;margin-left: 10px;" href="javascript:;">''' + \
                   str(
                       D1['creat_time']) + '''【系统提示】：''' + D1[
                       'title'] + '''</a></div>''' + but1 + '''</dd>'''
    data2 = models.SysFeedback.objects.filter(state=2)
    for D2 in data2.values('id', 'creat_time', 'title'):
        result2 += '''<dd><div class="layui-status-img"><a href="javascript:;"><img style="width: 32px;height: 32px;border-radius: 50px;"src=/static/images/end.png>''' + \
                   '''</a></div><div><a style="color: #1e9fff;margin-left: 10px;" href="javascript:;">''' + \
                   str(
                       D2['creat_time']) + '''【系统提示】：''' + D2[
                       'title'] + '''</a></div></dd>'''
    data3 = models.SysFeedback.objects.all()
    for D3 in data3.values('id', 'creat_time', 'title'):
        result3 += '''<dd><div class="layui-status-img"><a href="javascript:;"><img style="width: 32px;height: 32px;border-radius: 50px;"src=/static/images/all.png>''' + \
                   '''</a></div><div><a style="color: #1e9fff;margin-left: 10px;" href="javascript:;">''' + \
                   str(
                       D3['creat_time']) + '''【系统提示】：''' + D3[
                       'title'] + '''</a></div></dd>'''
    data4 = models.SysFeedbackInfo.objects.all().order_by('-update_time')[:10]
    for D4 in data4.values('pid', 'update_time', 'content'):
        stime = D4['update_time'].strftime('%H:%M:%S')
        data5 = models.SysFeedback.objects.filter(id=D4['pid'])
        for D5 in data5.values('title'):
            result4 += '''<li id="''' + D4['pid'] + '''" class="list-item"><a href = "/feedback_detail.html?id=''' + D4[
                'pid'] + '''" class="title">''' + stime + '''  </span><span class="footer">问题 ''' + D5[
                           'title'] + '''  有更新</a></li>'''
            result4 += '''<li id="''' + D4['pid'] + '''" class="list-item"><a href = "/feedback_detail.html?id=''' + D4[
                'pid'] + '''" class="title">''' + stime + '''  </span><span class="footer">问题 ''' + D5[
                           'title'] + '''  有更新</a></li>'''
    return {'url_data': re_url, 'result0': result0, 'result1': result1, 'result2': result2, 'result3': result3,
            'result4': result4, 'l': len(data0), 'l1': len(data1), 'l2': len(data2), 'l3': len(data3)}


def feed_detail_insert(request, data, uid, now_time):
    try:
        up_acc = request.session['acc']
        up_name = request.session['u']
        if data['key'] == 'insert_feedback_detail':
            models.SysFeedbackInfo.objects.create(id=uid(), pid=data['re_id'], update_time=now_time,
                                                  op_username=up_name, op_account=up_acc,
                                                  content=data['base[remark]'])
            stat_data = models.SysFeedback.objects.filter(id=data['re_id'])
            for stat in stat_data.values('state'):
                if stat['state'] == 0:
                    models.SysFeedback.objects.filter(id=data['re_id']).update(state=1)
            return True
        elif data['key'] == 'close':
            models.SysFeedback.objects.filter(id=data['base']).update(state=2)
            return True
        elif data['key'] == 'delete':
            creat_id = models.SysFeedback.objects.filter(id=data['base'])
            for creat in creat_id.values('creat_account'):
                if up_acc == creat['creat_account']:
                    models.SysFeedback.objects.filter(id=data['base']).delete()
                    models.SysFeedbackInfo.objects.filter(pid=data['base']).delete()
                else:
                    return False
            return True
    except:
        return False

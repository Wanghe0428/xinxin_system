#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time      :2019-11-18 9:26
# Author    :"wangjunlin"
from app import models
import datetime,uuid
import hashlib
from utils import call
import cv2,time
from treelib import Tree
from django.db.models import Q
from django.db import connection
import os,re,requests
from fake_useragent import UserAgent

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_loin_information(request):
    get_ip = get_client_ip(request)
    if get_ip != '127.0.0.1':
        try:
            sys_data = models.SysDicMain.objects.filter(key='system')
            pid = sys_data.values('id')[0]['id']
            sys_Fromdata = models.SysDicFrom.objects.filter(Q(p_id=pid) & Q(dic_key='ip_query'))
            url = sys_Fromdata.values('dic_values')[0]['dic_values']
            User_Agent = UserAgent().random
            headers = {'User-Agent': User_Agent}
            get_html = requests.get(url + get_ip + '.html', headers=headers)
            address_data = re.search('tab0_address.+</div>', get_html.text).group()[14:-6].split()
            get_address = address_data[1] + address_data[2]
        except:
            get_ip = None
            get_address = None
    else:
        get_address = '本地登录'
    request.session['ip'] = get_ip
    request.session['address'] = get_address

def now_time():
    time = datetime.datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")
    return time

def uid():
    uid = str (uuid.uuid1())
    suid = ''.join (uid.split ('-'))
    return suid

def dlfs_login(request):
    user = request.POST.get('account', None)
    pwd = request.POST.get('password', None)
    in_dense = hashlib.md5()
    in_dense.update(pwd.encode(encoding='utf-8'))
    if user == '' or pwd == '':
        return None
    else:
        mim = models.SysUser.objects.filter(account=user)
        pdqy = ''
        for i in mim.values('pwd', 'level', 'name', 'sfqy', 'id', 'url'):
            in_pwd = list(i.values())[0]
            pdqy = list(i.values())[3]
        if pdqy == 0:
            return 'stop'
        elif len(mim) == 0 or in_pwd != in_dense.hexdigest():
            return False
        else:
            get_loin_information(request)
            request.session['acc'] = user
            request.session['u'] = list(i.values())[2]
            request.session['level'] = list(i.values())[1]
            request.session['user_id'] = list(i.values())[4]
            request.session['url'] = list(i.values())[5]
            request.session['is_login'] = True
            request.session.set_expiry(60 * 60)
            login_ip = request.session['ip']
            login_address = request.session['address']
            models.SysLog.objects.create(id=call.uid(), accout=user, name=list(i.values())[2], type='login',
                                         time=now_time(), content=list(i.values())[2] + '登录系统', ip=login_ip, address=login_address)
            return True

def create_log(request,values,tex,name):
    u_name = request.session['u']
    account = request.session['acc']
    login_ip = request.session['ip']
    login_address = request.session['address']
    text = u_name + tex + '：《' + name + "》"
    models.SysLog.objects.create (id=uid(), accout=account, name=u_name, type=values, time=now_time(), content=text, ip=login_ip, address=login_address)

def create_Information(request,edit_id,val,text):
    u_name = request.session['u']
    values = now_time() +'《' + u_name +'》' + val
    models.SysInformation.objects.create(id=uid(),user_id=edit_id,content=values,state=0,type=text, time=now_time())

def is_login(request):
    try:
        request.session['is_login']
        return True
    except KeyError:
        return False

def is_grant(request,re_url):
    try:
        '''数据展示权限拦截器'''
        user_account = request.session['acc']
        url_id = models.SysMenu.objects.filter(url=re_url[1:])
        for uid in url_id.values('id'):
            m_id = uid['id']
        grant_result = models.SysUserGrant.objects.filter(
            Q(menu_id=m_id) & Q(user_account=user_account) & Q(grant_code='show'))
        if len(grant_result) > 0 or user_account == 'admin':
            return True
        else:
            return False
    except KeyError:
        return False

def is_edit_grant(request,re_url):
    try:
        '''数据编辑权限拦截器'''
        user_account = request.session['acc']
        url_id = models.SysMenu.objects.filter(url=re_url[1:])
        for uid in url_id.values('id'):
            m_id = uid['id']
        grant_result = models.SysUserGrant.objects.filter(
            Q(menu_id=m_id) & Q(user_account=user_account) & Q(grant_code='edit'))
        if len(grant_result) > 0 or user_account == 'admin':
            return True
        else:
            return False
    except KeyError:
        return False

def is_delete_grant(request,re_url):
    try:
        '''数据删除权限拦截器'''
        user_account = request.session['acc']
        url_id = models.SysMenu.objects.filter(url=re_url[1:])
        for uid in url_id.values('id'):
            m_id = uid['id']
        grant_result = models.SysUserGrant.objects.filter(
            Q(menu_id=m_id) & Q(user_account=user_account) & Q(grant_code='del'))
        if len(grant_result) > 0 or user_account == 'admin':
            return True
        else:
            return False
    except KeyError:
        return False

def is_see_grant(request,re_url):
    try:
        '''数据查看权限拦截器'''
        user_account = request.session['acc']
        url_id = models.SysMenu.objects.filter(url=re_url[1:])
        for uid in url_id.values('id'):
            m_id = uid['id']
        grant_result = models.SysUserGrant.objects.filter(
            Q(menu_id=m_id) & Q(user_account=user_account) & Q(grant_code='see'))
        if len(grant_result) > 0 or user_account == 'admin':
            return True
        else:
            return False
    except KeyError:
        return False

def create_menu(id):
    Parent = []
    Node = {}
    menu1 = ''
    menu2 = ''
    # 查询所有的PID
    for i in id:
        q_obj = models.SysMenu.objects.filter (id=i)
        for q in q_obj.values ('id', 'caption', 'lcon', 'url', 'pid'):
            if q['pid'] not in Parent:
                if q['pid'] != '0':
                    Parent.append (q['pid'])
                    if q['pid'] in id:
                        id.remove(q['pid'])
                else:
                    if q['pid'] not in Parent:
                        Parent.append (q['id'])
    #对一级节点进行排序
    ord_obj = models.SysMenu.objects.filter (pid='0').order_by('order')
    temp = []
    for no in ord_obj.values('id'):
        temp.append (no['id'])
    data = sorted(Parent, key=temp.index)#让一级节点Parent列表按照temp进行排序
    # 查询每个根节点下的所有子节点
    for p in data:
        Child = []
        p_obj = models.SysMenu.objects.filter (pid=p).order_by('order')
        for n in p_obj.values ('id'):
            Child.append (n['id'])
        # 求二级节点交集并按照Child列表进行排序
        Node[p] = sorted(list(set(id)&set(Child)),key=Child.index)
    menu = ''
    for k,v in Node.items():
        if v != []:
            # 如果父节点不是根节点，则查询节点下的所有子节点
            m_obj = models.SysMenu.objects.filter (id=k)
            for m in m_obj.values ('id', 'caption', 'lcon', 'url'):
                menu2 = "<li class='layui-nav-item'><a href='javascript:;'><i class='"  + 'fa '+ str (m['lcon']) + ' pad' + "'></i>" + str (
                    m['caption']) + "</a><dl  class='layui-nav-child'>"
            for v1 in v:
                v_obj = models.SysMenu.objects.filter (id=v1)
                for v2 in v_obj.values('id', 'caption', 'lcon', 'url'):
                    menu3 = "<dd><a href='javascript:;' data-url='" + str (v2['url']) + "' data-id='" + str (
                        v2['id']) + "' data-text=" + str (v2['caption']) + "><span style='margin-left:20px;' class='" + 'Submenu ' + 'fa ' + str (
                        v2['lcon']) + ' pad' + "'></span>" + str (v2['caption']) + "</a></dd>"
                    menu2 += menu3
            menu2 += "</dl></li>"
            menu += menu2
        else:
            # 如果父节点是根节点，则直接生成菜单
            ml_obj = models.SysMenu.objects.filter (id=k)
            for i in ml_obj.values ('id', 'caption', 'lcon', 'url'):
                menu1 = "<li class='layui-nav-item'><a href='javascript:;' data-url='" + str (
                    i['url']) + "' data-id='" + str (
                    i['id']) + "' data-text=" + str (i['caption']) + "><i class='" + 'fa '+ str (i['lcon']) + ' pad' + "'></i>" + str (
                    i['caption']) + "</a></li>"
            menu += menu1
    return menu

def user_org(request):
    cur = connection.cursor()
    '''组装当前用户的所属机构对应的树'''
    user_id = request.session['user_id']
    cur.execute("select b.id,b.org_name from sys_user_org a INNER JOIN sys_org b on(a.org_id = b.id) where a.user_id=%s and a.used=1",user_id)
    org_id = cur.fetchall()
    root_code = models.SysOrg.objects.filter(org_code='root')
    for root_id in root_code.values('id', 'pid'):
        pass
    tree = Tree()
    tree.create_node(identifier=root_id['id'])  # root node
    org_obj = models.SysOrg.objects.filter(~Q(pid=root_id['pid'])).order_by('great_date')
    for values in org_obj.values('id', 'org_name', 'pid'):
        tree.create_node(identifier=values['id'], parent=values['pid'])
    new_tree = tree.subtree(org_id[0][0])
    cur.close()
    return new_tree

def create_tree(request):
    cur = connection.cursor()
    # 使用python3的treelib插件，在进行字符串替换
    user_account = request.session['acc']
    not_list = []
    cur.execute ("select id from sys_org where id not in (select pid from sys_org)")
    not_in_pid = cur.fetchall()
    for i in not_in_pid:
        not_list.append(i[0])
    root_code = models.SysOrg.objects.filter(org_code='root')
    for root_id in root_code.values('id','pid'):
        pass
    tree = Tree()
    tree.create_node(identifier = root_id['id'])  # root node
    org_obj = models.SysOrg.objects.filter(~Q(pid=root_id['pid'])).order_by('great_date')
    for values in org_obj.values('id','org_name','pid'):
        tree.create_node(identifier=values['id'], parent=values['pid'])
    if user_account != 'admin':
        new_tree = user_org(request)
    else:
        new_tree = tree
    date=new_tree.to_json(with_data=False)
    org_obj1 = models.SysOrg.objects.filter()
    for values1 in org_obj1.values('id', 'org_name', 'pid'):
        dic = {}
        dic['title'] = values1['org_name']
        dic['id'] = values1['id']
        if values1['id'] in not_list:
            date = date.replace('"'+values1['id']+'"','{'+str(dic)[1:-1]+'}')
        else:
            date = date.replace('"' + values1['id'] + '"', str(dic)[1:-1])
    date = date.replace(": {", ",")
    date = date.replace("}}", "}")
    date = "[" + date + "]"
    cur.close()
    return date

def select_user_type(request):
    '''查询数据字典用户类型'''
    type_dic = {}
    dic_main = models.SysDicMain.objects.filter(key='user_type')
    for main in dic_main.values('id'):
        from_val = main['id']
    dic_from = models.SysDicFrom.objects.filter(p_id=from_val)
    for F in dic_from.values('dic_key','dic_values'):
        type_dic[F['dic_key']] = F['dic_values']
    return type_dic

def inser_user(request):
    data = request.POST
    # 查询账号是否存在
    ex_acc = models.SysUser.objects.filter (account=data['base[account]'])
    if len (ex_acc) == 0:
        # 判断两次密码是否一致
        if data['base[password2]'] == data['base[password3]']:
            dic_from = models.SysDicFrom.objects.filter(dic_key=data['user_type'])
            for F in dic_from.values('dic_values'):
                user_type = F['dic_values']
            dense = hashlib.md5 ()
            dense.update (data['base[password2]'].encode (encoding='utf-8'))
            models.SysUser.objects.create (id=uid(),account=data['base[account]'], name=data['base[name]'], pwd=dense.hexdigest (),
                                           gender=data['base[sex]'], tell=data['base[tell]'], email=data['base[email]'],
                                           address=data['base[address]'],level=user_type,sfcj=0,sfqy=1)
            org_id = data['base[select]'].split (",")
            for i in org_id:
                use = 0
                if org_id.index(i) == 0:
                    use = 1
                org_obj = models.SysOrg.objects.filter (id=i)
                u_id = models.SysUser.objects.filter (name=data['base[name]'])
                models.SysUserOrg.objects.create (id=uid(),org_id=i, org_name=org_obj.values ()[0]['org_name'],
                                                  user_id=u_id.values ()[0]['id'], user_name=data['base[name]'],used=use)
            create_log (request, 'create', '新增用户', data['base[name]'])
            return True
        else:
            return 'error_pwd'
    else:
        return 'exis_user'

def edit_user(request,edit_id):
    temp = request.POST
    if temp['base[password2]'] == temp['base[password3]']:
        if 'base[display]' in temp:
            sfqy = 1
        else:
            sfqy = 0
        edit_dense = hashlib.md5 ()
        edit_dense.update (temp['base[password2]'].encode (encoding='utf-8'))
        models.SysUser.objects.filter (id=temp['base[id]']).update (name=temp['base[name]'], pwd=edit_dense.hexdigest (),
                                                                    gender=temp['base[sex]'], tell=temp['base[tell]'],
                                                                    email=temp['base[email]'],
                                                                    address=temp['base[address]'],sfqy=sfqy)
        ex_uorg = models.SysUserOrg.objects.filter (user_id=temp['base[id]'])
        org_list = []
        for ex in ex_uorg.values ():
            org_list.append (ex['id'])
        org_b = temp['base[select]'].split (",")
        if len (org_list) > len (org_b):
            big = len (org_list)
        else:
            big = len (org_b)
        for u in range (0, big):
            is_used = 0
            if u == 0:
                is_used = 1
            if u + 1 <= len (org_b) and u + 1 <= len (org_list):
                org_obj = models.SysOrg.objects.filter (id=org_b[u])
                models.SysUserOrg.objects.filter (id=org_list[u]).update (org_id=org_b[u],
                                                                          org_name=org_obj.values ()[0]['org_name'],
                                                                          user_id=temp['base[id]'],
                                                                          user_name=temp['base[name]'],
                                                                          used = is_used)
            elif u + 1 > len (org_b):
                models.SysUserOrg.objects.filter (id=org_list[u]).delete ()
            elif u + 1 > len (org_list):
                org_obj1 = models.SysOrg.objects.filter (id=org_b[u])
                models.SysUserOrg.objects.create (id=uid(),org_id=org_b[u], org_name=org_obj1.values ()[0]['org_name'],
                                                  user_id=temp['base[id]'], user_name=temp['base[name]'],used = is_used)
        create_log (request, 'update', '修改用户', temp['base[name]'])
        dic_data = models.SysDicFrom.objects.filter(dic_key = 'ordinary')
        for dic in dic_data.values('dic_values'):
            pass
        create_Information(request,edit_id,' 修改了你的信息！',dic['dic_values'])
        return True
    else:
        return False

def ex_data(user_id):
    ob_list = []
    ex_obj = models.SysUserOrg.objects.filter(user_id=user_id)
    for ob in ex_obj.values():
        ob_data = {}
        ob_data['title'] = ob['org_name']
        ob_data['id'] = ob['org_id']
        ob_list.append(ob_data)
    return ob_list

def ex_btn(user_id):
    ob_list = []
    ex_obj = models.SysUserOrg.objects.filter(user_id=user_id)
    for ob in ex_obj.values():
        ob_list.append(ob['org_name'])
    return ob_list

def face_cj(request):
    re_base = request.POST
    if re_base['key'] == 'update':
        if 'base[close]' in re_base.keys():
            zt = 1
        else:
            zt =0
        try:
            models.SysImageSetting.objects.filter(edition=1).update(path=re_base['base[save_path]'],cjcs=re_base['base[cj_conut]'],jgsj=re_base['base[cj_time]'],temp_path=re_base['base[catalog]'],dqsj=re_base['base[login_time]'],sfqy=zt)
            return True
        except:
            return False
    elif re_base['key'] == '人脸采集':
        mim = models.SysImageSetting.objects.filter(edition=1)
        for m in mim.values('path', 'cjcs', 'jgsj'):
            d_path = list(m.values())[0]
            cjcs = list(m.values())[1]
            jgsj = list(m.values())[2]
        try:
            cap = cv2.VideoCapture(0)
            flag = cap.isOpened()
            dir_path = d_path + re_base['account'] + '/'
            ex_path = os.path.exists(dir_path)
            if ex_path == False:
                os.makedirs(dir_path)
            start_time = datetime.datetime.now()
            cnum = 1
            while (flag):
                ret, frame = cap.read()
                cv2.imshow("Capture_Paizhao", frame)
                end_time = datetime.datetime.now()
                cv2.waitKey(1) & 0xFF
                if (end_time - start_time).seconds >= jgsj * cnum:
                    cv2.imencode('.jpg', frame)[1].tofile(dir_path + re_base['account'] + str(cnum) + '.jpg')
                    time.sleep(1)
                    cnum += 1
                    if cnum > cjcs:
                        break
            cap.release()
            cv2.destroyAllWindows()
            if re_base['zt'] != '1':
                models.SysUser.objects.filter(id=re_base['id']).update(sfcj=1)
            return True
        except:
            cap.release()
            cv2.destroyAllWindows()
            return False

def ex_pwd_edit(request):
    pwd_data = request.POST
    if pwd_data['key'] == 'pwd_edit':
        old_pwd = pwd_data['base[old_password]']
        old_dense = hashlib.md5()
        old_dense.update(old_pwd.encode(encoding='utf-8'))
        p_data = models.SysUser.objects.filter(id=pwd_data['base[id]'])
        for md5_data in p_data.values('pwd'):
            pass
        if md5_data['pwd'] != old_dense.hexdigest():
            return False
        else:
            if pwd_data['base[password2]'] != pwd_data['base[password3]']:
                return None
            else:
                new_dense = hashlib.md5()
                new_dense.update(pwd_data['base[password2]'].encode(encoding='utf-8'))
                models.SysUser.objects.filter(id=pwd_data['base[id]']).update(pwd=new_dense.hexdigest())
        create_log(request, 'update', '修改了个人密码', '********')
        return True
    else:
        return 'illegal'

def upload_image(request):
    file = request.FILES.get('file')
    user_id = request.POST.get('id')
    curPath = os.path.abspath(os.path.dirname('static'))
    re_name = re.search('\..+', file.name).group()
    img_path = os.path.abspath(curPath + '/static/images/portrait/' + user_id + re_name)
    img_path_res = '/static/images/portrait/' + user_id + re_name
    f = open(img_path, 'wb')
    for i in file.chunks():
        f.write(i)
    f.close()
    models.SysUser.objects.filter(id=user_id).update(url=img_path_res)
    create_log(request,'update','上传了头像照片',file.name)

def see_grant(request,re_url):
    if call.is_see_grant(request,re_url):
        return 1
    else:
        return 0

def edit_grant(request,re_url):
    if call.is_edit_grant(request,re_url):
        return 1
    else:
        return 0

def delete_grant(request,re_url):
    if call.is_delete_grant(request,re_url):
        return 1
    else:
        return 0

def grant_creat(menu_id,role_id):
    models.SysGrant.objects.filter(menu_id=role_id['key']).delete()
    if 'base[grantshow]' in role_id:
        models.SysGrant.objects.create(id=uid(),menu_id=menu_id,menu_name=role_id['base[p_name]'],grant_code='show',menu_grant='数据展示')
    if 'base[grantsee]' in role_id:
        models.SysGrant.objects.create(id=uid(), menu_id=menu_id, menu_name=role_id['base[p_name]'], grant_code='see',menu_grant='查看详情')
    if 'base[grantedit]' in role_id:
        models.SysGrant.objects.create(id=uid(),menu_id=menu_id,menu_name=role_id['base[p_name]'],grant_code='edit',menu_grant='编辑数据')
    if 'base[grantdel]' in role_id:
        models.SysGrant.objects.create(id=uid(),menu_id=menu_id,menu_name=role_id['base[p_name]'],grant_code='del',menu_grant='删除数据')
    get_role_id = models.SysRole.objects.filter(caption='管理员')
    for get_id in get_role_id.values('id'):
        admin_id = get_id['id']
    models.SysRoleMenu.objects.create(id=uid(),role_id=admin_id,role_name='管理员',menu_id=menu_id,menu_name=role_id['base[p_name]'])

def grant_update(menu_base):
    models.SysGrant.objects.filter(menu_id=menu_base['base[menu_id]']).delete()
    if 'base[grantshow]' in menu_base:
        models.SysGrant.objects.create(id=uid(), menu_id=menu_base['base[menu_id]'], menu_name=menu_base['base[p_name]'], grant_code='show',menu_grant='数据展示')
    if 'base[grantsee]' in menu_base:
        models.SysGrant.objects.create(id=uid(), menu_id=menu_base['base[menu_id]'],menu_name=menu_base['base[p_name]'], grant_code='see', menu_grant='查看详情')
    if 'base[grantedit]' in menu_base:
        models.SysGrant.objects.create(id=uid(), menu_id=menu_base['base[menu_id]'],menu_name=menu_base['base[p_name]'], grant_code='edit', menu_grant='编辑数据')
    if 'base[grantdel]' in menu_base:
        models.SysGrant.objects.create(id=uid(), menu_id=menu_base['base[menu_id]'],menu_name=menu_base['base[p_name]'], grant_code='del', menu_grant='删除数据')

def upload_theme(request):
    file = request.FILES.get('file')
    str_name = uid()
    curPath = os.path.abspath(os.path.dirname('static'))
    re_name = re.search('\..+', file.name).group()
    img_path = os.path.abspath(curPath + '/static/images/' + str_name + re_name)
    img_path_res = '/static/images/' + str_name + re_name
    str_path = img_path.replace('\\','/')
    f = open(img_path, 'wb')
    for i in file.chunks():
        f.write(i)
    f.close()
    models.SysTheme.objects.create(id=uid(),state = 0,path =img_path_res,image_name=str_name + re_name,full_path=str_path,creat_data=now_time(),type=0)
    create_log(request,'create','上传了桌面壁纸',file.name)

def design_login(re_url,user_id):
    theme_image = models.SysTheme.objects.filter(state=1)
    for image in theme_image.values('path','type'):
        image_path = image['path']
    data = models.SysLoginSetting.objects.filter(state=0)
    if len(data) == 0:
        data = models.SysLoginSetting.objects.filter(state=1)
    for date in data.values('font_size', 'font_color', 'background_color', 'login_width', 'longin_height',
                            'move_window_right', 'move_window_down', 'but_color','inner_frame_width','move_inner_frame_right','move_inner_frame_down'):
        pass
    if image['type'] == 0:
        date['images'] = "background-image: url(" + image_path + ")"
    else:
        date['images'] = ""
        date['canvas'] = '''<canvas class="d1" id="canvas" class="d1"></canvas>'''
        date['js'] = '''<script src="../../static/js/script.js" ></script>'''
        date['cs'] = '''<link rel="stylesheet" href="../../static/css/style.css">'''
    date['url_data'] = re_url
    date['re_id'] = user_id
    date['move_window_right1'] = 'calc(' + date['move_window_right'] + '% - ' + str(int(date['login_width']) / 2) + 'px)'
    date['move_window_down1'] = 'calc(' + date['move_window_down'] + '% - ' + str(int(date['longin_height']) / 2) + 'px)'
    date['longin_height1'] = date['longin_height'] + 'px'
    date['login_width1'] = date['login_width'] + 'px'
    date['inner_frame_width1'] = date['inner_frame_width'] + 'px'
    date['inner_frame_width2'] = str(int(date['inner_frame_width'])+56) + 'px'
    date['move_inner_frame_right1'] = date['move_inner_frame_right'] + '%'
    date['move_inner_frame_right2'] = 'calc(' + date['move_inner_frame_right'] + '% + 48px)'
    date['move_inner_frame_down1'] = date['move_inner_frame_down'] + '%'
    date['move_inner_frame_down2'] = 'calc(' + date['move_inner_frame_down'] + '% + 60px)'
    date['move_inner_frame_down3'] = 'calc(' + date['move_inner_frame_down'] + '% + 130px)'
    date['move_inner_frame_down4'] = 'calc(' + date['move_inner_frame_down'] + '% + 190px)'
    date['font_size1'] = date['font_size'] + 'px'
    return date

def login_setting(request,re_date):
    data = models.SysLoginSetting.objects.filter(state=0)
    if len(data) > 0:
        for ex_id in data.values('id'):
            models.SysLoginSetting.objects.filter(id=ex_id['id']).update( user_id=re_date['re_id'],
                                                                          font_size=re_date['base[font]'],
                                                                          font_color=re_date['base[font_color]'],
                                                                          background_color=re_date['base[bj_color]'],
                                                                          login_width=re_date['base[wk_kd]'],
                                                                          longin_height=re_date['base[wk_gd]'],
                                                                          move_window_right=re_date['base[ck_yy]'],
                                                                          move_window_down=re_date['base[ck_xy]'],
                                                                          but_color=re_date['base[an_color]'],
                                                                          inner_frame_width=re_date['base[nk_kd]'],
                                                                          move_inner_frame_right=re_date['base[nk_yy]'],
                                                                          move_inner_frame_down=re_date['base[nk_xy]'],
                                                                          last_time=now_time(),
                                                                          state=0)
        create_log(request, 'edit', '修改了设置', '登录窗口')
    else:
        models.SysLoginSetting.objects.create(id=uid(), user_id=re_date['re_id'],
                                              font_size=re_date['base[font]'],
                                              font_color=re_date['base[font_color]'],
                                              background_color=re_date['base[bj_color]'],
                                              login_width=re_date['base[wk_kd]'],
                                              longin_height=re_date['base[wk_gd]'],
                                              move_window_right=re_date['base[ck_yy]'],
                                              move_window_down=re_date['base[ck_xy]'],
                                              but_color=re_date['base[an_color]'],
                                              inner_frame_width=re_date['base[nk_kd]'],
                                              move_inner_frame_right=re_date['base[nk_yy]'],
                                              move_inner_frame_down=re_date['base[nk_xy]'],
                                              last_time=now_time(),
                                              state=0)
        create_log(request, 'create', '添加了设置', '登录窗口')
    return True

def theme_setting(request,re_url,user_id):
    re_data = request.GET
    theme_image = models.SysTheme.objects.filter(id=re_data['image_id'])
    for image in theme_image.values('path','type'):
        image_path = image['path']
    data = models.SysLoginSetting.objects.filter(Q(user_id=user_id) & Q(state=0))
    if len(data) == 0:
        data = models.SysLoginSetting.objects.filter(state=1)
    for date in data.values('font_size', 'font_color', 'background_color', 'login_width', 'longin_height',
                            'move_window_right', 'move_window_down', 'but_color','inner_frame_width','move_inner_frame_right','move_inner_frame_down'):
        pass
    if image['type'] == 0:
        date['images'] = "background-image: url(" + image_path + ")"
    else:
        date['images'] = ""
        date['canvas'] = '''<canvas class="d1" id="canvas" class="d1"></canvas>'''
        date['js'] = '''<script src="../../static/js/script.js" ></script>'''
        date['cs'] = '''<link rel="stylesheet" href="../../static/css/style.css">'''
    date['url_data'] = re_url
    date['re_id'] = user_id
    date['move_window_right'] = 'calc(' + date['move_window_right'] + '% - ' + str(
        int(date['login_width']) / 2) + 'px)'
    date['move_window_down'] = 'calc(' + date['move_window_down'] + '% - ' + str(
        int(date['longin_height']) / 2) + 'px)'
    date['longin_height'] = date['longin_height'] + 'px'
    date['login_width'] = date['login_width'] + 'px'
    date['inner_frame_width1'] = date['inner_frame_width'] + 'px'
    date['inner_frame_width2'] = str(int(date['inner_frame_width'])+56) + 'px'
    date['move_inner_frame_right1'] = date['move_inner_frame_right'] + '%'
    date['move_inner_frame_right2'] = 'calc(' + date['move_inner_frame_right'] + '% + 48px)'
    date['move_inner_frame_down1'] = date['move_inner_frame_down'] + '%'
    date['move_inner_frame_down2'] = 'calc(' + date['move_inner_frame_down'] + '% + 60px)'
    date['move_inner_frame_down3'] = 'calc(' + date['move_inner_frame_down'] + '% + 130px)'
    date['move_inner_frame_down4'] = 'calc(' + date['move_inner_frame_down'] + '% + 190px)'
    date['font_size1'] = date['font_size'] + 'px'
    return date

def login_select():
    theme_image = models.SysTheme.objects.filter(state=1)
    for image in theme_image.values('path','type'):
        image_path = image['path']
    data = models.SysLoginSetting.objects.filter(state=0)
    if len(theme_image) == 0:
        data = models.SysLoginSetting.objects.filter(state=1)
    for date in data.values('font_size', 'font_color', 'background_color', 'login_width', 'longin_height',
                            'move_window_right', 'move_window_down', 'but_color','inner_frame_width','move_inner_frame_right','move_inner_frame_down'):
        pass
    if image['type'] == 0:
        date['images'] = "background-image: url(" + image_path + ")"
    else:
        date['images'] = ""
        date['canvas'] = '''<canvas class="d1" id="canvas" class="d1"></canvas>'''
        date['js'] = '''<script src="../../static/js/script.js" ></script>'''
        date['cs'] = '''<link rel="stylesheet" href="../../static/css/style.css">'''
    # date['images'] = "background-image: url(" + image_path + ")"
    date['move_window_right'] = 'calc(' + date['move_window_right'] + '% - ' + str(int(date['login_width']) / 2) + 'px)'
    date['move_window_down'] = 'calc(' + date['move_window_down'] + '% - ' + str(int(date['longin_height']) / 2) + 'px)'
    date['longin_height'] = date['longin_height'] + 'px'
    date['login_width'] = date['login_width'] + 'px'
    date['inner_frame_width1'] = date['inner_frame_width'] + 'px'
    date['inner_frame_width2'] = str(int(date['inner_frame_width'])+56) + 'px'
    date['move_inner_frame_right1'] = date['move_inner_frame_right'] + '%'
    date['move_inner_frame_right2'] = 'calc(' + date['move_inner_frame_right'] + '% + 48px)'
    date['move_inner_frame_down1'] = date['move_inner_frame_down'] + '%'
    date['move_inner_frame_down2'] = 'calc(' + date['move_inner_frame_down'] + '% + 60px)'
    date['move_inner_frame_down3'] = 'calc(' + date['move_inner_frame_down'] + '% + 130px)'
    date['move_inner_frame_down4'] = 'calc(' + date['move_inner_frame_down'] + '% + 190px)'
    date['font_size1'] = date['font_size'] + 'px'
    return date

def user_uesd_org(request,user_id):
    re_url = request.path_info
    cur = connection.cursor()
    '''获取当前用户的所有机构'''
    cur.execute(
        "select b.id,b.org_name from sys_user_org a INNER JOIN sys_org b on(a.org_id = b.id) where a.user_id=%s order by a.used desc",
        user_id)
    org_id = cur.fetchall()
    cur.close()
    org_dic = {}
    for org in org_id:
        org_dic[org[0]] = org[1]
    data = {'menu': org_dic, 'url_data': re_url}
    return data

def chang_used_org(request,user_id):
    change_org_id = request.POST.get('key', None)
    models.SysUserOrg.objects.filter(Q(org_id=change_org_id) & Q(user_id=user_id)).update(used=1)
    models.SysUserOrg.objects.filter(~Q(org_id=change_org_id) & Q(user_id=user_id)).update(used=0)
    return True
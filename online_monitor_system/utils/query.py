#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time      :2019-11-18 9:58
# Author    :"wangjunlin"
from utils import call
from app import models
# import face_recognition
import cv2,os,datetime
from django.db import connection
import uuid,json
from django.db.models import Q

def uid():
    uid = str (uuid.uuid1())
    suid = ''.join (uid.split ('-'))
    return suid

def creat_path():
    dqlj = os.path.abspath('manager')
    models.SysImageSetting.objects.filter(edition=1).update(path=dqlj[:-7]+"face\\",temp_path=dqlj[:-7]+"temp\\")

def now_time():
    n_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return n_time

def query_authority(acc):
    cur = connection.cursor()
    id = []
    cur.execute("select menu_id from sys_role_menu where role_id in(select rle_id from sys_user_role where user_id in (select id from sys_user where account = %s)) and menu_id not in (select id from sys_menu where pid in(select id from sys_menu where display=0) or display=0)",[acc])
    role_obj = cur.fetchall()
    if len(role_obj) != 0:
        '''拥有角色权限—>查询菜单'''
        for role_id in role_obj:
            id.append(role_id[0])
        menu_list = call.create_menu (list (set (id)))
        return menu_list
        cur.close()
    else:
        cur.close()
        '''没有角色权限，只有初级权限'''
        pass

def index_data(user_id):
    sys_name = 'SYSTEM'
    version = ""
    user_data = models.SysUser.objects.filter(id=user_id)
    for UD in user_data.values('account', 'level', 'name', 'sfqy', 'id', 'url'):
        pass
    m_list = query_authority(UD['account'])
    try:
        sys_data = models.SysDicMain.objects.filter(key = 'system')
        pid = sys_data.values('id')[0]['id']
        sys_data = models.SysDicFrom.objects.filter(Q(p_id=pid) & Q(dic_key ='system_name' ))
        for sys in sys_data.values('dic_values'):
            sys_name = sys['dic_values']
        version_data = models.SysDicFrom.objects.filter(Q(p_id=pid) & Q(dic_key ='version' ))
        for ver in version_data.values('dic_values'):
            version = ver['dic_values']
    except:
        pass
    if UD['url']==None:
        sys_image = models.SysDicFrom.objects.filter(Q(p_id = pid) & Q(dic_key='default_image'))
        UD['url'] = '/static/images/portrait/' + sys_image.values('dic_values')[0]['dic_values']
    data = {'user_id': UD['id'], 'username': UD['name'], 'level': UD['level'], 'm_list': m_list,
            'user_image': UD['url'], 'sys_name':sys_name,'version':version}
    return data

def detail_user(request,uid):
    cur = connection.cursor()
    cur.execute("select id,account,name,gender,address,tell,email,sfqy from sys_user where id = %s",[uid])
    user_data = cur.fetchall ()
    data = user_data[0]
    call.create_log (request, 'select', '查看用户', user_data[0][2])
    cur.close()
    return data

def P_role(request):
    cur = connection.cursor()
    role_base = request.POST.get ('key', None)
    user_base = request.POST.get ('base', None)
    user_base = eval(user_base)
    role_base = eval(role_base)
    cur.execute("select menu_id,role_name from sys_role_menu where role_id = %s",[role_base[0]])
    ro_data = cur.fetchall()
    data_list = []
    for d in ro_data:
        data_list.append(d[0])
    for r in user_base:
        if r in data_list:
            data_list.remove(r)
        else:
            cur.execute ("select id,caption from sys_menu where id = %s", [r])
            cd_data = cur.fetchall ()
            cd_list = list(cd_data[0])
            cur.execute ("insert into sys_role_menu (id,role_id,role_name,menu_id,menu_name) values (%s,%s,%s,%s,%s)",
                         [call.uid(),role_base[0], role_base[1], cd_list[0], cd_list[1]])
    for more in data_list:
        cur.execute("delete from sys_role_menu where role_id = %s and menu_id = %s",[role_base[0],more])
    cur.execute("select caption from sys_role where id = %s",[role_base[0]])
    r_cpa = cur.fetchall()
    call.create_log (request, 'update', '更新角色菜单', r_cpa[0][0])
    cur.close()

def G_role(request,u_id):
    cur = connection.cursor()
    re_list = []
    ex_list = []
    cur.execute ("select menu_id from sys_role_menu where role_id = %s", [u_id])
    ex_id = cur.fetchall ()
    for ex in ex_id:
        ex_list.append (ex[0])
    # 查询所有的菜单并组装菜单树
    user_id = request.session['user_id']
    user_acc = request.session['acc']
    all_list = []
    if user_acc != 'admin':
        cur.execute("select b.menu_id,b.menu_name from sys_user_role a INNER JOIN sys_role_menu b on a.rle_id = b.role_id where a.user_id=%s and b.role_id=%s",[user_id,u_id])
        all_menu = cur.fetchall()
        for all in all_menu:
            all_list.append(all[0])
    role_obj = models.SysMenu.objects.filter (pid=0).order_by('order')
    ex_pid = []
    for ro in role_obj.values ('id', 'caption'):
        if ro['id'] in all_list or user_acc == 'admin':
            id_obj = models.SysMenu.objects.filter (pid=ro['id']).order_by('order')
            id_list = []
            for id in id_obj.values ('id', 'caption'):
                if id['id'] in all_list or user_acc == 'admin':
                    id_dic = {}
                    ex_pid.append(ro['id'])
                    id_dic['title'] = id['caption']
                    id_dic['id'] = id['id']
                    id_dic['spread'] = 'true'
                    if id['id'] in ex_list:
                        id_dic['checked'] = 'true'
                    id_list.append (id_dic)
            re_dic = {}
            if ro['id'] not in ex_pid and ro['id'] in ex_list:
                re_dic['checked'] = 'true'
            re_dic['id'] = ro['id']
            re_dic['title'] = ro['caption']
            re_dic['field'] = ''
            re_dic['spread'] = 'true'
            re_dic['children'] = id_list
            re_list.append (re_dic)
    cur.close()
    return re_list

def tree(request):
    cur = connection.cursor()
    U_acc = request.session['acc']
    U_id = request.session['user_id']
    t_number = 0
    data_dic = {}
    re_list = []
    re_url = request.GET.get('type', None)
    ckqx = call.see_grant(request,re_url)
    bjqx = call.edit_grant(request, re_url)
    scqx =  call.delete_grant(request, re_url)
    # 查询所有的菜单并组装菜单树,并排序
    if U_acc != 'admin':
        id_list = []
        cur.execute("select menu_id from sys_role_menu where role_id in (select rle_id from sys_user_role where user_id =%s)",[U_id])
        mid = cur.fetchall()
        for m in mid:
            id_list.append(m[0])
        role_obj = models.SysMenu.objects.filter(id__in = id_list).order_by('order')
    else:
        role_obj = models.SysMenu.objects.all().order_by ('order')
    data_dic['msg'] = True
    data_dic['code'] = 0
    for ro in role_obj.values ('id', 'caption','lcon','url','order','pid','remark','display'):
        t_number += 1
        re_dic = {}
        re_dic['id'] = ro['id']
        re_dic['orderid'] = t_number
        re_dic['caption'] = ro['caption']
        re_dic['lcon'] = ro['lcon']
        re_dic['url'] = ro['url']
        re_dic['order'] = ro['order']
        re_dic['pid'] = ro['pid']
        re_dic['remark'] = ro['remark']
        re_dic['ckqx'] = ckqx
        re_dic['bjqx'] = bjqx
        re_dic['scqx'] = scqx
        if ro['display'] == 1:
            re_dic['display'] = '显示'
        else:
            re_dic['display'] = '影藏'
        re_list.append(re_dic)
    data_dic['count'] = len (re_list)
    data_dic['data'] = re_list
    cur.close()
    return data_dic

def G_roleid(request):
    cur = connection.cursor()
    role_id = []
    cur.execute ("select id from sys_menu order by id")
    ro_id = cur.fetchall ()
    for re in ro_id:
        role_id.append(re[0])
    cur.close()
    return role_id

# def ex_jc(request,cap):
#     flag = cap.isOpened()
#     '''临时目录路径'''
#     temp_path = models.SysImageSetting.objects.filter(edition=1)
#     for tmp in temp_path.values('temp_path', 'dqsj', 'path', 'cjcs'):
#         dir_path = list(tmp.values())[0]
#         tep_jgsj = list(tmp.values())[1]
#         path = list(tmp.values())[2]
#         lrcs = list(tmp.values())[3]
#     ex_path = os.path.exists(dir_path)
#     if ex_path == False:
#         os.mkdir(dir_path)
#     start_time = datetime.datetime.now()
#     while (flag):
#         ret, frame = cap.read()
#         cv2.imshow("Capture_Paizhao", frame)
#         end_time = datetime.datetime.now()
#         cv2.waitKey(1) & 0xFF
#         if (end_time - start_time).seconds >= tep_jgsj:
#             cv2.imencode('.jpg', frame)[1].tofile(dir_path + 'image' + '.jpg')
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     list1_name = []
#     images_base = []
#     ex_path1 = os.path.exists(path)
#     if ex_path1 == False:
#         os.mkdir(path)
#     list_p = os.listdir(path)
#     for p in range(0, len(list_p)):
#         list_name = []
#         filename1 = os.path.splitext(list_p[p])[0]
#         path_c = path + filename1 + '/'
#         list1_name.append(filename1)
#         list_one = os.listdir(path_c)
#         if len(list_one) == lrcs:
#             for i1 in range(0, lrcs):
#                 filename = ''.join(os.path.splitext(list_one[i1]))
#                 list_name.append(filename)
#         else:
#             list1_name.remove(filename1)
#         for i2 in list_name:
#             exist_image = face_recognition.load_image_file(path_c + str(i2))
#             jobs_encoding = face_recognition.face_encodings(exist_image)[0]
#             images_base.append(jobs_encoding)
#     current_image = face_recognition.load_image_file(dir_path + 'image.jpg')
#     try:
#         current_encoding = face_recognition.face_encodings(current_image)[0]
#         results = face_recognition.compare_faces(images_base, current_encoding)
#         for r in range(0, len(results)):
#             if results[r] == True:
#                 login_account = list1_name[int(r / lrcs)]
#                 account_search = models.SysUser.objects.filter(account=login_account,sfqy=1)
#                 if len(account_search) > 0:
#                     for mode_ures in account_search.values('pwd', 'level', 'name','id','url'):
#                         request.session['acc'] = login_account
#                         request.session['u'] = list(mode_ures.values())[2]
#                         request.session['level'] = list(mode_ures.values())[1]
#                         request.session['is_login'] = True
#                         request.session['user_id'] = list(mode_ures.values())[3]
#                         request.session['url'] = list(mode_ures.values())[4]
#                         request.session.set_expiry(60 * 60)
#                         models.SysLog.objects.create(id=call.uid(), accout=login_account, name=list(mode_ures.values())[2],
#                                                      type='login',
#                                                      time=now_time(), content=list(mode_ures.values())[2] + '使用人脸识别登录系统')
#                     call.get_loin_information(request)
#                     return True
#                 else:
#                     return ('account_stop')
#             if True not in results:
#                 return False
#     except:
#         return None

# def face_login(request):
#     try:
#         cap = cv2.VideoCapture(0)
#         base = ex_jc(request, cap)
#         return base
#     except:
#         try:
#             cap = cv2.VideoCapture(1)
#             base = ex_jc(request, cap)
#             return base
#         except:
#             return 'No_cameras'

def change_grant(request):
    '''给用户赋权'''
    re_url = request.POST.get('type', None)
    if call.is_edit_grant(request,re_url):
        grant_key = request.POST.get('key', None)
        grant_state = request.POST.get('base', None)
        choosed_user = request.POST.get('user_data', None)
        choosed_menu = request.POST.get('menu_state', None)
        choosed_menu_id = json.loads(choosed_menu)
        for loop in json.loads(choosed_user):
            choosed_user_id = loop['id']
            choosed_user_account = loop['account']
            choosed_user_name = loop['name']
            grant_base = models.SysGrant.objects.filter(Q(grant_code=grant_key) & Q(menu_id=choosed_menu_id))
            for gb in grant_base.values('id', 'grant_code', 'menu_grant','menu_name'):
                if grant_state == 'true':
                    ex_grant_data=models.SysUserGrant.objects.filter(Q(user_id=choosed_user_id,menu_id=choosed_menu_id,grant_code=gb['grant_code'],grant_name=gb['menu_grant']))
                    if len(ex_grant_data)==0:
                        models.SysUserGrant.objects.create(id=uid(),user_id=choosed_user_id,user_account=choosed_user_account,user_name=choosed_user_name,menu_id=choosed_menu_id,menu_name=gb['menu_name'],grant_id=gb['id'],grant_code=gb['grant_code'],grant_name=gb['menu_grant'])
                else:
                    models.SysUserGrant.objects.filter(Q(user_id=choosed_user_id,menu_id=choosed_menu_id,grant_code=gb['grant_code'],grant_name=gb['menu_grant'])).delete()
        return True
    else:
        return False

def menu_tree(request,acc):
    cur = connection.cursor()
    search = request.GET.get('keyword', None)
    page_num = int (request.GET.get ('page', 1))
    bg_hs = int (request.GET.get ('limit', 5))
    re_url = request.GET.get('type', None)
    if search == 'obtain':
        '''点击用户获取权限'''
        grant_code = str(call.edit_grant(request,re_url))
        quest_date = request.GET.get('base', None)
        quest_date = json.loads(quest_date)
        t_number = 0
        re_list = []
        cur.execute("select id,caption from sys_menu where id in (select menu_id from sys_role_menu where role_id in(select rle_id from sys_user_role where user_id in (select id from sys_user where account = %s)) and menu_id not in (select id from sys_menu where pid in(select id from sys_menu where display=0) or display=0) and menu_id not in (select pid from sys_menu)) order by `order`",[acc])
        pid_list = cur.fetchall()
        pid_list1 = pid_list[(page_num - 1) * bg_hs:page_num * bg_hs]
        for p_id in pid_list1:
            p_dic = {}
            t_number += 1
            p_dic['id'] = p_id[0]
            p_dic['caption'] = p_id[1]
            p_dic['orderid'] = (page_num - 1) * bg_hs + t_number
            p_dic['shownumber'] = '2'
            p_dic['seenumber'] = '2'
            p_dic['editnumber'] = '2'
            p_dic['delnumber'] = '2'
            cur.execute("select grant_code from sys_user_grant where user_id=%s and menu_id=%s",[quest_date['id'],p_id[0]])
            mg_menu=cur.fetchall()
            ex_zt = models.SysGrant.objects.filter(menu_id=p_id[0])
            for ex_id in ex_zt.values('grant_code'):
                d_name = ex_id['grant_code'] + 'number'
                p_dic[d_name] = '0'
            if len(mg_menu)>0:
                for m in mg_menu:
                    dic_name = m[0]+'number'
                    p_dic[dic_name] ='1'
            p_dic['grant_code'] = grant_code
            re_list.append(p_dic)
        cur.close()
        return {"code": 0,'count': len (pid_list), 'data': re_list}
    else:
        '''进入页面时获取所有菜单的权限'''
        grant_code = str(call.edit_grant(request,re_url))
        t_number = 0
        data_dic = {}
        re_list = []
        data_dic['msg'] = True
        data_dic['code'] = 0
        cur.execute("select menu_id from sys_role_menu where role_id in(select rle_id from sys_user_role where user_id in (select id from sys_user where account = %s)) and menu_id not in (select id from sys_menu where pid in(select id from sys_menu where display=0) or display=0) and menu_id not in (select pid from sys_menu)",[acc])
        pid_list = cur.fetchall()
        p_list = []
        for p_id in pid_list:
            p_list.append(p_id[0])
        if search !='' and search !=None:
            role_data = models.SysMenu.objects.filter(id__in = p_list).filter(caption=search).order_by('order')
            role_obj = role_data[(page_num - 1) * bg_hs:page_num * bg_hs]
        else:
            role_data = models.SysMenu.objects.filter(id__in = p_list).order_by('order')
            role_obj = role_data[(page_num - 1) * bg_hs:page_num * bg_hs]
        for ro in role_obj.values ('id', 'caption'):
            id_list = []
            t_number += 1
            re_dic = {}
            re_dic['id'] = ro['id']
            re_dic['caption'] = ro['caption']
            re_dic['orderid'] = (page_num - 1) * bg_hs + t_number
            ex_zt = models.SysGrant.objects.filter(menu_id = ro['id'])
            for ex_id in ex_zt.values ('grant_code'):
                id_list.append(ex_id['grant_code'])
            re_dic['shownumber'] = '2'
            re_dic['seenumber'] = '2'
            re_dic['editnumber'] = '2'
            re_dic['delnumber'] = '2'
            if 'show' in id_list:
                re_dic['shownumber'] = '0'
            if 'see' in id_list:
                re_dic['seenumber'] = '0'
            if 'edit' in id_list:
                re_dic['editnumber'] = '0'
            if 'del' in id_list:
                re_dic['delnumber'] = '0'
            re_dic['grant_code'] = grant_code
            re_list.append(re_dic)
        cur.close()
        return {"code": 0, 'page_num': page_num, 'bg_hs': bg_hs, 'count': len (role_data), 'data': re_list}

def creat_theme(request,re_url):
    data_dic = {}
    str_data =''
    theme = models.SysTheme.objects.all().order_by('-creat_data')
    for th in theme.values('id','path','state','type'):
        if th['type'] == 0:
            tplx = '预览'
            ys = " layui-btn-warm"
        else:
            tplx = '动态预览'
            ys = " dynamic"
        if th['state'] == 1:
            if call.see_grant(request, re_url):
                sfkck = "layui-btn " + ys
                ck_filter = "detail"
            else:
                sfkck = "layui-btn layui-btn-disabled"
                ck_filter = ""
            if call.is_edit_grant(request, re_url):
                sfkbj = "layui-btn layui-btn-normal"
                US_filter = ""
            else:
                sfkbj = "layui-btn layui-btn-disabled"
                US_filter = ""
            if call.is_delete_grant(request, re_url):
                sfksc = "layui-btn layui-btn-disabled layui-btn-danger"
                SC_filter = ""
            data_dic[th['id']] = th['path']
            str_data += '''<li class="ad"><img class="layui-upload-img index_image" id=''' + th['id'] + ''' style="height: 200px;width: 300px;" src=''' + \
                        th['path'] + '''><div class="code ma"><button lay-submit id=''' + th['id'] + ''' class="'''+ sfkck +'''" lay-filter=''' + ck_filter + '''>'''+ tplx +'''</button><button lay-submit id=''' + th[
                            'id'] + ''' class="''' + sfkbj + '''" lay-filter=''' + US_filter + '''>使用中</button><button lay-submit id=''' + th['id'] + ''' class="'''+ sfksc +'''" lay-filter=''' + SC_filter + '''>删除</button></div></li>'''
        else:
            if call.see_grant(request, re_url):
                sfkck = "layui-btn" + ys
                ck_filter = "detail"
            else:
                sfkck = "layui-btn layui-btn-disabled"
                ck_filter = ""
            if call.is_edit_grant(request, re_url):
                sfkbj = "layui-btn"
                US_filter = "adminInfo"
            else:
                sfkbj = "layui-btn layui-btn-disabled"
                US_filter = ""
            if call.is_delete_grant(request, re_url):
                sfksc = "layui-btn layui-btn-danger"
                SC_filter = "delete"
            else:
                sfksc = "layui-btn layui-btn-disabled layui-btn-danger"
                SC_filter = ""
            str_data += '''<li class="ad"><img class="layui-upload-img index_image"  id=''' + th['id'] + ''' style="height: 200px;width: 300px;" src=''' + th['path'] + '''><div class="code ma"><button lay-submit id=''' + th['id'] + ''' class="'''+ sfkck +'''" lay-filter=''' + ck_filter + '''>'''+ tplx +'''</button><button lay-submit id=''' + th['id'] + ''' class="'''+ sfkbj +'''" lay-filter=''' + US_filter + '''>设为壁纸</button><button lay-submit id=''' + th['id'] + ''' class="'''+ sfksc +'''" lay-filter=''' + SC_filter + '''>删除</button></div></li>'''
    return str_data

def menu_theme(request, re_url):
    if call.is_edit_grant(request, re_url):
        menu_str = '''<div class="layui-upload-list" style="text-align: center"><button type="button ma" class="layui-btn image_button" id="theme_image">上传图片</button><button lay-submit="" class="layui-btn mbuttn" lay-filter="refresh">刷新</button></div>'''
    else:
        menu_str = '''<div class="layui-upload-list" style="text-align: center"><button type="button ma" class="layui-btn image_button layui-btn-disabled">上传图片</button><button lay-submit="" class="layui-btn mbuttn" lay-filter="refresh">刷新</button></div>'''
    return menu_str

def creat_feed(request):
    acc = request.session['acc']
    name = request.session['u']
    uu = uid()
    data = request.POST
    try:
        models.SysFeedback.objects.create(id=uu, creat_time=now_time(), urgent=data['base[urgent]'],
                                          creat_account=acc, creat_username=name, title=data['base[title]'], state=0)
        models.SysFeedbackInfo.objects.create(id=uid(), pid=uu, update_time=now_time(), op_username=name,
                                              op_account=acc, content=data['base[remark]'])
        return True
    except:
        return False

def feed_detail_insert(request,data):
    try:
        up_acc = request.session['acc']
        up_name = request.session['u']
        if data['key'] == 'insert_feedback_detail':
            models.SysFeedbackInfo.objects.create(id=uid(), pid=data['re_id'], update_time=now_time(),
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
                    return True
                else:
                    return False
    except:
        return False
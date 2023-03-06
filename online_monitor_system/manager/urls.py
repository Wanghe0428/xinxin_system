"""manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^index.html', views.index),
    url(r'^login.html', views.login),
    url(r'^home.html', views.home),
    url(r'^live.html', views.live),
    url(r'^rtmp.html', views.rtmp),
    url(r'^design.html', views.design),
    url(r'^design_submit', views.design_submit),
    url(r'^theme.html', views.theme),
    url(r'^theme_use.html', views.theme_use),
    url(r'^theme_detail.html', views.theme_detail),
    url(r'^theme_delete.html', views.theme_delete),
    url(r'^theme_upload', views.theme_upload),
    url(r'^role.html', views.role),
    url(r'^role_user.html', views.role_user),
    url(r'^role_insert.html', views.role_insert),
    url(r'^role_edit.html', views.role_edit),
    url(r'^role_del.html', views.role_del),
    url(r'^role_menu.html', views.role_menu),
    url(r'^menu_edit.html', views.menu_edit),
    url(r'^menu.html', views.menu),
    url(r'^menu_insert.html', views.menu_insert),
    url(r'^menu_detail.html', views.menu_detail),
    url(r'^menu_del.html', views.menu_del),
    url(r'^user.html', views.user),
    url(r'^user_insert.html', views.user_insert),
    url(r'^user_detail.html', views.user_detail),
    url(r'^user_edit.html', views.user_edit),
    url(r'^user_del.html', views.user_del),
    url(r'^user_data.html', views.user_data),
    url(r'^role_data.html', views.role_data),
    url(r'^menu_data.html', views.menu_data),
    url(r'^log.html', views.log),
    url(r'^log_data.html', views.log_data),
    url(r'^position.html', views.position),
    url(r'^org_add.html', views.org_add),
    url(r'^org_edit.html', views.org_edit),
    url(r'^org_del.html', views.org_del),
    url(r'^org_data.html', views.org_data),
    url(r'^face_gather.html', views.face_gather),
    url(r'^data_rights.html', views.data_rights),
    url(r'^data_rights.html', views.data_rights),
    url(r'^menu_grant.html', views.menu_grant),
    url(r'^403.html', views.no_permission),
    url(r'^single.html', views.single),
    url(r'^pwd_edit.html', views.pwd_edit),
    url(r'^image_upload', views.image_upload),
    url(r'^dictionary.html', views.dictionary),
    url(r'^dictkey_data', views.dictkey_data),
    url(r'^dictvalues_data', views.dictvalues_data),
    url(r'^dict_main_insert.html', views.dict_main_insert),
    url(r'^dict_main_edit.html', views.dict_main_edit),
    url(r'^dict_main_detail.html', views.dict_main_detail),
    url(r'^dict_main_delete', views.dict_main_delete),
    url(r'^dic_child_insert.html', views.dic_child_insert),
    url(r'^dic_child_edit.html', views.dic_child_edit),
    url(r'^dic_child_detail.html', views.dic_child_detail),
    url(r'^dic_child_delete', views.dic_child_delete),
    url(r'^information.html', views.information),
    url(r'^information_data', views.information_data),
    url(r'^information_del.html', views.information_del),
    url(r'^information_batch_del', views.information_batch_del),
    url(r'^information_batch_read', views.information_batch_read),
    url(r'^information_update.html', views.information_update),
    url(r'^feedback.html', views.feedback),
    url(r'^creat_feedback.html', views.creat_feedback),
    url(r'^feedback_detail.html', views.feedback_detail),
    url(r'^insert_feedback_detail', views.insert_feedback_detail),
    url(r'^change_org.html', views.change_org),
    # 新加页面
    url(r'^resource_manage.html', views.resource_manage),
    url(r'^online_observe.html', views.online_observe),
    url(r'^title.html', views.title),
    url(r'^about.html', views.about),
    url(r'^data_Visualization.html', views.data_Visualization),
]

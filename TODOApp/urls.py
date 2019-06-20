
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls import url
from todo.views import *

urlpatterns = [
    #url(r'^profiles/new/$', NewUserProfileView.as_view(), name="ADD-Task"),             #add Task
    #url(r'^users/(?P<pk>\d+)/edit/$', EditUserProfileView.as_view(), name="edit-TASK"),         #edit task
    #url(r'^add_Task/$', NewUserProfileView.as_view(), name="ADD-Task"),
    url(r'^add_Task/$', add_Task ,name ='add_Task'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^general/addTask/$', add ,name ='add'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', home, name='home'),
    url(r'^general/$', general, name='general'),
    url(r'^todo/(?P<items_id>[0-9]+)/$', detail, name='detail'),
    url(r'^add_Task/$', add_Task, name='add_Task'),
    url(r'^todoedit/(?P<items_id>[0-9]+)/$', genral_delete, name='genral_delete'),
    url(r'^(?P<items_id>[0-9]+)EDIT/$', edit_task, name='edit_task'),                            #NotWorking


]

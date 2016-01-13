from django.conf.urls import url
from django.contrib import admin
from students import views as students_views

urlpatterns = [
    # Students urls
    url(r'^$', students_views.students_list, name='home'),
    url(r'^students/add/$',  students_views.students_add,
         name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$',
         students_views.students_edit,
         name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$',
         students_views.students_delete,
         name='students_delete'),

    # Groups urls
    url(r'^groups/$', students_views.groups_list, name='groups'),
    url(r'^groups/add/$',students_views.groups_add,
         name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', students_views.groups_edit,
         name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', students_views.groups_delete,
         name='groups_delete'),

    url(r'^admin/', admin.site.urls),
]


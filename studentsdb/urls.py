from django.conf.urls import url
from django.contrib import admin
from students import views as students_views

urlpatterns = [
    # Students urls
    url(r'^$', students_views.students_list, name='home'),
    url(r'^students/add/$',  students_views.students_add,
         name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
         students_views.StudentUpdateView.as_view(),
         name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',
         students_views.StudentDeleteView.as_view(),
         name='students_delete'),

    # Groups urls
    url(r'^groups/$', students_views.groups_list, name='groups'),
    url(r'^groups/add/$',students_views.groups_add,
         name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', students_views.groups_edit,
         name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', students_views.groups_delete,
         name='groups_delete'),
    # One-group url
    url(r'^group/(?P<gid>\d+)/$', students_views.group_view),

    url(r'^admin/', admin.site.urls),
]


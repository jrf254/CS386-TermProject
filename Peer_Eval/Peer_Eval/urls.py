from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
from Peer_Eval.admin import manager_admin, project_admin
#admin.autodiscover()
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples
    # lo
    # url(r'^$', 'Peer_Eval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^manageradmin/', include(manager_admin.urls)),
    url(r'^projectadmin/', include(project_admin.urls)),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', splash),
    url(r'^home/', home),
    url(r'^available/', available),
    url(r'^submitted/', submitted),
    url(r'^login/', log_in),
    url(r'^logout/', log_out),
    url(r'^create_user/', create_user),
    url(r'^base/', base),
   url(r'^dynamic_forms/',include('dynamic_forms.urls', namespace='dynamic_forms')),

)
urlpatterns += staticfiles_urlpatterns()

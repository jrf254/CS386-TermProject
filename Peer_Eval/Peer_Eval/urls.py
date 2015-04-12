from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples
    # url(r'^$', 'Peer_Eval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', splash),
    url(r'^home/', home),
    url(r'^login/', log_in),
    url(r'^logout/', log_out),
    url(r'^create_user/', create_user),
    url(r'^base/', base),
   # url(r'^dynamic_forms/',include('dynamic_forms.urls', namespace='dynamic_forms')),

)
urlpatterns += staticfiles_urlpatterns()

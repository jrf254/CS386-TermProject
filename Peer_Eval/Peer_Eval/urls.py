from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Peer_Eval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', splash),
    url(r'^home/', home),
    url(r'^login/', login),
    url(r'^logout/', logout),

)

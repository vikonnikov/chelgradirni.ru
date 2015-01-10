from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chelgradirni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)

try:
    import local_urls
except ImportError:
    pass
else:
    urlpatterns += local_urls.urlpatterns

urlpatterns += patterns('core.views',
    (r'^(?P<url>.*?/)$', 'flatpage'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chelgradirni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^google5a5a66ed4665c7ff.html$', 'core.views.google_verification'),
    url(r'^yandex_689db1240a05a501.txt$', 'core.views.yandex_verification'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {
        'flatpages': FlatPageSitemap}}),
    url(r'^robots.txt$', 'core.views.robots'),
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

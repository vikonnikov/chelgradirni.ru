from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chelgradirni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = +patterns('',
    # ... the rest of your URLconf goes here ...
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('apps.base.views',
    url(r'^$', 'home', name='home'),
)

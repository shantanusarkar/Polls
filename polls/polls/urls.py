from django.conf.urls import patterns, include, url
from polls_app import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'polls_app.views.home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls_app/', include('polls_app.urls', namespace = "polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'polls_app.views.IndexView')
)

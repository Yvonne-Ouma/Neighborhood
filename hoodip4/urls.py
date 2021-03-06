from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^business/$', views.business, name='business'),
    url(r'^neighborhood/$', views.neighborhood, name='neighborhood'),
    url(r'^search/$', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

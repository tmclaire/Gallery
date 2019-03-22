from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.photos_of_day,name = 'welcome'),
    url('^$',views.photos_of_day,name='photosToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)', views.location, name='location'),
    url(r'^share/(\d+)', views.share, name='share')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

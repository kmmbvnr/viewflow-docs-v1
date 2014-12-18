from django.conf.urls import include, url
from django.contrib import admin


def serve(request):
    pass


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', serve)
]

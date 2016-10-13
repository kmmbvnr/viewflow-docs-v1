import os

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import Http404
from django.views import static


BotNames = [
    'Googlebot', 'Slurp', 'Twiceler', 'msnbot', 'KaloogaBot',
    'YodaoBot', '"Baiduspider', 'googlebot', 'Speedy Spider',
    'DotBot', 'YandexBot']

OpenPages = [
    "_build/index.html",
    "_build/introduction.html",
    '_build/material_admin.html',
    '_build/admin_customization.html',
    '_build/admin_quickstart.html',
    '_build/admin_unsupported.html',
    '_build/material_forms.html',
    '_build/forms_quickstart.html',
    '_build/forms_templatetags.html',
    '_build/forms_layout.html',
    '_build/forms_formsets.html',
    '_build/material_frontend.html',
]


def is_crawler(request):
    user_agent = request.META.get('HTTP_USER_AGENT', None)

    for botname in BotNames:
        if botname in user_agent:
            return True

    return False


def serve(request):
    file_name = ""

    if request.path == '/':
        file_name = "_build/index.html"
    elif request.path.endswith('.html'):
        file_name = '_build/{}'.format(request.path.rsplit('/', 1)[-1])
    elif request.path.startswith('/_images/') and request.path.endswith('.png'):
        file_name = '_build/_images/{}'.format(request.path.rsplit('/', 1)[-1])
    elif request.path.endswith('.js') or request.path.endswith('.css') or request.path.endswith('.png'):
        file_name = '_build/_static/{}'.format(request.path.rsplit('/', 1)[-1])

    # if file_name.endswith('.html') and not request.user.is_authenticated():
    #    if file_name not in OpenPages and not is_crawler(request):
    #        file_name = "_build/login.html"

    absolute_path = os.path.join(settings.BASE_DIR, 'docs', file_name)

    if os.path.exists(absolute_path):
        document_root, path = os.path.split(absolute_path)
        return static.serve(request, path, document_root=document_root)
    else:
        raise Http404


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', serve)
]

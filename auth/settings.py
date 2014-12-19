import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'du81na3*yg&!y)pxv$0*&&_qlpl*z%-6^vji(x#v_sa)d-&2u$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'auth.urls'

WSGI_APPLICATION = 'auth.wsgi.application'

# Templates

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

# Auth

AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',  # fa-gihub

    'social.backends.bitbucket.BitbucketOAuth',  # fa-bitbucket-square

    'social.backends.facebook.FacebookAppOAuth2',  # fa-facebook-square
    'social.backends.facebook.FacebookOAuth2',

    'social.backends.google.GoogleOAuth2',  # fa-google-plus-square

    'social.backends.linkedin.LinkedinOAuth',  # fa-linkedin-square
    'social.backends.linkedin.LinkedinOAuth2',

    'social.backends.reddit.RedditOAuth2',  # fa-reddit-square

    'social.backends.twitter.TwitterOAuth',  # fa-twitter-square

    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_REDIRECT_URL = '/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_ETAGS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

try:
    from deploy.local_settings import *  # NOQA
except ImportError:
    pass

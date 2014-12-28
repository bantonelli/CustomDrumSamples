"""
Django settings for CustomDrumSamples project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Static asset configuration

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Static Root is where the production server finds the static files
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/assets/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'CustomDrumSamples/static'),
    os.path.join(BASE_DIR, 'KitBuilder/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
#    os.path.join(BASE_DIR, "templates/registration"),
#    os.path.join(BASE_DIR, "templates/courses"),
#    os.path.join(BASE_DIR, "templates/userlogin"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k4wbvl10oydbd%yi!@=q_u!eh@j_uz+rpk2$h0u%re4#mth^-f'

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
    'kitbuilder',
    'custom_quote',
    'oauth2_provider',
    'rest_framework',
    'userprofile',
    'api'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CustomDrumSamples.urls'

WSGI_APPLICATION = 'CustomDrumSamples.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#Below is Development setup for database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'customdrumsamplesdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

OAUTH2_PROVIDER = {
    #this is the list of available scopes
    #OAUTH2_PROVIDER.SCOPES parameter contains the scopes that the application will be aware of
    #so we can use them for permission check.
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

# Kit Builder Client ID = aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2
# Kit Builder Client Secret = U_qMHU-cWBD58vu5DOcp3U0RO79t5zEfIdoF1Xn.E:FT_ztn2WsdAxfV_V@V0Ji?Wb=IQl:1xM!X8WTb9kIH-!!uu1PUS0XVpYr6DxwXeEgJlUFBwpS7co8xtB9!5CAC
# use curl -X POST -d "client_id=<client_id>&client_secret=<client_secret>&grant_type=password&username=<user_name>&password=<password>" http://127.0.0.1:8000/o/token/

    #curl -X POST -d 'client_id=aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2&client_secret=U_qMHU-cWBD58vu5DOcp3U0RO79t5zEfIdoF1Xn.E:FT_ztn2WsdAxfV_V@V0Ji?Wb=IQl:1xM!X8WTb9kIH-!!uu1PUS0XVpYr6DxwXeEgJlUFBwpS7co8xtB9!5CAC&grant_type=password&username=humbertozayas&password=123456' http://127.0.0.1:8000/o/token/
    #this http request grants a token to any registered user of the application.


# Temporary Access Token humbertozayas = XMrPJCExlOem0cXyPTJxhGyvyZqVB8 (latest)
# Refresh Token = CPI9GBlQ3n75EEmxB003MnX0Ubmeik (latest)
    # use--> curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/?format=json
            # use--> curl -H "Authorization: Bearer XMrPJCExlOem0cXyPTJxhGyvyZqVB8" http://127.0.0.1:8000/api/?format=json
    # this request is an example of how a user can access the api urls

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
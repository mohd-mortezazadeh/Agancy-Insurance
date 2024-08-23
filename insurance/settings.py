

import os
import socket
from pathlib import Path

#from decouple import config
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-rx8bm1hi_^n!_a_5&bjkx0p0du$x(a6ws7_46sk$zx@j8z7w+6"

CSRF_TRUSTED_ORIGINS = ['https://academybime.com','https://www.academybime.com', ]
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['https://academybime.com/', 'academybime.com', '*']

INSTALLED_APPS = [
    'daphne',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
    'category.apps.CategoryConfig',
    'django.contrib.sites',
    'tag.apps.TagConfig',
    'contact',
    'dashboard.apps.DashboardConfig',
    'accounts.apps.AccountsConfig',
    'rest_framework',
    'widget_tweaks',
    'users', 
    'debug_toolbar',
    'ckeditor',
    'django.contrib.sitemaps',
    
    'rest_framework.authtoken',
    'dj_rest_auth',

    'allauth',
    'social_django',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # for Google OAuth 2.0

    'dj_rest_auth.registration',
    'django_filters',
    
    'search.apps.SearchConfig',
    # 'django_elasticsearch_dsl',

    'aboutus',
    'team',
    'slider',
    'faq',
    'newsletters',
    'renewal',
    'news',
    'feedback',
    'comment',
    'tickets',
    # 'channels_redis',
    'star_ratings',
    'channels',
    'django_celery_beat',
    'django_celery_results',
    'notifications',
    'jalali_date',
    'clearcache',
    
    ]



ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'accounts.middleware.SaveIPAddressMiddleware',
    'allauth.account.middleware.AccountMiddleware '

]

ROOT_URLCONF = 'insurance.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.context_processors.context_processors.posts_view_context_processor',
            ],
           
        },
    },
]



WSGI_APPLICATION = 'insurance.wsgi.application'
ASGI_APPLICATION = 'insurance.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            #"hosts": [("redis", 17084)],
            #"hosts": [os.environ.get('REDIS_URL',"redis://services.irn4.chabokan.net:17084")],
            "hosts": [("redis://:kWC8hWtQtK0T9kvu@services.irn4.chabokan.net:17084/1")],
        },
                  
        
    },

}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'api.permissions.IsStaffOrReadOnly',
    ],
      'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'access'
JWT_AUTH_REFRESH_COOKIE = 'refresh'

REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'api.serializers.RegisterSerializer',
}



DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'roger',
        'USER': 'postgres',
        'PASSWORD':'jqWfqd88nmZsbteJ',
        'HOST':'services.irn2.chabokan.net',
        'PORT':43508,
    },
}

AUTH_USER_MODEL = 'accounts.User'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_I18N = True
USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'upload')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media', 'static'),
)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT =587
EMAIL_HOST_USER = "siyamak1981@gmail.com"
EMAIL_HOST_PASSWORD = "hkgttjourdfnhwcm"
EMAIL_USE_TLS = True



#Django’s Debug Toolbar Showing Inside Docker
INTERNAL_IPS = [
    "127.0.0.1",
    'localhost',
 
]

# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

DEBUG_TOOLBAR_CONFIG = {
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'my_cache_table',
   }
}

CELERY_IMPORTS = [
    'notifications.tasks',
]


#redis viewers
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://:kWC8hWtQtK0T9kvu@services.irn4.chabokan.net:17084/5',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
CACHE_TTL = 60 * 60 * 24 # 1 day


RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY",default="")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY",default="")

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_URL_NAMESPACE = 'social'
ACCOUNT_EMAIL_VERIFICATION = None


LOGIN_REDIRECT_URL = "blog:post_and_category"  
LOGOUT_REDIRECT_URL = 'login'


# CELERY STUFF
CELERY_BROKER_URL = "redis://:kWC8hWtQtK0T9kvu@services.irn4.chabokan.net:17084/1"
CELERY_RESULT_BACKEND = "redis://:kWC8hWtQtK0T9kvu@services.irn4.chabokan.net:17084/1"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER ='json'
CELERY_RESULT_SERIALIZER ='json'
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_REDIS_PORT = 17084
CELERY_REDIS_PASSWORD="kWC8hWtQtK0T9kvu"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


REDIS_HOST = "services.irn4.chabokan.net"
REDIS_PORT =17084
REDIS_PASSWORD ="kWC8hWtQtK0T9kvu"

REDIS_URL = 'redis://:{}@{}:{}/1'.format(
    REDIS_PASSWORD,  
    REDIS_HOST,  
    REDIS_PORT
)

# ELASTICSEARCH_DSL = {
#      'default': {
#          'hosts': os.getenv("ELASTICSEARCH_DSL_HOSTS", 'localhost:9200'),
#          'http_auth': ("elastic", "RhwLc4GWsnXE3ER6"),
#      },
#  }
# from elasticsearch_dsl import connections
# connections.create_connection(hosts=os.getenv("ELASTICSEARCH_DSL_HOST"),timeout=20)

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-error',
 }

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# RATINGS
STAR_RATINGS_STAR_WIDTH = 15
STAR_RATINGS_STAR_HEIGHT = 15
# # editable =
STAR_RATINGS_RERATE = False
STAR_RATINGS_ANONYMOUS = True


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'extraPlugins': 'wordcount', 
        
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe',]},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar os.environ.get here
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',


        ]),
    }
}

import os
from django.urls import reverse_lazy
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = ')0_(@#_(gcr3(z#lt-a0+t6z_s0t3tv^4d_k^vaob_0z06x_qo'
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'crispy_forms',

    'accounts',
    'portal',
    'complaints',
    'wallets',
    'recharges',
    'payments',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'printmycopy.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'printmycopy.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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

#   CUSTOM SETTINGS

#   GLOBAL PROJECTS SETTINGS

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#   ACCOUNTS
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


AUTH_USER_MODEL = "accounts.User"
API_KEY_2FA = "c9ef2a2e-806a-11e9-ade6-0200cd936042"


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

)

LOGIN_URL = reverse_lazy("accounts:login")
LOGIN_REDIRECT_URL = reverse_lazy("portal:home")

SITE_DOMAIN = "http://www.printmycopy.com"
SITE_DOMAIN_NAKED = "http://www.printmycopy.com"


#   PAYTM
PAYTM_MERCHANT_KEY = "V7Iwt5LFE1HofLPn"
PAYTM_MERCHANT_ID = "VmqjrA24654503525332"
PAYTM_WEBSITE = 'DEFAULT'
PAYTM_CALLBACK_URL = SITE_DOMAIN + "/payments/paytm/response/"


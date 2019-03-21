"""
Django settings for TravelWebSite project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_app'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u5rr=2_6ik#)g1n+sktb7u^n=kh^)lnq7m=p@8i%d((muikt!7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'news',
    'users',
    'app01',
    'captcha',
    'shop',
    'scenicspots',
    'diarys',
    'operation',
    'pay'

]
# 后台管理用户模型 替代 django自带模型
AUTH_USER_MODEL = 'users.MyUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TravelWebSite.urls'

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
                # 处理静态问题
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'TravelWebSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travelwebsite',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_DIRS = (
    os.path.join(BASE_DIR, 'media')
)
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
# STATICFILES_DIRS = (('js',os.path.join(STATIC_ROOT,'js')),
#                     ('css',os.))
# session 设置
SESSION_COOKIE_AGE = 60 * 30 # 30分钟
SESSION_SAVE_EVERY_REQUEST = True
# login_required 判断没有登陆跳转登陆页面  配合view 中class 继承LoginRequiredMixin使用
LOGIN_URL = '/login'

# 支付宝设置
ALIPAY_APPID = '2016092700610971'
# 公钥 支付宝公钥并不是应用公钥
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_public_key')
# 私钥
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_app_private_key')
# 接口
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do?'
# 支付关闭时间：
ALIPAY_CLOSE_TIME = '60m'

DOMAIN_NAME = 'http://127.0.0.1:8000/'
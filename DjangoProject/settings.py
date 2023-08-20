"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6**p!r%3s-$c71k_xyzu%57vuqbshi&+w%&v=an!xg70wapl3j'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True
# ALLOWED_HOSTS = ['211.78.42.201']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite.apps.MysiteConfig',
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

ROOT_URLCONF = 'DjangoProject.urls'

# 樣板的路徑特別，因為這部分是套版加上阿里阿紮的網路教學做法是先把套板加在templates>>XXX資料夾*(這邊為agitweb)>>放在這裡面
# 預設會是templates 請麻煩補上了
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/agitweb')]
        ,
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

WSGI_APPLICATION = 'DjangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# 串接mssql
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',  # 網路上的，官方教學沒幹用
        'NAME': 'AGIT_SQL',  # "資料庫名稱"不是資料庫伺服器名稱喔!!下面的那個host才是
        'USER': 'sa',  # 使用者名稱，有關加入使用者帳號google吧
        'PASSWORD': 'What23072891229',  # 密碼 BJ4
        'HOST': 'DESKTOP-E1DPA4S',  # 資料庫伺服器名稱
        'PORT': '',  # 我也不知道是幹啥用的有遇到在跟你說

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # 去看ODBC的版本是多少
        },
    },
}

'''
有關加入使用者帳號.....
1.點選自資料庫伺服器右鍵 >> 屬性 >> 左邊選取頁面下的安全性>> 伺服器驗證記得把"SQL server 及 Windows驗證模式打開"(你創好了這個沒打開你會登入失敗一輩子)
2.資料庫伺服器下面的安全性 >> 在登入按右鍵 >> 新增登入 >> 點選下面的 SQL Server驗證 >> 寫好帳號密碼 >>強制密碼逾期||使用者必須在下次登入時變更密碼勾掉(或者你可以取消強制執行密碼原則就可以了)
   >> 使用這對應到你可以自行設定要對應到的資料庫並下面給她資格(通常直接給owner啦)>>狀態看一下有沒有打開授與和已啟用。
3.換了資料庫跑一下 
  python manage.py makemigrations
  python manage.py migrate
   
3.F:\Anaconda\Lib\site-packages\sql_server\pyodbc\base.py
    _sql_server_versions = {
        10: 2008,
        11: 2012,
        12: 2014,
        13: 2016,
        14: 2017,
        15: 2017,
        16: 2019,       # 補上這行 我也不知道為啥沒這東西不能用
    }

'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# 調整時區 只會設定台灣啦 除非你猛到去國外寫網站

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
'''
python manage.py collectstatic
最好是下面建立這些東西 你再跑上面這段代碼的時候才會成功而且你在templates那些畫面引用的{% static '/agitweb/plugins/bootstrap/bootstrap.min.css'%}
才會生效
'''
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# SMTP setting
# ymlbanjvgmbvgsse應用程式密碼

# 設定寄信的 Google爬文一下照著做理論上不會錯
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP伺服器
EMAIL_PORT = 587  # TLS通訊埠號
EMAIL_USE_TLS = True  # 開啟TLS(傳輸層安全性)
EMAIL_HOST_USER = 'ex07@agit-global.com'  # 寄件者電子郵件
EMAIL_HOST_PASSWORD = 'ymlbanjvgmbvgsse'  # Gmail應用程式的密碼

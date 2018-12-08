"""
Django settings for videsite project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
import datetime

DEBUG = False

ALLOWED_HOSTS = ['movie.zfdev.com', 'tv.zfdev.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用mysql引擎
        'NAME': 'videosite',  # 数据库名称
        'USER': 'gapen',  # 用户名
        'PASSWORD': 'forsql123258',  # 秘密
        'HOST': '47.98.168.135',  # 地址默认loaclhost
        'PORT': '9753',  # 端口
        'OPTIONS': {
            # 'autocommit': True, # 自动提交
            'init_command': 'SET default_storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci;'
            # 设置数据库默认引擎
        }
    }
}
# ------------------ 跨域配置 ------------------
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'v.zfdev.com',
)
# CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'clienttype',
)

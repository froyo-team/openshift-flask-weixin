# -*- coding: utf-8 -*-
import os
class Config(object):
    DEBUG = True

    MONGODB_DB = os.environ['OPENSHIFT_APP_NAME']
    MONGODB_USERNAME = 'admin'
    MONGODB_PASSWORD = ' you password'
    MONGODB_HOST = os.environ['OPENSHIFT_MONGODB_DB_URL']

class WeiXinConfig(object):
		TOKEN = 'you token'
		RULE = '/weixin'
# -*- coding: utf-8 -*-

import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'jeeart.settings_server'
app_apth = "/home/horizonchen/jeeart/site/django_app/jeeart/"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()

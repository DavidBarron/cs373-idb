#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yafootballdb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



envpath = '/root/mv-venv/local/lib/python2.7/site-packages'

# we add currently directory to path and change to it
pwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(pwd)
sys.path = [pwd] + sys.path

# Append paths
site.addsitedir(envpath)

# now start django
from django.core.handlers.wsgi import WSGIHandler
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()
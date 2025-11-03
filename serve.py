import os
os.environ.setdefault("DJANGO_SETTING_MODULE","config.settings")

from waitress import serve
from config.wsgi import application

serve(application, host='127.0.0.1', port=8000)
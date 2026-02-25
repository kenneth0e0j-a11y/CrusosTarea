"""
WSGI entry point for Render deployment
"""
import os
import sys
from pathlib import Path

# Add the Universidad directory to the Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / 'Universidad'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Universidad.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

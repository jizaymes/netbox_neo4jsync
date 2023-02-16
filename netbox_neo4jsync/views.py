# from netbox.views import generic
# from dcim.models import Device, Site

# import logging

# logger = logging.getLogger(__name__)

# from . import tables


## Neo4jSyncList Views
from django.http import HttpResponse
import datetime

def Neo4jSyncListView(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
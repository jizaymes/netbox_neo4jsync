from netbox.views import generic
from dcim.models import Device, Site, Cable

import logging

logger = logging.getLogger(__name__)

from . import models, tables


## Neo4jSyncList Views

class Neo4jSyncListView(generic.ObjectListView):
    queryset = Site.objects.all()
    table = tables.ListOfStuffTable
    # filterset = filters.RiskFilterSet
    # filterset_form = forms.RiskFilterForm

class Neo4jSyncList(generic.ObjectView):
    queryset = Site.objects.all()

# class RiskEditView(generic.ObjectEditView):
#     queryset = models.Risk.objects.all()
#     form = forms.RiskForm

# class RiskDeleteView(generic.ObjectDeleteView):
#     queryset = models.Risk.objects.all()

# class RiskBulkDeleteView(generic.BulkDeleteView):
#     queryset = models.Risk.objects.all()
#     table = tables.RiskTable
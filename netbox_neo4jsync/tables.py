import django_tables2 as tables

from netbox.tables import NetBoxTable

# ThreatSource Tables


# class ThreatSourceTable(NetBoxTable):
    
#     name = tables.Column(linkify=True)

#     class Meta(NetBoxTable.Meta):
#         model = models.ThreatSource
#         fields = ["name", "threat_type", "capability", "intent", "targeting"]


# # ThreatEvent Tables


# class ThreatEventTable(NetBoxTable):
    
#     name = tables.Column(linkify=True)

#     class Meta(NetBoxTable.Meta):
#         model = models.ThreatEvent
#         fields = ["name", "threat_source", "relevance", "likelihood", "impact"]


# # Vulnerability Tables


# class VulnerabilityTable(NetBoxTable):

#     name = tables.Column(linkify=True)
    
#     class Meta(NetBoxTable.Meta):
#         model = models.Vulnerability
#         fields = ["name", "cve", "description", "asset"]


# # VulnerabilityAssignment Tables


# class VulnerabilityAssignmentTable(NetBoxTable):

#     actions = columns.ActionsColumn(actions=('delete',))

#     class Meta(NetBoxTable.Meta):
#         model = models.VulnerabilityAssignment
#         fields = ["vulnerability", "vulnerability__cve", "vulnerability__description"]

# class VulnerabilityAssignmentListTable(NetBoxTable):

#     actions = columns.ActionsColumn(actions=('delete',))

#     asset = tables.Column(linkify=True)

#     asset_object_type = tables.Column(verbose_name="Asset Type")

#     class Meta(NetBoxTable.Meta):
#         model = models.VulnerabilityAssignment
#         fields = ["asset", "asset_object_type"]

# class VulnerabilityExploitListTable(NetBoxTable):

#     actions = columns.ActionsColumn(actions=('delete',))

#     asset = tables.Column(linkify=True)

#     vulnerability = tables.Column(linkify=True)

#     asset_object_type = tables.Column(verbose_name="Asset Type")

#     class Meta(NetBoxTable.Meta):
#         model = models.VulnerabilityAssignment
#         fields = ["asset", "vulnerability", "asset_object_type"] 


# # Risk Tables

# class RiskTable(NetBoxTable):

#     name = tables.Column(linkify=True)

#     risk_level = tables.Column(verbose_name="Risk Level")

#     class Meta(NetBoxTable.Meta):
#         model = models.Risk
#         fields = ["name", "threat_event", "likelihood", "impact", "risk_level"]

# # List of Stuff Tables

class ListOfStuffTable(tables.Table):

    id = tables.Column(attrs={'td': {'class': 'text-end text-nowrap'}})
    description = tables.Column()
   
    class Meta:
        attrs = {
            'class': 'table table-hover object-list',
        }

    
from pydantic import BaseModel

class Neo4jSyncDataModel(BaseModel):
    class_name: str         #  Name of the NetBox class of the affected element (Site, Device, Rack, etc)
    field_name: str         #  Field that was affected
    value: str              #  The current value of the field (idea being that combining class_name and field_name (i.e. Site.name) would = 'Site 1')
    old_value: str          #  The previous value
    action: str             #  The action being taken (create, update, delete)
    object_id: int          #  Object ID of the class thats affected (/sites/<123>/edit)

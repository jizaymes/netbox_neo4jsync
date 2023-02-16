# from extras.scripts import *

# from neo4j import GraphDatabase
# from rich import inspect

# from dcim.models import Site, Device
# from extras.plugins import get_plugin_config

# from netbox-neo4jsync.neo4jsync import Neo4jSync
# from netbox-neo4jsync.models import Neo4jSyncDataModel

# class Neo4jBulkSync(Script):
#     class Meta:
#         name = 'Custom script to synchronize Netbox -> Neo4j'
#         description "Longer version of the same thing"


#     def run(self, data, commit):
#         inspect(data)
#         inspect(commit)
#         # #objdata2 = Site.objects.all()

#         # models_to_watch = get_plugin_config('netbox_neo4jsync', 'models_to_watch')
#         # for class_name, field_name in models_to_watch:
#         #     clas = class_name + '.objects.all()'
#         #     print(clas)
#         #     objdata = eval(class)

#         #     for obj in objdata:
#         #         data = Neo4jSyncDataModel(
#         #             class_name=class_name,
#         #             field_name=field_name,
#         #             value=objdata[field_name],
#         #             old_value='',
#         #             action='bgsync',
#         #             object_id=obj.object_id
#         #             )
#         #         Neo4jSync.process_data(data)
#         #         self.stdout.write(self.style.SUCCESS(f"Successfully added {class_name}.{field_name}: {objdata[field_name]}"))

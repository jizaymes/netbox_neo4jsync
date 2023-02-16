from extras.plugins import PluginConfig

class NetBoxNeo4jSyncConfig(PluginConfig):
    name = 'netbox_neo4jsync'
    verbose_name = 'NetBox Neo4j Sync'
    description = 'Automatically synchronize data from Netbox into Neo4j'
    version = '0.1'
    base_url = 'neo4jsync'
    default_settings = {
        'models_to_watch': [ ('Site', 'name'), ('Device', 'name') ],
    }

    def ready(self):
        from . import signals

config = NetBoxNeo4jSyncConfig
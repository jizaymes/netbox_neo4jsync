from extras.plugins import PluginConfig

class NetBoxNeo4jSyncConfig(PluginConfig):
    name = 'netbox_neo4jsync'
    verbose_name = 'NetBox Neo4j Sync'
    description = 'Tools to synchronize data from NetBox into Neo4j'
    version = '0.1'
    base_url = 'neo4jsync'
    default_settings = {
        'models_to_watch': [ ('Site', 'name'), ('Device', 'name') ],
    }

    def ready(self):
        from . import signals
        super().ready()

config = NetBoxNeo4jSyncConfig
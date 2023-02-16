from extras.plugins import PluginMenuItem

menu_items = (
        PluginMenuItem(
            link="plugins:netbox_neo4jsync:neo4jsync_list",
            link_text="Bulk Sync",
        )
    )

menu = PluginMenu(
    label="Neo4j Sync",
    groups=(("Neo4jBulkSync", menu_items),),
    ),
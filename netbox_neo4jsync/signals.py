from django.db.models.signals import post_save
from django.dispatch import receiver
from extras.plugins import get_plugin_config
from extras.models import ObjectChange


from .models import Neo4jSyncDataModel
from .neo4jsync import Neo4jSync

import inspect
from rich import inspect as insp

@receiver(post_save,sender=ObjectChange)
def run_after_device_save(sender, instance, **kwargs):
    # This is running synchronously so don't do anything slow as it will impede UI performance for the user
    
    # insp(instance)
    models_to_watch = get_plugin_config('netbox_neo4jsync', 'models_to_watch')

    neo4jsync = Neo4jSync(False)  ## True = Debug enabled

    for class_name, field_name in models_to_watch:
        if not instance.changed_object.__class__.__name__ == class_name:
            # print(f"Not matching Object : {instance.changed_object.__class__.__name__ } != {class_name}")
            continue

        if instance.action == 'create' and not instance.prechange_data:
            old_value = ''
        else:
            old_value = instance.prechange_data[field_name]

        if instance.action == 'delete' and not instance.postchange_data:
            new_value = ''
        else:
            new_value = instance.postchange_data[field_name]

    
        data = Neo4jSyncDataModel(
            class_name=instance.changed_object.__class__.__name__,
            field_name=field_name,
            value=new_value,
            old_value=old_value,
            action=instance.action,
            object_id=instance.changed_object_id
            )

        neo4jsync.process_data(data)
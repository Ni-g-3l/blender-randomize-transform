import bpy
import random

from randomize_transform_addon.api.randomize_object_transform_service import RandomizeObjectTransformService


class RandomizeTransformOperator(bpy.types.Operator):

    bl_idname = "object.randomize_transform"
    bl_label = "Randomize Transform"


    def execute(self, context):
        # Get the selected objects
        scene = context.scene
        selected_objects = bpy.context.selected_objects
        # Apply random scale and rotation to each selected object
        for obj in selected_objects:

            RandomizeObjectTransformService.randomize_object_location(obj, scene.randomize_location_property_group)
            RandomizeObjectTransformService.randomize_object_rotation(obj, scene.randomize_rotation_property_group)
            RandomizeObjectTransformService.randomize_object_scale(obj, scene.randomize_scale_property_group)

        return {'FINISHED'}
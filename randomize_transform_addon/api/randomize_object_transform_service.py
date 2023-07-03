from randomize_transform_addon.domain.transform_action import (RandomizeRotationAction,
                                                               RandomizeScaleAction,
                                                               RandomizeLocationAction)


class RandomizeObjectTransformService(object):

    @classmethod
    def randomize_object_location(cls, obj, blender_property):
        RandomizeLocationAction.execute(obj, blender_property)

    @classmethod
    def randomize_object_rotation(cls, obj, blender_property):
        RandomizeRotationAction.execute(obj, blender_property)

    @classmethod
    def randomize_object_scale(cls, obj, blender_property):
        RandomizeScaleAction.execute(obj, blender_property)

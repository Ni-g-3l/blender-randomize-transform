import bpy

class RotationRangeProperty(bpy.types.PropertyGroup):

    min_range_value = 0
    max_range_value = 360

    min: bpy.props.FloatProperty(name='min', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=min_range_value, precision=0)
    max: bpy.props.FloatProperty(name='max', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=max_range_value, precision=0)

class AxeRotationProperty(bpy.types.PropertyGroup):
    enabled: bpy.props.BoolProperty(name='enabled', default=True)
    range: bpy.props.PointerProperty(type=RotationRangeProperty)

class RandomizeRotationProperty(bpy.types.PropertyGroup):
    x: bpy.props.PointerProperty(type=AxeRotationProperty)
    y: bpy.props.PointerProperty(type=AxeRotationProperty)
    z: bpy.props.PointerProperty(type=AxeRotationProperty)

class ScaleRangeProperty(bpy.types.PropertyGroup):

    min_range_value = 0
    max_range_value = 1
    
    min: bpy.props.FloatProperty(name='min', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=min_range_value, precision=0)
    max: bpy.props.FloatProperty(name='max', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=max_range_value, precision=0)

class AxeScaleProperty(bpy.types.PropertyGroup):
    enabled: bpy.props.BoolProperty(name='enabled', default=True)
    range: bpy.props.PointerProperty(type=ScaleRangeProperty)

class RandomizeScaleProperty(bpy.types.PropertyGroup):
    x: bpy.props.PointerProperty(type=AxeScaleProperty)
    y: bpy.props.PointerProperty(type=AxeScaleProperty)
    z: bpy.props.PointerProperty(type=AxeScaleProperty)

class LocationRangeProperty(bpy.types.PropertyGroup):

    min_range_value = 0
    max_range_value = 10
    
    min: bpy.props.FloatProperty(name='min', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=min_range_value, precision=2)
    max: bpy.props.FloatProperty(name='max', min=min_range_value, max=max_range_value,
                                 soft_min=min_range_value, soft_max=max_range_value,
                                 default=max_range_value, precision=2)

class AxeLocationProperty(bpy.types.PropertyGroup):
    enabled: bpy.props.BoolProperty(name='enabled', default=True)
    range: bpy.props.PointerProperty(type=LocationRangeProperty)

class RandomizeLocationProperty(bpy.types.PropertyGroup):
    x: bpy.props.PointerProperty(type=AxeLocationProperty)
    y: bpy.props.PointerProperty(type=AxeLocationProperty)
    z: bpy.props.PointerProperty(type=AxeLocationProperty)



def register():
    bpy.types.Scene.randomize_scale_property_group = bpy.props.PointerProperty(type=RandomizeScaleProperty)
    bpy.types.Scene.randomize_location_property_group = bpy.props.PointerProperty(type=RandomizeLocationProperty)
    bpy.types.Scene.randomize_rotation_property_group = bpy.props.PointerProperty(type=RandomizeRotationProperty)

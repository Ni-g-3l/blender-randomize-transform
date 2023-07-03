import bpy

from randomize_transform_addon.adapter.bpy.operator import RandomizeTransformOperator

class RootPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def _draw_axe_property(cls, layout, axe_name, pp):
        split = layout.split(align=True)
        
        col = split.column()
        col.prop(pp, property="enabled", text=axe_name)
        
        col = split.column()
        col.prop(pp.range, property="min", text="Min")
        
        col = split.column()
        col.prop(pp.range, property="max", text="Max")

    @classmethod
    def _draw_transform_property(cls, layout, title, transform_property):
        layout.label(text=f"{title} :")
        cls._draw_axe_property(layout, "x", transform_property.x)
        cls._draw_axe_property(layout, "y", transform_property.y)
        cls._draw_axe_property(layout, "z", transform_property.z)
    
class RandomTransformPanel(RootPanel, bpy.types.Panel):
    bl_idname = "OBJECT_PT_randomize_transform_panel"
    bl_label = "Randomize"

    def draw(self, context):
        layout = self.layout

        layout.operator(RandomizeTransformOperator.bl_idname, text="Randomize")

        self._draw_transform_property(layout, "Location", context.scene.randomize_location_property_group)
        self._draw_transform_property(layout, "Rotation", context.scene.randomize_rotation_property_group)
        self._draw_transform_property(layout, "Scale", context.scene.randomize_scale_property_group)
bl_info = {
    "name": "Randomize Transform",
    "author": "Nig3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "View 3D > Transform",
    "description": "Randomize Transform on blender selected object",
    "warning": "",
    "doc_url": "https://github.com/Nig3l/blender-randomize-transform",
    "category": "3D View",
}

from randomize_transform_addon import bpy_loader

def register():
    bpy_loader.register()

def unregister():
    bpy_loader.unregister()


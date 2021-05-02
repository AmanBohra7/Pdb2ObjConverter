import bpy
import sys
from shutil import move
from os import path


# argv = sys.argv
# argv = argv[argv.index("--") + 1:]  # get all args after "--"

prout = "./OBJ/mol"
pin = "./WRL/mol.wrl"

#import WRML
# bpy.ops.import_scene.x3d(filepath=pin, axis_forward='Z', axis_up='Y')

# bpy.ops.import_scene.fbx(filepath="space_ship.fbx")

# remove default cube and camera
# print(dir(bpy.data.objects['Camera'])
# objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA','CUBE')]
# bpy.ops.object.delete({"selected_objects": objs})




bpy.data.objects["Cube"].select_set(True)
bpy.ops.object.delete()

bpy.data.objects['Camera'].select_set(True)
bpy.ops.object.delete()


bpy.ops.import_scene.x3d(filepath=pin)

object = bpy.data.objects['Shape_Cylinder']

bpy.context.view_layer.objects.active = object

bpy.ops.object.join()






# # joins all meshes -> need to fix for more complex model
# for ob in bpy.context.scene.objects:
#     if ob.type == 'MESH':
#         ob.select_set(True)
#         print("Something is ACTIVE")
#         bpy.context.view_layer.objects.active = ob
#     else:
#         ob.select_set(False)
# try:
#     bpy.ops.object.join()
# except:
#     print("Nothing to join")

# # UV wrap
# bpy.ops.uv.smart_project()
# #bpy.data.screens["Default"]

# # export UVmap
# bpy.ops.uv.export_layout(filepath=prout + ".png", size=(1024, 1024))
# # change folder .png
# #move(prout.split("/")[-1] + ".png", path.dirname(prout) + "/" + prout.split("/")[-1] + ".png")

# # export obj
bpy.ops.export_scene.obj(filepath=prout + ".obj")






test = """
bpy.ops.import_scene.x3d(filepath="TestWrlFile.wrl")
object = bpy.data.objects['Shape_Cylinder']
bpy.ops.object.join()
bpy.context.view_layer.objects.active = object
"""

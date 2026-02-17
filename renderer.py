import sys
import bpy
import shutil
from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    bpy.context.scene.render.filepath = render_output_path
    bpy.ops.render.render(write_still=True)

def load_scene(path):
    bpy.ops.wm.open_mainfile(filepath=path)
        
scene_name = "Scene"
path = "Scenes//TestScene1.blend"
render_output_path = "Rendering//TestScene1.png"
if len(sys.argv) > 1:
    path = sys.argv(1)

if path:
    blender_bin = shutil.which("blender")
    if blender_bin:
        print("Found:", blender_bin)
        bpy.app.binary_path = blender_bin
        bpy.app.handlers.load_post.append(load_handler)

        load_scene(path)

        print(bpy.data.scenes[scene_name].camera.data)
        
    else:
        print("Unable to find blender!")
else:
    print("No blender file specified! Nothing to do!")


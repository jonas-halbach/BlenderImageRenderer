import sys
import bpy
import shutil
from scenerenderer import SceneRenderer
from bpy.app.handlers import persistent

scene_name = "Scene"

@persistent
def load_handler(dummy):
    scene_renderer = SceneRenderer(bpy.data.scenes[scene_name].camera, "Rendering//TestScene")
    scene_renderer.render_scene()

def load_scene(path):
    bpy.ops.wm.open_mainfile(filepath=path)
        

path = "Scenes//TestScene1.blend"
if len(sys.argv) > 1:
    path = sys.argv(1)

if path:
    blender_bin = shutil.which("blender")
    if blender_bin:
        print("Found:", blender_bin)
        bpy.app.binary_path = blender_bin
        bpy.app.handlers.load_post.append(load_handler)
        
        print(bpy.data.scenes[scene_name].camera.data)

        load_scene(path)
    else:
        print("Unable to find blender!")
else:
    print("No blender file specified! Nothing to do!")


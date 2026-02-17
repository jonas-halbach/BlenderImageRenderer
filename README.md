# BlenderImageRenderer
Renders a BlenderScene from multiple perspectives

## Packages to install
For running the scripts of this repository you need to install the following packages (ideally in a virtual environment):
- [bpy](https://pypi.org/project/bpy/) (via this command: > pip install bpy==3.6.0 --extra-index-url https://download.blender.org/pypi/)

## How to run
The script can be executed via:
```
python3 renderer.py
```
The script needs a blender scene to render. This scene is expected to be located at the following path:
> "Scenes//TestScene1.blend"

If you want to render a different scene, the path can also be specified via the first command line argument.

Right now the scene will be simply rendered from the perspective of the first existing camera in this scene. This will be changed in the future!

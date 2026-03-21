import bpy
import mathutils
from cameramover import CameraMover

class SceneRenderer:

    def __init__(self, camera, base_path):
        self.camera = camera
        self.camera_rotation_radius = 0.2
        self.camera_rotation_degree_step_size = 45
        self.current_x_rotation = 0
        self.current_y_rotation = 0
        self.camera_mover = CameraMover(self.camera_rotation_radius, self.camera_rotation_degree_step_size)
        self.base_path = base_path

    def render_scene(self):
        self.render_current_view()
        while(self.camera_mover.has_next()):
            self.camera_mover.next_rotation_vector()
            self.render_current_view()

    def render_current_view(self):
        print(self.camera_mover.current_rotation)
        camera_transformation_matrix = self.camera_mover.get_current_transformation_matrix()
        self.camera.matrix_world = camera_transformation_matrix
        self.look_at(mathutils.Vector())
        bpy.context.view_layer.update()
        bpy.context.scene.render.filepath = self.base_path + str(self.camera.location) + " " + str(self.camera.rotation_euler) + ".png"
        bpy.ops.render.render(write_still=True)

    def look_at(self, point):
        loc_camera = self.camera.matrix_world.to_translation()

        direction = point - loc_camera

        # point the cameras '-Z' and use its 'Y' as up
        rot_quat = direction.to_track_quat('-Z', 'Y')

        # assume we're using euler rotation
        self.camera.rotation_euler = rot_quat.to_euler()
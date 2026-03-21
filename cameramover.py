import mathutils
from math import radians

class CameraMover:

    def __init__(self, rotation_radius, rotation_degree_step):
        self.rotation_radius = rotation_radius
        self.rotation_degree_step = rotation_degree_step
        self.current_rotation = mathutils.Vector((0, 0, 0))
        self.top_transformation_matrix_already_calulated_multiplier = 0

    def get_translation_matrix(self):
        return mathutils.Matrix.Translation((self.rotation_radius, 0, 0))
    
    def get_rotation_matrix(self):
        x_rotation_matrix = mathutils.Matrix.Rotation(radians(self.current_rotation.x), 4,'X')
        y_rotation_matrix = mathutils.Matrix.Rotation(radians(self.current_rotation.y), 4,'Y')
        z_rotation_matrix = mathutils.Matrix.Rotation(radians(self.current_rotation.z), 4,'Z')
        return x_rotation_matrix @ y_rotation_matrix @ z_rotation_matrix

    def get_current_transformation_matrix(self):
        return self.get_rotation_matrix() @ self.get_translation_matrix() 

    def next_rotation_vector(self):
        self.current_rotation.y = self.current_rotation.y + self.rotation_degree_step
        if self.exceeded_max_y_rotation():
            self.flag_top_transformation_matrix_already_calculated()
            self.current_rotation.x = self.current_rotation.x + self.rotation_degree_step
            self.current_rotation.y = self.rotation_degree_step

    def exceeded_max_y_rotation(self):
        return self.current_rotation.y > 180 - self.top_transformation_matrix_already_calulated_multiplier * self.rotation_degree_step

    def flag_top_transformation_matrix_already_calculated(self):
        self.top_transformation_matrix_already_calulated_multiplier = 1

    def has_next(self):
        return self.current_rotation.x < 360 - self.rotation_degree_step or \
            self.current_rotation.y < 180 - self.rotation_degree_step
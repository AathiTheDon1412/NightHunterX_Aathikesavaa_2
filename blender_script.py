import bpy
import sys

description = sys.argv[-1]

def create_cube(location):
    bpy.ops.mesh.primitive_cube_add(location=location)

def create_sphere(location):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)

def create_cylinder(location):
    bpy.ops.mesh.primitive_cylinder_add(location=location)

def generate_objects(description):
    words = description.lower().split()
    location_offset = 0

    for word in words:
        if word in ['cube', 'cubes']:
            create_cube((0, location_offset, 0))
            location_offset += 2
        elif word in ['sphere', 'spheres']:
            create_sphere((0, location_offset, 0))
            location_offset += 2
        elif word in ['cylinder', 'cylinders']:
            create_cylinder((0, location_offset, 0))
            location_offset += 2

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

generate_objects(description)

bpy.ops.export_scene.obj(filepath='output_model.obj')
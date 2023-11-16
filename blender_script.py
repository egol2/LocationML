import bpy
import os
import json
import random

# Global variables
current_render = 0
max_renders = 2000  # Reduce for testing
move_distance = 1
rotations_per_interval = 100  # Reduced for testing

# Get the directory of the current .blend file
blend_file_directory = bpy.path.abspath("//")

output_directory = os.path.join(blend_file_directory, "renders")

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get the camera and save initial positions
camera = bpy.data.objects.get("Camera")
if not camera:
    print("No camera found with the name 'Camera'")
    exit()
root_camera_position = camera.location.copy()
initial_camera_position = camera.location.copy()
initial_camera_rotation = camera.rotation_euler.copy()

camera_positions = []  # To store camera positions

def render_scene():
    global current_render, move_distance, initial_camera_position
    for _ in range(max_renders):
        render_filename = os.path.join(output_directory, f"render_{current_render + 1:03}.png")
        bpy.context.scene.render.filepath = render_filename
        bpy.ops.render.render(write_still=True)

        # Post-render actions
        camera_positions.append({
            "filename": f"render_{current_render + 1:03}.png",
            "position": {
                "x": camera.location.x,
                "y": camera.location.y,
                "z": camera.location.z
            }
        })
        if current_render % rotations_per_interval == 0:
            initial_camera_position.x += move_distance
            camera.location = initial_camera_position
            camera.rotation_euler = initial_camera_rotation
        else:
#            camera.location.x += random.uniform(-move_distance/2, move_distance/2)
#            camera.location.y += random.uniform(-move_distance/2, move_distance/2)
            # Random rotation
            camera.rotation_euler.x = initial_camera_rotation.x + random.uniform(-0.1, 0.1)
            camera.rotation_euler.y = initial_camera_rotation.y + random.uniform(-0.1, 0.1)
            camera.rotation_euler.z = initial_camera_rotation.z + random.uniform(-0.1, 0.1)

        current_render += 1

    # Reset camera to initial position and save data
    camera.location = root_camera_position
    camera.rotation_euler = initial_camera_rotation
    with open(os.path.join(output_directory, "camera_positions.json"), "w") as outfile:
        json.dump(camera_positions, outfile, indent=4)

print("Starting render")
render_scene()

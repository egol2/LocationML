python test_simple.py --image_path assets/render_001.png --model_name mono+stereo_640x192

## Running example manydepth
1. Download Anaconda
2. Add enviroment.yml to Anaconda
3. pip unistall numpy
4. pip install numpy=1.19.5
5. python -m manydepth.test_simple --target_image_path assets/test_sequence_target.jpg --source_image_path assets/test_sequence_source.jpg --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path KITTI_MR
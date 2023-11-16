python test_simple.py --image_path assets/render_001.png --model_name mono+stereo_640x192

## Running example manydepth
1. Download Anaconda
2. Clone this repository
3. Run: `git submodule update` and `git clone --recursive` to clone submodule as well
4. Add enviroment.yml to Anaconda
5. Open up a terminal inside the Anaconda enviroment and go to the manydepth directory
6. pip unistall numpy (this fixes an error I had for some reason)
7. pip install numpy=1.19.5
8. Download the KITTI_MR model and place it in the manydepth directory: [KITTI_MR.zip](https://storage.googleapis.com/niantic-lon-static/research/manydepth/models/KITTI_MR.zip)
9. python -m manydepth.test_simple --target_image_path assets/test_sequence_target.jpg --source_image_path assets/test_sequence_source.jpg --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path KITTI_MR

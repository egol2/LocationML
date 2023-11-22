python test_simple.py --image_path assets/render_001.png --model_name mono+stereo_640x192

## Running example manydepth:
1. Download Anaconda
2. Add enviroment.yml to Anaconda
3. Open up a terminal inside the Anaconda enviroment and go to the manydepth directory
4. pip unistall numpy (this fixes an error I had for some reason)
5. pip install numpy=1.19.5
6. Download the KITTI_MR model and place it in the manydepth directory: [KITTI_MR.zip](https://storage.googleapis.com/niantic-lon-static/research/manydepth/models/KITTI_MR.zip)
7. `python -m manydepth.test_simple --target_image_path assets/test_sequence_target.jpg --source_image_path assets/test_sequence_source.jpg --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path ../KITTI_MR`


## Q&A:
1. Q: OSError: [WinError 182] The operating system cannot run %1. Error loading "..\conda\envs\simplerecon_env\lib\site-packages\torch\lib\caffe2_detectron_ops_gpu.dll" or one of its dependencies.
    - A: (inside conda enviroment terminal) `conda uninstall pytorch torchvision torchaudio`
    - `conda install pytorch torchvision torchaudio -c pytorch`


## Finetuning:
Add the following to the training command to load an existing model for finetuning:
```shell
CUDA_VISIBLE_DEVICES=<your_desired_GPU>
python -m manydepth.train --data_path ../renders --log_dir ../logs --model_name finetuned_mono --load_weights_folder ../KITTI_MR
```

## Evaluating:

```shell
python -m manydepth.evaluate_depth -data_path <to tagged dataset> --load_weights_folder ../KITTI_MR
    --eval_mono
```
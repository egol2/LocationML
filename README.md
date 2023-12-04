python test_simple.py --image_path assets/render_001.png --model_name mono+stereo_640x192

## Running example manydepth:
1. Download Anaconda
2. Clone this repository
3. Run: `git submodule update` and `git clone --recursive` to clone submodule as well
4. Add enviroment.yml to Anaconda
5. Open up a terminal inside the Anaconda enviroment and go to the manydepth directory
6. pip uninstall numpy (this fixes an error I had for some reason)
7. pip install numpy==1.19.5
8. Download the KITTI_MR model and place it in the manydepth directory: [KITTI_MR.zip](https://storage.googleapis.com/niantic-lon-static/research/manydepth/models/KITTI_MR.zip)
9. `python -m manydepth.test_simple --target_image_path assets/test_target.jpg --source_image_path assets/test.jpg --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path ../KITTI_MR`
`python -m manydepth.test_simple --target_image_path assets/test_target.jpg --source_image_path assets/test.jpg --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path ../KITTI_MR`
`python -m manydepth.process_images_to_video --folder_path ../car --intrinsics_json_path assets/test_sequence_intrinsics.json --model_path ../KITTI_MR --output_path ../caro`
```
[[1.333, 0.0, 4.8],
 [0.0, 1.333, 2.72],
 [0.0, 0.0, 1.0]]
```
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

1. Download dataset
In an anaconda enviroment:
2. `python -m manydepth.export_gt_depth --data_path ../kitti_data --split eigen`
3. `python -m manydepth.evaluate_depth --data_path ../kitti_data --load_weights_folder ../KITTI_MR --eval_mono --batch_size 4 --freeze_teacher_epoch 5 --num_workers 0`
5. `conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`
6. delete `caffe2_detectron_ops.dll` from the anaconda directory. Example path: `C:\Users\Egor\.conda\envs\manydepth\lib\site-packages\torch\lib\caffe2_detectron_ops.dll`
7. restart terminal/computer

```shell
python -m manydepth.evaluate_depth -data_path <to tagged dataset> --load_weights_folder ../KITTI_MR
    --eval_mono
```

output (for evaluation using their model):
```shell
(manydepth) F:\ML-dataset\LocationML\manydepth>python -m manydepth.evaluate_depth --data_path ../kitti_data --load_weights_folder ../KITTI_MR --eval_mono --batch_size 4 --freeze_teacher_epoch 5 --num_workers 0
-> Loading weights from ../KITTI_MR
C:\Users\Egor\.conda\envs\manydepth\lib\site-packages\torchvision\transforms\transforms.py:288: UserWarning: Argument interpolation should be of type InterpolationMode instead of int. Please, use InterpolationMode enum.
  "Argument interpolation should be of type InterpolationMode instead of int. "
-> Computing predictions with size 192x640
175it [00:54,  3.20it/s]
finished predicting!
-> Evaluating
   Mono evaluation - using median scaling
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 697/697 [00:02<00:00, 298.10it/s]
 Scaling ratios | med: 34.621 | std: 0.083

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.098  &   0.770  &   4.457  &   0.176  &   0.900  &   0.965  &   0.983  \\

-> Done!
```

## Training

1. `python -m manydepth.train --data_path ../kitti_data --log_dir ../logs --model_name custom_model --num_workers 0 --png`
# GrokSAR
___
## official repository for DenoDet
"DenoDet: Attention as Deformable Multi-Subspace Feature Denoising for Target Detection in SAR Images" at: [https://arxiv.org/pdf/2406.02833](https://arxiv.org/pdf/2406.02833)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/denodet-attention-as-deformable-multi/2d-object-detection-on-sardet-100k)](https://paperswithcode.com/sota/2d-object-detection-on-sardet-100k?p=denodet-attention-as-deformable-multi)
___

GrokSAR is an open-source toolbox for SAR target detection and recognition.

- [GrokSAR](#groksar)
  - [official repository for DenoDet](#official-repository-for-denodet)
  - [Installation](#installation)
    - [Step 1: Create a conda environment](#step-1-create-a-conda-environment)
    - [Step 2: Install PyTorch](#step-2-install-pytorch)
    - [Step 3: Install OpenMMLab 2.x Codebases](#step-3-install-openmmlab-2x-codebases)
    - [Step 4: Install `groksar`](#step-4-install-groksar)
  - [Getting Started](#getting-started)
    - [Training](#training)
      - [Single GPU Training](#single-gpu-training)
      - [Multi GPU Training](#multi-gpu-training)
    - [Inference](#inference)
      - [Single GPU Inference](#single-gpu-inference)
      - [Multi GPU Inference](#multi-gpu-inference)
  - [Model Zoo and Benchmark](#model-zoo-and-benchmark)
    - [Leaderboard](#leaderboard)
    - [Model Zoo](#model-zoo)
      - [DenoDet](#denodet)
      - [DenoDet V2](#denodet-v2)
  - [Citation](#citation)
  - [License](#license)


## Installation

### Step 1: Create a conda environment

```shell
conda create --name groksar python=3.8
source activate groksar
```

### Step 2: Install PyTorch

```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
```

### Step 3: Install OpenMMLab 2.x Codebases

```shell
# openmmlab codebases
pip install -U openmim dadaptation cmake lit --no-input
mim install mmengine "mmcv>=2.0.0rc4, <2.1.0" "mmdet>=3.0.0rc5, < 3.1.0" "mmsegmentation>=1.0.0" "mmrotate>=1.0.0rc1" mmyolo mmpretrain
# heatmap generation dependencies
pip install grad-cam==1.4.0
# other dependencies
pip install ninja --no-input
pip install scikit-learn
pip install psutil
pip install scikit-image
```

### Step 4: Install `groksar`

```shell
python setup.py develop
```

**Note**: make sure you have `cd` to the root directory of `groksar`

```shell
$ git clone git@github.com:GrokCV/groksar.git
$ cd groksar
```

## Getting Started

### Training

#### Single GPU Training

For SARDet-100K dataset:

```shell
python tools/train_det.py configs/DenoDet/DenoDet_1x_SARDet_100k.py
```

For SAR-AIRcraft-1.0 dataset:

```shell
python tools/train_det.py configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py
```

For MSAR dataset:

```shell
python tools/train_det.py configs/DenoDet/DenoDet_3x_MSAR.py
```

For AIR-SARShip-1.0 dataset:

```shell
python tools/train_det.py configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py
```

#### Multi GPU Training 

Take a 4-GPU machine as example.

For SARDet-100K dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_train.sh configs/DenoDet/DenoDet_1x_SARDet_100k.py 4
```

For SAR-AIRcraft-1.0 dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_train.sh configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py 4
```

For MSAR dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_train.sh configs/DenoDet/DenoDet_3x_MSAR.py 4
```

For AIR-SARShip-1.0 dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_train.sh configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py 4
```
Here, `4` is the number of GPUs in your machine.

### Inference

#### Single GPU Inference

For SARDet-100K dataset:

```shell
python tools/test_det.py configs/DenoDet/DenoDet_1x_SARDet_100k.py {checkpoint_path}
```

For SAR-AIRcraft-1.0 dataset:

```shell
python tools/test_det.py configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py {checkpoint_path}
```

For MSAR dataset:

```shell
python tools/test_det.py configs/DenoDet/DenoDet_3x_MSAR.py {checkpoint_path}
```

For AIR-SARShip-1.0 dataset:

```shell
python tools/test_det.py configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py {checkpoint_path}
```

Here, `{checkpoint_path}` represents the path to the weights you downloaded or trained. The `{curly braces}` are for reference only and should not be included when using the scripts.

#### Multi GPU Inference 

Take a 4-GPU machine as example.

For SARDet-100K dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_test.sh configs/DenoDet/DenoDet_1x_SARDet_100k.py {checkpoint_path} 4
```

For SAR-AIRcraft-1.0 dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_test.sh configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py {checkpoint_path} 4
```

For MSAR dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_test.sh configs/DenoDet/DenoDet_3x_MSAR.py {checkpoint_path} 4
```

For AIR-SARShip-1.0 dataset:

```shell
CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29500 tools/dist_test.sh configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py {checkpoint_path} 4
```

Here, `{checkpoint_path}` represents the path to the weights you downloaded or trained. The `{curly braces}` are for reference only and should not be included when using the scripts, and `{4}` is the number of GPUs in your machine.

## Model Zoo and Benchmark

**Note: Both passwords for BaiduYun and OneDrive is `grok`**.

### Leaderboard

### Model Zoo

#### DenoDet

SARDet-100K
<table>
    <tr>
        <td>Model</td>
        <td>mAP(COCO)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet</td>
        <td>55.88</td>
        <td>52.69G</td>
        <td ><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDet/DenoDet_1x_SARDet_100k.py"> DenoDet_1x_SARDet_100k.py </a>
        </td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1ZiXbWo9eHHP0LZYylcPpRQ?pwd=pdyh"> 百度网盘 </a> | <a href="https://1drv.ms/f/c/698f69b8b2172561/EgIfrje7GrxJkCWZjPEHi3oBxnaICQXnEmpzl5OtsuEIIA?e=wbxSwk"> OneDirve </a>
        </td>
</table>

MSAR
<table>
    <tr>
        <td>Model</td>
        <td>mAP(07)</td>
        <td>mAP(12)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet</td>
        <td>69.90</td>
        <td>71.21</td>
        <td>12.89G</td>
        <td ><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDet/DenoDet_3x_MSAR.py"> DenoDet_3x_MSAR.py </a>
        </td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1JsLqIUr0_BA3Kh44USQ6gQ?pwd=jnfi"> 百度网盘 </a> | <a href="https://1drv.ms/f/s!AmElF7K4aY9p3EnDJlAc3Wmjq0V0?e=YVmI4y"> OneDirve </a>
        </td>
</table>

SAR-AIRcraft-1.0
<table>
    <tr>
        <td>Model</td>
        <td>mAP(07)</td>
        <td>mAP(12)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet</td>
        <td>68.60</td>
        <td>69.56</td>
        <td>48.53G</td>
        <td><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py"> DenoDet_1x_SAR-AIRcraft-1.0.py </a></td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/19LfXFmSpHJAcLovvE9NE8A?pwd=vwz7"> 百度网盘 </a> | <a href="https://1drv.ms/f/s!AmElF7K4aY9p2BjA1okkWgTGqU0V?e=DQk0Ld"> OneDirve </a>
        </td>
</table>

AIR-SARShip-1.0
<table>
    <tr>
        <td>Model</td>
        <td>mAP(07)</td>
        <td>mAP(12)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet</td>
        <td>72.42</td>
        <td>73.36</td>
        <td>48.52G</td>
        <td><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py"> DenoDet_6x_AIR-SARShip-1.0.py </a></td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1lktF3yxp4PE1fDGWIx5OoA?pwd=w07n"> 百度网盘 </a> | <a href="https://1drv.ms/f/s!AmElF7K4aY9phG32rZfCEjAcP-qA?e=3fCH3f"> OneDirve </a>
        </td>
</table>

#### DenoDet V2

SARDet-100K(val set)
<table>
    <tr>
        <td>Model</td>
        <td>mAP(COCO)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet V2</td>
        <td>56.71</td>
        <td>52.47G</td>
        <td ><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDetV2/DenoDetV2_1x_SARDet_100k.py"> DenoDetV2_1x_SARDet_100k.py </a>
        </td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1Ab467RioPPCse1ea5AuuLQ?pwd=grok"> 百度网盘 </a> | <a href="https://1drv.ms/f/c/869d5f1d401ac2ec/ElTBf5nRCkpBtrLSrx-444UBacdKTmKmJ_YREyd7zjV6bw?e=tU73cd"> OneDirve </a>
        </td>
</table>

SARDet-100K(test set)
<table>
    <tr>
        <td>Model</td>
        <td>mAP(COCO)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet V2</td>
        <td>56.39</td>
        <td>0.21T</td>
        <td ><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDetV2/DenoDetV2_1x_SARDet_100k_test.py"> DenoDetV2_1x_SARDet_100k_test.py </a>
        </td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1mlGBeByB2kSjJLbxnrhSOw?pwd=grok"> 百度网盘 </a> | <a href="https://1drv.ms/f/c/869d5f1d401ac2ec/EjzcFMZEbv9AqH5YD6v7_TwBhLLDev5xZ3yiPFKUx3KFfQ?e=6rQdoK"> OneDirve </a>
        </td>
</table>

SAR-AIRcraft-1.0
<table>
    <tr>
        <td>Model</td>
        <td>mAP(07)</td>
        <td>mAP(12)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet V2</td>
        <td>69.93</td>
        <td>70.73</td>
        <td>48.61G</td>
        <td><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDetV2/DenoDetV2_1x_SAR-AIRcraft-1.0.py"> DenoDetV2_1x_SAR-AIRcraft-1.0.py </a></td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1gEkKETMMYb_kR6UbSYQIcw?pwd=grok"> 百度网盘 </a> | <a href="https://1drv.ms/f/c/869d5f1d401ac2ec/ElY5Slvg07hCtuTy2zOmAxoBCDWhuJpHKdKl75x8cRHREQ?e=fikLa9"> OneDirve </a>
        </td>
</table>

AIR-SARShip-1.0
<table>
    <tr>
        <td>Model</td>
        <td>mAP(07)</td>
        <td>mAP(12)</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
    <tr>
    <tr>
        <td>DenoDet V2</td>
        <td>73.98</td>
        <td>74.86</td>
        <td>48.61G</td>
        <td><a href="https://github.com/GrokCV/GrokSAR/blob/master/configs/DenoDet/DenoDetV2_6x_AIR-SARShip-1.0.py"> DenoDetV2_6x_AIR-SARShip-1.0.py </a></td>
        <td colspan="2">
            <a href="https://pan.baidu.com/s/1gdhLgnlQ85uELdB4IOBToA?pwd=grok"> 百度网盘 </a> | <a href="https://1drv.ms/f/c/869d5f1d401ac2ec/EsAyh0Gdd3tNhImS03HRK6oBQRkjT3x-RO2NSvzmi4en_Q?e=skKdN0"> OneDirve </a>
        </td>
</table>

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```bibtex
@article{dai2024denodet,
	title={DenoDet: Attention as Deformable Multi-Subspace Feature Denoising for Target Detection in SAR Images},
	author={Dai, Yimian and Zou, Minrui and Li, Yuxuan and Li, Xiang and Ni, Kang and Yang, Jian},
	journal={IEEE Transactions on Aerospace and Electronic Systems (TAES)},
	year={2024}
}

@inproceedings{li2024sardet100k,
	title={SARDet-100K: Towards Open-Source Benchmark and ToolKit for Large-Scale SAR Object Detection}, 
	author={Yuxuan Li and Xiang Li and Weijie Li and Qibin Hou and Li Liu and Ming-Ming Cheng and Jian Yang},
	year={2024},
	booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems (NeurIPS)},
}
```

## License

This project is released under the [Attribution-NonCommercial 4.0 International](LICENSE).

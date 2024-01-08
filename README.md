# GrokSAR
Toolkit for GrokSAR

- [Installation](#installation)
  - [Step 1: Create a conda environment](#step-1-create-a-conda-environment)
  - [Step 2: Install PyTorch](#step-2-install-pytorch)
  - [Step 3: Install OpenMMLab 2.x Codebases](#step-3-install-openmmlab-2x-codebases)
  - [Step 4: Install `groksar`](#step-4-install-groksar)
- [Model Zoo and Benchmark](#model-zoo-and-benchmark)
  - [Leaderboard](#leaderboard)
  - [Model Zoo](#model-zoo)
    - [Method A](#method-a)
    - [Method B](#method-b)


## Installation

### Step 1: Create a conda environment

```shell
$ conda create --name groksar python=3.9
$ source activate groksar
```

### Step 2: Install PyTorch

```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
```

### Step 3: Install OpenMMLab 2.x Codebases

```shell
# openmmlab codebases
pip install -U openmim dadaptation --no-input
mim install mmengine "mmcv>=2.0.0" "mmdet>=3.0.0" "mmsegmentation>=1.0.0" "mmrotate>=1.0.0rc1" mmyolo
# heatmap generation dependencies
pip install grad-cam
# other dependencies
pip install ninja --no-input
pip install scikit-learn
pip install psutil
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

## Model Zoo and Benchmark

**Note: Both passwords for BaiduYun and OneDrive is `grok`**.

### Leaderboard

### Model Zoo

#### Method A

<table>
    <tr>
        <td>Model</td>
        <td>mAP</td>
        <td>#Params</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
        <td>Visualization</td>
    <tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="4">
            <a href=""> 百度网盘 </a> | <a href=""> OneDirve </a>
        </td>
    <tr>
</table>

#### Method B

<table>
    <tr>
        <td>Model</td>
        <td>mAP</td>
        <td>#Params</td>
        <td>FLOPs</td>
        <td>Config</td>
        <td>Training Log</td>
        <td>Checkpoint</td>
        <td>Visualization</td>
    <tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="4">
            <a href=""> 百度网盘 </a> | <a href=""> OneDirve </a>
        </td>
    <tr>
</table>
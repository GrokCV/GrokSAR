# GrokSAR

GrokSAR is an open-source toolbox for SAR target detection and recognition.

- [Installation](#installation)
  - [Step 1: Create a conda environment](#step-1-create-a-conda-environment)
  - [Step 2: Install PyTorch](#step-2-install-pytorch)
  - [Step 3: Install OpenMMLab 2.x Codebases](#step-3-install-openmmlab-2x-codebases)
  - [Step 4: Install `groksar`](#step-4-install-groksar)
- [Model Zoo and Benchmark](#model-zoo-and-benchmark)
  - [Leaderboard](#leaderboard)
  - [Model Zoo](#model-zoo)
    - [DenoDet](#denodet)


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

#### DenoDet

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
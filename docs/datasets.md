# Dataset folders and setup

All paths are relative to the **repository root** (next to `tools/` and `datasets/`). Dataset paths used in configs are under `configs/_base_/datasets/`.

---

## SAR-AIRcraft-1.0

### 1. Lay out the raw release

```text
datasets/SAR-AIRcraft-1.0/
└── dota/
    ├── train/
    │   ├── images/     # full-scene training images
    │   └── labels/     # DOTA-format txt, one file per image stem
    ├── val/
    │   ├── images/
    │   └── labels/
    └── test/
        ├── images/
        └── labels/
```

Each `labels/*.txt` line: **8** coordinates, **class name**, difficulty integer, whitespace-separated (DOTA text label).

### 2. Build train / val / test patches

Run from the repository root. If `save_dir` already exists, the script will fail; remove or rename that directory first.

```shell
python tools/img_split.py --base-json tools/split_configs/SAR-AIRcraft-1.0_train.json
python tools/img_split.py --base-json tools/split_configs/SAR-AIRcraft-1.0_val.json
python tools/img_split.py --base-json tools/split_configs/SAR-AIRcraft-1.0_test.json
```

You should get:

```text
datasets/split_SAR-AIRcraft-1.0/
├── train/
│   ├── images/
│   └── annfiles/
├── val/
│   ├── images/
│   └── annfiles/
└── test/
    ├── images/
    └── annfiles/
```

### 3. Train or test

Use the matching config, e.g. `configs/DenoDet/DenoDet_1x_SAR-AIRcraft-1.0.py` (use the exact filename present in the repo).

---

## AIR-SARShip-1.0

### 1. Lay out the raw release

```text
datasets/AIR-SARShip-1.0/
└── dota/
    ├── train/
    │   ├── images/
    │   └── labels/
    └── val/
        ├── images/
        └── labels/
```

`labels/*.txt` uses the same DOTA line format as SAR-AIRcraft-1.0.

### 2. Build train / val patches

```shell
python tools/img_split.py --base-json tools/split_configs/AIR-SARShip-1.0_train.json
python tools/img_split.py --base-json tools/split_configs/AIR-SARShip-1.0_val.json
```

Expected output:

```text
datasets/split_AIR-SARShip-1.0/
├── train/
│   ├── images/
│   └── annfiles/
└── val/
    ├── images/
    └── annfiles/
```

In the current configs, the test dataloader reuses the val setup; if you only use the official train/val split, the two commands above are enough.

### 3. Train or test

e.g. `configs/DenoDet/DenoDet_6x_AIR-SARShip-1.0.py`.

---

## MSAR

### 1. Folder layout

```text
datasets/MSAR/
├── JPEGImages/
├── Annotations/
├── train.txt
└── val.txt
```

### 2. File expectations

- `train.txt` and `val.txt`: one image **ID** per line (no path, usually no extension), matching basenames under `JPEGImages/`.
- `Annotations/`: VOC-style `*.xml` per ID.

### 3. Train or test

e.g. `configs/DenoDet/DenoDet_3x_MSAR.py`.

---

## SARDet_100K

### 1. Folder layout

```text
datasets/SARDet_100K/
├── JPEGImages/
└── Annotations/
    ├── train.json
    └── val.json
```

If you add `test.json`, switch to it using the commented blocks in the dataset config when needed.

### 2. File expectations

- `train.json` / `val.json`: COCO format (`images`, `annotations`, `categories`, etc.).
- `JPEGImages/`: image files that match each entry’s `file_name` in the JSON (including any relative subpath if used).

### 3. Train or test

e.g. `configs/DenoDet/DenoDet_1x_SARDet_100k.py`.

---

## Reference tree (configs and data roots)

```text
.
├── configs/
└── datasets/
    ├── AIR-SARShip-1.0/
    ├── SAR-AIRcraft-1.0/
    ├── MSAR/
    ├── SARDet_100K/
    ├── split_AIR-SARShip-1.0/
    └── split_SAR-AIRcraft-1.0/
```

Unpack or arrange downloads under `datasets/` so paths match `configs/_base_/datasets/*.py` and `tools/split_configs/*.json`.

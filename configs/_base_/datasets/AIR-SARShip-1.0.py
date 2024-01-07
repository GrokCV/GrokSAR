# dataset settings
dataset_type = 'sareye.DotaBig2SmallDataset'
backend_args = None

METAINFO = {
        'classes':
        ('ship',),
        # palette is a list of color tuples, which is used for visualization.
        'palette': [(106, 0, 228),]
    }

train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True, box_type='qbox'),
    dict(type='mmrotate.ConvertBoxType', box_type_mapping=dict(gt_bboxes='hbox')),
    dict(type='Resize', scale=(512, 512), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
val_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(512, 512), keep_ratio=True, clip_object_border=False),
    # avoid bboxes being resized
    dict(type='LoadAnnotations', with_bbox=True, box_type='qbox'),
    dict(type='mmrotate.ConvertBoxType', box_type_mapping=dict(gt_bboxes='hbox')),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
test_pipeline = val_pipeline

train_dataloader = dict(
    batch_size=32,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=None,
    dataset=dict(
        type=dataset_type,
        metainfo=METAINFO,
        data_prefix=dict(img_path='datasets/split_AIR-SARShip-1.0/train/images'),
        img_suffix='jpg',
        ann_file='datasets/split_AIR-SARShip-1.0/train/annfiles',
        filter_cfg=dict(filter_empty_gt=True),
        pipeline=train_pipeline,
    ))
val_dataloader = dict(
    batch_size=32,
    num_workers=8,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=METAINFO,
        data_prefix=dict(img_path='datasets/split_AIR-SARShip-1.0/val/images'),
        img_suffix='jpg',
        ann_file='datasets/AIR-SARShip-1.0/dota/val/labels/',
        test_mode=True,
        tile_mode=True,
        pipeline=val_pipeline,
    ))
test_dataloader = val_dataloader

val_evaluator = dict(type='sareye.DotaBig2SmallMetric', metric='mAP', eval_mode='11points')
test_evaluator = val_evaluator
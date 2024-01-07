_base_ = [
    '../_base_/datasets/AIR-SARShip-1.0.py',
    '../_base_/schedules/schedule_6x.py',
    'mmdet::_base_/default_runtime.py'
]

# model settings
model = dict(
    type='FCOS',
    data_preprocessor=dict(
        type='DetDataPreprocessor',
        mean=[43.35241434599897, 43.35241434599897, 43.35241434599897],
        std=[51.60430728243554, 51.60430728243554, 51.60430728243554],
        bgr_to_rgb=False,
        pad_size_divisor=32),
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=-1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=False,
        style='pytorch',
        init_cfg=dict(type='Pretrained', checkpoint='torchvision://resnet50')),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=1,
        add_extra_convs='on_output',  # use P5
        num_outs=5,
        relu_before_extra_convs=True),
    bbox_head=dict(
        type='FCOSHead',
        num_classes=1,
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        strides=[8, 16, 32, 64, 128],
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            loss_weight=1.0),
        loss_bbox=dict(type='IoULoss', loss_weight=1.0),
        loss_centerness=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0)),
    # testing settings
    test_cfg=dict(
        nms_pre=1000,
        min_bbox_size=0,
        score_thr=0.05,
        nms=dict(type='nms', iou_threshold=0.5),
        max_per_img=500))

# training schedule for 1x
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=72, val_interval=1)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

# optimizer
base_lr = 1.0
optim_wrapper = dict(
    _delete_=True,
    type='OptimWrapper',
    optimizer=dict(
        type='DAdaptAdam', lr=base_lr, weight_decay=0.05, decouple=True
    ),
    paramwise_cfg=dict(
        norm_decay_mult=0, bias_decay_mult=0, bypass_duplicate=True))

default_hooks = dict(
    checkpoint=dict(
        type='CheckpointHook',
        interval=-1,
        _scope_='mmdet',
        save_best='auto'))

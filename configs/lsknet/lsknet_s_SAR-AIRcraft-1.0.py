_base_ = '../faster_rcnn/faster-rcnn_r50_fpn_1x_SAR-AIRcraft-1.0.py'

angle_version = 'le90'
model = dict(
    backbone=dict(
        _delete_=True,
        type='groksar.LSKNet',
        embed_dims=[64, 128, 320, 512],
        drop_rate=0.1,
        drop_path_rate=0.1,
        depths=[2, 2, 4, 2],
        init_cfg=dict(
            type='Pretrained',
            checkpoint='https://download.openmmlab.com/mmrotate/v1.0/lsknet/\
backbones/lsk_s_backbone-e9d2e551.pth'),
        norm_cfg=dict(type='SyncBN', requires_grad=True)),
    neck=dict(in_channels=[64, 128, 320, 512]),
    )

optim_wrapper = dict(
    optimizer=dict(
        _delete_=True,
        type='AdamW',
        lr=0.0002,
        betas=(0.9, 0.999),
        weight_decay=0.05))

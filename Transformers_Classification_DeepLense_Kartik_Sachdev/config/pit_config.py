from ray import tune
import numpy as np

PIT_CONFIG = {
    "network_type": "PiT",
    "pretrained": False,
    "image_size": 224,
    "batch_size": 128,
    "num_epochs": 15,
    "optimizer_config": {
        "name": "AdamW",
        "weight_decay": 0.01,
        "lr": 0.001,
        "momentum": 0.9,
        "betas": (0.9, 0.999),
        "warmup_epoch": 3,
    },
    "lr_schedule_config": {
        "use_lr_schedule": True,
        "step_lr": {"gamma": 0.5, "step_size": 20,},
        "reduce_on_plateau": {
            "factor": 0.1,
            "patience": 4,
            "threshold": 0.0000001,
            "verbose": True,
        },
    },
    "channels": 1,
    "network_config": {
        "patch_size": 14,
        "dim": 128,
        "depth": (3, 3, 4,),
        "heads": 3,
        "mlp_dim": 256,
        "dropout": 0.1,
        "emb_dropout": 0.1,
    },
}


PIT_RAY_CONFIG = {
    "network_type": "PiT",
    "pretrained": False,
    "image_size": 224,
    "batch_size": 128,
    "num_epochs": 15,
    "optimizer_config": {
        "name": "AdamW",
        "weight_decay": 0.01,
        "lr": tune.sample_from(lambda spec: 10 ** (-10 * np.random.rand())),
        "momentum": tune.uniform(0.7, 0.99),
        "betas": (0.9, 0.999),
        "warmup_epoch": 3,
    },
    "lr_schedule_config": {
        "use_lr_schedule": True,
        "step_lr": {"gamma": 0.5, "step_size": 20,},
        "reduce_on_plateau": {
            "factor": 0.1,
            "patience": 4,
            "threshold": 0.0000001,
            "verbose": True,
        },
    },
    "channels": 1,
    "network_config": {
        "patch_size": 14,
        "dim": tune.randint(128, 512),
        "depth": (3, 3, 4,),
        "heads": tune.randint(2, 5),
        "mlp_dim": 256,
        "dropout": tune.choice([0.0, 0.1, 0.2]),
        "emb_dropout": tune.choice([0.0, 0.1, 0.2]),
    },
}

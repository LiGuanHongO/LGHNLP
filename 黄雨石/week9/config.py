# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": "ner_data/schema.json",
    "train_data_path": "ner_data/train",
    "valid_data_path": "ner_data/test",
    "vocab_path":"chars.txt",
    "model_type": "bert",
    "max_length": 50,
    "hidden_size": 64,
    "num_layers": 3,
    "epoch": 20,
    "batch_size": 25,
    "optimizer": "adam",
    "learning_rate": 1e-4,
    "use_crf": False,
    "dropout": 0.5,
    "class_num": 9,
    "output_size": 4,
    "seed": 9,
    "pooling_style": "max",
    "simple_size": 300,
    "kernel_size": 3,
    "bert_path": r"D:\bert-base-chinese"
}




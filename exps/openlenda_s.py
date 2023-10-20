#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        # max training epoch
        self.max_epoch = 30
        self.num_classes = 8
        # --------------- transform config ----------------- #
        self.flip_prob = 0
        self.input_size = (1280, 1280)  # (height, width)

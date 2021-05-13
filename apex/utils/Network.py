import os
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
from torchvision import models

class Network(nn.Module):
    def __init__(self, net):
        super(Network, self).__init__()

        self.network = pytorch_vgg16
        self.conv1 = nn.Conv2d()
        self.vgg16 = net

    def forward(self, x, front_r):
        midd_result = self.vgg16(x)

        result = midd_result

        return result

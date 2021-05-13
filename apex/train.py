import os

import torch

from util.Network import Network


class TrainEngine():
    def __init__(self, dataloader, device, epoch=10):

        self.network =
        self.dataloader = dateloader

        self.device = device
        self.epoch = epoch

    def __call__(self):
        print("network is ", self.network)

        self.network.apply(self.init_weights)

        vae_optimizer = optim.Adam(self.network.parameters(), lr = 0.005)

        for epo in tqdm(range(self.epoch)):
            for img in self.dataloader:
                self.network.train()


#!/usr/bin/env python
import pyart
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage, signal
import time

if __name__ == "__main__":
    radar = pyart.io.read('./data/csapr_test_case.nc')
    display = pyart.graph.RadarMapDisplay(radar)
    fig = plt.figure(figsize = [10,8])
    display.plot_ppi_map('reflectivity', sweep = 2, resolution = 'i',
                    vmin = -10, vmax = 64, mask_outside = False,
                    cmap = pyart.graph.cm.NWSRef)
    plt.savefig('./awesome.png')


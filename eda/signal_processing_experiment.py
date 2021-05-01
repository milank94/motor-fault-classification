# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
# -

from data_acquisition.main import get_data
from data_processing.utils import _downSampler, _FFT, _dataScaler
from eda.utils import time_plot, fft_plot
import data_processing.data_processing_config as config

dataset = get_data()

# ## Data Plotting

data_n = dataset.normal.copy()
data_horizontal = dataset.horizontal.copy()
data_imbalance = dataset.imbalance.copy()

time_plot(data_n[0], 0, 250000)

# ## Data Resampling

data_n_resampled = _downSampler(data_n, 0, 100)
data_n_resampled_fft = _FFT(data_n_resampled)
fft_plot(data_n_resampled_fft[0])

data_horizontal_resampled = _downSampler(data_horizontal, 0, 100)
data_horizontal_resampled_fft = _FFT(data_horizontal_resampled)
fft_plot(data_horizontal_resampled_fft[0])

data_imbalance_resampled = _downSampler(data_imbalance, 0, 100)
data_imbalance_resampled_fft = _FFT(data_imbalance_resampled)
fft_plot(data_imbalance_resampled_fft[0])

# ## Data Scaling

data_n_resampled_scaled = _dataScaler(data_n_resampled)
time_plot(data_n_resampled_scaled[0], 0, 2500)



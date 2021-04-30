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
#from scipy.io.wavfile import write

dataset = get_data()

# ## Feature Scaling

data_n = dataset.normal.copy()

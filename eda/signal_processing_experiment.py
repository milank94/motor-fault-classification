from data_acquisition.main import get_save_data
from data_processing.utils import _downSampler, _FFT, _dataScaler
from eda.utils import time_plot, fft_plot
import eda.config as config

dataset = get_save_data()

config.OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Data Plotting
data_n = dataset.normal.copy()
data_horizontal = dataset.horizontal.copy()
data_imbalance = dataset.imbalance.copy()
time_plot(data_n[0], 0, 250000, 'time_plot')

# Data Resampling
data_n_resampled = _downSampler(data_n, 0, 100)
data_n_resampled_fft = _FFT(data_n_resampled)
fft_plot(data_n_resampled_fft[0], 'fft_normal_resampled')

data_horizontal_resampled = _downSampler(data_horizontal, 0, 100)
data_horizontal_resampled_fft = _FFT(data_horizontal_resampled)
fft_plot(data_horizontal_resampled_fft[0], 'fft_horizontal_resampled')

data_imbalance_resampled = _downSampler(data_imbalance, 0, 100)
data_imbalance_resampled_fft = _FFT(data_imbalance_resampled)
fft_plot(data_imbalance_resampled_fft[0], 'fft_imbalance_resampled')

# Data Scaling
data_n_resampled_scaled = _dataScaler(data_n_resampled)
time_plot(data_n_resampled_scaled[0], 0, 2500, 'data_scaled')

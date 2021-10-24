"""
Any utility function that is required for data exploratory analysis goes here
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfftfreq
import data_processing.data_processing_config as config
import eda.config as eda_config


def time_plot(yf: np.ndarray, start: int, stop: int, fname: str):
    '''
    Plots a time series

    params:
    ---
    yf (np.ndarray): input data to plot
    start (int): start time (s)
    stop (int): stop time (s)
    fname (str): save file name
    '''
    time = np.linspace(0, config.DURATION, len(yf), endpoint=False)

    _, axs = plt.subplots(nrows=1, figsize=(11, 9))
    plt.rcParams['font.size'] = '14'

    for label in (axs.get_xticklabels() + axs.get_yticklabels()):
        label.set_fontsize(14)

    plt.plot(time[start:stop], yf[start:stop])
    axs.set_title('Time-series signal')
    axs.set_ylabel('Voltage (V)', fontsize=14)
    axs.set_xlabel('Time (s)', fontsize=14)

    file_location = eda_config.OUTPUT_DATA_DIR / Path(f'{fname}.png')
    plt.savefig(file_location)


def fft_plot(yf: np.ndarray, fname: str):
    '''
    Plots the FFT

    params:
    ---
    yf (np.ndarray): input data to plot
    fname (str): save file name
    '''
    N = int((config.SAMPLE_RATE / config.RESAMPLE_RATE) * config.DURATION)
    xf = rfftfreq(N-1, 1 / int(config.SAMPLE_RATE / config.RESAMPLE_RATE))

    _, axs = plt.subplots(nrows=1, figsize=(11, 9))
    plt.rcParams['font.size'] = '14'

    for label in (axs.get_xticklabels() + axs.get_yticklabels()):
        label.set_fontsize(14)

    plt.plot(xf, yf)
    axs.set_title('Frequency spectra')
    axs.set_ylabel('Signal strength', fontsize=14)
    axs.set_xlabel('Frequency (Hz)', fontsize=14)

    file_location = eda_config.OUTPUT_DATA_DIR / Path(f'{fname}.png')
    plt.savefig(file_location)

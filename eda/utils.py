"""
Any utility function that is required for data exploratory analysis goes here
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfftfreq
import data_processing.data_processing_config as config


def time_plot(yf: np.ndarray, start: int, stop: int):
    '''
    Plots a time series

    params:
    ---
    yf (np.ndarray): input data to plot
    sample_rate (int): sampling rate (Hz)
    duration (int): signal duration in seconds
    '''
    time = np.linspace(0, config.DURATION, len(yf), endpoint=False)

    fig, axs = plt.subplots(nrows=1, figsize=(11, 9))
    plt.rcParams['font.size'] = '14'

    for label in (axs.get_xticklabels() + axs.get_yticklabels()):
        label.set_fontsize(14)

    plt.plot(time[start:stop], yf[start:stop])
    axs.set_title('Time-series signal')
    axs.set_ylabel('Voltage (V)', fontsize=14)
    axs.set_xlabel('Time (s)', fontsize=14)
    plt.show()


def fft_plot(yf: np.ndarray):
    '''
    Plots the FFT

    params:
    ---
    yf (np.ndarray): input data to plot
    sample_rate (int): sampling rate (Hz)
    duration (int): signal duration in seconds
    '''
    N = int((config.SAMPLE_RATE / config.RESAMPLE_RATE) * config.DURATION)
    xf = rfftfreq(N-1, 1 / int(config.SAMPLE_RATE / config.RESAMPLE_RATE))

    fig, axs = plt.subplots(nrows=1, figsize=(11, 9))
    plt.rcParams['font.size'] = '14'

    for label in (axs.get_xticklabels() + axs.get_yticklabels()):
        label.set_fontsize(14)

    plt.plot(xf, yf)
    axs.set_title('Frequency spectra')
    axs.set_ylabel('Signal strength', fontsize=14)
    axs.set_xlabel('Frequency (Hz)', fontsize=14)
    plt.show()

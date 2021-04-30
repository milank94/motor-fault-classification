"""
Any utility function that is required for data exploratory analysis goes here
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfftfreq
import data_processing.data_processing_config as config


def time_plot(yf:np.ndarray, start:int, stop:int):
    '''
    Plots a time series
    
    params:
    ---
    yf (np.ndarray): input data to plot
    sample_rate (int): sampling rate (Hz)
    duration (int): signal duration in seconds
    '''   
    time = np.linspace(0, config.DURATION, len(yf), endpoint=False)
    
    plt.plot(time[start:stop], yf[start:stop])
    plt.show()


def fft_plot(yf:np.ndarray):
    '''
    Plots the FFT
    
    params:
    ---
    yf (np.ndarray): input data to plot
    sample_rate (int): sampling rate (Hz)
    duration (int): signal duration in seconds
    '''   
    N = int((config.SAMPLE_RATE / config.RESAMPLE_RATE) * config.DURATION)
    xf = rfftfreq(N, 1 / int(config.SAMPLE_RATE / config.RESAMPLE_RATE))
    
    plt.plot(xf, yf)
    plt.show()

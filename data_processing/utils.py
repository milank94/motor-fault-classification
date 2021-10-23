"""
Any utility function that is required for data processing goes here
"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.fft import rfft


def _dataScaler(data: list) -> list:
    '''
    Reads in data and returns a scaled list.

    params:
    ---
    data (list): data to down sample

    returns:
    ---
    final_sequence (list): resampled data
    '''
    data_temp = np.reshape(data, (-1, data.shape[2]))
    norm = MinMaxScaler().fit(data_temp)
    data_norm = norm.transform(data_temp)
    data_final = np.reshape(data_norm, (-1, data.shape[1], data.shape[2]))

    return data_final


def _downSampler(data: list, start_index: int, sample_rate: int) -> list:
    '''
    Reads in raw data from .csv files and returns a resampled list

    params:
    ---
    data (list): data to down sample
    start_index (int): starting index
    sample_rate (int): sampling rate

    returns:
    ---
    final_sequence (list): resampled data
    '''
    final_sequence = list()
    for dataset in data:
        data_resampled = []
        start = start_index
        stop = sample_rate
        for i in range(int(len(dataset)/sample_rate)):
            data_resampled.append(dataset[start:stop, :].mean(axis=0))
            start += sample_rate
            stop += sample_rate
        final_sequence.append(np.stack(data_resampled))

    return np.stack(final_sequence)


def _FFT(data: list) -> list:
    '''
    Reads in resampled data and performs a Fast Fourier Transform with DC offset removal

    params:
    ---
    data (pd.DataFrame): data to perform Fast Fourier Transform

    returns:
    ---
    data_fft (list): FFT data
    '''
    data_fft = list()
    for dataset in data:
        data_fft.append(np.stack(np.abs(rfft(dataset, axis=0))[1:, :]))

    return np.stack(data_fft)

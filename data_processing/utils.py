"""
Any utility function that is required for data processing goes here
"""

from pathlib import Path
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from scipy.fft import rfft
import logging
import pickle
from data_acquisition.custom_types import Dataset
from data_processing.custom_types import ProcessedDataset
import data_processing.data_processing_config as config

logging.basicConfig(level=logging.INFO)


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


def get_save_train_test_data(raw_data: Dataset) -> ProcessedDataset:
    '''
    runs the 'get_data()' and '_downSampler' methods
    to generate training and testing data sets

    params:
    ---
    dataset (Dataset): raw data set from data_acquisition module

    returns:
    ---
    train_test_data (Dataset): named tuple of (X_train, y_train, X_test, y_test)
    '''
    if Path.exists(config.OUTPUT_DATA_FILE):
        logging.info('Loading previously pickled `train_test_data`')
        train_test_data = pickle.load(open(config.OUTPUT_DATA_FILE, 'rb'))
    else:
        config.OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)

        logging.info(f"Data is being resampled at a sample rate of: {config.RESAMPLE_RATE}")
        data_n = _downSampler(raw_data.normal, 0, config.RESAMPLE_RATE)
        data_horizontal = _downSampler(raw_data.horizontal, 0, config.RESAMPLE_RATE)
        data_imbalance = _downSampler(raw_data.imbalance, 0, config.RESAMPLE_RATE)
        data_vertical = _downSampler(raw_data.vertical, 0, config.RESAMPLE_RATE)
        data_overhang = _downSampler(raw_data.overhang, 0, config.RESAMPLE_RATE)
        data_underhang = _downSampler(raw_data.underhang, 0, config.RESAMPLE_RATE)

        logging.info("Scaling the data.")
        data_n = _dataScaler(data_n)
        data_horizontal = _dataScaler(data_horizontal)
        data_imbalance = _dataScaler(data_imbalance)
        data_vertical = _dataScaler(data_vertical)
        data_overhang = _dataScaler(data_overhang)
        data_underhang = _dataScaler(data_underhang)

        logging.info("Performing FFT.")
        data_n = _FFT(data_n)
        data_horizontal = _FFT(data_horizontal)
        data_imbalance = _FFT(data_imbalance)
        data_vertical = _FFT(data_vertical)
        data_overhang = _FFT(data_overhang)
        data_underhang = _FFT(data_underhang)

        y_1 = np.zeros(int(len(data_n)), dtype=int)
        y_2 = np.full(int(len(data_horizontal)), 1)
        y_3 = np.full(int(len(data_imbalance)), 2)
        y_4 = np.full(int(len(data_vertical)), 3)
        y_5 = np.full(int(len(data_overhang)), 4)
        y_6 = np.full(int(len(data_underhang)), 5)
        y = np.concatenate((y_1, y_2, y_3, y_4, y_5, y_6))

        X = np.concatenate((data_n, data_horizontal, data_imbalance, data_vertical, data_overhang, data_underhang))

        logging.info(f"Spliting data to a test size of: {config.DATA_TEST_SIZE}")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.DATA_TEST_SIZE, random_state=42)

        train_test_data = ProcessedDataset(X_train, X_test, y_train, y_test)
        pickle.dump(train_test_data, open(config.OUTPUT_DATA_FILE, 'wb'))

        logging.info("Complete. Happy modelling :).")

    return train_test_data

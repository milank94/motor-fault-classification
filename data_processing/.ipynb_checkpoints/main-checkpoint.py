# +
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import logging
import collections
import os
import re

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

logging.basicConfig(level=logging.INFO)
# -

from data_acquisition.main import get_data
from data_processing.utils import _dataScaler, _downSampler, _FFT
import data_processing.data_processing_config as config

Dataset = collections.namedtuple('Dataset', 'X_train X_test y_train y_test')


def get_train_test_data(raw_data:Dataset) -> Dataset:
    '''
    runs the 'get_data()' and '_downSampler' methods to generate training and testing data sets
    
    params:
    ---
    dataset (Dataset): raw data set from data_acquisition module
    
    returns:
    ---
    train_test_data (Dataset): named tuple of (X_train, y_train, X_test, y_test)
    '''   
    logging.info(f"Data is being resampled at a sample rate of: {config.RESAMPLE_RATE}")    
    data_n = _downSampler(raw_data.normal, 0, config.RESAMPLE_RATE)
    data_horizontal = _downSampler(raw_data.horizontal, 0, config.RESAMPLE_RATE)
    data_imbalance = _downSampler(raw_data.imbalance, 0, config.RESAMPLE_RATE)
 
    logging.info(f"Scaling the data.")
    data_n = _dataScaler(data_n)
    data_horizontal = _dataScaler(data_horizontal)
    data_imbalance = _dataScaler(data_imbalance)
       
    logging.info(f"Performing FFT.")
    data_n = _FFT(data_n)
    data_horizontal = _FFT(data_horizontal)
    data_imbalance = _FFT(data_imbalance)
    
    y_1 = np.zeros(int(len(data_n)),dtype=int)
    y_2 = np.full(int(len(data_horizontal)),1)
    y_3 = np.full(int(len(data_imbalance)),2)
    y = np.concatenate((y_1, y_2, y_3))
    
    X = np.concatenate((data_n, data_horizontal, data_imbalance))
    
    logging.info(f"Spliting data to a test size of: {config.DATA_TEST_SIZE}")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.DATA_TEST_SIZE, random_state=42)
       
    train_test_data = Dataset(X_train, X_test, y_train, y_test)
    
    logging.info(f"Complete. Happy modelling :).")
    
    return train_test_data

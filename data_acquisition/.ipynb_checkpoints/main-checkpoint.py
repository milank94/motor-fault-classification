# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from pyprojroot import here as get_project_root
import os
os.chdir(get_project_root()) # hack for notebook development

# +
import os
import sys
import pandas as pd
import numpy as np
import logging
import collections
import data_acquisition.data_acquisition_config as config

logging.basicConfig(level=logging.INFO)
# -

Dataset = collections.namedtuple('Dataset', 'normal horizontal imbalance')


def _dataReader(path_names:list) -> list:
    '''
    Reads in raw data from .csv files and returns a list
    
    params:
    ---
    path_names (list): list of all the data files to read in
    
    returns:
    ---
    sequences (list): raw dataset from data directory
    '''
    
    sequences = list()
    
    for name in path_names:
        data = pd.read_csv(name, header=None)
        sequences.append(data.values)
          
    return sequences


def get_data() -> Dataset:
    '''
    runs the `_dataReader` method and stores the raw data into a Dataset named tuple. 
    
    returns:
    ---
    dataset (Dataset): named tuple of (data_n)
    '''
    
    logging.info(f"Loading raw data.")
    
    data_n = np.stack(_dataReader(config.NORMAL_FILE_NAMES))
    data_horizontal = np.stack(_dataReader(config.HORI_MIS_FILE_NAMES))
    data_imbalance = np.stack(_dataReader(config.IMBALANCE_FILE_NAMES))
    
    logging.info(f"Load complete.")
    
    dataset = Dataset(data_n, data_horizontal, data_imbalance)
    return dataset

from pyprojroot import here as get_project_root
import os
os.chdir(get_project_root()) # hack for notebook development

import pandas as pd
import numpy as np
import logging
import data_acquisition.data_acquisition_config as config
from data_acquisition.custom_types import Dataset

logging.basicConfig(level=logging.INFO)

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
    
    data_normal = np.stack(_dataReader(config.NORMAL_FILE_NAMES))
    data_horizontal = np.stack(_dataReader(config.HORI_MIS_FILE_NAMES))
    data_vertical = np.stack(_dataReader(config.VERT_MIS_FILE_NAMES))
    data_imbalance = np.stack(_dataReader(config.IMBALANCE_FILE_NAMES))
    data_overhang = data_imbalance = np.stack(_dataReader(config.OVERHANG_FILE_NAMES))
    data_underhang = data_imbalance = np.stack(_dataReader(config.UNDERHANG_FILE_NAMES))
    
    logging.info(f"Load complete.")
    
    dataset = Dataset(data_normal, data_horizontal, data_vertical, data_imbalance, data_overhang, data_underhang)
    return dataset
